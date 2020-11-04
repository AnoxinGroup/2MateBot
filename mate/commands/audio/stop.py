
from mate.core.command import command
from mate.utils.audio import stop_audio
from mate.utils.voice import get_voice_client


@command(aliases=["st"])
async def stop(cog, ctx):
    voice_client = get_voice_client(
        ctx.bot.voice_clients, ctx.guild)

    if not voice_client:
        return

    stop_audio(voice_client)
