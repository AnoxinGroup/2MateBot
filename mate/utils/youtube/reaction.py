
from mate.meta.youtube import YoutubePlayMeta


async def react_on_play(message, emoji=YoutubePlayMeta.PLAY_REACTION_EMOJI):
    await message.add_reaction(emoji)
