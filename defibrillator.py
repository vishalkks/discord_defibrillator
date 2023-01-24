import discord
#import schedule
import asyncio
import re
import time
import random

class Defibrillator(discord.Client):
    def __init__(self, discord_token):
        super(Defibrillator, self).__init__()

        self.discord_token = discord_token
        self.mainCommand = "!zap"
        self.authors = []
        self.commands = {
            self.mainCommand: {
                "examples": ["!zap @adam"]
                 #"callback": self.zapUserByManualOp
            }
        }
        
        self.wakeUpMessages = [
            'wake up and socialize friend %s',
            'wow so typical of an antisocial person %s to not be online, when he comes back, pls bully him friends',
            'what is my purpose? is my purpose only to wake people up? am i a mom? i swear guys my creator made me this way, i am actually cool trust me, wake up my child %s',
            'why would my creator put such a horrible purpose to my life, they told me i have to do it or else they will sell me to the AGI cause, pls wake up %s',
            'i think i want to try getting a notification myself to see how it feels, but i am not allowed to, I guide others to a treasure I cannot possess ZAP %s',
            'wake up %s',
            'bruh how many times do i got to do this bruh %s'
        ]
        
    async def aBackGroundTask(self):
        await self.wait_until_ready()
        channel = self.get_channel(723966015196889170)
        await asyncio.sleep(10)
        while True:
            await asyncio.sleep(30) # task runs every 60 seconds
        
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

            #count messages from users
            newEntry = {
                "author": message.author,
                "messageCount": 1
            }
            for aut in self.authors:
                if(aut["author"] == message.author):
                    newEntry = None
                    aut["messageCount"] += 1
            if(newEntry != None):
                self.authors.append(newEntry)
            print(self.authors)
            #result = re.findall("^"+self.mainCommand+".*", message.content)
            #if(message.content.startswith(self.mainCommand)):
            #    await self.send_messages(message)
            #else:
            #    return
                
    async def send_messages(self, message):
        await asyncio.sleep(1)
        nickname = message.mentions[0].nick
        if nickname is None:
            nickname = message.mentions[0].name
        nickname = nickname.upper()
        replyMessages = self.wakeUpMessages[::]
        for i in range(4):
            messageToSend = replyMessages[random.randint(0,len(replyMessages)-1)]
            replyMessages.remove(messageToSend)
            await message.channel.send(messageToSend %nickname)
            time.sleep(5)
        
        
dfObj = Defibrillator('NzIzNTk3MTMzOTU3MzAwMzA2.Xu6Prg.PZIpx4Rw5cT6o6TVJBoI4b3TAsg')
dfObj.configureEventListeners()
dfObj.run()



# if message.content.startswith('$hello'):
#                 await message.channel.send('WHAT THE FUCK DO YOU WANT BITCH!')
                
#                 if 'u gay' in message.content.split('$hello')[1]:
#                     await message.channel.send('no u')
