
from discord.utils import get


def get_voice_client(voice_clients_list, current_guild):
    return get(
        voice_clients_list, guild=current_guild)
