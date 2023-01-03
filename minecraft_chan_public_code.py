import discord
import urllib.request 

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)
code = None

@client.event
async def on_message(message): 
    if message.author == client.user:
        return
    if message.content.startswith('$start'):
        try:
            get_url= urllib.request.urlopen('Enter HTTP Trigger')
            code = str(get_url.getcode())
        except:
            await message.channel.send('#Unable to start the server! ( •_•)')
            await message.channel.send(file=discord.File(''))
        if code == '200':
            await message.channel.send('#Starting the Benzene Server!  ٩(＾◡＾)۶')
            await message.channel.send(file=discord.File(''))
    if message.content.startswith('$stop'):
        try:
            get_url= urllib.request.urlopen('Enter HTTP Trigger')
            code = str(get_url.getcode())
        except:
            await message.channel.send('#Unable to stop the server! ( •_•)')
            await message.channel.send(file=discord.File(''))
        if code == '200':
            await message.channel.send('#Shutting Down the Benzene Server! (>﹏<)')
            await message.channel.send(file=discord.File(''))  
   
client.run('Enter Your Token')

        