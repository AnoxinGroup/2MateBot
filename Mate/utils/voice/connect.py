
from mate.exceptions.audio import NoVoiceConnection


async def connect_voice_channel(member_voice_state):
    """

    Connects bot to the voice channel by the
    member voice state. If member has no voice
    state, this function raises `NoVoiceConnection` error.

    """
    if not member_voice_state:
        raise NoVoiceConnection()
    return await member_voice_state.channel.connect()
