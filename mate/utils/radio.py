
from typing import Optional
from pyradios import RadioBrowser

from mate.embeds.radio import RadioPlayEmbed

from mate.utils.audio import (
    Audio, AudioData,
    play_certain_audio)


class RadioAudio(Audio):

    _embed = None

    async def on_playing(self, ctx, voice_client):
        self._embed = await ctx.send(
            embed=RadioPlayEmbed(self.data))

    async def on_exhausted(self, asked, voice_client):
        if self._embed:
            await self._embed.delete()


class RadioData(AudioData):

    def __init__(self, name):
        self._browser = RadioBrowser()

        self._radio_data = self._browser.search(
            name=name, limit=1, name_exact=False)[0]

    @property
    def url(self):
        return self._radio_data.get("url_resolved", "")

    @property
    def title(self):
        return self._radio_data.get("name", "")

    @property
    def thumbnail(self):
        return self._radio_data.get("favicon", "")

    @property
    def source(self):
        return RadioAudio(self)


def get_radio(name) -> RadioData:
    return RadioData(name)


def search_radio(name) -> Optional[RadioData]:
    return get_radio(name)


async def play_radio(ctx, voice_client, name):
    await play_certain_audio(
        ctx,
        voice_client,
        search_radio(name),
        RadioAudio)
