
from discord.ext.commands import Cog, command

from mate.utils.url import is_url
from mate.utils.radio import search_radio
from mate.utils.voice import get_voice_client, get_certain_vcli
from mate.embeds.audio import AudioQueueEmbed
from mate.utils.autoplay import play_certain_audio

from mate.utils.audio import (
    play_audio,
    stop_audio,
    get_audio_queue,
    play_audio_queue,
    stop_audio_queue,
    remove_audio_queue,
    play_next_audio, play_previos_audio)

from mate.utils.youtube import (
    is_youtube_link, search_youtube, get_youtube)


class Audio(Cog):

    def __init__(self, bot):
        self.bot = bot

    # @command(aliases=["aud"])
    # async def audio(self, ctx):
    #     """

    #     Shows up an informations about this category.

    #     """
    #     await ctx.send(
    #         embed=AudioInfoEmbed())

    @command(aliases=["pl"])
    async def play(self, ctx, *, url_or_name=""):
        """

        Searches and plays an audio fragment by the given
        URL link or name.
        * If the link do not refer to any recognised
        web service, bot tries to play it as a direct audio stream
        and returns error on failure.
        * If the given string is not
        URL at all, 2Mate tries to find a video from the Youtube
        and play it in the current voice channel.
        * If the string is
        not given, bot will try to restore the last audio queue and play
        it.

        """

        voice_client = await get_voice_client(ctx)

        #
        # RESUME BLOCK
        audio_queue = get_audio_queue(guild_for=ctx.guild)

        if not url_or_name:
            if not audio_queue.is_empty():
                return await play_audio_queue(
                    ctx, voice_client, audio_queue)
            else:
                return

        #
        # AUDIO PLAY BLOCK
        await play_certain_audio(ctx, voice_client, url_or_name)

    @command(aliases=["st"])
    async def stop(self, ctx):
        """

        Stops playing an audio queue. Can be resumed then
        by the command `play` or `resume`.

        """
        voice_client = await get_voice_client(ctx)

        if not voice_client:
            return

        audio_queue = get_audio_queue(guild_for=ctx.guild)

        if not voice_client.is_playing():
            return

        await stop_audio_queue(ctx.author, voice_client, audio_queue)

        await ctx.message.add_reaction("🛑")

    @command(aliases=["nx"])
    async def next(self, ctx):
        """

        Plays the next song in the current audio queue. When
        the audio ended (The last audio is playing
        at the moment), bot reacts on your message with
        error reaction.

        """
        voice_client = await get_voice_client(ctx)

        if not voice_client:
            return

        audio_queue = get_audio_queue(
            guild_for=ctx.guild)

        result = await play_next_audio(
            ctx, voice_client, audio_queue)

        if result == -1:
            return

        await ctx.message.add_reaction("⏭️")

    @command(aliases=["pr", "prev"])
    async def previos(self, ctx):
        """

        Plays the previos song in the current audio queue. When
        the audio queue begun (The first audio is playing),
        bot reacts on your message with error reaction.

        """
        voice_client = await get_voice_client(ctx)

        if not voice_client:
            return

        audio_queue = get_audio_queue(
            guild_for=ctx.guild)

        result = await play_previos_audio(
            ctx, voice_client, audio_queue)

        if result == -1:
            return

        await ctx.message.add_reaction("⏮️")

    @command(aliases=["q"])
    async def queue(self, ctx):
        """

        Shows up elements of the current audio queue in
        this format:
            1. Song #1
            2. Song #2
            ...

        """

        await ctx.message.add_reaction("🔢")

        audio_queue = get_audio_queue(
            guild_for=ctx.guild)

        await ctx.send(embed=AudioQueueEmbed(audio_queue))

    @command(aliases=["r"])
    async def reset(self, ctx):
        """

        Shows up elements of the current audio queue in
        this format:
            1. Song #1
            2. Song #2
            ...

        """

        await ctx.message.add_reaction("🔄")

        audio_queue = get_audio_queue(
            guild_for=ctx.guild)

        audio_queue.reset()

    @command(aliases=["lv"])
    async def leave(self, ctx):
        """

        Leaves the current voice channel.

        """

        voice_client = await get_voice_client(ctx)

        if voice_client.is_playing():
            await stop_audio(voice_client)

        remove_audio_queue(ctx.guild)

        await voice_client.disconnect()

    @command(aliases=["rad"])
    async def radio(self, ctx, *, name):
        """

        Searches and plays a radio audio stream.

        """

        voice_client = await get_voice_client(ctx)

        radio_audio = search_radio(name)

        if not radio_audio:
            pass

        await play_audio(ctx, voice_client, radio_audio)

    @Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        voice_client = get_certain_vcli(self.bot.voice_clients, member.guild)

        if not voice_client:
            return

        audio_queue = get_audio_queue(guild_for=member.guild)

        if voice_client.channel == before.channel:
            if not after.channel and len(before.channel.members) < 2:
                await stop_audio_queue(member, voice_client, audio_queue)

                await voice_client.disconnect()
