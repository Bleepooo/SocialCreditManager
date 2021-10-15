import discord
import json
import random
import time
from discord.ext import commands

client = commands.Bot(command_prefix="khsbgduhbil")

with open('users.json', 'r') as f:
  users = json.load(f)
 
@client.event    
async def on_message(message):
  user = message.author
  if message.author.bot == False:
    with open('users.json', 'r') as f:
      users = json.load(f)
    await level_up(users, message.author, message)
    with open('users.json', 'w') as f:
      json.dump(users, f)
      await client.process_commands(message)

  if message.content == "!sc":
    lvl = users[str(user.id)]['social_credit']
    if not lvl < 0:
      embed = discord.Embed(
        title = "做得好!!",
        description = f"你有 {lvl} social credit!",
        color = discord.Colour.green()
      )
      embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/_GlFZ1d6LQ-tTXE8SrO21BComHmWaB9gNlThe1lga7U/https/amogus.monster/images/good.png")
      await message.channel.send(embed=embed)
    else:
      embed = discord.Embed(
        title = "愚蠢的混蛋! 非常壞的公民!!",
        description = f" {lvl} social credit",
        color = discord.Colour.red()
      )
      embed.set_footer(text="愚蠢的他媽的白痴")
      embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/lkA-K8QmB1YLl__yw_Gl7qVuvxXwtaNTeoqE6wPgkmk/https/amogus.monster/images/bad.png")
      await message.channel.send(embed=embed)
  elif message.content == "!work":
    social_credit = random.randint(1, 200)
    if not str(user.id) in users:
      users[str(user.id)] = {}
      users[str(user.id)]['social_credit'] = 0

    users[str(user.id)]["social_credit"] += social_credit
    embed = discord.Embed(
      title = "幹得好朋友！",
      description = f"+ {social_credit}!",
      color = discord.Colour.green()
    )
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/mDqrQ4PMynS1ALKn7QbUtz751wGvbCw7I-08vVuyG3k/https/www.funny-emoticons.com/files/smileys-emoticons/funny-emoticons/32-well-done.png")
    await message.channel.send(embed=embed)
 
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

  elif "china" in message.content: 
    users[str(user.id)]["social_credit"] += 10
    embedd = discord.Embed(
      title = "好公民！",
      description = "中國是你唯一需要的地方，這就是你應該談論的一切!",
      color = discord.Colour.green()
    )
    embedd.set_thumbnail(url="https://images-ext-1.discordapp.net/external/mDqrQ4PMynS1ALKn7QbUtz751wGvbCw7I-08vVuyG3k/https/www.funny-emoticons.com/files/smileys-emoticons/funny-emoticons/32-well-done.png")
    await message.channel.send(embed=embedd)
  # await message.channel.send("做得好!!")

 
@client.command()
async def rank(ctx):
  user = ctx.message.author
  #with open('users.json', 'r') as f:
    #users2 = json.load(f)
    
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
