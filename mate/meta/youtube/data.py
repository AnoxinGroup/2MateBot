

class YoutubeDLMeta:

    YTDL_OPTIONS = {
        'audioquality': 8,
        'format': 'worstaudio',
        'restrictfilenames': True,
        'nocheckcertificate': True,
        'logtostderr': True,
        "extractaudio": True,
        "audioformat": "opus",
        'default_search': 'auto',
        'source_address': '0.0.0.0'
    }
