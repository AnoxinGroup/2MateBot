
from discord.ext.commands import (
    Command as _Command
)


class Command(_Command):

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(
            self.oncall, **kwargs)
        self.error(self.onerror)

    async def oncall(self, *args, **kwargs):
        pass

    async def onerror(self, *args, **kwargs):
        pass


__all__ = (
    "Command",
)
