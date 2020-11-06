
import pafy
from mate.meta.youtube import YoutubeDLMeta


async def load_youtube_data(url):
    return pafy.new(
        url, ydl_opts=YoutubeDLMeta.YTDL_OPTIONS)
