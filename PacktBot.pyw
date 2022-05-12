import discord
import search_packt
from datetime import datetime, time

TOKEN = 'enterbuildtokenhere'

datetime.now()

client = discord.Client()

channel = client.get_channel(insert channel id)
desTime = time(0)
interval = 1
startRun = 1

async def checkPackt(desTime, interval, startRun):
  await client.wait_until_ready()
  if startRun:
    message, image = search_packt.search()
    if message == "Could not establish a connection with PackT":
      desTime = time(interval)
      interval+=1
      startRun = 0
    else:
      embedVar = discord.Embed(title="Free Text Alert", description=message, color=0xFFA500)
      embedVar.set_image(url=image)
      await client.get_channel(insert channel id).send(embed=embedVar)
      desTime = time(0)
      interval = 1
      startRun = 0
  if datetime.now() == desTime:
    message, image = search_packt.search()
    if message == "Could not establish a connection with PackT":
      desTime = time(interval)
      interval+=1
    else:
      embedVar = discord.Embed(title="Free Text Alert", description=message, color=0x00ff00)
      embedVar.set_image(url=image)
      await client.get_channel(insert channel id).send(embed=embedVar)
      desTime = time(0)
      interval = 1

client.loop.create_task(checkPackt(desTime, interval, startRun))
client.run(TOKEN)

