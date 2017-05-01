from discord.ext import commands
from core import checks
import discord


class Basic:
    """A Basic command example for D.py Rewrite/Red V3"""

    @commands.command()
    async def basicping(self, ctx):
        """Your basic ping command"""
        # Even though we no longer need to use ``Pass_context``,
        # We still have to pass it in the command sceheme.
        await ctx.send("Pong!")

    @commands.command()
    async def nsfwping(self, ctx):
        """A ping with a check"""
        if ctx.channel.is_nsfw() is True:
            await ctx.send("Pong!")
        else:
            await ctx.send("This isn't a NSFW Channel")

    @commands.command()
    @checks.is_owner()
    async def error(self, ctx):
        """A command that errors"""
        raise Exception('DEAR GOD STUFF BROKE!')
