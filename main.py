import discord
from discord.ext import commands
from discord.embeds import Embed


client = commands.Bot(command_prefix="$")
client.remove_command("help")

token = ""

@client.event
async def on_ready():
    print(f"We have logged in as...\n{client.user}")

@client.command()
async def massunban(ctx):
    embed=discord.Embed()
    embed.add_field(name="Mass unban started!", value="github.com/tescomealdealll")
    await ctx.send(embed=embed)
    blist = await ctx.guild.bans()
    for users in blist:
        try:
            await ctx.guild.unban(user=users.user)
        except:
            pass

@client.event
async def on_member_unban(guild, user):
    print("Unbanned a user!")

client.run(token)
