import discord
from discord.ext import commands

class funCmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hey!")

    @commands.command()
    async def testTest(self, ctx):
        await ctx.send("Hey!")

    @commands.command()
    async def retestTest(self, ctx):
        await ctx.send("reload success")

def setup(bot):
    bot.add_cog(funCmds(bot))
