
from mate.cogs import Cogs
from mate.core.bot import Bot


class ZMateBot(Bot):

    def __init__(self, *args, **kwargs):
        super(ZMateBot, self).__init__(*args, **kwargs, case_insensitive=True)

        self.add_cog(Cogs.INFO)
        self.add_cog(Cogs.AUDIO)
