
from mate.exceptions.audio import NowhereLeftFrom


async def disconnect_voice_channel(voice_client):
    if not voice_client:
        raise NowhereLeftFrom
    await voice_client.disconnect()
