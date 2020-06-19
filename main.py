import discord
import threading
import schedule
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('WHAT THE FUCK DO YOU WANT BITCH!')
        
        if 'u gay' in message.content.split('$hello')[1]:
            await message.channel.send('no u')
        
# #todo : fix this function and use this as this is an internal discord package functionality, better to use
async def aBackGroundTask():
    await client.wait_until_ready()
    channel = client.get_channel(723201817533743119)
    await asyncio.sleep(10)
    while True:
        await channel.send('OH MY GOD I GOT TO DO THIS TOO?! FUCK')
        await asyncio.sleep(86400) # task runs every 60 seconds
    

#if the file is imported as a package this won't be called
if __name__ == "__main__":
    #threaded(scheduleTheTask)
    client.loop.create_task(aBackGroundTask())
    client.run('NzIzNTk3MTMzOTU3MzAwMzA2.Xu0Tvw.8DgE18KME2V-wkONqA5FA7ykIjg')





