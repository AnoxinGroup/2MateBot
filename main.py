
from os import environ
from mate.main import ZMateBot


ZMateBot.run(
    ZMateBot(
        command_prefix="2"),
    environ.get("M2TOKEN")
)
