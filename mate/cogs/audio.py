
from mate.core.cog import Cog
from mate.embeds.audio import AudioErrorEmbed
from mate.commands.audio import (
    play, stop, leave, radio, audio)


class Audio(Cog):

    play = play
    stop = stop
    leave = leave
    radio = radio
    audio = audio

    async def cog_command_error(self, ctx, error):
        await super().cog_command_error(ctx, error, AudioErrorEmbed)
