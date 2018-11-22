from redbot.core import commands

class fliptable(commands.Cog):
    """flip a table."""

    @commands.command()
    async def fliptable(self, ctx):
        """it flips a table"""
        await ctx.send("(╯°□°）╯︵ ┻━┻")
