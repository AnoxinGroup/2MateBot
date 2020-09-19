
from Mate.embeds import Embeds

from Mate.core.command import Command


class BotInfo(Command):

    async def oncall(self, cog, ctx):
        await ctx.send(embed=Embeds.BOT)
