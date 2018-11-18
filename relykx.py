#######################################################################################################################
# 🤖 B O T - S T A R T U P
#######################################################################################################################

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time
from time import gmtime, strftime
import os

bot = commands.Bot(command_prefix='m!')

@bot.event
async def on_ready():
	print ("Ready when you are...")
	print ("I am running on " + bot.user.name)
	print ("With the ID: " + bot.user.id)
	
	
#######################################################################################################################
# 📖 G E N E R A L - C O M M A N D S
#######################################################################################################################

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
@commands.has_role("Moderator")
async def kick(ctx, user: discord.Member):
	await bot.say(":boot: Cya, {}. ya loser!".format(user.name))
	await bot.kick(user)

@bot.command(pass_context=True)
async def about(ctx):
	embed = discord.Embed(title="https://discord.gg/UjuGRB9", description="For any other help please join our Discord server...", url="https://discord.gg/UjuGRB9", color=0xffafc9)
	embed.set_author(name="MikiBot", url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.add_field(name="About", value="Hey everyone, I'm MikiBot ^^ \nI'm also very new discord and I'd like your help to improve myself :D \nPlease use ;help to see what else I can do for you~ \n\n<:curiouscat:508516637700259850> Curious Cat: https://curiouscat.me/MikiDiscord \n - If you have any questions please ask here. \n\n<:twitter:508515087330312193> Twitter: https://twitter.com/MikiDiscord \n - You can follow me on twitter here.", inline=False)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def servercount(ctx):
	embed = discord.Embed(description='Currently watching over ' + str(len(bot.servers)) + ' Discord servers <:discord:501956002158215198>', color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def invite(ctx):
	embed = discord.Embed(description="If you'd like to add MikiBot to your server, click here: \nhttps://discordapp.com/oauth2/authorize?&client_id=513265987349643264&scope=bot&permissions=66186303", color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def vote(ctx):
	embed = discord.Embed(description='You can vote here: \nhttps://discordbots.org/bot/496214977267630080/vote', color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def donate(ctx):
	embed = discord.Embed(description='You can donate by purchasing roles from the MikiBot Help server here: \nhttps://donatebot.io/checkout/499771629396688907?buyer=257784039795064833', color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def time(ctx):
	dash = strftime("%I:%M", gmtime())
	wholetime = dash[0] + dash[1]
	resttime = dash[2:]
	await bot.say("The server time now is: **" + wholetime + resttime + ", Obtained by 24timezones**")
	
	
#######################################################################################################################
# 😜 F U N - C O M M A N D S													      
#######################################################################################################################
	
@bot.command(pass_context=True)
async def wallpaper(ctx):
	embed = discord.Embed(color=0xffafc9,)
	embed.set_image(url='https://picsum.photos/1280/720/?image=' + str(random.randint(1, 999)))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def gif(ctx):
	embed = discord.Embed(color=0xffafc9,)
	embed.set_image(url='http://replygif.net/i/' + str(random.randint(90, 1100)) + '.gif')
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("🏓 pong!")
	print ("user has pinged")
	
@bot.command(pass_context=True)
async def diceroll(ctx):
	randomlist = ['1','2','3','4','5','6',]
	embed = discord.Embed(title ='**Game: Dice Roll**', color=0xffafc9, description="🎲 *rolls a dice* \n\nYou rolled a dice and it landed on a \n Side: **%s** \n ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿" %(random.choice(randomlist),))
	embed.add_field(name="Other Games:", value="Coin Flip | ;coinflip \n 8 Ball | ;8ball", inline=True)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def coinflip(ctx):
	randomlist = ['Heads','Tails',]
	embed = discord.Embed(title ='**Game: Coin Flip**', color=0xffafc9, description="💰 *flips a coin* \n\nYou flipped a coin and it landed on \n Face: **%s** \n ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿" %(random.choice(randomlist),))
	embed.add_field(name="Other Games:", value="Dice Roll | ;dicerole \n 8 Ball | ;8ball", inline=True)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def eightball(ctx):
	randomlist = ['It is certain.',
                      'It is decidedly so.',
                      'Without a doubt.',
                      'Yes - definitely.',
                      'You may rely on it.',
                      'As I see it, yes.',
                      'Most likely.',
                      'Outlook good.',
                      'Yes.',
                      'Signs point to yes.',
                      'Reply hazy, try again',
                      'Ask again later.',
                      'Better not tell you now.',
                      'Cannot predict now.',
                      'Concentrate and ask again.',
                      "Don't count on it.",
                      'My reply is no.',
                      'My sources say no.',
                      'Outlook not so good.',
                      'Very doubtful.',
                     ]
	embed = discord.Embed(title ='**Game: 8 Ball**', color=0xffafc9, description="🎱 *shakes the 8 Ball up...*` \n\nYou shook the 8 ball and it shows you... \n Answer: **%s** \n ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿" %(random.choice(randomlist),))
	embed.add_field(name="Other Games:", value="Dice Roll | ;dicerole \n Coin Flip | ;coinflip", inline=True)
	await bot.say(embed=embed)
	
	
#######################################################################################################################
# ℹ️ H E L P - C O M M A N D S	
#######################################################################################################################
	
@bot.command(pass_context=True)
async def commands(ctx):
	embed = discord.Embed(title="🤖 Bot", color=0xffafc9)
	embed.add_field(name="prefix", value=bot, inline=True)
	embed.add_field(name="commands", value="{}command".format(bot), inline=True)
	await bot.say(embed=embed)
	embed = discord.Embed(title="📖 General", color=0xffafc9)
	embed.add_field(name="server", value="Displays the info of the current server.", inline=False)
	embed.add_field(name="info", value="Displays a profile of the mentioned user.", inline=False)
	embed.add_field(name="kick", value="Kicks the mentioned user.", inline=False)
	embed.add_field(name="about", value="Shows the About description of MikiBot.", inline=False)
	embed.add_field(name="servercount", value="Shows how many servers this bot occupies.", inline=False)
	embed.add_field(name="invite", value="Sends the invite to add MikiBot to your server.", inline=False)
	embed.add_field(name="vote", value="Vote for MikiBot.", inline=False)
	embed.add_field(name="donate", value="Donate to MikiBot.", inline=False)
	embed.add_field(name="time", value="Displays the current time of the server.", inline=False)
	await bot.say(embed=embed)
	embed = discord.Embed(title="😜 Fun", color=0xffafc9)
	embed.add_field(name="wallpaper", value="Generates a random wallpaper.", inline=False)
	embed.add_field(name="gif", value="Generates a random gif.", inline=False)
	embed.add_field(name="ping", value="Pongs the user's ping.", inline=False)
	embed.add_field(name="dicroll", value="Rolls a six sided die.", inline=False)
	embed.add_field(name="coinflip", value="Flips a coin, could be heads could be tails.", inline=False)
	embed.add_field(name="eightball", value="Ask a question and shake the 8 Ball.", inline=False)
	await bot.say(embed=embed)
	
#@bot.command(pass_context=True)
#async def embed(ctx):
#	embed = discord.Embed(title="this is the title", description="this is the descriptionf", color=0xffafc9)
#	embed.set_author(name="this is the author")
#	embed.set_footer(text="this is a footer")
#	embed.add_field(name="this is a field", value="this is the value", inline=True)
#	await bot.say(embed=embed)

bot.run(os.getenv("BOT_TOKEN"))
