import discord
from discord.ext import commands

class Rotation(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f' {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Rotation(client))