
from mate.core.command import command
from mate.utils.voice import (
    get_voice_client, connect_voice_channel)
from mate.utils.url import is_url
from mate.utils.radio import play_radio_audio, search_and_play


@command(aliases=["rad"])
async def radio(cog, ctx, *, url_or_name):

    voice_client = get_voice_client(
        ctx.bot.voice_clients, ctx.guild)

    if not voice_client:
        voice_client = await connect_voice_channel(
            ctx.author.voice)

    if is_url(url_or_name):
        await play_radio_audio(ctx, voice_client, url_or_name)
    else:
        await search_and_play(ctx, voice_client, url_or_name)
