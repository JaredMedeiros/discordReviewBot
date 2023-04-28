import pytest
import asyncio

from discordReviewBot import on_reaction_add
from discordReviewBot import CODE_REVIEW_CHANNEL_ID

def author(isBot):
    def __init__(self):
        self.bot = isBot

def channel(id):
    def __init__(self):
        self.id = id

def message(channel, author):
    def __init__(self):
        self.channel = channel
        self.author = author

def reaction(message, emoji):
    def __init__(self):
        self.message = message
        self.emoji = emoji

def user(isBot):
     def __init__(self):
         self.bot = isBot

random_channel = channel(99)
code_review_channel = channel(CODE_REVIEW_CHANNEL_ID)
bot_author = author(True)
real_author = author(False)

bot_user = user(True)
real_user = user(False)

@pytest.mark.asyncio
async def test_on_reaction_add_from_bot_user_in_random_channel():
    random_channel_bot_author_message = message(random_channel, bot_author)
    random_channel_bot_author_message_reaction = reaction(random_channel_bot_author_message, "✅")
    response = await on_reaction_add(random_channel_bot_author_message_reaction, bot_user)
    assert response == None

@pytest.mark.asyncio
async def test_on_reaction_add_from_bot_user_in_code_review_channel():
    random_channel_bot_author_message = message(code_review_channel, bot_author)
    random_channel_bot_author_message_reaction = reaction(random_channel_bot_author_message, "✅")
    response = await on_reaction_add(random_channel_bot_author_message_reaction, bot_user)
    assert response == None

@pytest.mark.asyncio
async def test_on_reaction_add_from_real_user_in_code_review_channel_wrong_emoji():
    random_channel_bot_author_message = message(code_review_channel, real_author)
    random_channel_bot_author_message_reaction = reaction(random_channel_bot_author_message, "🚀")
    response = await on_reaction_add(random_channel_bot_author_message_reaction, real_user)
    assert response == None
