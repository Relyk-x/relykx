##############################################################################################################################
# 🤖 | B O T - S T A R T U P
##############################################################################################################################

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import time
from time import gmtime, strftime
import os

bot = commands.Bot(command_prefix='m!')
msglimit = 100

@bot.event
async def on_ready():
	servers = list(bot.servers)
	status = "over {} servers".format(str(len(bot.servers)))
	print ('MikiBot is up and running with ' + str(len(bot.servers)) + ' servers connected!')
	print ("Ready when you are...")
	print ("I am running on " + bot.user.name)
	print ("With the ID: " + bot.user.id)
	await bot.change_presence(game=discord.Game(name=status,type=3))
# WATCHING 'over ' + str(len(bot.servers)) + ' servers', url="https://www.twitch.tv/streamer"

@bot.event
async def on_member_join(member):
	servers = list(bot.servers)
	print("Connected on {} servers:".fomat(str(len(bot.servers))))
	for x in range(len(servers)):
	 print(' ' + servers[x-1].name)
	embed = discord.Embed(title="https://discord.gg/UjuGRB9", description="For any other help please join our Discord server...", url="https://discord.gg/UjuGRB9", color=0xffafc9)
	embed.set_author(name="MikiBot", url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.add_field(name="About", value="Hey everyone, I'm MikiBot ^^ \nI'm also very new discord and I'd like your help to improve myself :D \nPlease use m!help to see what else I can do for you~", inline=False)
	embed.add_field(name="Social", value="<:curiouscat:508516637700259850> Curious Cat | <:twitter:508515087330312193>Twitter", inline=True)
	embed.add_field(name="Website", value="🌏 https://goo.gl/wKEVjA", inline=True)
# embed.set_footer(text="version: " + VERSION)
	await bot.send_message(member, embed=embed)
	
##############################################################################################################################
# 📖 | G E N E R A L - C O M M A N D S
##############################################################################################################################

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
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="{}'s avatar".format(user.name), description="Here it is...",color=0xffafc9)
	embed.set_image(url=user.avatar_url)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
@commands.has_role("Creator")
async def kick(ctx, user: discord.Member):
	await bot.say(":boot: Cya, {}. ya loser!".format(user.name))
	await bot.kick(user)

@bot.command(pass_context=True)
@commands.has_role("Creator")
async def clear(ctx, msglimit : int):
	deleted = await bot.purge_from(ctx.message.channel, limit=msglimit)
	embed = discord.Embed(description='Cleared **{}** message(s) from the channel! ⚠'.format(len(deleted)), color=0xffafc9,)
	selfdel = await bot.say(embed=embed)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	#embed = discord.Embed(description="Sorry that's too much...", color=0xffafc9,)
	#await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def about(ctx):
	embed = discord.Embed(title="https://discord.gg/UjuGRB9", description="For any other help please join our Discord server...", url="https://discord.gg/UjuGRB9", color=0xffafc9)
	embed.set_author(name="MikiBot", url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.add_field(name="About", value="Hey everyone, I'm MikiBot ^^ \nI'm also very new discord and I'd like your help to improve myself :D \nPlease use m!help to see what else I can do for you~", inline=False)
	embed.add_field(name="Social", value="<:curiouscat:508516637700259850> Curious Cat | <:twitter:508515087330312193> Twitter", inline=True)
	embed.add_field(name="Website", value="🌏 https://goo.gl/wKEVjA", inline=True)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def servercount(ctx):
	embed = discord.Embed(description='Currently watching over ' + str(len(bot.servers)) + ' Discord servers <:discord:501956002158215198>', color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def invite(ctx):
	embed = discord.Embed(description="If you'd like to add MikiBot to your server, go to our website here: https://relykxdiscord.wixsite.com/mikibot", color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def vote(ctx):
	embed = discord.Embed(description="You can vote here: \nhttps://discordbots.org/bot/496214977267630080/vote", color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def donate(ctx):
	embed = discord.Embed(title="Patreon", description="You can donate here: \nhttps://www.patreon.com/join/mikidiscord?", color=0xffafc9)
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/499771950764261396/513936104357888000/icon_color_variations.jpg")
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def time(ctx):
	dash = strftime("%I:%M", gmtime())
	wholetime = dash[0] + dash[1]
	resttime = dash[2:]
	await bot.say("The server time now is: **" + wholetime + resttime + ", Obtained by 24timezones**")
	
##############################################################################################################################
# 😜 | F U N - C O M M A N D S													      
##############################################################################################################################
	
@bot.command(pass_context=True)
async def hi(ctx):
	randomlist = ['>//< hellu',
                      'hai ^^',
                      'hewo o3o',
		      'h-hi o-o',
		      'hello ^-^',
		      'hellu',
		      'hai',
		      'hewo',
		      'h-hi',
		      'hello',
                     ]
	await bot.say("%s" %(random.choice(randomlist),))

@bot.command(pass_context=True)
async def kawaii(ctx):
	embed = discord.Embed(title="💠 Kawaii Emoji", description="Find more here: https://kawaiiface.net/", color=0xffafc9,)
	embed.add_field(name="Happy", value="`(✿◠‿◠)` `≧◡≦` `(▰˘◡˘▰)` `(●´ω｀●)`\n`(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧` `（ミ￣ー￣ミ）` `(づ｡◕‿‿◕｡)づ` `✌.ʕʘ‿ʘʔ.✌`\n`◎[▪‿▪]◎`", inline=False)
	embed.add_field(name="Sad", value="`ಥ_ಥ` `┐(‘～'；)┌` `◄.►` `(◕︵◕)`\n`v( ‘.’ )v` `ਉ_ਉ` `o(╥﹏╥)o` `●︿●`\n`(∩︵∩)`", inline=False)
	embed.add_field(name="Mad", value="`〴⋋_⋌〵` `(◣_◢)` `☉▵☉凸` `ↁ_ↁ`\n`╚(•⌂•)╝` `ᇂﮌᇂ)` `ლ(́◉◞౪◟◉‵ლ`\n`(┛◉Д◉)┛彡┻━┻ `", inline=False)
	embed.add_field(name="Love", value="`v(=∩_∩=)ﾌ` `(n˘v˘•)¬` `♥╣[-_-]╠♥` `★~(◡﹏◕✿)`\n`(◕‿-)` `( ^▽^)σ)~O~)` `♥‿♥` `(✿ ♥‿♥)`\n`(●´ω｀●)`", inline=False)
	embed.add_field(name="Party", value="`\m/(>.<)\m/` `ヾ(〃^∇^)ﾉ` `(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧` `♨(⋆‿⋆)♨`\n`┌( ಠ_ಠ)┘` `Ｏ(≧▽≦)Ｏ` `☜-(ΘLΘ)-☞` `@(ᵕ.ᵕ)@`\n`╘[◉﹃◉]╕`", inline=False)
	embed.add_field(name="Weird", value="`（ ´_⊃｀）` `(￣。￣)～ｚｚｚ` `~(⊕⌢⊕)~` `⊂•⊃_⊂•⊃`\n`ᕙ(⇀‸↼‶)ᕗ` `( 　ﾟ,_ゝﾟ)` `(⊙︿⊙✿)` `̿̿’̿’\̵͇̿̿\=(•̪●)=/̵͇̿̿/’̿̿ ̿ ̿ ̿`\n`( ͡° ͜ʖ ͡°)`", inline=False)
	await bot.say(embed=embed)
	
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
	embed = discord.Embed(title ="🎲 Dice Roll", description="*rolls a dice*", color=0xffafc9,)
	embed.add_field(name="You rolled a dice and it landed on...", value="Side: **%s**" %(random.choice(randomlist),))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def coinflip(ctx):
	randomlist = ['Heads','Tails',]
	embed = discord.Embed(title ="💰 Coin Flip", description="*flips a coin*", color=0xffafc9,)
	embed.add_field(name="You flipped a coin and it landed on", value="Face: **%s**" %(random.choice(randomlist),))
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
	embed = discord.Embed(title ="🎱 8 Ball", description="*shakes the 8 Ball up...*", color=0xffafc9,)
	embed.add_field(name="You shook the 8 ball and it shows you...", value="Answer: **%s**" %(random.choice(randomlist),))
	await bot.say(embed=embed)
	
##############################################################################################################################
# ℹ️ | H E L P - C O M M A N D S	
##############################################################################################################################
	
@bot.command(pass_context=True)
async def commands(ctx):
	embed = discord.Embed(title="📖 General", color=0xffafc9)
	embed.add_field(name="server", value="Displays the info of the current server.", inline=False)
	embed.add_field(name="info", value="Displays a profile of the mentioned user.", inline=False)
	embed.add_field(name="avatar", value="Dusplays the profile pic of the mentioned user.", inline=False)
	embed.add_field(name="kick", value="Kicks the mentioned user.", inline=False)
	embed.add_field(name="clear", value="Clears a specific amount of messages in a channel.", inline=False)
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
