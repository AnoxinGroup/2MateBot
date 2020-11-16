
from discord import Embed


MAX_TITLE_SIZE = 30


class AudioQueueEmbed(Embed):

    def __init__(self, audio_queue):
        super().__init__(
            description=self._prepare_queue_string(audio_queue))

    def _reduce_title_name(self, title: str):
        if len(title) > MAX_TITLE_SIZE:
            return title[:MAX_TITLE_SIZE] + "..."

    def _prepare_queue_string(self, audio_queue):
        out_str = ""

        current_audio = audio_queue.current()

        for index, audio in audio_queue.count():
            audio_title = self._reduce_title_name(audio.title)

            if audio == current_audio:
                out_str += "**%d: *%s* **\n" % (index, audio_title)
            else:
                out_str += "%d: *%s*\n" % (index, audio_title)

        if not out_str:
            return "Nothing to play"

        return out_str
