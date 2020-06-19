import discord
import threading
import schedule
import asyncio

class Defibrillator(discord.Client):
    def __init__(self, discord_token):
        super(Defibrillator, self).__init__()

        self.discord_token = discord_token
        
        # Represents all available commands and how to use them.
        #!schedule "Hearthstone Tourney 4" 2017-06-07 7:30PM PST "Bring your best decks!"
        self.commands = {
            "!schedule": {
                "examples": ["!schedule \"Game Night\" 2017-06-01 05:30PM PST \"Bring your own beer.\""]
            },
            "!reply": {
                "examples": ["!reply \"Game Night\" yes"]
            },
            "!events": {
                "examples": ["!events 2017-06-01"]
            },
            "!scheduler-bot": {
                "examples": ["!scheduler-bot"]
            },
            "!delete-event":{
                "examples": ["!delete-event \"Game Night\""]
            },
            "!edit-event":{
                "examples": ["!edit-event \"Game Night\" date 2017-06-06 time 5:30PM"]
            }

        }
        
    async def aBackGroundTask(self):
        await self.wait_until_ready()
        channel = self.get_channel(723201817533743119)
        await asyncio.sleep(10)
        while True:
            await channel.send('OH MY GOD I GOT TO DO THIS TOO?! FUCK')
            await asyncio.sleep(86400) # task runs every 60 seconds
        
    def run(self):
        # Calling superclass to do discord.Client's run.
        self.loop.create_task(self.aBackGroundTask())
        super(Defibrillator, self).run(self.discord_token)
        
    def configureEventListeners(self):
        @self.event
        async def on_ready():
            print('We have logged in as {0.user}'.format(self))
            
        @self.event
        async def on_message(message):
            if message.author == self.user:
                return

            if message.content.startswith('$hello'):
                await message.channel.send('WHAT THE FUCK DO YOU WANT BITCH!')
                
                if 'u gay' in message.content.split('$hello')[1]:
                    await message.channel.send('no u')
                
        
dfObj = Defibrillator('NzIzNTk3MTMzOTU3MzAwMzA2.Xu0Tvw.8DgE18KME2V-wkONqA5FA7ykIjg')
dfObj.configureEventListeners()
dfObj.run()