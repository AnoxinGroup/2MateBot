
from .search import search_radio
from .embed import radio_play_embed
from mate.utils.audio import play_audio


async def play_radio_audio(
        ctx, voice_client, url, radio_data=None, show_embed=True):

    if show_embed and radio_data:
        await radio_play_embed(
            ctx.channel,
            radio_data.name,
            radio_data.icon,
            radio_data.homepage)

    play_audio(voice_client, url)


async def search_and_play(ctx, voice_client, url_or_name):
    radio_found = search_radio(url_or_name)

    if not radio_found:
        raise Exception("Unable to find the radio by this name")

    await play_radio_audio(
        ctx, voice_client, radio_found.url, radio_found)
