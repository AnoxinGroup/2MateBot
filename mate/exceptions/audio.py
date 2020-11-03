
from mate.meta.voice import VoiceErrorMeta


class NoVoiceConnection(Exception):

    def __init__(self, message=None):
        super().__init__(message or VoiceErrorMeta.EXC_TEXT)


class NowhereLeftFrom(Exception):
    pass
