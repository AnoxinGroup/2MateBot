
async def show_embed(channel, embed, delete_after=None, instead_of=None):
    if instead_of:
        return await instead_of.edit(
            embed=embed,
            delete_after=delete_after)
    return await channel.send(
        embed=embed,
        delete_after=delete_after)
