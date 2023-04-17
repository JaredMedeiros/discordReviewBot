import discord
from discord.ext import commands
import requests
import re


intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents)
TOKEN = "MTA5NzI5MjgzMDQyNDE4Mjc4NA.GS0J52.-E4qPoVi5L_lxnHaks511AAE_tu0wDESqDF6Pg"
client = commands.Bot(command_prefix="!")
permissions = discord.Permissions(permissions=3136)  # send messages, read message history, add reactions

@client.event
async def on_ready():
    print("Bot is ready.")



# The ID of the server
SERVER_ID = 1097291717037797450

# The ID of the Code review channel
CODE_REVIEW_CHANNEL_ID = 1097292075445264504

# A dictionary that maps language names to the IDs of their corresponding channels
LANGUAGE_CHANNELS = {
    "python": 1097291870104731698,
    "javascript": 1097291833287131146,
    "java": 1097291787686654086
}

# A dictionary that maps user IDs to the number of code reviews they've completed
CODE_REVIEW_COUNTS = {}

# A list of tuples containing the number of code reviews required to reach each milestone
MILESTONES = [(5, "Bronze"), (10, "Silver"), (15, "Gold"), (20, "Platinum"), (25, "Diamond")]

# The ID of the Tatsumaki bot
TATSUMAKI_BOT_ID = 172002275412279296


def extract_github_url(message):
    pattern = r"(?:https:\/\/)?(?:www\.)?(?:github\.com)\/(?:[a-zA-Z0-9_-]+\/){2}[a-zA-Z0-9_-]+(?:\/.*)?"
    match = re.search(pattern, message)
    if match:
        return match.group()
    else:
        return None    

@client.command()
async def request(ctx, language):
    # Check if the command was sent in the "code review" channel
    if ctx.channel.id != CODE_REVIEW_CHANNEL_ID:
        return
    
    # Check if the specified language is valid
    if language.lower() not in LANGUAGE_CHANNELS:
        await ctx.send(f"Sorry, {language} is not a valid language.")
        return
    
    # Get the channel ID for the specified language
    channel_id = LANGUAGE_CHANNELS[language.lower()]
    
    # Get the user's nickname or username if they don't have a nickname
    user = ctx.author.nick or ctx.author.name
    
    # Send a message to the corresponding language channel
    language_channel = client.get_channel(channel_id)
    message = await language_channel.send(f"{user} has requested a code review. Please go to the code review channel.")
    
    # Add a reaction to the message so that users can mark it as "done"
    await message.add_reaction("✅")

@client.event
async def on_reaction_add(reaction, user):
    # Check if the reaction was added to a message in a language channel
    if reaction.message.channel.id not in LANGUAGE_CHANNELS.values():
        return
    
    # Check if the reaction is the "done" emoji
    if str(reaction.emoji) != "✅":
        return
    
    # Check if the user who added the reaction is not a bot
    if user.bot:
        return
    
    # Update the user's code review count
    user_id = str(user.id)

    CODE_REVIEW_COUNTS[user_id] = CODE_REVIEW_COUNTS.get(user_id, 0) + 1
    
    # Check if the user has completed a milestone
    for milestone_count, milestone_name in MILESTONES:
        if CODE_REVIEW_COUNTS.get(user_id, 0) == milestone_count:
            await reaction.message.channel.send(f"Congratulations, {user.name}! You've completed {milestone_count} code reviews and earned the {milestone_name} badge.")
