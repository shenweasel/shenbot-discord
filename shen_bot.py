from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
import snap_card_fetch
import simple_nreign_rand
import simple_er_challenge_run

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
#    await channel.send("Hello, I am online!")

    @bot.command()
    async def hello(ctx):
        await ctx.send("Hello!")

    @bot.command()
    async def commands(ctx):
        await ctx.send("current commands include !snapcard, !snapcardhelp, !nightpick, and !nightpickhelp, !erchallenge, and !erchallengeget. For more information on each command use the help command after the command name. ex: !snapcardhelp")

    @bot.command()
    async def snapcard(ctx, *, card_name: str):
        # placeholder for card lookup logic
        await ctx.send(f"Looking up card: {card_name}")
        # Call the SnapCard.py logic here
        card_name, card_stats, ability = snap_card_fetch.main(card_name)
        # Send the card details back to the Discord channel
        await ctx.send(f"{card_name} is {card_stats} and {ability}")

    @bot.command()
    async def snapcardhelp(ctx):    
        await ctx.send("This bot fetches the card stats and ability for a given card. ex: !snapcard Baron Zemo to search for Baron Zemo. For High Evolutionary cards, use !snapcard evolved <character name>.") 

    @bot.command()
    async def nightpick(ctx, numrolls: int = 1, allow_dupes: str = "no"):
        if allow_dupes == "yes":
            characters = simple_nreign_rand.main(numrolls, allow_dupes)
            dupes_allowed = "duplicates allowed"
        else:
            characters = simple_nreign_rand.main(numrolls, allow_dupes)
            dupes_allowed = "no duplicates allowed"
        #return response in a readable fashion
        await ctx.send(f"For {numrolls} players with {dupes_allowed} you have been given {characters} to play for this expedition. GL, HF!")

    @bot.command()
    async def nightpickhelp(ctx):    
        await ctx.send("Get a random nightfarer for 1 to 3 players. Input should always be a number from 1 to 3. ex: !nightpick 2 will get two characters")
        await ctx.send("!nightpick 3 yes will get three characters with duplicates allowed.") 
        await ctx.send("If you want to use the default of 1 player and no duplicates, just use !nightpick or !nightpick 1.")
    
    @bot.command()
    async def erchallenge(ctx, class_type: str, soul_level_1: str = "no"):
        await ctx.send(f"getting challenge run information with class type: {class_type}.")
        # Call the simple_er_challenge_run.py logic here
        soul_level_cap = simple_er_challenge_run.is_sl1(soul_level_1).decode('utf-8', 'ignore')
        character_class = simple_er_challenge_run.get_class_type(class_type)
        class_weapon_to_use = simple_er_challenge_run.get_weapon_type(class_type).decode('utf-8', 'ignore')
        region_locked = simple_er_challenge_run.is_region_locked("random").decode('utf-8', 'ignore')
        # Send the challenge details back to the Discord channel
        await ctx.send(f"{soul_level_cap}, your class will be {character_class} and {class_weapon_to_use}. {region_locked}")

    @bot.command()
    async def erchallengehelp(ctx):
        await ctx.send("To start a challenge use !erchallenge <class_type> the valid class types are melee, ranged, caster, or any to pick randomly from all classes.")
        await ctx.send("You will receive an SL cap, starting class, and a weapon type restriction based on the class, for example melee can't roll ranged weapons.")
        await ctx.send("You can also use !erchallenge <class_type> yes to lock the run to SL1.")



bot.run(bot_token)