import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import Color 
import os
import pickle
import random
from discord.ext.commands import cooldown, BucketType
import datetime
import requests
import json
import base64
import asyncio
from PIL import Image
from io import BytesIO
import giphy_client
from giphy_client.rest import ApiException


bot=commands.Bot(command_prefix="m! ")
bot.remove_command('help')
TOKEN= 'NzY1NTIxNzAwNjQwNTIyMjcx.X4WBpA.az7Yy84Q-7aowH93TqmaWKso9NA'


os.chdir('C:\\Users\\pande\\Documents\\Namish Pande\\CODING\\Projects\\Marshmallow Bot')



data_filename = "data.pickle"

class Data:
    def __init__(self, wallet, bank, laptop_count, diamond_credz_count, phone_count,gold_credz_count, luck_booster_count, inv):
        self.wallet = wallet
        self.bank = bank
        self.laptop_count = laptop_count
        self.diamond_credz_count = diamond_credz_count
        self.phone_count = phone_count
        self.gold_credz_count = gold_credz_count
        self.luck_booster_count = luck_booster_count
        self.inv = inv





@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        cooldown = str(datetime.timedelta(seconds=error.retry_after))
        cooldown_without_microseconds = str(cooldown).split(".")[0]
        m = f"Give your hands some rest. **Try again after {cooldown_without_microseconds}  seconds**"
        await ctx.send(m)

@bot.command(pass_context=True)
async def help(ctx, type1 : str = "default"):
    print("help calling owo")
    query = type1.lower()
    if query == "default":
        print("default")
        embed = discord.Embed(title="HELP MENU", description="Type ``m! help <query>`` for detailed help.")
        embed.add_field(name="Fun", value="All of the fun commands such as spank, wanted, meme, etc.")
        embed.add_field(name="Economy", value="All of the eco commands such as buy, shop, work, etc.")
        embed.add_field(name="Admin", value="All the stuff admins can do. Add role, remove role, etc.")
        print("embed done")
        await ctx.send(embed=embed)
    elif query=='admin':
        embed = discord.Embed(title="ADMIN", description="SOME ADMIN PREVILIGES.")
        embed.add_field(name="``m! addrole <role> <user>``", value="Adds a specific role to a user", inline=False)
        embed.add_field(name="``m! removerole <role> <user>``", value="Removes a specific role from user", inline=False)
        embed.add_field(name="``m! kick <user> <reason>``", value="Kicks a user.", inline=False)
        embed.add_field(name="``m! ban <user> <reason>``", value="Bans a user.", inline=False)
        embed.add_field(name="``m! unban <user>``", value="Unbans a user", inline=False)
        await ctx.send(embed=embed)
    elif query=="fun":
        embed = discord.Embed(title="FUN", description="SOME FUN COMMANDS TO USE WHEN YOU'RE BORED")
        embed.add_field(name="``m! meme``", value="Generates a random meme", inline=False)
        embed.add_field(name="``m! aww``", value="Shows you a cute image", inline=False)
        embed.add_field(name="``m! facepalm``", value="Things that make you smash your head", inline=False)
        embed.add_field(name="``m! gif <query>``", value="Returns a gif", inline=False)
        embed.add_field(name="``m! nature``", value="Shows you the beauty of Earth", inline=False)
        embed.add_field(name="``m! fact``",value="Gives you a random and useless fact.", inline=False)
        embed.add_field(name="``m! joke``", value="Returns a joke", inline=False)
        embed.add_field(name="``m! rip <user>``", value="Returns a picture of the user on a tombstone", inline=False)
        embed.add_field(name="``m! spank <user>``", value="Kinda self explanatory", inline=False)
        embed.add_field(name="``m! wanted <user>``", value="Makes you a wanted criminal", inline=False)
        embed.add_field(name="``m! trivia``", value="Asks a random trivia question.", inline=False)
        embed.add_field(name="``m! 8ball <question>``", value="Ask the majestic 8ball any question", inline=False)
        embed.add_field(name="``m! news``" ,value="Shows news. refreshed every hour", inline=False)
        embed.add_field(name="``m! quote``", value="Returns a quote", inline=False)
        await ctx.send(embed=embed)
    elif query == "economy":
        embed = discord.Embed(title="Economy", description="Ways to earn money and show off.", inline=False)
        embed.add_field(name="``m! shop``", value="Display all the items you can buy", inline=False)
        embed.add_field(name='``m! buy <item>``', value="Buys the specific item", inline=False)
        embed.add_field(name="``m! sell <item>``", value="Sells the specific item", inline=False)
        embed.add_field(name="``m! inventory``", value="Shows your items", inline=False)
        embed.add_field(name="``m! bal``", value="Shows balance", inline=False)
        embed.add_field(name="``m! laptop``", value="Use your laptop", inline=False)
        embed.add_field(name="``m! phone``", value="Use your phone", inline=False)
        embed.add_field(name="``m! gamble``", value="Gambling is bad for you....or is it.")
        embed.add_field(name="``m! work``", value="Do your job.", inline=False)
        embed.add_field(name="``m! beg``", value="Beg for credz", inline=False)
        embed.add_field(name="``m! deposit <amount>``", value="Deposit credz", inline=False)
        embed.add_field(name="``m! withdraw <amount>``", value="Withdraw credz", inline=False)
        await ctx.send(embed=embed)


        
    else:
        ctx.send("Wait, What?")


@bot.command()
async def gif(ctx, *, q = "smile"):
    api_key = 'tvVtQksOlAk0BN6jggZpUfgAfsXKkn38'
    instance = giphy_client.DefaultApi()
    try :
        response = instance.gifs_search_get(api_key, q, limit=100, rating='pg')
        lst = list(response.data)
        print("lst")
        giff = random.choice(lst)
        print("gifff")
        await ctx.channel.send(giff.embed_url)
        print("okay")
    except Exception as e:
        print(e)
        await ctx.send("There was a error processing your request.")

@bot.command()
async def wanted(ctx, user : discord.Member = None):
    if user == None:
        user = ctx.author
    want = Image.open('wanted.jpg')

    asset = user.avatar_url_as(size=128)
    data  = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((235,235))

    want.paste(pfp, (126, 256))
    want.save("profile.jpg")
    await ctx.send(file = discord.File('profile.jpg'))
@bot.command()
async def rip(ctx, user : discord.Member = None):
    if user == None:
        user = ctx.author
    want = Image.open('rip.jpg')

    asset = user.avatar_url_as(size=128)
    data  = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((83,83))

    want.paste(pfp, (56, 95))
    want.save("ripbro.jpg")
    await ctx.send("F in Chat bois.")
    await ctx.send(file = discord.File('ripbro.jpg'))

@bot.command()
async def spank(ctx, user : discord.Member = None):
    if user == None:
        user = ctx.author
    want = Image.open('spank.jpg')

    asset = user.avatar_url_as(size=128)
    data  = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((182,182))

    want.paste(pfp, (441, 250))
    want.save("spankpic.jpg")
    await ctx.send(file = discord.File('spankpic.jpg'))

#shop
@bot.command()
async def shop(ctx):
    em = discord.Embed(title='**Shop**', desciption="All the Items you can buy are here.")
    em.add_field(name="Laptop 💻", value= "A small and handy laptop. Can be used to earn credz. Buy using ``m! buy laptop``. Cost = 8000 credz", inline=False)
    em.add_field(name="Phone 📱", value= " A mobile Phone. Invest in stocks and play poker. ``m! buy phone``. Cost = 3000 credz", inline=False)
    em.add_field(name="Diamond Credz 💠", value= "The rarest item in game. Use this to showoff. Buy using ``m! buy diamond-credz``. Cost = 40000 credz", inline=False)
    em.add_field(name="Golden Credz 🟡", value= "A golden coin. Use this to buy a luck multiplier. Buy using ``m! buy golden-credz``. Cost = 4000 credz", inline=False)
    em.add_field(name="Luck Booster 🚀", value= "This item multiplies your luck by 90%. Works only in gambling. You can still lose. And also, only one time use. Buy using ``m! buy luck-booster``. Cost = 2 golden credz", inline=False)
    await ctx.send(embed= em)

@bot.command(aliases=['inventory', 'inv'])
async def inven(ctx, user : discord.Member = None):
    print('inv calling')
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    c3 = random.randint(0,255)
    if user == None:
        user = ctx.author
    member_data = load_member_data(user.id)
    em = discord.Embed(title=f'{user.name}\'s Inventory.', color=discord.Color.from_rgb(c1, c2, c3))
    inventory = member_data.inv
    print(inventory.keys())
    print(inventory)

    if inventory == {}:
        em.add_field(name="Nothing In Inventory", value="Buy something. It feels really empty")
    else:
        if all(value == 0 for value in inventory.values()):
            em.add_field(name="Nothing In Inventory", value="Buy something. It feels really empty")
        else:
            for key, value in inventory.items() :
                if value == 0:
                    pass
                else:
                    em.add_field(name=key, value=f"Count - {value}", inline=False)
    
    await ctx.send(embed=em)

    save_member_data(user.id, member_data)



@bot.command()
async def sell(ctx, *, object:str = None):
    if object == None:
        await ctx.send("NOTHING TO SELL")
    print("working")
    member_data = load_member_data(ctx.author.id)

    if object.lower() == "laptop":
        if member_data.laptop_count > 0:
                
            print("yes")
            sellprice = 8000 / 2
            member_data.wallet += sellprice
            member_data.laptop_count -= 1
            member_data.inv['Laptop 💻'] = member_data.laptop_count
            print(member_data.laptop_count)
            await ctx.send(f"You sold your laptop and got {str(sellprice)} credz")
        else:
            await ctx.send("You don't have a laptop")
    elif object.lower() == "phone":
        print("yes")
        if member_data.phone_count > 0:
            sellprice = 3000 / 2
            member_data.wallet += sellprice
            member_data.phone_count -= 1
            member_data.inv['Phone 📱'] = member_data.phone_count
            await ctx.send(f"You sold your phone and got {str(sellprice)} credz")
        else:
            await ctx.send("You don't have a phone")
    elif object.lower() == "diamond credz":
        if member_data.diamond_credz_count > 0:
                
            print("yes")
            sellprice = 40000
            member_data.wallet += sellprice
            member_data.diamond_credz_count -= 1
            member_data.inv['Diamond Credz 💠'] = member_data.diamond_credz_count

            await ctx.send(f"You sold your diamond credz and got {str(sellprice)} credz")
        else:
            await ctx.send("You dont have a diamond credz.")
    else:
        await ctx.send("No such thing in inventory.")

    save_member_data(ctx.author.id, member_data)

@bot.command()
@commands.cooldown(1, 3600, commands.BucketType.user)
async def work( message):
    try:

        member_data = load_member_data(message.author.id)
        earning = random.randint(0, 3000)
        if earning < 100:
            await message.channel.send(f"You did very poorly. You only got {earning} credz")
        elif earning >= 100 and earning <= 500:
            await message.channel.send(f"You did ok. You  got {earning} credz")
        elif earning > 500 and earning <= 800:
            await message.channel.send(f"You did a good job. You  got {earning} credz!!")
        else:
            await message.channel.send(f"You did a fantastic job. You  got {earning} credz!! ENJOY!!")
        member_data.wallet += earning
    except Exception as e:
        print(e)
    save_member_data(message.author.id, member_data)


@bot.command()
async def buy(ctx, *, object : str):
    member_data = load_member_data(ctx.author.id)


    #code here
    if object.lower() == "laptop":
        if member_data.wallet < 8500:
            await ctx.send(f'**Insufficient Funds**. Looks like you can\'t buy a laptop.')
        else : 
            await ctx.send(f"Successfully Bought A Laptop for {ctx.author.name}")
            global laptop_price
            laptop_price = 8500
            member_data.wallet = member_data.wallet - 8500
            
            print(member_data.wallet)

            member_data.laptop_count += 1
            member_data.inv['Laptop 💻'] = member_data.laptop_count
            print(member_data.laptop_count)

    elif object.lower() == "phone":
        if member_data.wallet < 3000:
            await ctx.send(f'**Insufficient Funds**. Looks like you can\'t buy a phone.')
        else : 
            await ctx.send(f"Successfully Bought A Phone for {ctx.author.name}")
            global phone_price
            phone_price = 3000
            member_data.wallet = member_data.wallet - 3000
 
            print(member_data.wallet)

            member_data.phone_count += 1
            member_data.inv['Phone 📱'] = member_data.phone_count
            print(member_data.inv)
            print(member_data.phone_count)
    
    elif object.lower() == "diamond-credz":
        if member_data.wallet < 40000:
            await ctx.send(f'**Insufficient Funds**. Looks like you can\'t buy a diamond credz.')
        else : 
            await ctx.send(f"Successfully Bought A Diamond Credz for {ctx.author.name}")
            global diamond_credz_price
            diamond_credz_price = 40000
            member_data.wallet = member_data.wallet - 40000
            print(member_data.wallet)

            member_data.diamond_credz_count += 1
            member_data.inv['Diamond Credz 💠'] = member_data.diamond_credz_count
            print(member_data.inv)
            print(member_data.diamond_credz_count)
    elif object.lower() == 'golden-credz':
        if member_data.wallet < 4000:
            await ctx.send(f"**Insufficient Funds.** Looks like you can't buy a golden_credz")
        else:
            await ctx.send(f"Successfuly bought A Golden Credz for {ctx.author.name}")
            global golden_credz_price
            golden_credz_price = 4000
            member_data.wallet -= golden_credz_price
            member_data.gold_credz_count += 1
            member_data.inv['Golden Credz 🟡'] = member_data.gold_credz_count
    elif object.lower() == 'luck-booster':
        if member_data.gold_credz_count < 2:
            await ctx.send(f"**Insufficient Funds.** Looks like you can't buy a luck booster")
        else:
            
            await ctx.send(f"Successfuly bought A Luck Booster for {ctx.author.name}")
            member_data.gold_credz_count -= 2
            member_data.inv['Golden Credz 🟡'] = member_data.gold_credz_count
            print(member_data.gold_credz_count)
            member_data.luck_booster_count += 1
            print(member_data.luck_booster_count)
            member_data.inv['Luck Booster 🚀'] = member_data.luck_booster_count
    else:
        await ctx.send("There is no such item.")

    save_member_data(ctx.author.id, member_data)

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def laptop(ctx):
        member_data = load_member_data(ctx.author.id)
        chance_of_laptop_breaking = random.randint(0, 100)
        chance = random.randint(0, 100)
        if member_data.laptop_count == 0:
            await ctx.send("You don't have a **LAPTOP**. Please buy one using ``m! buy laptop``")
            ctx.command.reset_cooldown(ctx)
        else:
            await ctx.send("What do you wanna do with your laptop? You can\n1) Post Meme\n2)Be A Front End Developer\n3)Be A Back End Developer\n4)Exit\nType your choice now. You have 20 Seconds")
            ms = await bot.wait_for('message' ,check = lambda message: message.author == ctx.author and message.channel == ctx.channel, timeout = 20)
            answer = str(ms.content).lower()
            if 'post meme' in answer:
                if chance == chance_of_laptop_breaking:
                    await ctx.send("Oh ho......Looks like you broke your laptop. Buy a new one using ``m! buy laptop``")
                else:
                    chance_meme = random.randint(0 , 2)
                    if chance_meme == 2:
                        meme_earning = random.randint(1000, 3000)
                        karma = random.randint(1000, 8000)
                        await ctx.send(f"**YOUR MEME IS BOOMING**. YOU  GOT {meme_earning} CREDZ!" )
                    else:
                        karma = random.randint(0, 1000)
                        if karma < 200:
                            meme_earning = random.randint(0, 100)
                            member_data.wallet += meme_earning
                            await ctx.send(f"Your meme was very bad and got only {karma} karma. You only got {meme_earning} credz.")
                        elif karma >  200 and karma and karma < 1000:
                            meme_earning = random.randint(100, 600)
                            member_data.wallet += meme_earning
                            await ctx.send(f"Your meme was ok. It got {karma} karma. You got {meme_earning} credz.")
                        elif karma >  1000 and karma and karma < 3000:
                            meme_earning = random.randint(600, 1000)
                            member_data.wallet += meme_earning
                            await ctx.send(f"Your meme was ok. It got {karma} karma. You got {meme_earning} credz.")
            elif 'be a front end developer'in answer:
                if chance == chance_of_laptop_breaking:
                    await ctx.send("Oh ho......Looks like you broke your laptop. Buy a new one using ``m! buy laptop``")
                else:             
                    chance_font = random.randint(0 , 2)
                    if chance_font == 2:
                        earning = random.randint(1000, 3000)
                        
                        await ctx.send(f"**YOU DID A EXCEPTIONAL JOB*. YOU  GOT {earning} CREDZ!" )
                    else:
                        karma = random.randint(0, 1000)
                        if karma < 200:
                            earning = random.randint(0, 100)
                            member_data.wallet += earning
                            await ctx.send(f"Your design was very bad and was not liked. You only got {earning} credz.")
                        elif karma >  200 and karma and karma < 1000:
                            earning = random.randint(100, 600)
                            member_data.wallet += earning
                            await ctx.send(f"Your design was ok. You got {earning} credz.")
                        elif karma >  1000 and karma and karma < 3000:
                            earning = random.randint(600, 1000)
                            member_data.wallet += earning
                            await ctx.send(f"Your design was very good. You got {earning} credz.")
            elif 'be a back end developer' in answer:
                if chance == chance_of_laptop_breaking:
                    await ctx.send("Oh ho......Looks like you broke your laptop. Buy a new one using ``m! buy laptop``")
                else:
                    chance_font = random.randint(0 , 2)
                    if chance_font == 2:
                        earning = random.randint(1000, 3000)
                        
                        await ctx.send(f"**YOU DID A EXCEPTIONAL JOB*. YOU  GOT {earning} CREDZ!" )
                    else:
                        karma = random.randint(0, 1000)
                        if karma < 200:
                            earning = random.randint(0, 100)
                            member_data.wallet += earning
                            await ctx.send(f"Your logic was very bad and was not liked. You only got {earning} credz.")
                        elif karma >  200 and karma and karma < 1000:
                            earning = random.randint(100, 600)
                            member_data.wallet += earning
                            await ctx.send(f"Your logic was ok. You got {earning} credz.")
                        elif karma >  1000 and karma and karma < 3000:
                            earning = random.randint(600, 1000)
                            member_data.wallet += earning
                            await ctx.send(f"Your logic was very good. You got {earning} credz.")
            elif 'exit' in answer:
                pass
            else:
                ctx.send("You entered a wrong value, DUMBO!")
                ctx.command.reset_cooldown(ctx)
        save_member_data(ctx.author.id, member_data)

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def phone(ctx):

    member_data = load_member_data(ctx.author.id)
    chance_of_phone_breaking = random.randint(0, 100)
    chance = random.randint(0, 100) 
    if member_data.phone_count == 0:
        await ctx.send("You don't have a **Phone**. Please buy one using ``m! buy phone``")
        
    else:
        await ctx.send("What do you wanna do with your Phone? You can\n1)Stock Trading \n2)Play Poker \n3)Exit\nType your choice now. You have 20 Seconds")
    
        ms = await bot.wait_for('message' ,check = lambda message: message.author == ctx.author and message.channel == ctx.channel, timeout = 20)
        answer = str(ms.content).lower()

        if  "stock trading" in answer :
            if chance == chance_of_phone_breaking:
                await ctx.send("Oh oh..... Looks like you broke your phone. Buy a new one using ``m! buy phone``")
                member_data.phone_count  -= 1
            else:
                stock_go_up_or_down = bool(random.getrandbits(1))
                print(stock_go_up_or_down)
                if stock_go_up_or_down == True:
                    money = random.randint(0, 1000)
                    await ctx.send(f"You got {money} credz by investing in stocks.")
                    member_data.wallet += money
                else:
                    money = random.randint(0, 1000)
                    await ctx.send(f"You lost {money} credz by investing in stocks.")
                    member_data.wallet -= money
        elif 'play poker' in answer:
            if chance == chance_of_phone_breaking:
                await ctx.send("Oh oh..... Looks like you broke your phone. Buy a new one using ``m! buy phone``")
                member_data.phone_count-=1
            else:
                win = bool(random.getrandbits(1))
                print(win)
                await ctx.send("How much money do you want to bet?")
                money = await bot.wait_for('message' ,check = lambda message: message.author == ctx.author and message.channel == ctx.channel, timeout = 10)
                print(money)
                try: 
                    money2 = int(money.content)
                    print(money2)
                    if win == True:
                        await ctx.send(f"You won. Here are your {money2} credz")
                        member_data.wallet += money2

                    else:
                        await ctx.send(f"You lost. I am taking away {money2} credz")
                        member_data.wallet -= money2
                except Exception as e:
                    print(e)
                    await ctx.send("You entered a wrong value")
        elif 'exit' in answer:
            pass
        else:
            ctx.send("You entered a wrong value, DUMBO!")
            ctx.command.reset_cooldown(ctx)

               
    save_member_data(ctx.author.id, member_data)

@bot.command(aliases=['dep', 'deposit'])
async def depos(message, value:int):
    member_data = load_member_data(message.author.id)
    if member_data.wallet - value  < 0:
         await message.channel.send(f'**Insufficient Funds**. Try a value equal or less than **{member_data.wallet}**')
    else:     
        member_data.wallet -= value
        member_data.bank += value
        await message.channel.send(f"{value} credz deposited")

    save_member_data(message.author.id, member_data)

@bot.command(aliases=['with', 'withdraw'])
async def withd(message, value:int):
     member_data = load_member_data(message.author.id)
     if member_data.bank - value < 0:
         await message.channel.send(f"**Insufficient Funds**. Please try a value equal or less than {member_data.bank}")
     else:
         member_data.wallet += value
         member_data.bank -= value
         await message.channel.send(f"{value} credz withdrawn")

     save_member_data(message.author.id, member_data)
     

@bot.command()
async def gamble(ctx, money : int):
    member_data = load_member_data(ctx.author.id)
    if member_data.luck_booster_count > 0:
        if money < 500:
            await ctx.send(f"**You need to gamble atleast 500 credz**")

        elif money >= 500:
            win_lose = random.randint(0, 100)
            if win_lose > 0 and win_lose <= 10:
                await ctx.send(f"**YOU LOST SUCKER.(even with your luck booster) *I am taking away your {money} credz")
                member_data.luck_booster_count -= 1
                member_data.inv['Luck Booster 🚀'] = member_data.luck_booster_count
                member_data.wallet -= money
            elif win_lose > 10 and win_lose <= 100:

                await ctx.send(f"**YOU WON *(because of your luck booster). Anyway here is your {money} credz")
                member_data.luck_booster_count -= 1
                member_data.inv['Luck Booster 🚀'] = member_data.luck_booster_count
                member_data.wallet += money
        else:
            await ctx.send("**YOU DID NOT PASS ANY VALUE**")
    else:
        if money < 500:
            await ctx.send(f"**You need to gamble atleast 500 credz**")
    
        elif money >= 500:
            win_lose = random.randint(0, 100)
            if win_lose > 0 and win_lose <= 50:
                await ctx.send(f"**YOU LOST SUCKER.** I am taking away your {money} credz")
                member_data.wallet -= money
            elif win_lose > 50 and win_lose <= 100:
                await ctx.send(f"**YOU WON **(very lucky). Anyway here is your {money} credz")
                member_data.wallet += money
        else:
            await ctx.send("**YOU DID NOT PASS ANY VALUE**")
    

    save_member_data(ctx.author.id, member_data)

@bot.command()
async def bal(message, user : discord.Member = None):
    if user == None:
        user = message.author
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    c3 = random.randint(0,255)
    member_data = load_member_data(user.id)
    print('member_data')

    embed = discord.Embed(title=f"{user.display_name}'s Balance", color=discord.Color.from_rgb( c1, c2, c3 ))
    embed.add_field(name="Wallet", value=str(member_data.wallet))
    embed.add_field(name="Bank", value=str(member_data.bank))

    await message.channel.send(embed=embed)

def base64ToString(b):
    return base64.b64decode(b).decode('utf-8')

@bot.command(aliases=['t', 'trivia'])
@commands.cooldown(1, 70, commands.BucketType.user)
async def tri( ctx):
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    c3 = random.randint(0,255)
    print("doneeee")
    r = requests.get('https://opentdb.com/api.php?amount=1&type=multiple&encode=base64')
    print("r is working")
    j  = r.json()
    print('j is working')

    question = random.choice(j['results'])

    # print(question)
    trivia_question = question['question']
    trivia_question = base64ToString(trivia_question)
    print(trivia_question)
  
    # print(trivia_question)
    correct = question['correct_answer']
    correct = base64ToString(correct)
    print(correct)
    options = [correct]
    # print(options)

    incorrect= question['incorrect_answers']
    # print(incorrect)
    for option in incorrect:
        option = base64ToString(option)
        options.append(option)
    # print(options)
    jumbled = random.sample(options, len(options))    
    # print(jumbled)
    question_cat = question['category']
    question_cat = base64ToString(question_cat)

    embed = discord.Embed(title="Trivia Quiz", description=f"{question_cat}",  color=discord.Color.from_rgb(c1, c2, c3))
    embed.add_field(name = f'Question - {trivia_question}', value=f"Options are\n1) {jumbled[0]}\n2){jumbled[1]}\n3){jumbled[2]}\n4){jumbled[3]}")
    embed.add_field(name= "You Have 15 Seconds", value="Type your answer below")
    number_option = ['1️','2️','3️','4️']
    dictionary = {emoji:url for emoji, url in zip(jumbled, number_option)}
    print(dictionary)
    msg = await ctx.send(embed=embed)

    print("running")
    try:
        print("ok")
        ms = await bot.wait_for('message' ,check = lambda message: message.author == ctx.author and message.channel == ctx.channel, timeout = 15)
        answer = str(ms.content).lower()
        print(answer)
        print('ok')
        print(correct.lower())
        earn = 100
        earn2 = 50
        member_data = load_member_data(ctx.author.id)
        if answer == correct.lower():
            member_data.wallet += earn
            print("correct")
            await ctx.send(f'Answer correct. I am giving you {earn} credz for your correct answer.')
        else:
            
            await ctx.send(f'Answer wrong. The correct answer was **{correct}**. I am taking away {earn2} credz from your account due to your wrong answer. ')
            member_data.wallet -= earn2
    except asyncio.TimeoutError:
        await ctx.send('Times out') 

    save_member_data(ctx.author.id, member_data)    

@bot.command()
@commands.cooldown(1, 70, commands.BucketType.user)
async def beg(ctx):
    member_data = load_member_data(ctx.author.id)
    luck = random.randint(0, 100)
    if luck < 95:
        earnings = random.randint(0, 1500)
    else:
        earnings = random.randint(0, 10000)
    member_data.wallet += earnings
    cel = ['Donald Trump','Minecraft Steve', 'Pewdiepie', 'KSI', 'Logan Paul', 'Johnny Depp', 'Narendra Modi', 'Elon Musk', 'YOUR MOM','Your Teacher']
    random_cel = random.choice(cel)
    await ctx.send(f'{random_cel} gave you {earnings} credz.')
    save_member_data(ctx.author.id, member_data)
    
def load_data():
    if os.path.isfile(data_filename):
        with open(data_filename, "rb") as file:
            return pickle.load(file)
    else:
        return dict()

def load_member_data(member_ID):
    data = load_data()

    if member_ID not in data:
        return Data(0, 0, 0, 0, 0 , 0, 0, {})

    return data[member_ID]

def save_member_data(member_ID, member_data):
    data = load_data()

    data[member_ID] = member_data

    with open(data_filename, "wb") as file:
        pickle.dump(data, file)

@bot.command()
async def load(ctx, extension):
    ctx.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    ctx.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)