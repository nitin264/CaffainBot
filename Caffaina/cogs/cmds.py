import discord
from discord.ext import commands

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def loadCmds(self, ctx):
        await ctx.send("load success")

    @commands.command()
    async def retestCmds(self, ctx):
        await ctx.send("reload success")

def setup(bot):
    bot.add_cog(cmds(bot))