
from urllib.parse import urlparse


def is_url(url) -> bool:
    parsed_url = urlparse(url)

    if parsed_url.scheme and parsed_url.netloc:
        return True
    else:
        return False
