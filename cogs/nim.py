#by dillon
import discord
from discord.ext import commands

class nim(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nim(self, ctx):
        #Check if user input is valid
        def check(num):
            return num.author == ctx.author and num.channel == ctx.channel and \
            num.content in ['1','2','3']
        marbles = ':nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet:'
        await ctx.send(f"Rules: last person to remove the marble wins the game. Each person can remove a maximum of 3 marbles. \n{marbles}")

        while marbles:
            #Get user input
            await ctx.send("How many marbles do you want to remove?")
            num = await self.client.wait_for("message", check=check)
            num = int(num.content)
            compNum = 4 - num
            #Subtract marbles based on user input
            marbles = marbles[:-num*14]
            await ctx.send(f"You removed {num} marbles. \n{marbles}")
            #Subtract marbles for computer
            marbles = marbles[:-compNum*14]
            await ctx.send(f"Computer removes {compNum} marbles. \n{marbles}")

        await ctx.send("Computer Wins!")

def setup(client):
    client.add_cog(nim(client))
