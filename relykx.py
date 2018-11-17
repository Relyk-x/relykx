# New MikiBot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='r!')

@bot.event
async def on_ready():
	print ("Ready when you are...")
	print ("I am running on " + bot.user.name)
	print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say(":ping_pong: pong!")
	print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0xffafc9)
	embed.set_thumbnail(url=user.avatar_url)
	embed.add_field(name="Name", value=user.name, inline=True)
	embed.add_field(name="ID", value=user.id, inline=True)
	embed.add_field(name="Status", value=user.status, inline=True)
	embed.add_field(name="Highest role", value=user.top_role, inline=True)
	embed.add_field(name="Joined", value=user.joined_at, inline=True)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def server(ctx):
	embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=0xffafc9)
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	embed.add_field(name="Name:", value=ctx.message.server.name, inline=True)
	embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
	embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
	embed.add_field(name="Members", value=len(ctx.message.server.members))
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Moderator")
async def kick(ctx, user: discord.member):
	await bot.say(":boot: Cya, {}. ya loser!".format(user.name))
	await bot.kick(user)

@bot.command(pass_context=True)
async def embed(ctx):
	embed = discord.Embed(title="test", description="my name jeff", color=0xffafc9)
	embed.set_author(name="ey boi this is the author")
	embed.set_footer(text="this is a footer")
	embed.add_field(name="this is a field", value="this is the value", inline=True)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def about(ctx):
	embed = discord.Embed(title="https://discord.gg/UjuGRB9", description="For any other help please join our Discord server...", url="https://discord.gg/UjuGRB9", color=0xffafc9)
	embed.set_author(name="MikiBot", url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.add_field(name="About", value="Hey everyone, I'm MikiBot ^^ \nI'm also very new discord and I'd like your help to improve myself :D \nPlease use ;help to see what else I can do for you~ \n\n<:curiouscat:508516637700259850> Curious Cat: https://curiouscat.me/MikiDiscord \n - If you have any questions please ask here. \n\n<:twitter:508515087330312193> Twitter: https://twitter.com/MikiDiscord \n - You can follow me on twitter here.", inline=False)
	await bot.say(embed=embed)
	
bot.run(os.getenv("BOT_TOKEN"))
