
_EMBED_DESC = """

Note: there's only basic commands, to see full
list of the commands click here.

<:2mate:773599716729683999>**play** *<url>*
Url can refer as to Youtube or Spotify
Music or Playlist, so to the audio stream. If
bot already play an audio, it merely put your
next song to the current song queue. More
about song queue look at the *add* command
text.

<:2mate:773599716729683999>**add** *<url>*
Something like the command *play* when the
song queue is not free. Puts your song into
the song queue. Note, that the song queue size
is about 20 songs.

<:2mate:773599716729683999>**stop**
Stops audio, but can be unfreezed by command
*play*. To fully free up song queue use *reset*
command.

<:2mate:773599716729683999>**reset**
Cleans up the certain song queue for the current
guild.

"""


class AudioInfoMeta:

    EMBED_DESC = _EMBED_DESC

    EMBED_TITLE = "Audio Overview"

    EMBED_COLOR = 0x43b581

    EMBED_THUMBNAIL = "https://github.com/dusework/2MateBot/" + \
        "blob/master/assets/images/bot/avatar_white.png?raw=true"

    EMBED_FOOTER_NAME = "Audio provided by the Youtube, Spotify, " +\
        "SoundCloud Services"
