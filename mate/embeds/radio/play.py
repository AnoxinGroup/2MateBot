
from mate.core.embed import Embed
from mate.meta.radio import RadioPlayMeta


class RadioPlayEmbed(Embed):

    def __init__(
            self,
            radio_name,
            radio_icon,
            radio_home):

        super().__init__(
            title=radio_name,
            color=RadioPlayMeta.COLOR,
            description=radio_home
        )

        self.set_thumbnail(
            url=radio_icon)
