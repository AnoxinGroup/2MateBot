
import pafy


async def load_youtube_data(url, retry=5):
    failed = 0
    successfully_load = False

    #
    # Pafy sometimes cannot load youtube data
    # for the first time, so retry this until
    # the video data is not loaded.
    while not successfully_load:
        try:
            loaded_content = pafy.new(url)
        except Exception:
            if failed > retry:
                return
            failed += 1
        else:
            successfully_load = True

    return loaded_content
