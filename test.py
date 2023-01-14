# import urllib.request
# get_url= urllib.request.urlopen('http://34.102.49.114')
# code = str(get_url.getcode())

# import os
# hostname = "34.102.49.114" 

# # ping the host and get the response
# response = os.system("ping " + hostname)

# print (response)


# response = os.system("ping " + hostname)



# #and then check the response...
# if response == 0:
#   print (hostname), 'is up!'
# else:
#   print (hostname), 'is down!'

# import os
# # print enviroment variable 
# print(os.environ['BENZENE_BOT_TOKEN'])


# from mcstatus import JavaServer
# # import os
# hostname = "34.102.49.114"
# server = JavaServer.lookup("mc.hypixel.net")

# print(server.status().players.online)
# print('#There are currently {} players online!)'.format(server.status().players.online))

# try:
#     print('#Getting the Benzene Server Status!  ▼・ᴥ・▼')
#     hostname = "34.102.49.114"
#     server = mcstatus.JavaServer.async_status(hostname)
#     print(server)
#     # response = os.system("ping " + hostname) # if 0 then server is up
#     # if response == 0:
# except TimeoutError:
#              print('#The Benzene Server is down!  (ಥ _ʖಥ)')
#              quit()
             
# print('#The Benzene Server is up!  ( ͡° ͜ʖ ͡°)')
# print('#There are currently {} players online!'.format(server.status().players.online))
           


# connection to sqlite database
import sqlite3
import time
import datetime
from mcstatus import JavaServer
import os


def estabish_connection():
    conn = None
    hostname = "34.102.49.114"
    # # t  = threading.Thread(response = os.system("ping " + hostname))
    response = os.system("ping " + hostname)
    try:
        conn = sqlite3.connect('minecraft_chan.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE time_log1 (server_status , time_stamp )")
        isUp = JavaServer.lookup(hostname).status.players.online if not bin(response) else "off"
        time.sleep(1)
        cur.execute("INSERT INTO time_log1 VALUES({0}, {1})",format( isUp ,time.time()))
        conn.commit()
    except:
        print("error connecting to database")
    return conn


# estabish_connection()


def createDB():
    conn = None
    try:
        conn = sqlite3.connect('minecraft_chanTest1.db')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS time_log (id integer primary key autoincrement, server_status , time_stamp )")
        conn.commit()
    except:
        print("error connecting to database")
    return conn


def insertDB(conn, server_status, time_stamp):
    cur = conn.cursor()
    cur.execute("INSERT INTO time_log (server_status , time_stamp) VALUES(?,?)", (server_status, time_stamp))
    conn.commit()
    return cur.lastrowid
    
start = time.monotonic()
def sinceStart(n):
       return print(time.monotonic() - n)
def checkStatus():
    hostname = "34.102.49.114"
    return os.system("ping " + hostname)
   
def howLong(conn):
    cur = conn.cursor()
    cur.execute("SELECT time_stamp FROM time_log")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    print("Done")
    return rows
def findLastUp(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM time_log ")
    rows = cur.fetchall()
    return rows
        
def findDeltaTime(rows):

    lastUps = []
    for i in range(len(rows)):
        print(rows[-i][0],rows[-i][1])   
        if rows[-i] [1] == "up":
            lastUps.append(rows[-i])
    print(lastUps)

    last = datetime.datetime.strptime(lastUps[-1][2], "%Y-%m-%d %H:%M:%S.%f")
    first = datetime.datetime.strptime(lastUps[0][2], "%Y-%m-%d %H:%M:%S.%f")
    diff =  first - last
    print(diff)
    if diff > datetime.timedelta(minutes=21):
        print("server has been up for more than 22 minutes")
    else:
        print("server has been up for less than 22 minutes")

    


conn = createDB()
while True:
    sinceStart(start)
    
    # Insert a row of data
    timeStamp = datetime.datetime.now()
    isUp = checkStatus()
    insertDB(conn, "up" if isUp == 0 else "down" , timeStamp)


    rows = findLastUp(conn)
    findDeltaTime(rows)
    time.sleep(30)


# hostname = "34.102.49.114"
# response = os.system("ping " + hostname)

# print(JavaServer.lookup("mc.hypixel.net").status.players.online if not bin(response) else "off")




# import urllib
# import google


# def make_authorized_get_request(endpoint, audience):
#     """
#     make_authorized_get_request makes a GET request to the specified HTTP endpoint
#     by authenticating with the ID token obtained from the google-auth client library
#     using the specified audience value.
#     """

#     # Cloud Run uses your service's hostname as the `audience` value
#     # audience = 'https://my-cloud-run-service.run.app/'
#     # For Cloud Run, `endpoint` is the URL (hostname + path) receiving the request
#     # endpoint = 'https://my-cloud-run-service.run.app/my/awesome/url'

#     req = urllib.request.Request(endpoint)

#     auth_req = google.auth.transport.requests.Request()
#     id_token = google.oauth2.id_token.fetch_id_token(auth_req, audience)

#     req.add_header("Authorization", f"Bearer {id_token}")
#     response = urllib.request.urlopen(req)

#     return response.read()


# print(make_authorized_get_request('https://us-west2-minecraft-server-360820.cloudfunctions.net/benzene-server-start','https://us-west2-minecraft-server-360820.cloudfunctions.net'))




# # "Authorization", f"Bearer {id_token}"
# import urllib.request
# try:
#     get_url= urllib.request.urlopen(' "Authorization: Bearer ya29.a0AX9GBdUL6TRC1cMS50YHs9lQcsH5h2M_AHJ0dzOIT2uujTqqap5kiC58XW3PP1OgH73s_BIle0ioMQf6t3kBOfGXHXgNafs8j3eqIIAFnlLnDQkUOuMoUhr1-cnNtx1-z-kndWj1XGmj7QBwjOtczpGmU-Uho9B2u02zTAaCgYKAbISAQASFQHUCsbCuqbEG_X-KArY4HzxDneSZA0173" https://us-west2-minecraft-server-360820.cloudfunctions.net/benzene-server-start')
#     code = str(get_url.getcode())
#     if code == '200':
#         print('#Starting the Benzene Server!  ٩(＾◡＾)۶')

# except:
#     print('#Unable to start the server! ( •_•)')
# import os      
# print(os.environ['MINECRAFT_CHAN_START_URL'])