import discord
from discord.ext import commands
import re
import traceback
import os
from dotenv import load_dotenv

from const import CODE_REVIEW_CHANNEL_ID

from validate import validate_reaction_user

# Load environment variables from .env file
load_dotenv()

# Access the token using the environment variable
TOKEN = os.getenv("TOKEN")

intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents)

# Create a list to store server IDs
joined_servers = []

@client.event
async def on_ready():
    print("Bot is ready.")
    
    for guild in client.guilds:
        if guild.id not in joined_servers:
            joined_servers.append(guild.id)
            await client.get_channel(CODE_REVIEW_CHANNEL_ID).send("Hi, :wave: I'm your friendly code review bot, Unitum!:handshake: :robot: :heart_hands: \n\n\nI am here to help make sure that you can get your code reviewed, and to facilitate sharing helpful feedback between your fellow Junior Devs.:woman_technologist: :technologist:\n\n\n Stuck on a project? Finished a new application? Taking a crack at a brand new coding language? Simply use the !request command followed by the language of your code, as well as a link to your GitHub repository to request a review. <request!> <language> <githublink>\n\n\n I'll send a message to the language channel on your behalf, letting folks know to head over here to review your code.\n\n\nDevs, let's help each other out when we can:pray:. Review a fellow Junior's code to allow them, and yourself, to learn and grow, as you earn badges at different milestones.:medal: The more code you review, the more badges you will receive!:rocket: \n\n\nHappy coding!:smile: :dizzy: ")

@client.event
async def on_error(event, *args, **kwargs):
    error = traceback.format_exc()
    print(f"An error occurred in {event}: {error}")    

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


def extract_github_url(message):
    pattern = r"(?:https:\/\/)?(?:www\.)?(?:github\.com)\/(?:[a-zA-Z0-9_-]+\/){2}[a-zA-Z0-9_-]+(?:\/.*)?"
    match = re.search(pattern, message)
    if match:
        return match.group()
    else:
        return None    

@client.command()
async def request(ctx, language):
    try:
        # Check if the command was sent in the "code review" channel
        if ctx.channel.id != CODE_REVIEW_CHANNEL_ID:
            await ctx.send("This command can only be used in the code review channel.")
            return
        
        # Check if the specified language is valid
        if language.lower() not in LANGUAGE_CHANNELS:
            await ctx.send(f"Sorry, {language} is not a valid language.")
            return
        
        
        # Add a reaction to the user's message so that users can mark it as "done"
        await ctx.message.add_reaction("✅")
        

        # Send a message to the user to confirm their request
        await ctx.send(f"Your code review request has been submitted. Thank you, {ctx.author.mention}!")
        
        # Get the user's nickname or username if they don't have a nickname
        # user = ctx.author.nick or ctx.author.name

        # Get the channel ID for the specified language
        channel_id = LANGUAGE_CHANNELS[language.lower()]
        

        # Send a message to the corresponding language channel
        language_channel = client.get_channel(channel_id)
        await language_channel.send(f"{ctx.author.mention} has requested a code review. Please go to the code review channel to help out your fellow developer. When you've finished, make sure to react with a ✅ and send your feedback in the message thread")

    except Exception as e:
        print(f"An error occurred while executing the 'request' command: {e}")


# List to store the IDs of messages that a user has already reacted to, so they cannot cheat the bot to increase their count
REACTION_IDS = []

@client.event
async def on_reaction_add(reaction, user):
    try:
        isValid = validate_reaction_user(reaction, user, REACTION_IDS)
        
        if isValid == False:
            return
        
        # Add the message ID to the list of IDs that the user has already reacted to
        REACTION_IDS.append(reaction.message.id)
        
        # Update the user's code review count
        user_id = str(user.id)
        CODE_REVIEW_COUNTS[user_id] = CODE_REVIEW_COUNTS.get(user_id, 0) + 1
        
        # Print the user and their code review count
        print(f"{user} has completed {CODE_REVIEW_COUNTS[user_id]} code reviews")
        
        # send a thank you message to the user who reacted
        channel = client.get_channel(CODE_REVIEW_CHANNEL_ID)
        await channel.send(f"Thanks for completing a code review, {user.mention}! Keep up the great work!")
        
        # Check if the user has completed a milestone
        for milestone_count, milestone_name in MILESTONES:
            if CODE_REVIEW_COUNTS.get(user_id, 0) == milestone_count:
                await reaction.message.channel.send(f":star_struck: :star_struck: :star_struck: Congratulations, {user.mention}! You've completed {milestone_count} code reviews and earned the {milestone_name} badge. :partying_face: :partying_face: :partying_face: ")

        return True
    except Exception as e:
        print(f"An error occurred in on_reaction_add: {e}")
    
try:
    client.run(TOKEN)
except Exception as e:
    print(f"An error occurred while running the client: {e}")
