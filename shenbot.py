from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
import SnapCard

# Load environment variables from .env file
load_dotenv()


bot_token = os.getenv('bot_token')
if not bot_token:
    raise ValueError("bot_token not found in environment variables.")

channel_id = int(os.getenv('channel_id'))
if channel_id == 0:
    raise ValueError("channel_id not found or invalid in environment variables.")

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    channel = bot.get_channel(channel_id)
    await channel.send("Hello, I am online!")

    @bot.command()
    async def hello(ctx):
        await ctx.send("Hello!")

    @bot.command()
    async def snapcard(ctx, *, card_name: str):
        # placeholder for card lookup logic
        await ctx.send(f"Looking up card: {card_name}")
        # Call the SnapCard.py logic here
        card_name, card_stats, ability = SnapCard.main(card_name)
        # Send the card details back to the Discord channel
        await ctx.send(f"{card_name} is {card_stats} and {ability}")

    @bot.command()
    async def snapinfo(ctx):    
        await ctx.send("This bot provides information about Marvel Snap cards. Use !snapcard <card_name> to get details. To search for High Evolutionary cards, use !snapcard Evolved Card Name.") 

bot.run(bot_token)