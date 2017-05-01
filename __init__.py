from .basic import Basic
from .data import Data


def setup(bot):
    bot.add_cog(Basic())
    bot.add_cog(Data())
