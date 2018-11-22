import discord
from redbot.core import commands

class fliptable(commands.Cog):
    """flip a table."""

    @commands.command()
    async def fliptable(self, ctx):
        """it flips a table"""
        embed=discord.Embed(color=0x8080ff)
embed.add_field(name=(╯°□°）╯︵ ┻━┻, value=You flipped a table. Your friends cheer for you., inline=False)
embed.set_footer(text="That was pretty neat.")
await ctx.send(embed=embed)
        await ctx.send("(╯°□°）╯︵ ┻━┻")
