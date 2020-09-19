
from Mate.main import ZMateBot
from Mate.meta import BaseMeta
from Mate.core.bot import Bot


Bot.run(
    ZMateBot(
        command_prefix=BaseMeta.PREFIX),
    BaseMeta.TOKEN
)
