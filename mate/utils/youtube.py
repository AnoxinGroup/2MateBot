
from pafy import new
from typing import Optional
from urllib.parse import urlparse
from youtube_search import YoutubeSearch

from mate.embeds.youtube import YoutubePlayEmbed

from mate.utils.audio import (
    Audio, AudioData,
    play_certain_audio)


YT_NETLOC1 = "youtu.be"

YT_NETLOC2 = "youtube"

YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'nocheckcertificate': True,
    'logtostderr': True,
    "extractaudio": True,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    "audioformat": "opus",
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}


class YoutubeAudio(Audio):

    _embed = None

    async def on_playing(self, ctx, voice_client):
        self._embed = await ctx.send(
            embed=YoutubePlayEmbed(self.data))

    async def on_exhausted(self, asked, voice_client):
        if self._embed:
            await self._embed.delete()


class YoutubeData(AudioData):

    def __init__(self, url):
        self._pafy = self._try_load(url, 2)

    def _try_load(self, url, retry):
        retries = 0
        unsuccessful = False

        while not unsuccessful:
            try:
                return new(url, ydl_opts=YTDL_OPTIONS)
            except Exception:
                if retries == retry:
                    unsuccessful = True
                retries += 1

        return

    @property
    def stream(self):
        return self._pafy.getbest()

    @property
    def url(self):
        return self.stream.url

    @property
    def title(self):
        return self._pafy.title

    @property
    def thumbnail(self):
        return self._pafy.bigthumbhd

    @property
    def source(self) -> YoutubeAudio:
        return YoutubeAudio(self)


def get_youtube(url) -> Optional[YoutubeData]:
    return YoutubeData(url)


def search_youtube(name) -> Optional[YoutubeData]:
    youtube_result = YoutubeSearch(name, max_results=1)

    if not youtube_result.videos:
        return

    search_result = youtube_result.videos[0]

    if "id" in search_result:
        return get_youtube(search_result["id"])


def is_youtube_link(url) -> bool:
    parsed_url = urlparse(url)

    return YT_NETLOC1 in parsed_url.netloc or YT_NETLOC2 in parsed_url.netloc


async def play_youtube(ctx, voice_client, url):
    await play_certain_audio(
        ctx,
        voice_client,
        get_youtube(url))


async def search_play_youtube(ctx, voice_client, url):
    await play_certain_audio(
        ctx,
        voice_client,
        search_youtube(url))
