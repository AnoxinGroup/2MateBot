
from mate.utils.url import is_url
from mate.utils.youtube import (
    is_youtube_link,
    play_youtube, search_play_youtube)


async def play_certain_audio(ctx, voice_client, query):

    if is_url(query):
        if is_youtube_link(query):
            await play_youtube(ctx, voice_client, query)

    else:
        await search_play_youtube(ctx, voice_client, query)
