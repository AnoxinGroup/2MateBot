
from mate.core.embed import Embed
from mate.meta.error import CommandErrorMeta


class CommandErrorEmbed(Embed):

    def __init__(
            self,
            cog_name,
            command_name,
            error_text,
            error_icon=CommandErrorMeta.EMBED_AUTHOR_IMAGE):

        super().__init__(
            title=error_text,
            color=CommandErrorMeta.COLOR)

        self.set_author(
            icon_url=error_icon,
            name=CommandErrorMeta.EMBED_AUTHOR_NAME % cog_name)
