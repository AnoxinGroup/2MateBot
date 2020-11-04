
from sys import platform
from discord import FFmpegPCMAudio


def play_audio(voice_client, url):
    if platform == "win32":
        voice_client.play(
            FFmpegPCMAudio(source=url, executable="ffmpeg/ffmpeg.exe"))
    else:
        voice_client.play(FFmpegPCMAudio(source=url))
