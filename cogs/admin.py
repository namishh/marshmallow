import discord
from discord.ext import commands, tasks
from discord.utils import get
import random

class Admin(commands.Cog):

    def __init__ (self, client):
        self.client = client

    #error handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please pass all the required arguents")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Oh...... I dont think you have all the permissions")
    
    #add role
    @commands.command()
    async def addrole(self, ctx,  role: discord.Role, user: discord.Member ):
        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
            c1 = random.randint(0,255)
            c2 = random.randint(0,255)
            c3 = random.randint(0,255)
            embed = discord.Embed(title=f"Giving a new role to {user.name}",  color=discord.Color.from_rgb(c1, c2, c3))
            embed.add_field(name = f'{user.name}', value=f"Is now a {role}")
            await user.add_roles(role)
            await ctx.send(embed=embed)

    #remove role
    @commands.command(name="removerole", help = "Removes the role Syntax= .removerole <Rolename> <User Id>")
    async def removerole(self, ctx, role: discord.Role, user: discord.Member ):

        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
            c1 = random.randint(0,255)
            c2 = random.randint(0,255)
            c3 = random.randint(0,255)
            await user.remove_roles(role)
            embed = discord.Embed(title=f"Taking away {role} from {user.name}",  color=discord.Color.from_rgb(c1, c2, c3))
            embed.add_field(name = f'{user.name}', value=f"is now removed from  {role}")
            
            await ctx.send(embed=embed)
            await ctx.message.add_reaction(f"Took away the role from {user.mention} ")

    #kick
    @commands.command()
    async def kick(self, ctx, member: discord.Member, * , reason=None):
        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
            await member.kick(reason=reason)

    #ban 
    @commands.command()
    async def ban(self, ctx, member: discord.Member, * , reason=None):
        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
            await ctx.send(f'Banned {user.mention}')    
            await member.ban(reason=reason)
            
    # unban
    @commands.command()
    async def unban(self, ctx, *, member):
        if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):   
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {user.mention}')


def setup(client):
    client.add_cog(Admin(client))