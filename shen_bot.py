from random import randint
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
import snap_card_fetch
import simple_nreign_random_pick
import simple_er_challenge_run
import asyncio

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

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def commands(ctx):
    await ctx.send("current commands include !snapcard, !snapcardhelp, !nightpick, and !nightpickhelp, !erchallenge, and !erchallengeget. "
                   "For more information on each command use the help command after the command name. ex: !snapcardhelp")

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
    await ctx.send("This bot fetches the card stats and ability for a given card. ex: !snapcard Baron Zemo to search for Baron Zemo. "
                   "For High Evolutionary cards, use !snapcard evolved <character name>.") 

@bot.command()
async def nightreign(ctx, numrolls: int = 1, allow_dupes: str = "no"):
    if numrolls < 1 or numrolls > 3:
        await ctx.send("Please enter a number from 1 to 3 for the number of players.")
        return
    if allow_dupes == "yes":
        characters = simple_nreign_random_pick.main(numrolls, allow_dupes)
        dupes_allowed = "duplicates allowed"
    else:
        characters = simple_nreign_random_pick.main(numrolls, allow_dupes)
        dupes_allowed = "no duplicates allowed"
    #return response in a readable fashion
    if numrolls > 1:
        await ctx.send(f"For {numrolls} players with {dupes_allowed} you have been given {characters} to play for this expedition. GL, HF!")
    else:
        await ctx.send(f"For {numrolls} player you have been given {characters} to play for this expedition. GL, HF!")

@bot.command()
async def nightpickhelp(ctx):    
    await ctx.send("Get a random nightfarer for 1 to 3 players. Input should always be a digit from 1 to 3. ex: !nightpick 2 will get two characters")
    await ctx.send("Default player value is 1 player and default allow dupes value is no.")
    await ctx.send("!nightpick 3 yes will get three characters with duplicates allowed.") 
    await ctx.send("!nightpick 1 will generate one character.")

@bot.command()
async def erchallenge(ctx, class_type: str = "any", soul_level_1: str = "no", sote: str = "nosote"):
    class_type = class_type.casefold().strip()
    soul_level_1 = soul_level_1.casefold().strip()
    sote = sote.casefold().strip()
    # Validate inputs
    if class_type not in ["melee", "ranged", "caster", "any"]:
        await ctx.send("Invalid class type. Valid options are melee, ranged, caster, or any.")
        return
    if soul_level_1 not in ["yes", "no", "any"]:
        await ctx.send("Invalid soul level option. Valid options are yes, no, or any.")
        return
    if sote not in ["yes", "no", "nosote", "any"]:
        await ctx.send("Invalid SotE option. Valid options are yes, no, nosote, or any.")
        return
    await ctx.send(f"generating your challenge run, please hold a moment...")
    # Short sleep to simulate processing time
    await asyncio.sleep(1)
    if class_type == "any" or soul_level_1 =="yes" or soul_level_1 == "any":
        crashout = randint(1, 1000)
        if crashout == 1:
            await ctx.send("Cast in the name of God: Ye Guilty. SL1 No Hit Challenge run. Choose your weapons wisely. GLHF!")
        elif crashout > 1:
            # Call the simple_er_challenge_run.py logic here we will not return sote_weapon_rule in the output 
            # as it is not used in the discord command
            soul_level_cap = simple_er_challenge_run.is_sl1(soul_level_1)
            character_class = simple_er_challenge_run.get_class_type(class_type)
            sote_rule = simple_er_challenge_run.is_sote(sote)
            sote_weapon_rule = simple_er_challenge_run.get_sote_weapon_rule(sote, sote_rule)
            class_weapon_to_use = simple_er_challenge_run.get_weapon_type(class_type, sote_weapon_rule)
            region_locked = simple_er_challenge_run.is_region_locked("either")
            # Send the challenge details back to the Discord channel
            await ctx.send(f"{soul_level_cap}, your class will be {character_class} and {class_weapon_to_use}. {region_locked} {sote_rule} GLHF!")

@bot.command()
async def erchallengehelp(ctx):
    await ctx.send("To start a challenge use !erchallenge <class_type> <soul_level_1> <sote>." )
    await ctx.send("the valid class types are melee, ranged, caster, or any.")
    await ctx.send("the valid soul_level_1 options are yes, no or any. Which will lock the run to SL1 or not.")
    await ctx.send("the valid sote options are yes, no, nosote, or any. Which will determine the use of Scadu Tree Fragments, skipping SotE entirely, or randomizing.")
    await ctx.send("You will receive an SL cap, starting class, and a weapon type restriction based on the initial class type chosen.")
    await ctx.send("!erchallenge alone will give a random class type and SL cap, with a choice of 3 weapons for weapon restrictions and asumes SotE will be skipped.")


bot.run(bot_token)