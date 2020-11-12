
from discord.utils import get


def get_certain_vcli(voice_clients_list, current_guild):
    return get(
        voice_clients_list, guild=current_guild)


async def connect_voice_channel(member_voice_state):
    if not member_voice_state:
        return
    return await member_voice_state.channel.connect()


async def get_voice_client(ctx):
    voice_client = get_certain_vcli(ctx.bot.voice_clients, ctx.guild)

    if not voice_client:
        voice_client = await connect_voice_channel(ctx.author.voice)

    return voice_client
