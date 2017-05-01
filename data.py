from discord.ext import commands
from core.utils.helpers import JsonDB


class Data:
    """A cog that uses the new JsonDB drivers!"""

    def __init__(self):
        self.dict = JsonDB("data/settings.json", create_dirs=True)

    @commands.command()
    async def showall(self, ctx):
        """Show all entries in the dict"""
        await ctx.send(self.dict.all())

    @commands.command()
    async def set(self, ctx, key, value):
        await self.dict.set(key, value)
        await ctx.send('Done!')

    @commands.command()
    async def pop(self, ctx, key):
        await self.dict.pop(key)
        await ctx.send('Done! {} is popped'.format(key))

    @commands.command()
    async def get(self, ctx, key):
        await ctx.send(self.dict.get(key))

    @commands.command()
    async def wipe(self, ctx):
        await self.dict.wipe()
        await ctx.send('Done! wiped everything >:D')
