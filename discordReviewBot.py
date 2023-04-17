import discord
from discord.ext import commands
import requests
import re
import traceback
import logging

logging.basicConfig(level=logging.DEBUG)



intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents)
TOKEN = "MTA5NzI5MjgzMDQyNDE4Mjc4NA.GxLEL1.xsvWj_SmmhzSc7omlIwtaxDVqqpjE3pbnhSszo"
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_error(event, *args, **kwargs):
    error = traceback.format_exc()
    print(f"An error occurred in {event}: {error}")    



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
    language_channel.send(f"{user} has requested a code review. Please go to the code review channel to help out your fellow developer. When you've finished, make sure to react with a ✅ and send your feedback in the message thread")
    
    # Wait for the user's message in the code review channel
    def check(m):
        return m.author == ctx.author and m.channel.id == CODE_REVIEW_CHANNEL_ID
    
    user_message = await client.wait_for('message', check=check)
    
    # Add a reaction to the user's message so that users can mark it as "done"
    await user_message.add_reaction("✅")
    
    # Send a message to the user to confirm their request
    await ctx.send("Your code review request has been submitted. Thank you!")

@client.event
async def on_reaction_add(reaction, user):
    # Check if the reaction was added to a message in the code review channel
    print("This has been triggered")
    if reaction.message.channel.id == CODE_REVIEW_CHANNEL_ID:
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
    

    #send a thank you message to the user who reacted
    await CODE_REVIEW_CHANNEL_ID.send(f"Thanks for completing a code review, {user.mention}! Keep up the great work!")

    # Check if the user has completed a milestone
    for milestone_count, milestone_name in MILESTONES:
        if CODE_REVIEW_COUNTS.get(user_id, 0) == milestone_count:
            await reaction.message.channel.send(f":star_struck: :star_struck: :star_struck: Congratulations, {user.name}! You've completed {milestone_count} code reviews and earned the {milestone_name} badge. :partying_face: :partying_face: :partying_face: ")


try:
    client.run(TOKEN)
except Exception as e:
    print(f"An error occurred while running the client: {e}")