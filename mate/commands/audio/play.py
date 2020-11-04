
from mate.core.command import command
from mate.utils.voice import (
    get_voice_client, connect_voice_channel)
from mate.utils.audio import play_certain_audio


def _normalize_name(name_or_url):
    if not isinstance(name_or_url, str):
        return " ".join(name_or_url)
    else:
        return name_or_url


@command(aliases=["pl"])
async def play(cog, ctx, *url_or_name):
    url_or_name = _normalize_name(url_or_name)

    voice_client = get_voice_client(
        ctx.bot.voice_clients, ctx.guild)

    if not voice_client:
        voice_client = await connect_voice_channel(
            ctx.author.voice)

    await play_certain_audio(ctx, voice_client, url_or_name)
