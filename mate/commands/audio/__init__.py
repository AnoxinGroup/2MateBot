
from .play import play
from .stop import stop
from .leave import leave
from .radio import radio
from mate.core.command import command
from mate.utils.embed import show_embed
from mate.embeds.audio import AudioInfoEmbed


@command(aliases=["aud"])
async def audio(cog, ctx):
    await show_embed(
        ctx.channel, AudioInfoEmbed())


__all__ = (
    "audio",
    "stop",
    "play",
    "leave",
    "radio"
)
