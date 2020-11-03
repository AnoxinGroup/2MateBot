
from .meta import YT_FULLNAME
from urllib.parse import urljoin
from youtube_search import YoutubeSearch


class YoutubeSearchData(object):
    """

    Small structure that temporaly storage
    some useful data received when the raw
    one loaded by the `youtube_search` tool.
    Basically, this structure stores video url
    suffix.

    """

    def __init__(self, **kwargs):
        self.id = kwargs.pop("id", "")


def search_videos(name, videos=10):
    return [
        YoutubeSearchData(**video) for video in YoutubeSearch(
            name, max_results=videos).videos
    ]


def search_video(name):
    videos = search_videos(name, videos=1)

    if videos:
        return videos[0]
