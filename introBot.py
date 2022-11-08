from fileinput import filename
from multiprocessing.connection import Client
import os
from turtle import end_fill
import discord
import time
from discord.ext import commands
from discord import FFmpegPCMAudio


intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

audioDictionary = {
    100000000000000000:"./sounds/bye.mp3",
    201544333617397760:"./sounds/cactus.mp3", #Cactus
    180201381230018560:"./sounds/ree.mp3",   #Rice bowl
    215744326989250561:"./sounds/tomjedi.mp3", #Tom jedi
    612251709267247129:"./sounds/danlel.mp3"#danlel
}

@client.event
async def on_voice_state_update(member, before, after):
    if member.id == 992290499245395998:
        return

    if not before.channel and after.channel:
        print(f'{member} has joined the vc')

        if audioDictionary[member.id] is None:
            return

        vc = await member.voice.channel.connect()
        playSound(member.id, vc)
        time.sleep(5)

        await vc.disconnect()
    elif before.channel and not after.channel:
        print(f'{member} disconnect')
        vc = await before.channel.connect()
        playSound(100000000000000000, vc)
        time.sleep(5)
        await vc.disconnect()
  
       
        



FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


def playSound(userID, vc):
    print(userID)

    player = vc.play(discord.FFmpegPCMAudio(executable="D:/ffmpeg/bin/ffmpeg.exe",source=audioDictionary[userID]), after=lambda e: print('done', e))
    

   
     




                        
       
     
       
     

client.run("OAUTH CODE")
