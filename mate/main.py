
from discord import Activity, ActivityType
from discord.ext.commands import Bot

from mate.cogs.info import Info
from mate.cogs.audio import Audio


class ZMateBot(Bot):

    def __init__(self, *args, **kwargs):
        super(ZMateBot, self).__init__(*args, **kwargs, case_insensitive=True)

        self.remove_command("help")

        self.add_cog(Info())
        self.add_cog(Audio(self))

    async def on_ready(self):
        await self.change_presence(
            activity=Activity(
                type=ActivityType.watching,
                name="2Help | 2Mate")
        )
