
from mate.core.command import command
from mate.utils.voice import (
    get_voice_client, disconnect_voice_channel)


@command(aliases=["lv"])
async def leave(cog, ctx):
    voice_client = get_voice_client(
        ctx.bot.voice_clients, ctx.guild)

    await disconnect_voice_channel(voice_client)
