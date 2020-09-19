
from os import environ

from enums import Enum


class BotEmbedMeta(Enum):

    DESC = """

        2Mate is a bot specially designed
        for a Dusework's Discord server,
        but anyway it can be used within
        other Discord server as well.

        This Project meant to be open-source.

        All helpful links can be found below.

        [GitHub](https://github.com/dusework/2MateBot)

    """

    TITLE = "About"

    COLOR = 0x00ff00


class BaseMeta(Enum):

    TOKEN = environ.get('M2TOKEN')

    PREFIX = '2'
