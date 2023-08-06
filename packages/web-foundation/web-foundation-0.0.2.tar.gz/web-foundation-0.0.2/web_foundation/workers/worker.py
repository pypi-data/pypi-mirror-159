from typing import List

from web_foundation.app.infrastructure.provide.initiator import Initiator
from web_foundation.kernel import Isolate


class Worker(Isolate):
    _initiators: List[Initiator]

    def __init__(self, async_mode: bool = False, debug: bool = False):
        super().__init__(async_mode, debug)
        self._initiators = []

    @property
    def initiators(self) -> List[Initiator]:
        return self._initiators

    @initiators.setter
    def initiators(self, value: List[Initiator]):
        self._initiators = value

    async def on_isolate_up(self, initiators: List[Initiator]):
        for init in initiators:
            await init.setup_connection(self.ctx)
