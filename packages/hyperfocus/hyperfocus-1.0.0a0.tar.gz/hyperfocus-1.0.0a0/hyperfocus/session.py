from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

import click

from hyperfocus.config.config import Config
from hyperfocus.database import database
from hyperfocus.exceptions import SessionError
from hyperfocus.services import DailyTracker


if TYPE_CHECKING:
    from typing import Callable


class Session:
    _database = database

    def __init__(self) -> None:
        self._config = Config.load()
        self._database.connect(self._config["core.database"])
        self._date = datetime.datetime.now()
        self._daily_tracker = DailyTracker.from_date(self._date)
        self._callback_commands: list[Callable] = []

    @property
    def config(self) -> Config:
        return self._config

    @property
    def date(self) -> datetime.date:
        return self._date.date()

    @property
    def daily_tracker(self) -> DailyTracker:
        return self._daily_tracker

    @property
    def callback_commands(self) -> list[Callable]:
        return self._callback_commands

    def register_callback(self, callback: Callable) -> None:
        self._callback_commands.append(callback)

    def bind_context(self, ctx: click.Context) -> None:
        ctx.obj = self
        ctx.call_on_close(self.teardown)

    def teardown(self) -> None:
        self._database.close()


def get_current_session() -> Session:
    ctx = click.get_current_context()
    if not isinstance(ctx.obj, Session):
        raise SessionError(
            "It appears that you are trying to invoke a command outside "
            "of the CLI context"
        )

    return ctx.obj
