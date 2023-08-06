import asyncio
from asyncio import Future
from typing import List

from aioprocessing import AioProcess

from web_foundation.kernel import NamedContext
from web_foundation.kernel.isolates.channel import IChannel


class Isolate:
    debug: bool
    _name: str
    _named_isolates: List[str] = []
    _channel: IChannel
    _proc: AioProcess
    _async_mode: bool
    _named_ctx: NamedContext

    def __init__(self, async_mode: bool = False, debug: bool = False):
        self._name = ""
        self._channel = IChannel(self.name)
        self._async_mode = async_mode
        self._proc = AioProcess(target=self._startup)
        self.debug = debug

    @property
    def name(self):
        self._check_name()
        return self._name

    @name.setter
    def name(self, value: str):
        if value in self._named_isolates:
            raise AttributeError("Isolate.name nums be uniq")
        self._name = value
        self._named_isolates.append(value)

    @property
    def ctx(self) -> NamedContext:
        return self._named_ctx

    @ctx.setter
    def ctx(self, value: NamedContext):
        self._named_ctx = value

    def _check_name(self):
        if self.name == "":
            raise AttributeError("Isolate must be attached to App (App.add_isolate)")

    @property
    def app_name(self):
        return self.name.split(".")[0]

    async def async_run(self):
        raise NotImplementedError

    def sync_run(self):
        raise NotImplementedError

    def _startup(self):
        if self._async_mode:
            asyncio.run(self.async_run())
        else:
            self.sync_run()

    async def _exec(self):
        self._proc.start()

    def perform(self) -> Future:
        return asyncio.ensure_future(self._exec())

    @property
    def channel(self) -> IChannel:
        return self._channel

    @property
    def pid(self) -> int:
        return self._proc.pid

    @property
    def process(self) -> AioProcess:
        return self._proc
