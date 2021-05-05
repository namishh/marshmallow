import discord
from discord.ext import commands, tasks
from discord.utils import get
import random


class Online(commands.Cog):

    def __init__ (self, bot):
        self.bot = bot

    #event
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user}")

        
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(f'{user.display_name}')

    #command
    @commands.command()
    async def greet(self, ctx):
        random_greet = ["Hello", "Hi", "Hola Amigo", "Konichiwa", "Bonjour", "Ello, mate", 'Salve', ]
        rand = random.choice(random_greet)
        await ctx.send(f"{rand}!")
    #clear
    @commands.command()
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)



def setup(bot):
    bot.add_cog(Online(bot))