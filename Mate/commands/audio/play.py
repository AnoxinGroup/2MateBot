
from mate.core.command import command
from mate.utils.voice import (
    get_voice_client, connect_voice_channel)
from mate.utils.audio import play_certain_audio


@command(aliases=["Play", "Pl"])
async def play(cog, ctx, url):
    voice_client = get_voice_client(
        ctx.bot.voice_clients, ctx.guild)

    if not voice_client:
        voice_client = await connect_voice_channel(
            ctx.author.voice)

    await play_certain_audio(ctx, voice_client, url)
