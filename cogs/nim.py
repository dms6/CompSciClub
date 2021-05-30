#by dillon
#change 5/30: Bot can now go first, still wins

import discord
from discord.ext import commands
import random
class nim(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nim(self, ctx):
        #Check if user input is valid
        def check(num):
            return num.author == ctx.author and num.channel == ctx.channel and num.content in ['1','2','3']
        marbles = ':nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet::nazar_amulet:'
        await ctx.send(f"Rules: Last person to remove the marble wins the game. You can remove 1, 2, or 3 marbles ")

        if random.randint(0,1):
            #USER GOES FIRST
            await ctx.send(f"Rolling who goes first... You go first\n{marbles}")
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
                await ctx.send(f"I remove {compNum} marbles. \n{marbles}")

            await ctx.send("I Win!")
        else:
            #BOT GOES FIRST
            await ctx.send(f"Rolling who goes first...  I go first\n{marbles}")
            #Can't win... gotta hope user makes a mistake
            while marbles:
                if len(marbles)/14 % 4 == 0 :
                    #Last resort, CHEAT!
                    if len(marbles)/14 <= 4:
                        compNum = 0
                        await ctx.send("Never said I couldn't remove 0 marbles... ")
                    #removes marbles, asks for input, blah  blah blah
                    else:
                        compNum = random.randint(1,3)
                        marbles = marbles [:-compNum*14]
                    await ctx.send(f"I remove {compNum} marbles. \n{marbles}")
                    await ctx.send("How many marbles do you want to remove?\n")
                    num = await self.client.wait_for("message", check=check)
                    num = int(num.content)
                    marbles = marbles[:-num*14]
                    await ctx.send(f"You removed {num} marbles. \n{marbles}")
                else:
                    #If user makes mistake, this code will win the game
                    compNum = int(len(marbles)/14 % 4)
                    marbles = marbles[:-compNum*14]
                    await ctx.send(f"I remove {compNum} marbles. \n{marbles}")
                    if marbles:
                        await ctx.send("How many marbles do you want to remove?")
                        num = await self.client.wait_for("message", check=check)
                        num = int(num.content)
                        marbles = marbles[:-num*14]
                        await ctx.send(f"You removed {num} marbles. \n{marbles}")
                    else:
                        #not needed, just like to keep track
                        print("cheated")
            await ctx.send("I win! Imagine losing... what an loser")


def setup(client):
    client.add_cog(nim(client))
