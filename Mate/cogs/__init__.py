
from enums import Enum

from .info import Info
from .audio import Audio


class Cogs(Enum):
    INFO = Info()
    AUDIO = Audio()
