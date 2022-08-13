import discord
from discord.ext import commands,tasks
from discord.ext.commands import Bot

Token = '' #PUT YOUR BOT'S TOKEN HERE
bot = commands.Bot(command_prefix=".", description='Music is life :notes::musical_note:')

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'france'
    }
]

@bot.event
async def on_ready():
    print('Speedy is online... :heavy_check_mark:')
    print(f'Logged in as {bot.user} :heavy_check_mark: \n(ID: {bot.user.id})')
    print('------')
    for guild in bot.guilds:
        for channel in guild.text_channels :
            if str(channel) == "『:clipboard:』𝐂𝐡𝐚𝐭":
                embed = discord.Embed(title="Music bot activated..", description="Dev by Fastiraz", color=0xAA00FF) #creates embed
                file = discord.File("./img/thicker.png", filename="thicker.png")
                embed.set_image(url="attachment://thicker.png")
                await channel.send(file=file, embed=embed)
        print('Active in {}\n Member Count : {}'.format(guild.name,guild.member_count))
    bot.load_extension('dismusic')

bot.run(Token)
