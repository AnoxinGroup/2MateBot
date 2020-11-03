
from mate.meta.audio import AudioErrorMeta
from mate.embeds.error import CommandErrorEmbed


class AudioErrorEmbed(CommandErrorEmbed):

    def __init__(self, cog_name, command_name, error_text):
        super().__init__(
            cog_name,
            command_name,
            error_text,
            AudioErrorMeta.EMBED_AUTHOR_IMAGE)
