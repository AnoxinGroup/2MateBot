

_EMBED_DESC = """

<:2mate:773599716729683999>**Mate** command list \
can be found here [click]().

Anyway, if it is unable to get command overview
from the website, you can see the usage hint of
the commands by invoking such commands:

<:2mate:773599716729683999>**info**
Show information about helpful commands, such as
*help*.

<:2mate:773599716729683999>**audio**
Show up all audio commands.

"""


class BotHelpMeta:

    EMBED_DESC = _EMBED_DESC

    EMBED_TITLE = "Command Overview"

    EMBED_COLOR = 0x43b581

    EMBED_THUMBNAIL = "https://github.com/dusework/2MateBot/" + \
        "blob/master/assets/images/bot/avatar_white.png?raw=true"

    EMBED_FOOTER_NAME = "Command list generated with Sphinx"
