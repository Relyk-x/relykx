##############################################################################################################################
# 🤖 | B O T - S T A R T U P
##############################################################################################################################

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import datetime
from datetime import datetime
import time
import os

bot = commands.Bot(command_prefix='m!')
msglimit = 100
now = datetime.now()
version = "v0.0.0"

@bot.event
async def on_ready():
	servers = list(bot.servers)
	status = f"over {str(len(bot.servers))} servers"
	print (f"MikiBot is up and running with {str(len(bot.servers))} servers connected!")
	print ("Ready when you are...")
	print (f"I am running on {bot.user.name}")
	print (f"With the ID: {bot.user.id}")
	await bot.change_presence(game=discord.Game(name=status,type=3))
# WATCHING 'over ' + str(len(bot.servers)) + ' servers', url="https://www.twitch.tv/streamer"

@bot.event
async def on_member_join(member):
	print('Sent message to ' + member.name)
	servers = list(client.servers)
	print("Connected on " + str(len(client.servers)) + "servers:")
	embed = discord.Embed(color=0xffafc9,)
	embed.set_author(name="MikiBot", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.add_field(name="About", value="Hey everyone, I'm MikiBot ^^ \nI'm also very new discord and I'd like your help to improve myself :D \nPlease use m!help to see what else I can do for you~", inline=False)
	embed.add_field(name="Creator", value="<@257784039795064833>", inline=True)
	embed.set_footer(text=f"version: {version}")
	await bot.send_message(member, embed=embed)
	
	embed = discord.Embed(color=0xffafc9,)
	embed.set_author(name="Website", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.add_field(name="Link:", value="https://relykxdiscord.wixsite.com/mikibot", inline=False)
	await bot.send_message(member, embed=embed)
	
	embed = discord.Embed(color=0x7289da,)
	embed.set_author(name="Server", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/500485578794729482/discord_logo1600.png")
	embed.add_field(name="Link:", value="https://discord.gg/UjuGRB9", inline=False)
	await bot.send_message(member, embed=embed)
	
	embed = discord.Embed(color=0xce7a1e,)
	embed.set_author(name="Curious Cat", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/514996231647395841/curiouscat.png")
	embed.add_field(name="Link:", value="https://curiouscat.me/MikiDiscord", inline=False)
	await bot.send_message(member, embed=embed)
	
	embed = discord.Embed(color=0x2da9e1,)
	embed.set_author(name="Twitter", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/514996202719150088/twitter.png")
	embed.add_field(name="Link:", value="https://twitter.com/MikiDiscord", inline=False)
	await bot.send_message(member, embed=embed)
	
##############################################################################################################################
# 🔑 | A D M I N - C O M M A N D S
##############################################################################################################################

@bot.command(pass_context=True)
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.Member):
	embed = discord.Embed(title="Ban", description = f"{user.mention} has been banned by {ctx.message.author}", color=0xffafc9,)
	seldel = await bot.say(embed=embed)
	await bot.ban(user)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.Member):
	embed = discord.Embed(title="Unban", description="{0.name} has been unbanned from the server".format(user), color=0xffafc9,)
	seldel = await bot.say(embed=embed)
	await bot.unban(user)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	
@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
	embed = discord.Embed(title="⚠ Bot Logs", description="**{}** has been kicked from the server".format(user.name), color=0xffafc9,)
	selfdel = await bot.say(embed=embed)
	await bot.kick(user)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
	
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, msglimit : int):
	deleted = await bot.purge_from(ctx.message.channel, limit=msglimit)
	embed = discord.Embed(title="⚠ Bot Logs", description='Cleared **{}** message(s) from the channel'.format(len(deleted)), color=0xffafc9,)
	selfdel = await bot.say(embed=embed)
	await asyncio.sleep(10)
	await bot.delete_message(selfdel)
# embed = discord.Embed(description="Sorry that's too much...", color=0xffafc9,)
# await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
	embed = discord.Embed(title=":ping_pong: Bot Ping", description=":construction:  under construction :construction:", color=0xffafc9)
	await bot.say(embed=embed)
	# Time the time required to send a message first.
	# This is the time taken for the message to be sent, awaited, and then 
	# for discord to send an ACK TCP header back to you to say it has been
	# received; this is dependant on your bot's load (the event loop latency)
	# and generally how shit your computer is, as well as how badly discord
	# is behaving.
#	start = time.monotonic()
#	msg = await ctx.send('Pinging...')
#	millis = (time.monotonic() - start) * 1000

	# Since sharded bots will have more than one latency, this will average them if needed.
#	heartbeat = ctx.bot.latency * 1000

#	await msg.edit(content=f'Heartbeat: {heartbeat:,.2f}ms\tACK: {millis:,.2f}ms.')
	
@bot.command(pass_context=True)
async def count(ctx):
	bots = 0
	members = 0
	total = 0
	for x in ctx.message.server.members:
	 if x.bot == True:
	  bots += 1
	  total += 1
	 else:
	  members += 1
	  total += 1
	embed = discord.Embed(title="Server Member Count",color=0xffafc9)
	embed.add_field(name="Bot Count",value=bots)
	embed.add_field(name="Member Count",value=members)
	embed.add_field(name="Total",value=total)
	await bot.say(embed=embed)

##############################################################################################################################
# 📖 | G E N E R A L - C O M M A N D S
##############################################################################################################################

@bot.command(pass_context=True)
async def server(ctx):
	embed = discord.Embed(title="📋 Server Info", description="Here's what I could find.", color=0xffafc9)
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	embed.add_field(name="Name:", value=ctx.message.server.name, inline=True)
	embed.add_field(name="ID:", value=ctx.message.server.id, inline=True)
	embed.add_field(name="Region:", value=ctx.message.server.region, inline=True)
	embed.add_field(name="Owner:", value=ctx.message.server.owner.mention, inline=True)
# embed.add_field(name="Varification level:, value=?, inline=True)
	embed.add_field(name="Roles:", value=len(ctx.message.server.roles), inline=True)
# embed.add_field(name="Channels:", value=?, inline=True)
	embed.add_field(name="Online:", value=f"{len([I for I in ctx.message.server.members if I.status is discord.Status.online])}",inline=False)
# embed.add_field(name="Members:", value=len(ctx.message.server.member.status = discord.Status.online) + "\n" + len(ctx.message.server.members == 'offline') + "\n" + len(ctx.message.server.members), inline=True)
	embed.add_field(name="Members:", value=len(ctx.message.server.members), inline=True)
	embed.add_field(name="Created:", value=ctx.message.server.created_at, inline=False)
# embed.add_field(name="Number of Emotes:", value=?, inline=True)
	embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url) 
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def user(ctx, user: discord.Member):
	embed = discord.Embed(title="📋 User Info", description="Here's what I could find.", color=0xffafc9)
	embed.set_thumbnail(url=user.avatar_url)
	embed.add_field(name="Name", value=user, inline=True)
	embed.add_field(name="ID", value=user.id, inline=True)
	embed.add_field(name="Status", value=user.status, inline=False)
	embed.add_field(name="Highest role", value=user.top_role, inline=True)
	embed.add_field(name="Created", value=user.created_at, inline=True)
	embed.add_field(name="Joined", value=user.joined_at, inline=True)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="🖼️ User Avatar", description=f"Here it is {user.name}'s profile pic",color=0xffafc9)
	embed.set_image(url=user.avatar_url)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def about(ctx):
	embed = discord.Embed(color=0xffafc9,)
	embed.set_author(name="MikiBot", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.add_field(name="About", value="Hey everyone, I'm MikiBot ^^ \nI'm also very new discord and I'd like your help to improve myself :D \nPlease use m!help to see what else I can do for you~", inline=False)
	embed.add_field(name="Creator", value="<@257784039795064833>", inline=True)
	embed.set_footer(text=f"version: {version}")
	await bot.say(embed=embed)
	
	embed = discord.Embed(color=0xffafc9,)
	embed.set_author(name="Website", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/506802847791185920/miki2.png")
	embed.add_field(name="Link:", value="https://relykxdiscord.wixsite.com/mikibot", inline=False)
	await bot.say(embed=embed)
	
	embed = discord.Embed(color=0x7289da,)
	embed.set_author(name="Server", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/500485578794729482/discord_logo1600.png")
	embed.add_field(name="Link:", value="https://discord.gg/UjuGRB9", inline=False)
	await bot.say(embed=embed)
	
	embed = discord.Embed(color=0xce7a1e,)
	embed.set_author(name="Curious Cat", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/514996231647395841/curiouscat.png")
	embed.add_field(name="Link:", value="https://curiouscat.me/MikiDiscord", inline=False)
	await bot.say(embed=embed)
	
	embed = discord.Embed(color=0x2da9e1,)
	embed.set_author(name="Twitter", icon_url="https://cdn.discordapp.com/attachments/499771950764261396/514996202719150088/twitter.png")
	embed.add_field(name="Link:", value="https://twitter.com/MikiDiscord", inline=False)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def invite(ctx):
	embed = discord.Embed(description="📨 If you'd like to add MikiBot to your server, go to our website here: https://relykxdiscord.wixsite.com/mikibot", color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def vote(ctx):
	embed = discord.Embed(description="📥 You can vote here: \nhttps://discordbots.org/bot/496214977267630080/vote", color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def donate(ctx):
	embed = discord.Embed(title="💵 Patreon", description="You can donate here: \nhttps://www.patreon.com/join/mikidiscord?", color=0xffafc9)
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/499771950764261396/513936104357888000/icon_color_variations.jpg")
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def time(ctx):
	time = now.strftime("%I:%M %p")
	date = now.strftime("%a, %d %b %Y")
	embed = discord.Embed(title="🕗 Clock", color=0xffafc9)
	embed.add_field(name="Time", value=time, inline=True)
	embed.add_field(name="Date", value=date, inline=True)
	embed.set_footer(text=f"Requested by {ctx.message.author}", icon_url=ctx.message.author.avatar_url) 
	await bot.say(embed=embed)
	
##############################################################################################################################
# 😜 | F U N - C O M M A N D S													      
##############################################################################################################################
	
@bot.command(pass_context=True)
async def google(ctx,*args):
	x = f"https://www.google.com/search?rlz=1C1CHBF_enUS753US753&ei=n62RW536KpL2swWl1IKIBg&q={args}&oq=google+search&gs_l=psy-ab.3..0i71l8.0.0..8290...0.0..0.0.0.......0......gws-wiz.vtjc2PzIHFg"
	y = x.replace(" ","+")
	await bot.say(y)

@bot.command(pass_context=True)
async def youtube(ctx,*args):
	x = f"https://www.youtube.com/results?search_query={args}"
	y = x.replace(" ","+")
	await bot.say(y)

@bot.command(pass_context=True)
async def greet(ctx):
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
	embed.add_field(name="Happy", value="`(✿◠‿◠)` `≧◡≦` `(▰˘◡˘▰)` `(●´ω｀●)`\n`(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧` `（ミ￣ー￣ミ）` `(づ｡◕‿‿◕｡)づ`\n`✌.ʕʘ‿ʘʔ.✌` `◎[▪‿▪]◎`", inline=False)
	embed.add_field(name="Sad", value="`ಥ_ಥ` `┐(‘～'；)┌` `◄.►` `(◕︵◕)`\n`v( ‘.’ )v` `ਉ_ਉ` `o(╥﹏╥)o` `●︿●` `(∩︵∩)`", inline=False)
	embed.add_field(name="Mad", value="`〴⋋_⋌〵` `(◣_◢)` `☉▵☉凸` `ↁ_ↁ`\n`╚(•⌂•)╝` `ᇂﮌᇂ)` `ლ(́◉◞౪◟◉‵ლ`\n`(┛◉Д◉)┛彡┻━┻ `", inline=False)
	embed.add_field(name="Love", value="`v(=∩_∩=)ﾌ` `(n˘v˘•)¬` `♥╣[-_-]╠♥` `★~(◡﹏◕✿)`\n`(◕‿-)` `( ^▽^)σ)~O~)` `♥‿♥` `(✿ ♥‿♥)` `(●´ω｀●)`", inline=False)
	embed.add_field(name="Party", value="`\m/(>.<)\m/` `ヾ(〃^∇^)ﾉ` `(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧`\n`♨(⋆‿⋆)♨` `┌( ಠ_ಠ)┘` `Ｏ(≧▽≦)Ｏ` `☜-(ΘLΘ)-☞`\n`@(ᵕ.ᵕ)@` `╘[◉﹃◉]╕`", inline=False)
	embed.add_field(name="Weird", value="`（ ´_⊃｀）` `(￣。￣)～ｚｚｚ` `~(⊕⌢⊕)~` `⊂•⊃_⊂•⊃`\n`ᕙ(⇀‸↼‶)ᕗ` `( 　ﾟ,_ゝﾟ)` `(⊙︿⊙✿)`\n`̿̿’̿’\̵͇̿̿\=(•̪●)=/̵͇̿̿/’̿̿ ̿ ̿ ̿` `( ͡° ͜ʖ ͡°)`", inline=False)
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
	embed.add_field(name="serverinfo", value="Displays the info of the current server.", inline=False)
	embed.add_field(name="userinfo", value="Displays a profile of the mentioned user.", inline=False)
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
	embed.add_field(name="hi", value='Generates a response, for example: "hai ^-^"', inline=False)
	embed.add_field(name="kawaii", value="Displays multiple different kawaii emoji", inline=False)
	embed.add_field(name="wallpaper", value="Generates a random wallpaper.", inline=False)
	embed.add_field(name="gif", value="Generates a random gif.", inline=False)
	embed.add_field(name="ping", value="Pongs the user's ping.", inline=False)
	embed.add_field(name="dicroll", value="Rolls a six sided die.", inline=False)
	embed.add_field(name="coinflip", value="Flips a coin, could be heads could be tails.", inline=False)
	embed.add_field(name="eightball", value="Ask a question and shake the 8 Ball.", inline=False)
	await bot.say(embed=embed)
	
##############################################################################################################################
# 🛠️ | O W N E R - C O M M A N D S	
##############################################################################################################################

@bot.command(hidden=True)
@commands.is_owner
async def servercount(ctx):
	embed = discord.Embed(description='<:discord:501956002158215198> Currently watching over ' + str(len(bot.servers)) + ' Discord servers', color=0xffafc9)
	await bot.say(embed=embed)
	
@bot.command(hidden=True)
@commands.is_owner
async def test(ctx):
	embed = discord.Embed(title=":warning: Admin", description="All commands under the Admin categorie:", color=0xffafc9)
	embed.add_field(name="ban", value="-",inline=True)
	embed.add_field(name="unban", value="-",inline=True)
	embed.add_field(name="kick", value="-",inline=True)
	embed.add_field(name="clear", value="-",inline=True)
	embed.add_field(name="ping", value="-",inline=True)
	embed.add_field(name="count", value="-",inline=True)
	await bot.say(embed=embed)
	embed = discord.Embed(title=":cyclone: General", description="All commands under the General categorie:", color=0xffafc9)
	embed.add_field(name="server", value="-",inline=True)
	embed.add_field(name="user", value="-",inline=True)
	embed.add_field(name="avatar", value="-",inline=True)
	embed.add_field(name="about", value="-",inline=True)
	embed.add_field(name="invite", value="-",inline=True)
	embed.add_field(name="donate", value="-",inline=True)
	await bot.say(embed=embed)
	embed = discord.Embed(title=":sparkles: Fun", description="All commands under the Fun categorie:", color=0xffafc9)
	embed.add_field(name="google", value="-",inline=True)
	embed.add_field(name="youtube", value="-",inline=True)
	embed.add_field(name="greet", value="-",inline=True)
	embed.add_field(name="time", value="-",inline=True)
	embed.add_field(name="kawaii", value="-",inline=True)
	embed.add_field(name="wallpaper", value="-",inline=True)
	embed.add_field(name="gif", value="-",inline=True)
	embed.add_field(name="diceroll", value="-",inline=True)
	embed.add_field(name="coinflip", value="-",inline=True)
	embed.add_field(name="eightball", value="-",inline=True)
	await bot.say(embed=embed)
	
bot.run(os.getenv("BOT_TOKEN"))
