import discord
import json 
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!")

with open("users.json", "ab+") as ab:
    ab.close()
    f = open('users.json','r+')
    f.readline()
    if os.stat("users.json").st_size == 0:
      f.write("{}")
      f.close()
    else:
      pass

with open('users.json', 'r') as f:
  users = json.load(f)
 
@client.event    
async def on_message(message):
  if message.author.bot == False:
    with open('users.json', 'r') as f:
      users = json.load(f)
    await level_up(users, message.author, message)
    with open('users.json', 'w') as f:
      json.dump(users, f)
      await client.process_commands(message)
 
async def level_up(users, user, message):
  if not str(user.id) in users:
    users[str(user.id)] = {}
    users[str(user.id)]['social_credit'] = 0

  users[str(user.id)]["social_credit"] += 1

  if "taiwan" in message.content: 
    users[str(user.id)]["social_credit"] -= 100
    embedd = discord.Embed(
      title = "一塊狗屎!!",
      description = "你這個愚蠢的他媽的被拖延成了黑鬼的錢傻瓜，如果你再談論台灣，我會驅逐你的屁股，你的混蛋!!!!!!!",
      color = discord.Colour.red()
    )
    embedd.set_thumbnail(url="https://images-ext-2.discordapp.net/external/5YH02NxKUFLf70htSzlVnQevMv_M9QyFtO4T9IdGfiA/https/clipartcraft.com/images/emoji-clipart-angry-13.png")
    await message.channel.send(embed=embedd)
  # await message.channel.send("做得好!!")

 
@client.command()
async def rank(ctx):
  user = ctx.message.author
  #with open('users.json', 'r') as f:
    #users2 = json.load(f)
  with open('users.json', 'r') as f:
    users = json.load(f)
    
  lvl = users[str(user.id)]['social_credit']
  embed = discord.Embed(
    title = "做得好!!",
    description = f"你有 {lvl} social credit!",
    color = discord.Colour.green()
  )
  embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/_GlFZ1d6LQ-tTXE8SrO21BComHmWaB9gNlThe1lga7U/https/amogus.monster/images/good.png")
  await ctx.send(embed=embed)

@client.command()
async def work(ctx):
  with open('users.json', 'r') as f:
    users = json.load(f)
  
  social_credit = random.randint(1, 200)
  users[str(ctx.author.id)]["social_credit"] += social_credit
  embed = discord.Embed(
    title = "幹得好朋友！",
    description = f"+ {social_credit}",
    color = discord.Colour.green()
  )
  embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/mDqrQ4PMynS1ALKn7QbUtz751wGvbCw7I-08vVuyG3k/https/www.funny-emoticons.com/files/smileys-emoticons/funny-emoticons/32-well-done.png")
  await ctx.send(embed=embed)
 
client.run("")
