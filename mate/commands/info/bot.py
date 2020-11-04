
from mate.core.command import command
from mate.embeds.info import BotInfoEmbed


@command(aliases=["b", "mate"])
async def bot(cog, ctx):
    await ctx.send(
        embed=BotInfoEmbed())
