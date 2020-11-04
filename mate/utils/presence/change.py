
async def change_presence(client, activity):
    await client.change_presence(
        activity=activity)
