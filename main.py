
from mate.main import ZMateBot
from mate.meta.base import BaseMeta
from mate.core.bot import Bot


Bot.run(
    ZMateBot(
        command_prefix=BaseMeta.PREFIX),
    BaseMeta.TOKEN
)
