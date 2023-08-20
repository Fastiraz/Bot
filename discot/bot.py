
##############################
##                          ##
## </> by Fastiraz with 💔  ##
##                          ##
##############################

import os, datetime, asyncio, threading, nextcord.utils
from nextcord.utils import get
from nextcord.ui import Button, View
from nextcord.ext import commands
#from googletrans import Translator #Translator

Token = 'TOKEN_HERE'

bot = commands.Bot(intents=nextcord.Intents.all(),
        command_prefix= ".",
        description='The Best Bot For the Best User!')
bot = nextcord.Client(intents=nextcord.Intents.all())

@bot.event
async def on_ready():
    os.system('clear')
    print('Online... ✔')
    print(f'Logged in as {bot.user} ✔ \n(ID: {bot.user.id})')
    print('------')
    for guild in bot.guilds:
        print('Active in {}\n➜ Member Count : {}\n'.format(guild.name,guild.member_count))

@bot.slash_command(name="ping")
async def ping(ctx):
    button = Button(label="Click me b*tch!",
        style=nextcord.ButtonStyle.blurple,
        emoji="🏓")

    async def button_callback(interaction):
        ping_ = bot.latency
        ping =  round(ping_ * 1000)
        embed=nextcord.Embed(title="🏓 Pong",
            description=f"My latency is {ping}ms",
            color=0xA827FC)
        await interaction.response.send_message(embed=embed)

    button.callback = button_callback

    view = View()
    view.add_item(button)
    await ctx.send("> ``Ping 🏓``", view=view)

@bot.slash_command(name="clear")
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()
    for each_message in messages:
        await each_message.delete()
    await ctx.send(f"``{number_of_messages} Messages have been cleared.🗯``")
    return

@bot.slash_command(name="help")
async def help(ctx):
    helptext = """> ``Commands:``
                >      ``help                - Display this.``
                >      ``Google Translate    - Translates your messages``
                >      ``ping                - To ping the bot. (1ms)``
                >      ``shazam              - To reboot the bot.``
                >      ``ticket              - To open a ticket for supports.``
                >      ``role                - To get roles.``
                >      ``map                 - Link of Assetto's mappings [/map shutoko]``
                >      ``carpack             - Links for Assetto's carpacks [/carpack gravygarage]``
                >      ``server              - Links to join Assetto's servers [/server midnight club]``
                >      ``doc                 - Links to get my doc``"""
    embed=nextcord.Embed(
        title="**__FEATURES__**",
        url="https://fastiraz.github.io/",
        description=helptext,
        color=0xff7979)
    await ctx.send(embed=embed)

@bot.slash_command(name="ticket")
async def ticket(ctx):
    embed=nextcord.Embed(
        title="**__ROLES MANAGEMENTS__**",
        url="https://fastiraz.github.io/",
        description="> ``Fonctionnalitée en cours de développement...``",
        color=0xff7979)
    await ctx.send(embed=embed)

@bot.slash_command(name="role")
async def role(ctx):
    desc = """
        > ``🍫 - Chocolate``
        > ``🥤 - Soda``
        > ``🍦 - Ice Cream``
        > ``🍣 - Sushi``
        > ``🍨 - Another Ice Cream``"""
    embed=nextcord.Embed(title="**__ROLES MANAGEMENTS__**", url="https://fastiraz.github.io/", description=desc, color=0xff7979)
    msg = await ctx.send(embed=embed)
    reactionList = ['🍫', '🥤', '🍦', '🍣', '🍨']
    for emoji in reactionList:
        await msg.add_reactions(emoji)


@bot.event
async def on_message(message):
    guild = message.guild
    log_channel = nextcord.utils.get(guild.channels, name="『✅』message-log")
    if log_channel is None:
        return
    if not message.author.bot:
        #await log_channel.send(message)
        embed=nextcord.Embed(
            color=0x00ff00,
            timestamp=datetime.datetime.utcnow(),
            description=f"in {message.channel.mention}:\n{message.content}"
        )
        embed.set_author(name=message.author)
        embed.set_footer(text=message.author.id)
        if len(message.attachments) > 0:
            embed.set_image(url = message.attachments[0].url)
        await log_channel.send(embed=embed)

@bot.event
async def on_message_delete(message):
    guild = message.guild
    log_channel = nextcord.utils.get(guild.channels, name="『❌』deleted-message")
    if log_channel is None:
        await bot.process_commands(message)
        return
    if not message.author.bot:
        embed=nextcord.Embed(
            color=0xff0000,
            timestamp=datetime.datetime.utcnow(),
            description="in {}:\n{}".format(message.channel.mention, message.content)
        )
        embed.set_author(name=message.author)
        embed.set_footer(text=message.author.id)
        if len(message.attachments) > 0:
            embed.set_image(url = message.attachments[0].url)
        await log_channel.send(embed=embed)
    await bot.process_commands(message)

@bot.event
async def on_message_edit(message_before, message_after):
    guild = message_before.guild
    channel = nextcord.utils.get(guild.channels, name="『📝』edited-message")
    embed = nextcord.Embed(title = f"{message_before.author} Edited Their Message",
        description = f"Before: {message_before.content}\nAfter: {message_after.content}\nAuthor: {message_before.author.mention}\nLocation: {message_before.channel.mention}",
        timestamp = datetime.datetime.utcnow(),
        color = nextcord.Colour.blue())
    embed.set_author(name = message_after.author.name, icon_url = message_after.author.display_avatar)
    await channel.send(embed = embed)

@bot.slash_command(name='fastiraz')
async def fastiraz(ctx):
    embed=nextcord.Embed(title="Fastiraz",
        url="https://fastiraz.github.io/",
        description="> ``Who is Fastiraz ?``",
        color=0xFF0000)
    await ctx.send(embed=embed)

@bot.slash_command(name="join")
async def join(self, ctx, *, channel: nextcord.VoiceChannel):
    """Joins a voice channel"""

    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)

    await channel.connect()

@bot.slash_command(name="map")
async def map(ctx, map, version):
    if map == "shutoko" and version == "all":
        url = """> Version 0.9.1: https://drive.google.com/file/d/1MiE_2gUptb7kC58IZP2RhbFHmd_GV91k/view?usp=sharing

        > Version 0.9.2: https://drive.google.com/file/d/1L6x_H-3nJrW1wzCsBI6LEVU8z8L1_Fj6/view?usp=sharing"""
    elif map == "shutoko" and version == "0.9.1":
        url = "> https://drive.google.com/file/d/1MiE_2gUptb7kC58IZP2RhbFHmd_GV91k/view?usp=sharing"
    elif map == "shutoko" and version == "0.9.2":
        url = "> https://drive.google.com/file/d/1L6x_H-3nJrW1wzCsBI6LEVU8z8L1_Fj6/view?usp=sharing"
    elif map == "union island" and version == "all":
        url = "> https://drive.google.com/file/d/1DIwTPHmCIIxub30WU1wCvSSFpYqxuyZ7/view"
    elif map == "daikoku" and version == "all":
        url = "> https://drive.google.com/file/d/1wRGLuv4dPb3Ifn4SBJy661_gsma8ym2D/view?usp=sharing"
    elif map == "underground" and version == "all":
        url = "> https://mega.nz/file/NPBCgKjR#Xb8DofvJianBlrugrSM9hA1BLlT4_UjW35uFFZTAyG0"
    elif map == "underground" and version == "6":
        url = "> https://mega.nz/file/NPBCgKjR#Xb8DofvJianBlrugrSM9hA1BLlT4_UjW35uFFZTAyG0"
    elif map == "mostwanted" and version == "all":
        url = "> https://mega.nz/file/0SowXBCR#-xdl5mPzEN457hnSh8gFM4pTu344YrdHe4GirZ_agns"
    elif map == "mostwanted" and version == "2.0":
        url = "> https://mega.nz/file/0SowXBCR#-xdl5mPzEN457hnSh8gFM4pTu344YrdHe4GirZ_agns"
    elif map == "akina" and version == "all":
        url = "> https://acmods.net/tracks/mount-akina-2017/"
    elif map == "monaco" and version == "all":
        url = "> https://sharemods.com/3zrhpgnukafo/RealMonaco.7z.html"

    embed=nextcord.Embed(
        title=f"**Assetto Corsa {map.upper()} map**",
        description=f"{url}",
        color=0xff7979
        )
    await ctx.send(embed=embed)

@bot.slash_command(name="carpack")
async def carpack(ctx, carpack):
    if carpack == "tando buddies":
        url = "> https://drive.google.com/drive/folders/1zmChYk5CfsbgOuSMpVLexfiu7npow5Ui"
    elif carpack == "gravygarage":
        url = "> https://drive.google.com/file/d/1NbC5GWQhZDi5wwbM6hNeUng7vqFMw8At/view?usp=sharing"
    elif carpack == "wdt":
        url = "> https://files.acstuff.ru/shared/tiCD/WDTCarPack2021.zip"
    elif carpack == "wdts":
        url = "> https://files.acstuff.ru/shared/cczR/WDT_StreetPack_11.zip"
    elif carpack == "wdtw":
        url = "> https://files.assettocorsaclub.com/file/acclub-files/3faf8a/WinterDriftPack2020_v12.zip"

    embed=nextcord.Embed(
        title=f"**Assetto Corsa {carpack.upper()} carpack**",
        description=f"{url}",
        color=0xff7979
        )
    await ctx.send(embed=embed)

@bot.slash_command(name="server")
async def server(ctx, server):
    if server == "midnight club":
        url = """> Midnight Club | Shutoko: https://acstuff.ru/s/q:race/online/join?ip=51.195.43.171&httpPort=8081
        > Midnight Club | Daikoku: https://acstuff.ru/s/q:race/online/join?ip=51.195.43.171&httpPort=8111
        > Midnight Club | Union Island: https://acstuff.ru/s/q:race/online/join?ip=51.195.43.171&httpPort=8101"""

    elif server == "aeo boyz":
        url = """> AEO Boyz | Shutoko EU1: https://acstuff.ru/s/q:race/online/join?ip=138.197.183.8&httpPort=8081
        > AEO Boyz | Shutoko EU2: https://acstuff.ru/s/q:race/online/join?ip=138.197.183.8&httpPort=8082"""

    elif server == "shutoko revival":
        url = """> Shutoko Revival | Shutoko EU1: https://acstuff.ru/s/q:race/online/join?ip=65.108.176.35&httpPort=8081
        > Shutoko Revival | Shutoko EU2: https://acstuff.ru/s/q:race/online/join?ip=65.108.176.35&httpPort=8082
        > Shutoko Revival | Shutoko EU3: https://acstuff.ru/s/q:race/online/join?ip=65.108.176.35&httpPort=8083"""

    elif server == "gravygarage":
        url = """> https://acstuff.ru/s/q:race/online/join?ip=103.212.224.118&httpPort=8090
        > https://acstuff.ru/s/q:race/online/join?ip=103.62.50.28&httpPort=8090
        > https://acstuff.ru/s/q:race/online/join?ip=103.62.51.124&httpPort=8150"""

    embed=nextcord.Embed(
        title=f"**Assetto Corsa {server.upper()} server**",
        description=f"{url}",
        color=0xff7979
        )
    await ctx.send(embed=embed)

@bot.slash_command(name="doc")
async def doc(ctx):
    embed=nextcord.Embed(
        title=f"**DOCUMENTATIONS**",
        description=f"https://fastiraz.gitbook.io/doc",
        color=0xff7979
        )
    await ctx.send(embed=embed)


@bot.slash_command(name="esgicode")
async def esgicode(ctx, nation: int):
    if nation == 1:
        code = "Y'en a pas mon reuf juste rentre."
    elif nation == 2:
        code = "1962A"
    elif nation == 3:
        code = "0310"

    embed=nextcord.Embed(
        title=f"**ESGI CODES**",
        description=f"Le code est {code}.",
        color=0xff7979)
    await ctx.send(embed=embed)

@bot.slash_command(name="esgirole")
async def esgirole(ctx):
    desc = """
        > ``🍫 - SI``
        > ``🥤 - SRC``
        > ``🍦 - NSFW``
        > ``🍣 - Sushi``
        > ``🍨 - Another Ice Cream``"""
    embed=nextcord.Embed(title="**__ROLES MANAGEMENTS__**", url="https://fastiraz.github.io/", description=desc, color=0xff7979)
    msg = await ctx.send(embed=embed)
    reactionList = ['🍫', '🥤', '🍦', '🍣', '🍨']
    for emoji in reactionList:
        await msg.add_reactions(emoji)

@bot.event
async def on_member_update(before, after):
    # Check if the member has updated their roles
    if before.roles != after.roles:
        # Get the names of the old and new roles
        old_roles = [role.name for role in before.roles]
        new_roles = [role.name for role in after.roles]

        guild = before.guild
        channel = nextcord.utils.get(guild.channels, name="『🔖』role-log")

        embed=nextcord.Embed(
            title=f"**ROLES LOGS**",
            description=f"""> {before.name} updated their roles:

                           > Old roles: {', '.join(old_roles)}

                           > New roles: {', '.join(new_roles)}""",
            color=0xff7979
        )
    await channel.send(embed=embed)


@bot.event
async def on_message(message):
    # Check if the message starts with "!ticket"
    if message.content.startswith(".ticket"):
        guild = message.guild
        category = nextcord.utils.get(guild.categories, name="𝗧𝗜𝗖𝗞𝗘𝗧𝗦")
        ticket_channel = await message.guild.create_text_channel(
            f"ticket-{message.author.id}", category=category
        )

        await ticket_channel.set_permissions(message.author, read_messages=True, send_messages=True)

        embed=nextcord.Embed(
            title=f"**TICKET TOOL**",
            description=f"> Your ticket has been created in {ticket_channel.mention}.",
            color=0xff7979
        )
        await message.channel.send(embed=embed)

        button = Button(label="Close",
            style=nextcord.ButtonStyle.red,
            emoji="❌")

        async def button_callback(interaction):
            await ticket_channel.delete()

        button.callback = button_callback

        view = View()
        view.add_item(button)

        embed=nextcord.Embed(
                title=f"**TICKET TOOL**",
                description=f"> When you've done with moderators, close the ticket with the button bellow.",
                color=0xff7979
            )
        await ticket_channel.send(embed=embed, view=view)


@bot.slash_command(name="chatgpt")
async def chatgpt(ctx, prompt):
    import openai #, requests
    openai.api_key = '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'
    print('\nOpenAI test...')
    async with ctx.channel.typing():
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )
        reply = completions.choices[0].text
        #reply = completions["choices"][0]["text"]
        if len(reply) > 2000:
            reply = 'More than 2000'
    embed=nextcord.Embed(
        title=f"**ChatGPT**",
        description=f'> {reply}',
        color=0xff7979
    )
    await ctx.send(embed=embed)



def encrypt(algo, str):
    if algo == "sha1":
        import hashlib
        hash = hashlib.sha1(str.encode())
        return hash.hexdigest()
    elif algo == "sha224":
        import hashlib
        hash = hashlib.sha224(str.encode())
        return hash.hexdigest()
    elif algo == "sha256":
        import hashlib
        hash = hashlib.sha256(str.encode())
        return hash.hexdigest()
    elif algo == "sha384":
        import hashlib
        hash = hashlib.sha384(str.encode())
        return hash.hexdigest()
    elif algo == "sha512":
        import hashlib
        hash = hashlib.sha512(str.encode())
        return hash.hexdigest()
    elif algo == "md5":
        import hashlib
        hash = hashlib.md5(str.encode())
        return hash.hexdigest()

"""def decrypt(algo, str):
    #list = []
    found = 0
    with open('wordlist.txt', 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            #list = [algo, line]
            hashed_line = encrypt(algo, line)
            if hashed_line == str:
                found = 1
                return f'Match found for {str} :\n> ``{line}``'
    if found == 0:
        return "``[FAILED!]``"

@bot.slash_command(name="hash")
async def hash(ctx, crypt, algo, string):
    #if password == "Fastiraz":
    #await ctx.defer(hidden=True)
    #await interaction.response.defer()
    #await interaction.response.defer(ephemeral=False)
    import hashlib
    if crypt == 'encrypt':
        str = encrypt(algo, string)
        embed=nextcord.Embed(
            title=f"**HACKING - HASH**",
            description=f"> {algo} hash for {string} : \n> ``{str}``",
            color=0x000000
        )
        await ctx.send(embed=embed)
    elif crypt == 'decrypt':
        await asyncio.sleep(10) # Doing stuff
        str = decrypt(algo, string)
        embed=nextcord.Embed(
            title=f"**HACKING - HASH**",
            description=f"> {str}",
            color=0x000000
        )
        await ctx.send(embed=embed)
    else:
        pass"""


def decrypt(algo, str, response):
    found = 0
    with open('wordlist.txt', 'r') as file:
        for line in file:
            line = line.replace("\n", "")
            hashed_line = encrypt(algo, line)
            if hashed_line == str:
                found = 1
                response.append(f'Match found for {str} :\n> ``{line}``')
    if found == 0:
        response.append("``[FAILED!]``")

@bot.slash_command(name="hash")
async def hash(ctx, crypt, algo, string):
    import hashlib
    if crypt == 'encrypt':
        str = encrypt(algo, string)
        embed=nextcord.Embed(
            title=f"**HACKING - HASH**",
            description=f"> {algo} hash for {string} : \n> ``{str}``",
            color=0x000000
        )
        await ctx.send(embed=embed)
    elif crypt == 'decrypt':
        response = []
        thread = threading.Thread(target=decrypt, args=(algo, string, response))
        thread.start()
        embed=nextcord.Embed(
            title=f"**HACKING - HASH**",
            description=f"Decrypting {algo} hash for {string}...\nThis may take a few seconds.",
            color=0x000000
        )
        msg = await ctx.send(embed=embed)
        thread.join()
        response_str = "\n".join(response)
        embed=nextcord.Embed(
            title=f"**HACKING - HASH**",
            description=response_str,
            color=0x000000
        )
        await msg.edit(embed=embed)
    else:
        pass


@bot.event
async def on_member_join(member):
    if member.guild.name == "BETA":
        role = nextcord.utils.get(member.guild.roles, name="User")
        await member.add_roles(role)
    elif member.guild.name == "ESGI-SI":
        role = nextcord.utils.get(member.guild.roles, name="𝙎𝙏𝙐𝘿𝙀𝙉𝙏𝙎")
        await member.add_roles(role)



@bot.slash_command(name="sherlock")
async def sherlock(ctx, username):
    pass

@bot.slash_command(name="holehe")
async def holehe(ctx, mail):
    pass


@bot.event
async def on_guild_channel_create(channel):
    log_channel = nextcord.utils.get(channel.guild.channels, name='『✅』created-channels')

    if log_channel is None:
        return

    embed=nextcord.Embed(
        color=0x00ff00,
        #description=f'> A channel named ``{channel.name}`` has been created by ``{channel.created_by}``.\n'
        description=f'> A channel named ``{channel.name}`` has been created.\n'
    )
    timestamp=datetime.datetime.utcnow(),
    embed.set_footer(text=timestamp)
    await log_channel.send(embed=embed)

@bot.event
async def on_guild_channel_update(before, after):
    log_channel = nextcord.utils.get(after.guild.channels, name='『📝』edited-channels')

    if log_channel is None:
        return

    embed=nextcord.Embed(
        color=0xFC9E27,
        #description=f'> A channel named ``{before.name}`` has been edited to ``{after.name}`` by ``{after.edited_by}``.\n'
        description=f'> A channel named ``{before.name}`` has been edited to ``{after.name}``.\n'
    )
    timestamp=datetime.datetime.utcnow(),
    embed.set_footer(text=timestamp)
    await log_channel.send(embed=embed)

@bot.event
async def on_guild_channel_delete(channel):
    log_channel = nextcord.utils.get(channel.guild.channels, name='『❌』deleted-channels')

    if log_channel is None:
        return

    embed=nextcord.Embed(
        color=0xFF0000,
        #description=f'> A channel named ``{channel.name}`` has been deleted by ``{channel.deleted_by}``.\n'
        description=f'> A channel named ``{channel.name}`` has been deleted.\n'
    )
    timestamp=datetime.datetime.utcnow(),
    embed.set_footer(text=timestamp)
    await log_channel.send(embed=embed)


@bot.slash_command(name="init")
async def init_logs_channels(ctx):
    guild = ctx.guild

    logs_category = nextcord.utils.get(guild.categories, name='LOGS')
    if logs_category is None:
        logs_category = await guild.create_category('LOGS')

    messages_channel = nextcord.utils.get(guild.channels, name='『✅』message-log')
    if messages_channel is None:
        messages_channel = await guild.create_text_channel('『✅』message-log', category=logs_category)

    edited_channel = nextcord.utils.get(guild.channels, name='『📝』edited-message')
    if edited_channel is None:
        edited_channel = await guild.create_text_channel('『📝』edited-message', category=logs_category)

    deleted_channel = nextcord.utils.get(guild.channels, name='『❌』deleted-message')
    if deleted_channel is None:
        deleted_channel = await guild.create_text_channel('『❌』deleted-message', category=logs_category)

    role_channel = nextcord.utils.get(guild.channels, name='『🔖』role-log')
    if role_channel is None:
        role_channel = await guild.create_text_channel('『🔖』role-log', category=logs_category)

    messages_channel = nextcord.utils.get(guild.channels, name='『✅』created-channels')
    if messages_channel is None:
        messages_channel = await guild.create_text_channel('『✅』created-channels', category=logs_category)

    edited_channel = nextcord.utils.get(guild.channels, name='『📝』edited-channels')
    if edited_channel is None:
        edited_channel = await guild.create_text_channel('『📝』edited-channels', category=logs_category)

    deleted_channel = nextcord.utils.get(guild.channels, name='『❌』deleted-channels')
    if deleted_channel is None:
        deleted_channel = await guild.create_text_channel('『❌』deleted-channels', category=logs_category)

    embed=nextcord.Embed(
        title=f"**DOCUMENTATIONS**",
        description=f"> `The logs channels have been created!`",
        color=0xff7979
        )
    await ctx.send(embed=embed)

#bot.run(os.getenv(Token))
bot.run(Token)
