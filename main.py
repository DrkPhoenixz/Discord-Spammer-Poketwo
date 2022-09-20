from webserver import keep_alive
import requests

channelID = 1012391740864475206
headers = {
    "authorization":
    "OTU4MzkwODg2NzgwMjUyMjcw.GDMBx3.xRYTDQ6moHVYtwwY5W9vBkScFVha0L97Bj1vIo"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
