import discord
from discord.ext import commands, tasks
from discord.utils import get
import requests
import json
import praw
import random
from newsapi.newsapi_client import NewsApiClient
import asyncio
import pickle
import os



newsapi = NewsApiClient(api_key='9319a21a7472491897d5efd548f290dc')




reddit = praw.Reddit(client_id = "EGO5A0fSrR1lfQ", client_secret = "IMxJH_5ebx68jd56QoflLe7zjpMehA", username = "Namish_Pande_2108",
user_agent="harrybotter", check_for_async=False
)


class Fun(commands.Cog):

    def __init__ (self, bot):
        self.bot = bot

    #meme
    @commands.command()
    async def meme(self, ctx):

        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        await ctx.send("Generating Meme!", delete_after=1.5)
        r = requests.get('https://memes.blademaker.tv/api?lang=en')

        random_pic = r.json()
        name = random_pic['title']
        url = random_pic['image']
        print(name, url)

        em = discord.Embed(title=name, color=discord.Color.from_rgb( c1, c2, c3 ))
        em.set_image(url=url)

        await ctx.send(embed=em)

    @commands.command()
    async def nature(self, ctx):
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        subreddit = reddit.subreddit("EarthPorn")
        top = subreddit.top(limit=100)
        allpics = []
        for submission in top:
            allpics.append(submission)
        random_pic = random.choice(allpics)
        name = random_pic.title
        url = random_pic.url
        print(name, url)

        em = discord.Embed(title=name,  color=discord.Color.from_rgb(c1, c2, c3))
        em.set_image(url=url)

        await ctx.send(embed=em)

    @commands.command()
    async def aww(self, ctx):
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        subreddit = reddit.subreddit("aww")
        top = subreddit.top(limit=100)
        allpics = []
        for submission in top:
            allpics.append(submission)
        random_pic = random.choice(allpics)
        name = random_pic.title
        url = random_pic.url
        print(name, url)

        em = discord.Embed(title=name,  color=discord.Color.from_rgb(c1, c2, c3))
        em.set_image(url=url)

        await ctx.send(embed=em)

    @commands.command()
    async def aww(self, ctx):
        await ctx.send("Generating a image that will make you go awwwwww....", delete_after=3)
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        subreddit = reddit.subreddit("aww")
        top = subreddit.top(limit=100)
        allpics = []
        final  = []
        for submission in top:
            allpics.append(submission)
        for subs in allpics:
            if 'https://v.redd.it/' in subs.url or subs.url.endswith('gifv'):
                pass
            else:
                final.append(subs)
        print(final)
        random_pic = random.choice(final)
        name = random_pic.title
        url = random_pic.url
        print(name, url)
        
        em = discord.Embed(title=name,  color=discord.Color.from_rgb(c1, c2, c3))
        em.set_image(url=url)

        await ctx.send(embed=em)

    @commands.command()
    async def facepalm(self, ctx):
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        subreddit = reddit.subreddit("facepalm")
        top = subreddit.top(limit=50)
        allpics = []
        for submission in top:
            allpics.append(submission)
        random_pic = random.choice(allpics)
        name = random_pic.title
        url = random_pic.url
        print(name, url)

        em = discord.Embed(title=name,  color=discord.Color.from_rgb(c1, c2, c3))
        em.set_image(url=url)

        await ctx.send(embed=em)


    
    #fact
    @commands.command()
    async def fact(self, ctx):
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        r = requests.get('https://useless-facts.sameerkumar.website/api')
        j = r.json()
        facts = j['data']
        embed = discord.Embed(title=f"Fun Facts With {self.bot.user.name}",color=discord.Color.from_rgb(c1, c2, c3))
        embed.add_field(name="Did you know that - ", value=facts)
        await ctx.send(embed=embed)
    
    #joke
    @commands.command()
    async def joke(self, ctx):
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        r2 = requests.get("https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist,sexist")
        j2=r2.json()
        print(j2)
        
        if j2['type'] == 'single':
            embed = discord.Embed( color=discord.Color.from_rgb(c1, c2, c3))
            cat =j2['category']
            embed.add_field(name = f'Category : {cat}', value=j2['joke']  )
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed( color=discord.Color.from_rgb(c1, c2, c3))
            embed.add_field(name = j2['setup'] ,value=j2['delivery'])
            await ctx.send(embed=embed)
    
    @commands.command()
    async def quote(self, ctx):
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        r2 = requests.get(f"https://api.quotable.io/random")
        j2=r2.json()
        quote = j2['content']
        author = j2['author']
        em = discord.Embed(title="Quotes", color=discord.Color.from_rgb(c1, c2, c3))
        em.add_field(name=quote, value=f"\t-{author}")
        await ctx.send(embed=em)
    #news 
    @commands.command()
    async def news(self, ctx):
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        all_articles = newsapi.get_everything(sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com',language='en',page=5)
        li = [news['title'] for news in all_articles['articles']]
        url = [news['url'] for news in all_articles['articles']]
        dict_query = {news: url for news, url in zip(li, url)}
        print(dict_query)
        #embed 
        embed = discord.Embed(title="New Headlines - Refreshes every hour", desciption="(Refreshed Every Hour)",  color=discord.Color.from_rgb(c1, c2, c3))

        for key, value in dict_query.items():
            # embed.add_field(name=key, value=f"Link- {value}", )
            embed.add_field(name=key, value=value, inline=True)


        await ctx.send(embed=embed)
    @commands.command(aliases=['8ball', 'test'])
    async def _8ball(self, ctx, *, question) :
        c1 = random.randint(0,255)
        c2 = random.randint(0,255)
        c3 = random.randint(0,255)
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        rand = random.choice(responses)
        embed = discord.Embed(title="THE MAJESTIC 8BALL",  color=discord.Color.from_rgb(c1, c2, c3))
        embed.add_field(name=question, value=rand)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Fun(bot))