import discord
import urllib.request
import os 
from mcstatus import JavaServer 

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)
code = None

@client.event
async def on_message(message): 
    if message.author == client.user or message.author.bot:
        return
    if message.content.startswith('$start'):
        try:
            get_url= urllib.request.urlopen(os.environ['MINECRAFT_CHAN_START_URL'])
            code = str(get_url.getcode())
            if code == '200':
                await message.channel.send('#Starting the Benzene Server!  ٩(＾◡＾)۶')
                await message.channel.send(file=discord.File('.\\media\\creeper_chan_smile.jpg'))
        except:
            await message.channel.send('#Unable to start the server! ( •_•)')
            await message.channel.send(file=discord.File('.\\media\\404_chan.png'))
        

    if message.content.startswith('$stop'):
        try:
            get_url= urllib.request.urlopen(os.environ['MINECRAFT_CHAN_STOP_URL'])
            code = str(get_url.getcode())
            if code == '200':
                await message.channel.send('#Shutting Down the Benzene Server! (>﹏<)')
                await message.channel.send(file=discord.File('.\\media\\creeper_chan_goodbye.jpg')) 
        except:
            await message.channel.send('#Unable to stop the server! ( •_•)')
            await message.channel.send(file=discord.File('.\\media\\404_chan.png'))
         

    if message.content.startswith('$status'):
        response = None
        try:
            await message.channel.send('#Getting the Benzene Server Status!  ▼・ᴥ・▼')
            hostname = "34.102.49.114"
            server = JavaServer.lookup("34.102.49.114") 
            response = os.system("ping " + hostname) # if 0 then server is up
            if response == 0:
                await message.channel.send('#The Benzene Server is up!  ( ͡° ͜ʖ ͡°)')
                await message.channel.send('#There are currently {0} {1} online!'.format(server.status().players.online, 'player' if server.status().players.online == 1 else 'players' ))
                await message.channel.send(file=discord.File('.\\media\\creeper_chan_smile.jpg'))
            else:
                await message.channel.send('#The Benzene Server is down!  (ಥ _ ಥ)')
                await message.channel.send(file=discord.File('.\\media\\404_chan.png'))
        except TimeoutError:
            pass
client.run(os.environ['MINECRAFT_CHAN_TOKEN'])

