
#  ___ _____ _____ ____  _____ _____
# |_  |  _  |  |  |    \|     |     |
# |  _|     |  |  |  |  |-   -|  |  |
# |___|__|__|_____|____/|_____|_____|
# 2AUDIO Utility Module
#

"""Audio Utilities

2ABOUT
------
This utility provides base abilities to
play only one audio content or whole audio
queue in the voice channel, also this module
contains helpful methods to switch an audio
in the certain audio queue, stop and reset audio queue.

2EXAMPLE
--------

That's example how to play audio stream directly.
.. code-block:: python

    # you need voice client first
    voice_client = ...

    # pass the URL link, that refer
    # to the direct audio stream
    audio = Audio("...")

    await play_audio(ctx, voice_client, audio)


Another example how to add some elements to the audio
queue and play them.
.. code-block:: python

    voice_client = ...

    # get an audio queue for the certain guild
    audio_queue = get_audio_queue(guild_for=ctx.guild)

    audio1 = Audio("...")
    audio2 = Audio("...")

    audio_queue.add(audio1)
    audio_queue.add(audio2)

    await play_audio_queue(ctx, voice_client, audio_queue)

"""

from sys import platform
from functools import partial
from discord import FFmpegPCMAudio


_guilds_audio_queues = {}


class AudioData:

    def __init__(self, url):
        self.url = url

    @property
    def source(self):
        """

        Returns a specific audio source.

        """
        return


class Audio(FFmpegPCMAudio):

    def __init__(self, data):
        self.data = data

        if platform == "win32":
            executable = "ffmpeg/ffmpeg.exe"
        else:
            executable = "ffmpeg"

        super().__init__(source=self.data.url, executable=executable)

    async def on_playing(self, ctx, voice):
        pass

    async def on_exhausted(self, asked, voice):
        pass


class AudioQueue:

    index = 0

    def __init__(self, max_count):
        self._max_count = max_count

        self._audios = []

    async def on_exhausted(self, ctx, voice_client):
        self.reset()

    def is_empty(self):
        return len(self._audios) == 0

    def is_begun(self):
        return self.index == 0

    def is_ended(self):
        return self.index == len(self._audios) - 1

    def current(self) -> Audio:
        if self.is_empty():
            return
        return self.get(self.index)

    def next(self):
        self.index += 1

    def previos(self):
        self.index -= 1

    def add(self, audio_data: AudioData):
        self._audios.append(audio_data)

    def get(self, index):
        return self._audios[index]

    def remove(self, index):
        del self._audios[index]

    def get_all(self):
        return self._audios

    def count(self):
        ind = 0

        for audio in self._audios:
            ind += 1
            yield (ind, audio)

    def reset(self):
        self.index = 0
        self._audios.clear()


def add_audio_queue(queue, guild_for):
    _guilds_audio_queues[guild_for.id] = queue


def create_audio_queue(max_count, guild_for):
    add_audio_queue(AudioQueue(max_count), guild_for)


def has_audio_queue(guild) -> bool:
    return guild.id in _guilds_audio_queues


def get_audio_queue(guild_for) -> AudioQueue:
    guild_id = guild_for.id

    if guild_id not in _guilds_audio_queues:
        create_audio_queue(20, guild_for)

    return _guilds_audio_queues[guild_id]


def remove_audio_queue(guild_for) -> int:
    guild_id = guild_for.id

    if guild_id not in _guilds_audio_queues:
        return -1

    del _guilds_audio_queues[guild_id]


def audio_switcher(asked, voice_client, audio, audio_queue, *args):

    run = voice_client.loop.run_until_complete

    run(
        exhaust_audio(asked, voice_client, audio))

    run(
        play_next_audio(asked, voice_client, audio_queue))


async def exhaust_audio(asked, voice_client, audio):
    await audio.on_exhausted(asked, voice_client)


async def stop_audio(asked, voice_client):
    #
    # Reset the `after` callback of the
    # current audio, to prevent audio
    # switching by this callback.
    voice_client._player.after = None

    if voice_client.source:
        #
        # Tries to exhaust last audio.
        await exhaust_audio(asked, voice_client, voice_client.source)

    voice_client.stop()


async def play_audio(
        ctx, voice_client, audio_data: AudioData, after=None):

    audio_source = audio_data.source

    if voice_client.is_playing():
        await stop_audio(ctx, voice_client)

    voice_client.play(
        audio_source)

    await audio_source.on_playing(ctx, voice_client)


async def play_audio_queue(
        ctx, voice_client, queue: AudioQueue):

    audio = queue.current()

    partial_after = partial(
        audio_switcher, ctx, voice_client, audio, queue)

    await play_audio(
        ctx,
        voice_client,
        audio,
        partial_after
    )


async def stop_audio_queue(asked, voice_client, queue: AudioQueue) -> int:

    if queue.is_empty():
        return -1

    await stop_audio(asked, voice_client)

    await queue.on_exhausted(asked, voice_client)


async def play_next_audio(ctx, voice_client, queue: AudioQueue) -> int:

    if queue.is_empty() or queue.is_ended():
        return await stop_audio_queue(ctx, voice_client, queue)

    queue.next()

    await play_audio_queue(
        ctx,
        voice_client,
        queue)


async def play_previos_audio(ctx, voice_client, queue: AudioQueue) -> int:

    if queue.is_empty() or queue.is_begun():
        return -1

    queue.previos()

    await play_audio_queue(
        ctx,
        voice_client,
        queue)


async def play_certain_audio(
        ctx, voice_client, audio_data: AudioData):

    audio_queue = get_audio_queue(guild_for=ctx.guild)

    audio_queue.add(audio_data)

    if not voice_client.is_playing():
        await play_audio_queue(ctx, voice_client, audio_queue)
