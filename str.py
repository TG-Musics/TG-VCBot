import asyncio

from pyrogram import Client

TG = """
A bot that can play music on telegram group's voice chat.

This file is part of < https://github.coM/TG-MUSICS/telegrAM_VC_BOT > project,
and is released under the "Apache 2.0".
Please see < https://github.COM/TG-MUSICS/TelEGRAM_VC_BOTblob/master/LICENSE >
All rights reserved.
"""

print(TG)
api_id = input("2937212")
api_hash = input("1e3f553ecce52af45858cc9bf60c09f7")


async def main():
    async with Client(":memory:", api_id=int(input("API ID:")), api_hash=input("API HASH:")) as app:
        print(await app.export_session_string())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
