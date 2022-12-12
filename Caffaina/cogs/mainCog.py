import discord
from discord.ext import commands


class devcmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reload', aliases=['rl'])
    async def reload(self, ctx, extension):
        try:
            await ctx.send(f"Working on unloading {extension}")
            self.bot.unload_extension("cogs." + extension)
            await ctx.send(f"Unloaded {extension}")
            try:
                await ctx.send(f"Working on loading {extension}")
                self.bot.load_extension("cogs." + extension)
                await ctx.send(f"Loaded {extension}")
            except Exception as error:
                await ctx.send(f"{extension} cannot be loaded. [{error}]")

        except Exception as error:
            await ctx.send(f"{extension} cannot be unloaded. [{error}]")

    @commands.command(name="unload", aliases=['ul'])
    async def unload(self, ctx, cog):
        try:
            self.bot.unload_extension("cogs." + cog)
            await ctx.send(f"Unloaded {cog}")
        except Exception as error:
            await ctx.send(f"{cog} cannot be unloaded. [{error}]")

    @commands.command(name="load")
    async def load(self, ctx, cog):
        try:
            self.bot.load_extension("cogs." + cog)
            await ctx.send(f"Loaded {cog}")
        except Exception as error:
            await ctx.send(f"{cog} cannot be loaded. [{error}]")

    @commands.command(name="listcogs", aliases=['lc'])
    async def listcogs(self, ctx):
        base_string = "```css\n" 
        base_string += "\n".join([str(cog) for cog in self.bot.extensions])
        base_string += "\n```"
        await ctx.send(base_string)

    @commands.command()
    async def status(self, ctx):
        await ctx.send("I am online")


def setup(bot):
    bot.add_cog(devcmds(bot))
