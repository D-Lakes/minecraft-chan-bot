# connection to sqlite database
import sqlite3
import time
import datetime
from mcstatus import JavaServer
import os

def createDB():
    conn = None
    try:
        conn = sqlite3.connect('minecraft_chan.db')
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
    lastUps = []
    flag = False
    for i in range(len(rows)):
        print(rows[-i][0],rows[-i][1])   
        if rows[-i] [1] == "up":
            lastUps.append(rows[-i])
            flag = True
        elif rows[-i] [1] == "down" and flag == True:
            break

    print(lastUps)
    return lastUps
        
def findDeltaTime(lastUps): 

    if lastUps == [] or lastUps == None:
        print("server has not been up ")
        return datetime.timedelta(minutes=0)

    last = datetime.datetime.strptime(lastUps[-1][2], "%Y-%m-%d %H:%M:%S.%f")
    first = datetime.datetime.strptime(lastUps[0][2], "%Y-%m-%d %H:%M:%S.%f")
    diff =  first - last
    print(diff)
    return diff
    
def pruneDB(conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM time_log WHERE id NOT IN (SELECT id FROM time_log ORDER BY time_stamp DESC LIMIT 100)")
    conn.commit()

if __name__ == '__main__':
    conn = createDB()
    while True:

        # Insert a row of data
        timeStamp = datetime.datetime.now()
        isUp = checkStatus()
        insertDB(conn, "up" if isUp == 0 else "down" , timeStamp)


        rows = findLastUp(conn)
        diff = findDeltaTime(rows)
        if diff > datetime.timedelta(minutes=15):
            print("server has been up for more than 22 minutes")
        else:
            print("server has been up for less than 22 minutes")

        time.sleep(30)

