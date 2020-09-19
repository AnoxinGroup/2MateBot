
from Mate.cogs import Cogs

from Mate.core.bot import Bot


class ZMateBot(Bot):

    def __init__(self, *args, **kwargs):
        super(ZMateBot, self).__init__(*args, **kwargs)

        self.add_cog(Cogs.INFO)
