import discord.py
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import time
from classes import nameCheck

bot = Bot(command_prefix="+")

with open('times.json') as file:
	times = json.load(file)
with open('users.json') as file:
	users = json.load(file)
with open('settings.json') as file:
	settings = json.load(file)

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
  
# +time <user>

@bot.command(name="time", pass_context = True)
async def _attack(ctx, user): #ctx.message.author.name
	name = classes.nameCheck(name)
	new-time = time.ctime(time.time() + (times[str(user)]*3600))
	await bot.say("The current time for " + name + " is " + new-time + ".")
  
bot.run(--bot code goes here--)
