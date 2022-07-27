import discord
from discord.ext import commands
import os
import keep_alive #For replit users

bot = commands.Bot(command_prefix='.')
bot.remove_command('help')

color = 00000000

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="Github.com/ZensDK"))


@bot.command()
async def help(ctx):
 if ctx.channel.type != discord.ChannelType.private:
    embed = discord.Embed(color=color)
    await ctx.send(f"_ _")
    embed.add_field(name='**Title**', value="Message", inline=True)
    embed.set_author(name=f"Github.com/ZensDK", icon_url='')
    await ctx.channel.send(embed=embed)
keep_alive.keep_alive() #If you're hosting replit.com 
bot.run("Bot-token")
