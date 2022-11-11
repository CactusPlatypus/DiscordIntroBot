from fileinput import filename
from glob import glob
from multiprocessing.connection import Client
import random
import os
from os import listdir
from turtle import end_fill
import discord
import time
from discord.ext import commands
from discord import FFmpegPCMAudio

import json

intents = discord.Intents.all()
intents.members = True
intents.presences = True


client = discord.Client(intents = intents)

audioDictionary = {}



@client.event
async def on_ready():
    print('start')
    with open('data.json') as json_file:
        global audioDictionary 
        audioDictionary= json.load(json_file)
        print(audioDictionary)


@client.event
async def on_voice_state_update(member, before, after):
    if member.id == 992290499245395998:
        return


    if not before.channel and after.channel:
        print(f'{member} has joined the vc')
        print(audioDictionary)
        if str(member.id) not in audioDictionary.keys():
            audioDictionary[str(member.id)] = "./sounds/ree.mp3"
        

        vc = await member.voice.channel.connect()
        playSound(member.id, vc)
        time.sleep(5)

        await vc.disconnect()
   
  


FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}


def playSound(userID, vc):
    print(userID)

    player = vc.play(discord.FFmpegPCMAudio(executable="D:/ffmpeg/bin/ffmpeg.exe",source=audioDictionary[str(userID)]), after=lambda e: print('done', e))
    
async def pickintro(message):
    if message.content.split(" ")[0] == "setintro":
        
        path = str("./sounds/" + str(message.content.split(" ")[1]) +".mp3")
        if (os.path.isfile(str("./sounds/" + str(message.content.split(" ")[1]) +".mp3"))):
            audioDictionary[str(message.author.id)] = path
            print(audioDictionary)
            await message.channel.send("Intro set to " + str(message.content.split(" ")[1]))

            with open("data.json", "w") as outfile:
                json.dump(audioDictionary, outfile)



        else:
            await message.channel.send(str(message.content.split(" ")[1]) + ".mp3 does not exist")

async def listIntros(message):
    files = listdir("./sounds")
    msg = ""
    print(files)
    for title in files:
        msg += title.replace(".mp3", " ") + "\n"

    embed=discord.Embed( color=0x37ff00)
    embed.add_field(name="Available Sounds: \n(use 'setintro [sound] to set your intro')",value=msg, inline=False)

    await message.channel.send(embed = embed)

@client.event
async def on_message(message):

    if message.content.split(" ")[0] == "setintro":
        await pickintro(message=message)
        
    if message.content == "intro list":
        await listIntros(message=message)
     




                        


client.run("OAUTH CODE")
