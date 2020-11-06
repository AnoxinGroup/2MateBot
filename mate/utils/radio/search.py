
import pyradios


class RadioSearchData(object):

    def __init__(self, **kwargs):
        self.url = kwargs.pop("url_resolved")
        self.name = kwargs.pop("name")
        self.tags = kwargs.pop("tags")
        self.icon = kwargs.pop("favicon")
        self.homepage = kwargs.pop("homepage")


def search_radios(name, limit):
    radio_browser = pyradios.RadioBrowser()

    return [
        RadioSearchData(**data) for data in radio_browser.search(
            name=name, limit=limit, name_exact=True)
    ]


def search_radio(name, limit=1):
    radios = search_radios(name, limit)

    if radios:
        return radios[0]
