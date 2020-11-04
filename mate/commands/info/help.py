
from mate.core.command import command
from mate.embeds.info import BotHelpEmbed


@command(aliases=["h"])
async def help(cog, ctx):
    await ctx.send(
        embed=BotHelpEmbed())
