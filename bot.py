import os
import discord
from discord.ext import commands,tasks
from discord.ext.commands import Bot
import asyncio
import datetime

Token = '' #put your bot's token between apostrophes
bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print('Fastiraz is online... ✔')
    print(f'Logged in as {bot.user} ✔ \n(ID: {bot.user.id})')
    print('------')
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "『📋』𝐂𝐡𝐚𝐭":
                embed = discord.Embed(title="Bot activated..", description="Dev by Fastiraz", color=0xAA00FF) #creates embed
                file = discord.File("./img/discor.png", filename="discor.png")
                embed.set_image(url="attachment://discor.png")
                await channel.send(file=file, embed=embed)
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))

@bot.command(name='join', help='``Makes the bot join the channel.``')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("``Fastiraz is connected.✔``")

@bot.command(name='leave')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("``Fastiraz is disconnected.💨``")
    else:
        await ctx.send("``The bot is not connected to a voice channel.``")

@bot.command(name='pause', help='``This command pauses the song.``')
async def pause(self,ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
        await ctx.channel.send("``Paused ⏸``")
    else:
        await ctx.send("``The bot is not playing anything at the moment.``")

@bot.command(name='resume', help='Resumes the song')
async def resume(self,ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
        await ctx.channel.send("``resume ▶``")
    else:
        await ctx.send("``The bot was not playing anything before this. Use play command.``")

@bot.command(name='search', help='``Search a song.``')
async def search(self,ctx):
    await ctx.channel.send("``Searching for the song...🔎``")

@bot.command(name='play', help='``Play a song.``')
async def play(self,ctx):
    await ctx.channel.send("``Searching for the song...🔎``")

@bot.command(name='shazam')
async def shazam(ctx):
    if not ctx.message.author.name=="Fastiraz":
        print('Someone is trying to reboot the bot. ❌')
        await ctx.send('``EN : You are not authorised to do that. ❌``')
        await ctx.send("``FR : Tu n'as pas le droit de faire ça. ❌``")
    else:
        await ctx.send("``Reboot.✔``")
        exit()

@bot.command(name='about')
async def about(ctx):
    text = "``My name is Fastiraz!\n I was built by Fastiraz. At present I have limited features(find out more by typing !help)\n :)``"
    await ctx.send(text)

@bot.event
async def on_member_join(member):
     for channel in member.guild.text_channels :
         if str(channel) == "『📋』𝐂𝐡𝐚𝐭" :
             on_mobile=False
             if member.is_on_mobile() == True :
                 on_mobile = True
             await channel.send("``Welcome to the Server {}!!\n On Mobile : {}``".format(member.name,on_mobile))   

@bot.event
async def on_message(message):
    guild = message.guild
    log_channel = discord.utils.get(guild.channels, name="『✅』message-log")
    if log_channel is None:
        await bot.process_commands(message)
        return
    if not message.author.bot:
        embed=discord.Embed(
            color=0x00ff00,
            timestamp=datetime.datetime.utcnow(),
            description="in {}:\n{}".format(message.channel.mention, message.content)
        )
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.set_footer(text=message.author.id)
        if len(message.attachments) > 0:
            embed.set_image(url = message.attachments[0].url)
        await log_channel.send(embed=embed)
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    guild = message.guild
    log_channel = discord.utils.get(guild.channels, name="『❌』deleted-message")
    if log_channel is None:
        await bot.process_commands(message)
        return
    if not message.author.bot:
        embed=discord.Embed(
            color=0xff0000,
            timestamp=datetime.datetime.utcnow(),
            description="in {}:\n{}".format(message.channel.mention, message.content)
        )
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.set_footer(text=message.author.id)
        if len(message.attachments) > 0:
            embed.set_image(url = message.attachments[0].url)
        await log_channel.send(embed=embed)
    await bot.process_commands(message)

@bot.event
async def on_message_edit(message_before, message_after):
    guild = message_before.guild
    embed = discord.Embed(title="{} edited a message".format(message_before.author.name), description="", color=0xFFA600)
    embed.set_author(name=message_before.author, icon_url=message_before.author.avatar_url)
    embed.set_footer(text=message_after.author.id)
    embed.add_field(name=message_before.content, value="This is the message before any edit", inline=True)
    embed.add_field(name=message_after.content, value="This is the message after the edit", inline=True)
    channel = discord.utils.get(guild.channels, name="『📝』edited-message")
    await channel.send(channel, embed=embed)

@bot.command(name='clear')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()
    for each_message in messages:
        await each_message.delete() 
    await ctx.send("``Messages have been cleared.🗯``")
    return

bot.run(Token)
