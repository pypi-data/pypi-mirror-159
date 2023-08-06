import socket
from typing import List

from pydantic import BaseModel as PDModel
from sanic import Sanic
from sanic.server.socket import bind_socket

from web_foundation.kernel import NamedContext
from web_foundation.workers.web.sanic_ext.pipline_ext import Pipeline, PipelinesExt
from web_foundation.workers.worker import Worker


class StreamingConf(PDModel):
    listen_timeout: float
    ping_timeout: float


class ServerConfig(PDModel):
    host: str
    port: int
    streaming: StreamingConf | None


class WebServer(Worker):
    config: ServerConfig
    pipelines_ext: PipelinesExt

    def __init__(self, config: ServerConfig, sock: socket.socket = None, **kwargs):
        super().__init__(**kwargs)
        self.config = config
        self.socket = sock if sock else self.create_socket(config)
        self.sanic_app = Sanic(self.name)
        self.sanic_app.after_server_stop(self.close)
        self.pipelines_ext = PipelinesExt()

    def close(self, *args, **kwargs):
        self.socket.close()

    def apply_named_ctx(self, ctx: NamedContext):
        self.sanic_app.ctx.named_ctx = ctx
        self.sanic_app.ctx.channel = self.channel

    def add_pipelines(self, pipelines: List[Pipeline] | Pipeline):
        if isinstance(pipelines, list):
            self.pipelines_ext.pipelines = pipelines
        else:
            self.pipelines_ext.pipelines.append(pipelines)

    def _init_ext(self):
        self.sanic_app.extend(extensions=[self.pipelines_ext], config={})

    async def async_run(self):
        await self.on_isolate_up(self.initiators)
        try:
            ctx = self.sanic_app.ctx.named_ctx
        except AttributeError:
            raise AttributeError("Please pass NamedContext before start ( apply_named_ctx() )")
        self._init_ext()
        try:
            self.sanic_app.run(sock=self.socket)
        except KeyboardInterrupt:
            pass

    @staticmethod
    def create_socket(config: ServerConfig):
        sock = bind_socket(config.host, config.port)
        sock.set_inheritable(True)
        return sock
