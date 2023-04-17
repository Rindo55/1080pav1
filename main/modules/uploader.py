import asyncio
import os
import time
import aiohttp
import requests
import aiofiles

from main.modules.utils import format_time, get_duration, get_epnum, get_filesize, status_text, tags_generator, encode

from main.modules.anilist import get_anime_name

from main.modules.anilist import get_anime_img

from main.modules.thumbnail import generate_thumbnail

from config import UPLOADS_ID

from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, Client

from main.modules.progress import progress_for_pyrogram

from os.path import isfile

import os

import time

from main import app, status

from pyrogram.errors import FloodWait

from main.inline import button1

async def upload_video(msg: Message,file,id,tit,name,ttl):

    try:

    

        fuk = isfile(file)

        if fuk:

            r = msg

            c_time = time.time()

            duration = get_duration(file)

            size = get_filesize(file)

            ep_num = get_epnum(name)
            
            rest = tit

            thumbnail = await generate_thumbnail(id,file)

            tags = tags_generator(tit)

            buttons = InlineKeyboardMarkup([

                [

                    InlineKeyboardButton(text="Info", url="https://t.me/AnimeXT"),

                    InlineKeyboardButton(text="Comments", url=f"https://t.me/ANIMECHATTERBOX")

                ]

            ])
            filed = os.path.basename(file)
            filed = filed.replace("(1080p)", "[720p x265]")
            fukpath = "downloads/" + filed
            caption = f"{name}"
            caption = caption.replace("(1080p)", "") 
            gcaption=f"**{caption}**" + "\n" + "✓  `720p x265 10Bit`" + "\n" + "✓  `English Sub`" + "\n" + f"__({tit})__" + "\n" + "#Encoded #HEVC"
            kayo_id = -1001948444792
            linkx_id = -1001578240792
            x = await app.send_document(

                kayo_id,

            document=file,

            caption=gcaption,

            file_name=filed,

            force_document=True,
                
            thumb=thumbnail,

            progress=progress_for_pyrogram,
 
            progress_args=(

                os.path.basename(file),

                r,

                c_time,

                ttl

            )

            ) 

    converted_id = x.id * abs(client.kayo_id)
    string = f"get-{converted_id}"
    base64_string = await encode(string)
    link = f"https://t.me/zoroloverbot?start={base64_string}"
    await await app.send_message(linkx_id,text={link})
    
    try:

            await r.delete()

            os.remove(file)
            
            os.remove(fukpath)

            os.remove(thumbnail)

    except:

        pass

    return x.message_id
