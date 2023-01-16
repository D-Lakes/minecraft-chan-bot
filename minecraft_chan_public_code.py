import discord
import os 
from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
from mcstatus import JavaServer
from idle_check import *
import threading 

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)
start_url = "https://us-west2-minecraft-server-360820.cloudfunctions.net/benzene-server-start"
stop_url = "https://us-west2-minecraft-server-360820.cloudfunctions.net/benzene-server-stop"
service_account_creds = "./MINECRAFT_CHAN_CREDENTIALS.json"
stop_session_creds = service_account.IDTokenCredentials.from_service_account_file(service_account_creds,target_audience=stop_url)
start_session_creds = service_account.IDTokenCredentials.from_service_account_file(service_account_creds,target_audience=start_url)
MChan_Token = os.environ['MINECRAFT_CHAN_TOKEN']
server_ip = os.environ['MC_SERVER']



# create a thread to check if the server is up
# if it is, then send a message to the discord channel
# if it is not, then send a message to the discord channel

def thread_idle_check():
    conn = createDB()
    while True:
        timeStamp = datetime.datetime.now()
        isUp = checkStatus()
        insertDB(conn, "up" if isUp == 0 else "down" , timeStamp)
        rows = findLastUp(conn)
        diff = findDeltaTime(rows)
        if diff > datetime.timedelta(minutes=10):
            isSuccess = use_authed_url(stop_url, stop_session_creds)

        print("one thread loop")
        time.sleep(30)


def use_authed_url(url, creds):
    authed_session = AuthorizedSession(creds)
    response = authed_session.get(url)
    response_code = response.status_code
    if response_code == 200:
        return True
    else:
        return False



@client.event
async def on_message(message): 
    if message.author == client.user or message.author.bot:
        return
    if message.content.startswith('$start'):
        await message.channel.send('#Attempting to Start the Server!  ▼・ᴥ・▼')
        try:
            isSuccess = use_authed_url(start_url, start_session_creds)
            if isSuccess == True:
                await message.channel.send('#Starting the Benzene Server!  ٩(＾◡＾)۶')
                await message.channel.send(file=discord.File('./media/creeper_chan_smile.jpg'))
            else:
                await message.channel.send('#Unable to start the server! ( •_•)')
                await message.channel.send(file=discord.File('./media/404_chan.png'))
        except FileNotFoundError:
            await message.channel.send('IMAGE FILE NOT FOUND')
        except:
            await message.channel.send('#Unable to start the server! ( •_•)')
            await message.channel.send(file=discord.File('./media/404_chan.png'))
            
        

    if message.content.startswith('$stop'):
        await message.channel.send('#Attempting to Stop the Server!  ▼・ᴥ・▼')
        try:
            isSuccess = use_authed_url(stop_url, stop_session_creds)
            if isSuccess == True:
                await message.channel.send('#Shutting Down the Benzene Server! (>﹏<)')
                await message.channel.send(file=discord.File('./media/creeper_chan_goodbye.jpg')) 
            else:
                await message.channel.send('#Unable to stop the server! ( •_•)')
                await message.channel.send(file=discord.File('./media/404_chan.png'))
        except:
            await message.channel.send('#Unable to stop the server! ( •_•)')
            await message.channel.send(file=discord.File('./media/404_chan.png'))
         

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
                await message.channel.send(file=discord.File('./media/creeper_chan_smile.jpg'))
            else:
                await message.channel.send('#The Benzene Server is down!  (ಥ _ ಥ)')
                await message.channel.send(file=discord.File('./media/404_chan.png'))
        except TimeoutError:
            pass
        

# Begin the thread
t1 = threading.Thread(target=thread_idle_check, args=())
t1.start()
# Run the bot
client.run(MChan_Token)



