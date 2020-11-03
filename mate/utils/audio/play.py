
from discord import FFmpegPCMAudio


def play_audio(voice_client, url):
    voice_client.play(FFmpegPCMAudio(source=url))
