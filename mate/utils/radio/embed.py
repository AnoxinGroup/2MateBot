
from mate.utils.embed import show_embed
from mate.embeds.radio import RadioPlayEmbed


async def radio_play_embed(
        channel,
        radio_name,
        radio_icon,
        radio_home):

    return await show_embed(
        channel,
        RadioPlayEmbed(
            radio_name, radio_icon, radio_home)
    )
