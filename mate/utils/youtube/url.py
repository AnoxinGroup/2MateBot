
from .meta import (
    YT_NETLOC1, YT_NETLOC2)
from discord.utils import get
from urllib.parse import urlparse


def is_youtube_link(url) -> bool:
    parsed_url = urlparse(url)

    if YT_NETLOC1 in parsed_url.netloc or YT_NETLOC2 in parsed_url.netloc:
        return True
    else:
        return False


def get_stream_by_bitrate(streams, bitrate):
    for stream in streams:
        if stream.rawbitrate < bitrate:
            return stream


def get_stream_url(video_data):
    stream = video_data.getbest()

    if not stream:
        raise Exception("no avaible stream found")

    return stream.url
