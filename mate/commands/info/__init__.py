
from .bot import bot
from .help import help
from mate.core.command import command
from mate.utils.embed import show_embed
from mate.embeds.info import BotInfoEmbed


@command(aliases=["inf"])
async def info(cog, ctx):
    await show_embed(
        ctx.channel, BotInfoEmbed())

__all__ = (
    "bot",
    "help"
)
