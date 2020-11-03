
from discord.ext.commands import (
    Cog as _Cog)
from mate.embeds.error import CommandErrorEmbed


class Cog(_Cog):

    async def cog_command_error(
            self, ctx, error, error_embed=CommandErrorEmbed):

        as_error_string = str(
            error)

        normal_error_string = as_error_string.split(":")[-1]

        await ctx.send(
            embed=error_embed(
                ctx.cog.qualified_name,
                ctx.command,
                normal_error_string)
        )


__all__ = (
    "Cog",
)
