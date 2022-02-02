""" This module updates user's Telegram information when his song on Spotify is changed.
Author: elpideus <elpideus@gmail.com>
Version: Beta 1.0 """
import time
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
from telethon import TelegramClient
from datetime import datetime
from termcolor import colored

api_hash = ""
api_id = 6969
timing = 30 #in seconds

client = TelegramClient(
    'default',
    api_id,
    api_hash)

lyrics = []
with open('lyrics.txt') as my_file:
    for line in my_file:
        lyrics.append(line)


async def main():

#    me = await client.get_me()

    ind = 0

    while True:
        print("bio changed: "+colored(lyrics[ind], "blue"))
        await client(UpdateProfileRequest(
            about=lyrics[ind]
        ))
        ind += 1
        if ind >= len(lyrics):
            break
        time.sleep(timing)



with client:
    print(datetime.now().strftime("%H:%M:%S > ") + colored("Program has been booted.", "green"))
    client.loop.run_until_complete(main())
