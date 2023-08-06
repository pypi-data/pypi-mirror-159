import os
import click
import sqlite3
from typing import Final, Callable
from pathlib import Path
import shutil

from result import Err, Ok

from . import (
    model,
    db,
    util,
    __version__,
    __package_name__,
)
from .model import MultiText


db.ensure_cfg_file()
app_cfg = db.load_app_cfg()
db_path: Final = app_cfg["db_path"]
lang: Final = app_cfg["lang"]


def connect() -> sqlite3.Connection:
    return db.connect(db_path)


def execute(func: Callable, *args):
    with connect() as conn:
        return func(conn, *args)


config = execute(db.get_cfg).unwrap()

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def show_info(ctx, _, value):
    if not value or ctx.resilient_parsing:
        return
    print()
    print(f"  [tt-focus] {__file__}")
    print(f"   [version] {__version__}")
    with connect() as conn:
        util.show_cfg(conn, app_cfg, config)
    ctx.exit()


help_text = MultiText(
    cn="""tt-focus: Command-line time tracker to help focus.

    专门为了帮助集中注意力而设计的命令行时间记录器。
    
    https://pypi.org/project/tt-focus/
    """,
    en="""tt-focus: Command-line time tracker to help focus.

    https://pypi.org/project/tt-focus/
    """,
)
help_info = MultiText(
    cn="显示关于本软件的一些有用信息。", en="Show information about tt-focus."
)
help_status = MultiText(
    cn="完全等同 'tt status'", en="Same as the 'tt status' command."
)
help_pause = MultiText(
    cn="完全等同 'tt pause'", en="Same as the 'tt pause' command."
)
help_resume = MultiText(
    cn="完全等同 'tt resume'", en="Same as the 'tt resume' command."
)


@click.group(invoke_without_command=True, help=help_text.str(lang))
@click.help_option("-h", "--help")
@click.version_option(
    __version__,
    "-v",
    "-V",
    "--version",
    package_name=__package_name__,
    message="%(prog)s version: %(version)s",
)
@click.option(
    "-i",
    "--info",
    is_flag=True,
    help=help_info.str(lang),
    expose_value=False,
    callback=show_info,
)
@click.option("stat", "-s", is_flag=True, help=help_status.str(lang))
@click.option("p", "-p", is_flag=True, help=help_pause.str(lang))
@click.option("r", "-r", is_flag=True, help=help_resume.str(lang))
@click.pass_context
def cli(ctx: click.Context, stat: bool, p: bool, r: bool):
    """tt-focus: Command-line time tracker to help focus.

    专门为了帮助集中注意力而设计的命令行时间记录器。

    https://pypi.org/project/tt-focus/
    """
    if stat:
        ctx.invoke(status)
        ctx.exit()
    if p:
        ctx.invoke(pause)
        ctx.exit()
    if r:
        ctx.invoke(resume)
        ctx.exit()

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())
        ctx.exit()


# 以上是主命令
############
# 以下是子命令


def update_db_path(new_db_path: Path, success: MultiText):
    app_cfg["db_path"] = new_db_path.resolve().__str__()
    db.write_cfg_file(app_cfg)
    print(success.str(lang))


def change_db_path(new_db_path: Path):
    success = MultiText(
        cn=f"数据库文件已更改为 {new_db_path}\n注意，旧数据库未删除: {db_path}",
        en=f"Now using file {new_db_path}\n"
        + f"The old database remains: {db_path}",
    )
    update_db_path(new_db_path, success)


def move_db_file(new_db_path: Path):
    success = MultiText(
        cn=f"数据库文件已移动到 {new_db_path}",
        en=f"The database file is moved to {new_db_path}",
    )
    shutil.copyfile(db_path, new_db_path)
    os.remove(db_path)
    update_db_path(new_db_path, success)


def set_db_folder(db_folder: str):
    new_db_path = Path(db_folder).joinpath(db.DB_Filename)

    if new_db_path.exists():
        # 无变化
        if new_db_path.samefile(db_path):
            print(f"[database]: {db_path}")
            return

        # 新文件夹含有 tt-focus.db, 则认为这是新数据库文件。
        change_db_path(new_db_path)
        return

    # 新文件夹中没有 tt-focus.db, 则移动 tt-focus.db 到新文件夹。
    move_db_file(new_db_path)


help_text = MultiText(
    cn="更改 tt-focus 的设置，或更改任务/事件的属性。",
    en="Change settings of tt-focus, or properties of a task/event.",
)
help_set_split_min = MultiText(
    cn="设置工作时长下限 (单位：分钟)", en="Set the minimum length(minutes) of a 'split'."
)
help_set_pause_min = MultiText(
    cn="设置休息时长下限 (单位：分钟)", en="Set the minimum length(minutes) of a 'pause'."
)
help_set_pause_max = MultiText(
    cn="设置休息时长上限 (单位：分钟)", en="Set the maximum length(minutes) of a 'pause'."
)
help_set_db_folder = MultiText(
    cn="指定一个文件夹，用于保存数据库文件(tt-focus.db)。",
    en="Specify a folder for the database (tt-focus.db).",
)
help_task_name = MultiText(cn="指定任务类型。", en="Specify a task type.")
help_set_alias = MultiText(cn="修改任务的别名", en="Modifies the alias of a task.")
help_set_task_name = MultiText(cn="修改任务名称", en="Modifies the name of a task.")
help_event_id = MultiText(cn="指定事件ID。", en="Specify an event-id.")
help_set_last_work = MultiText(
    cn="修改指定事件的最后一个小节的工作时长。",
    en="Modifies the working time of the last lap of an event.",
)
help_set_notes = MultiText(
    cn="添加或修改事件备注。", en="Adds or modifies the notes of an event"
)
err_no_task = MultiText(
    cn="修改任务属性时，必须用 '--task' 参数指定任务类型。",
    en="Must use '--task' to specify a task type when modifying a task.",
)


@cli.command(
    context_settings=CONTEXT_SETTINGS, help=help_text.str(lang), name="set"
)
@click.option(
    "language",
    "-lang",
    help="Set language (语言) -> cn: 中文, en: English",
    type=click.Choice(["cn", "en"]),
)
@click.option(
    "split_min",
    "--split-min",
    type=int,
    help=help_set_split_min.str(lang),
)
@click.option(
    "pause_min",
    "--pause-min",
    type=int,
    help=help_set_pause_min.str(lang),
)
@click.option(
    "pause_max",
    "--pause-max",
    type=int,
    help=help_set_pause_max.str(lang),
)
@click.option(
    "db_folder",
    "-db",
    "--db-folder",
    type=click.Path(exists=True, file_okay=False),
    help=help_set_db_folder.str(lang),
)
@click.option("task_name", "-t", "--task", help=help_task_name.str(lang))
@click.option(
    "alias",
    "-alias",
    help=help_set_alias.str(lang),
)
@click.option(
    "new_name",
    "-name",
    help=help_set_task_name.str(lang),
)
@click.option("event_id", "-e", "--event", help=help_event_id.str(lang))
@click.option(
    "last_work",
    "--last-work",
    type=int,
    help=help_set_last_work.str(lang),
)
@click.option("notes", "-notes", help=help_set_notes.str(lang))
@click.pass_context
def set_command(
    ctx: click.Context,
    language: str,
    split_min: int,
    pause_min: int,
    pause_max: int,
    db_folder: str,
    task_name: str,
    alias: str | None,
    new_name: str | None,
    last_work: int,
    event_id: str | None,
    notes: str,
):
    """Change settings of tt-focus, or properties of a task/event.

    更改 tt-focus 的设置，或更改任务/事件的属性。
    """
    if language:
        app_cfg["lang"] = language
        db.write_cfg_file(app_cfg)
        msg = MultiText(cn=" [语言] cn (中文)", en=" [language] en")
        print(msg.str(language))
        ctx.exit()

    if db_folder:
        set_db_folder(db_folder)
        ctx.exit()

    if task_name is None and (alias is not None or new_name is not None):
        print(err_no_task.str(lang))
        ctx.exit()

    with connect() as conn:
        cfg = db.get_cfg(conn).unwrap()

        if split_min:
            cfg["split_min"] = split_min
            db.update_cfg(conn, cfg)
            info = MultiText(
                cn=f"工作时长下限: {cfg['split_min']} 分钟",
                en=f"[split min] {cfg['split_min']} minutes",
            )
            print(info.str(lang))
        elif pause_min:
            cfg["pause_min"] = pause_min
            db.update_cfg(conn, cfg)
            info = MultiText(
                cn=f"休息时长下限: {cfg['pause_min']} 分钟",
                en=f"[pause min] {cfg['pause_min']} minutes",
            )
            print(info.str(lang))
        elif pause_max:
            cfg["pause_max"] = pause_max
            db.update_cfg(conn, cfg)
            info = MultiText(
                cn=f" 休息时长上限: {cfg['pause_max']} 分钟",
                en=f"[pause max] {cfg['pause_max']} minutes",
            )
            print(info.str(lang))
        elif new_name:
            util.set_task_name(conn, new_name, task_name, lang)
        elif alias:
            util.set_task_alias(conn, alias, task_name, lang)
        elif notes:
            util.set_event_notes(conn, lang, notes, event_id)
        elif last_work:
            util.set_last_work(conn, last_work, event_id, lang)
        else:
            print(ctx.get_help())


short_help = MultiText(cn="新增任务类型。", en="Add a new type of task.")

help_add_alias = MultiText(
    cn="新任务类型的别名。", en="Set an alias of the new task type."
)


@cli.command(
    context_settings=CONTEXT_SETTINGS,
    short_help=short_help.str(lang),
)
@click.argument("name")
@click.option(
    "alias",
    "-alias",
    default="",
    help=help_add_alias.str(lang),
)
@click.pass_context
def add(ctx: click.Context, name: str, alias: str):
    """Add a new type of task. 新增任务类型。"""
    with connect() as conn:
        match model.new_task(dict(name=name, alias=alias)):
            case Err(e):
                print(e.str(lang))
            case Ok(task):

                match db.insert_task(conn, task):
                    case Err(e):
                        print(e.str(lang))
                    case Ok():
                        print(f"Task added: {task}")
    ctx.exit()


short_help = MultiText(cn="任务列表或事件列表。", en="List out tasks or events.")
help_text = MultiText(
    cn="""任务列表或事件列表。

    示例：

    tt list         # 列出最近事件列表

    tt list rc163d  # 列出一个事件的详细内容

    tt list -t      # 列出全部任务类型
    """,
    en="""List out task or events.

    Examples:

    tt list         # List out recent events

    tt list rc163d  # Show details about the event

    tt list -t      # List out all task types
    """,
)
help_list_tasks = MultiText(cn="列出全部任务类型。", en="List out all task types.")
help_list_day = MultiText(
    cn="列出某一天的全部事件 (YYYY-MM-DD)", en="All events on a day (YYYY-MM-DD)"
)
help_list_month = MultiText(
    cn="列出一个月的全部事件 (YYYY-MM)", en="All events on a month (YYYY-MM)"
)
help_list_year = MultiText(
    cn="指定年份的每个月的事件数量 (YYYY)", en="Count events per month in a year (YYYY)"
)
help_list_verbose = MultiText(cn="显示更详细的信息。", en="Show more details.")


@cli.command(
    context_settings=CONTEXT_SETTINGS,
    short_help=short_help.str(lang),
    help=help_text.str(lang),
    name="list",
)
@click.option(
    "verbose",
    "-v",
    "--verbose",
    is_flag=True,
    help=help_list_verbose.str(lang),
)
@click.option(
    "t",
    "-t",
    "--tasks",
    is_flag=True,
    help=help_list_tasks.str(lang),
)
@click.option(
    "day",
    "-day",
    help=help_list_day.str(lang),
)
@click.option(
    "month",
    "-month",
    help=help_list_month.str(lang),
)
@click.option(
    "year",
    "-year",
    help=help_list_year.str(lang),
)
@click.argument("event_id", required=False)
@click.pass_context
def list_command(
    ctx: click.Context,
    verbose: bool,
    t: bool,
    event_id: str | None,
    day: str,
    month: str,
    year: str,
):
    """List out tasks or events. 任务列表或事件列表。"""
    with connect() as conn:
        if t:
            tasks = db.get_all_task(conn)
            util.show_tasks(tasks, lang)
        elif event_id:
            util.show_status(conn, lang, event_id)
        elif day:
            util.show_events_by_date(conn, day, "day", lang, verbose)
        elif month:
            util.show_events_by_date(conn, month, "month", lang, verbose)
        elif year:
            util.show_events_year_count(conn, year, lang)
        else:
            util.show_recent_events(conn, lang, verbose)

    ctx.exit()


short_help = MultiText(
    cn="启动一个事件（开始做任务）。", en="Start an event (to do a task)."
)


@cli.command(
    context_settings=CONTEXT_SETTINGS, short_help=short_help.str(lang)
)
@click.argument("task", required=False)
@click.pass_context
def start(ctx: click.Context, task: str | None):
    """List out task or events. 任务列表或事件列表。"""
    with connect() as conn:
        info = util.event_start(conn, task)
        print(info.str(lang))

    ctx.exit()


short_help = MultiText(cn="查看正在计时的事件的状态。", en="Status of the current event.")


@cli.command(
    context_settings=CONTEXT_SETTINGS, short_help=short_help.str(lang)
)
@click.pass_context
def status(ctx: click.Context):
    """Status of the current event. 查看正在计时的事件的状态。"""
    with connect() as conn:
        util.show_status(conn, lang)

    ctx.exit()


short_help = MultiText(
    cn="分割当前事件（产生一个新的工作小节）。", en="Split the current event (create a new lap)."
)


@cli.command(
    context_settings=CONTEXT_SETTINGS, short_help=short_help.str(lang)
)
@click.pass_context
def split(ctx: click.Context):
    """Split the current event (create a new lap).

    分割当前事件（产生一个新的计时小节）。
    """
    with connect() as conn:
        cfg = db.get_cfg(conn).unwrap()
        util.event_split(conn, cfg, lang)

    ctx.exit()


short_help = MultiText(
    cn="暂停当前工作（产生一个新的休息小节）。", en="Pause the current event (take a break)."
)


@cli.command(
    context_settings=CONTEXT_SETTINGS, short_help=short_help.str(lang)
)
@click.pass_context
def pause(ctx: click.Context):
    """Pause the current event (take a break).

    暂停当前工作（产生一个新的休息小节）。
    """
    with connect() as conn:
        cfg = db.get_cfg(conn).unwrap()
        util.event_pause(conn, cfg, lang)

    ctx.exit()


short_help = MultiText(cn="恢复工作（从休息回到工作）。", en="Resume the current event.")


@cli.command(
    context_settings=CONTEXT_SETTINGS, short_help=short_help.str(lang)
)
@click.pass_context
def resume(ctx: click.Context):
    """Resume the current event.

    恢复工作（从休息回到工作）。
    """
    with connect() as conn:
        cfg = db.get_cfg(conn).unwrap()
        util.event_resume(conn, cfg, lang)

    ctx.exit()


short_help = MultiText(cn="结束当前事件。", en="Stop the current event.")


@cli.command(
    context_settings=CONTEXT_SETTINGS, short_help=short_help.str(lang)
)
@click.pass_context
def stop(ctx: click.Context):
    """Stop the current event. 结束当前事件。"""
    with connect() as conn:
        cfg = db.get_cfg(conn).unwrap()
        util.event_stop(conn, cfg, lang)

    ctx.exit()


short_help = MultiText(cn="合并事件。", en="Merge events.")
help_merge_preview = MultiText(cn="预览合并结果。", en="Preview the result of merge.")


@cli.command(
    context_settings=CONTEXT_SETTINGS, short_help=short_help.str(lang)
)
@click.argument("events", type=str, nargs=-1)
@click.option(
    "preview",
    "-p",
    "--preview",
    is_flag=True,
    help=help_merge_preview.str(lang),
)
@click.pass_context
def merge(ctx: click.Context, events: tuple[str, ...], preview: bool):
    """Merge events. 合并事件。"""
    with connect() as conn:
        util.merge_events(conn, lang, preview, *events)

    ctx.exit()


short_help = MultiText(cn="删除事件或任务。", en="Delete an event or a task.")
help_del_event = MultiText(cn="指定要删除的事件的ID", en="Delete an event.")
help_del_task = MultiText(cn="指定要删除的任务类型", en="Delete a task.")
info_del = MultiText(cn="确认删除", en="Confirm deletion")
info_del_task = MultiText(
    cn="注意，会同时删除与该任务关联的全部事件，请确认",
    en="Delete the task and all events belongs to it?",
)


def del_event(conn, event_id: str) -> None:
    match db.get_event_by_id(conn, event_id):
        case Err(err):
            print(err.str(lang))
        case Ok(event):
            print()
            util.show_events(conn, [event], True)
            click.confirm(info_del.str(lang), abort=True)
            db.delete_event(conn, event_id)
            print("OK, deleted.")


def del_task(conn, name: str) -> None:
    match db.get_task_by_name(conn, name):
        case Err(err):
            print(f"{err.str(lang)}: {name}")
        case Ok(task):
            print(f"\nTask: {task}\n")
            click.confirm(info_del_task.str(lang), abort=True)
            db.delete_task(conn, task.id)
            print("OK deleted.")


@cli.command(
    context_settings=CONTEXT_SETTINGS, short_help=short_help.str(lang)
)
@click.option("event_id", "-e", "--event", help=help_del_event.str(lang))
@click.option("task_name", "-t", "--task", help=help_del_task.str(lang))
@click.pass_context
def delete(ctx: click.Context, event_id: str, task_name: str):
    """Delete an event or a task. 删除事件或任务。"""
    with connect() as conn:
        if event_id:
            del_event(conn, event_id)
        elif task_name:
            del_task(conn, task_name)
        else:
            print(ctx.get_help())

    ctx.exit()
