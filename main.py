import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print("Inside the on message event listener")
    print(message.content)
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print("Inside the hello block")
        await message.channel.send('WHAT THE FUCK DO YOU WANT BITCH!')
        
    elif 'u gay' in message.content.split('$hello')[1]:
            await message.channel.send('no u')

client.run('NzIzNTk3MTMzOTU3MzAwMzA2.Xuz8Zw.fUh1We6vdjzhRNF1loNsywE8LLQ')
