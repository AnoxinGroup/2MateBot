
import pafy


def load_youtube_data(url):
    successfully_load = False

    #
    # Pafy sometimes cannot load youtube data
    # for the first time, so retry this until
    # the video data is not loaded.
    while not successfully_load:
        try:
            loaded_content = pafy.new(url)
        except Exception:
            pass
        else:
            successfully_load = True

    return loaded_content
