import discord
import os 
from google.oauth2 import service_account
import google.auth.transport.requests
from google.auth.transport.requests import AuthorizedSession
from mcstatus import JavaServer

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)
start_url = os.environ['MINECRAFT_CHAN_START_URL']
stop_url = os.environ['MINECRAFT_CHAN_STOP_URL']
service_account_creds = os.environ['MINECRAFT_CHAN_CREDS']
stop_session_creds = service_account.IDTokenCredentials.from_service_account_file(service_account_creds,target_audience=stop_url)
start_session_creds = service_account.IDTokenCredentials.from_service_account_file(service_account_creds,target_audience=start_url)
MChan_Token = os.environ['MINECRAFT_CHAN_TOKEN']
server_ip = os.environ['MC_SERVER']

@client.event
async def on_message(message): 
    if message.author == client.user or message.author.bot:
        return
    if message.content.startswith('$start'):
        await message.channel.send('#Attempting to Start the Server!  ▼・ᴥ・▼')
        try:
            authed_session = AuthorizedSession(start_session_creds)
            response = authed_session.get(start_url)
            response_code = response.status_code
            if response_code == 200:
                await message.channel.send('#Starting the Benzene Server!  ٩(＾◡＾)۶')
                await message.channel.send(file=discord.File('..\\Additional Files\\creeper_chan_smile.jpg'))
            else:
                await message.channel.send('#Unable to start the server! ( •_•)')
                await message.channel.send(file=discord.File('..\\Additional Files\\404_chan.png'))
        except:
            await message.channel.send('#Unable to start the server! ( •_•)')
            await message.channel.send(file=discord.File('..\\Additional Files\\404_chan.png'))
            
        

    if message.content.startswith('$stop'):
        await message.channel.send('#Attempting to Stop the Server!  ▼・ᴥ・▼')
        try:
            authed_session = AuthorizedSession(stop_session_creds)
            response = authed_session.get(stop_url)
            response_code = response.status_code
            if response_code == 200:
                await message.channel.send('#Shutting Down the Benzene Server! (>﹏<)')
                await message.channel.send(file=discord.File('..\\Additional Files\\creeper_chan_goodbye.jpg')) 
            else:
                await message.channel.send('#Unable to stop the server! ( •_•)')
                await message.channel.send(file=discord.File('..\\Additional Files\\404_chan.png'))
        except:
            await message.channel.send('#Unable to stop the server! ( •_•)')
            await message.channel.send(file=discord.File('..\\Additional Files\\404_chan.png'))
         

    if message.content.startswith('$status'):
        response = None
        try:
            await message.channel.send('#Getting the Benzene Server Status!  ▼・ᴥ・▼')
            hostname = server_ip
            server = JavaServer.lookup(server_ip) 
            response = os.system("ping " + hostname) # if 0 then server is up
            if response == 0:
                await message.channel.send('#The Benzene Server is up!  ( ͡° ͜ʖ ͡°)')
                await message.channel.send('#There are currently {0} {1} online!'.format(server.status().players.online, 'player' if server.status().players.online == 1 else 'players' ))
                await message.channel.send(file=discord.File('..\\Additional Files\\creeper_chan_smile.jpg'))
            else:
                await message.channel.send('#The Benzene Server is down!  (ಥ _ ಥ)')
                await message.channel.send(file=discord.File('..\\Additional Files\\404_chan.png'))
        except TimeoutError:
            pass
client.run(MChan_Token)

