
from mate.cogs import Cogs
from mate.core.bot import Bot
from mate.meta.bot import BotMeta
from discord import Activity, ActivityType
from mate.utils.presence import change_presence


class ZMateBot(Bot):

    def __init__(self, *args, **kwargs):
        super(ZMateBot, self).__init__(*args, **kwargs, case_insensitive=True)

        self.add_cog(Cogs.INFO)
        self.add_cog(Cogs.AUDIO)

    async def on_ready(self):
        await change_presence(
            self, Activity(
                type=ActivityType.watching, name=BotMeta.ACTIVITY_NAME))
