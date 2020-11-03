
from .play import play_audio
from mate.utils.url import is_url
from mate.utils.youtube import (
    is_youtube_link, play_youtube_audio, search_and_play)


async def play_certain_audio(ctx, voice_client, url):
    if is_url(url):
        if is_youtube_link(url):
            await play_youtube_audio(ctx, voice_client, url)
        else:
            play_audio(voice_client, url)
    else:
        await search_and_play(ctx, voice_client, url)
