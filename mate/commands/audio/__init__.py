
from .play import play
from .stop import stop
from .leave import leave
from mate.core.command import command


@command(aliases=["aud"])
async def audio(cog, ctx):
    pass


__all__ = (
    "audio",
    "stop",
    "play",
    "leave"
)
