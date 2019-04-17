import discord.py
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

mode = "Daylight"

bot = Bot(command_prefix="+")

times = {
  "Hawaii": 0,
  "Pacific-Daylight": 3,
  "Mountain-Daylight": 4,
  "Central-Daylight": 5,
  "Eastern-Daylight": 6,
  "Pacific-Standard": 2,
  "Mountain-Standard": 3,
  "Central-Standard": 4,
  "Eastern-Standard": 5,
  "Australia": 21
  }

# !time <time> <am/pm> <user>

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
  
@bot.command(name="time", pass_context = True)
async def _attack(ctx, time, ampm, user):
  
