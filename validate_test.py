from validate import validate_reaction_user
from discordReviewBot import CODE_REVIEW_CHANNEL_ID

class Author():
    def __init__(self, isBot):
        self.bot = isBot

class Channel():
    def __init__(self, id):
        self.id = id

class Message():
    def __init__(self, channel, author, id, content):
        self.channel = channel
        self.author = author
        self.id = id
        self.content = content

class Reaction():
    def __init__(self, message, emoji):
        self.message = message
        self.emoji = emoji

class User():
     def __init__(self, isBot):
         self.bot = isBot

random_channel = Channel(99)
code_review_channel = Channel(CODE_REVIEW_CHANNEL_ID)
bot_author = Author(True)
real_author = Author(False)

bot_user = User(True)
real_user = User(False)

empty_reaction_ids = []

def test_validate_reaction_user_from_bot_user_in_random_channel():
    random_channel_bot_author_message = Message(random_channel, bot_author, '99', '')
    random_channel_bot_author_message_reaction = Reaction(random_channel_bot_author_message, "✅")
    response = validate_reaction_user(random_channel_bot_author_message_reaction, bot_user, empty_reaction_ids)
    assert response == False

def test_validate_reaction_user_from_bot_user_in_code_review_channel():
    random_channel_bot_author_message = Message(code_review_channel, bot_author, '99', '')
    random_channel_bot_author_message_reaction = Reaction(random_channel_bot_author_message, "✅")
    response = validate_reaction_user(random_channel_bot_author_message_reaction, bot_user, empty_reaction_ids)
    assert response == False

def test_validate_reaction_user_from_real_user_in_code_review_channel_wrong_emoji():
    code_review_channel_real_author_message = Message(code_review_channel, real_author, '99', '')
    code_review_channel_real_author_message_reaction = Reaction(code_review_channel_real_author_message, "🚀")
    response = validate_reaction_user(code_review_channel_real_author_message_reaction, real_user, empty_reaction_ids)
    assert response == False


def test_validate_reaction_user_from_real_user_in_code_review_channel_correct_emoji_no_content():
    code_review_channel_real_author_message = Message(code_review_channel, real_author, '99', '')
    code_review_channel_real_author_message_reaction = Reaction(code_review_channel_real_author_message, "✅")
    response = validate_reaction_user(code_review_channel_real_author_message_reaction, real_user, empty_reaction_ids)
    assert response == False

def test_validate_reaction_user_from_real_user_in_code_review_channel_correct_emoji_request():
    code_review_channel_real_author_message = Message(code_review_channel, real_author, '99', '!request review')
    code_review_channel_real_author_message_reaction = Reaction(code_review_channel_real_author_message, "✅")
    response = validate_reaction_user(code_review_channel_real_author_message_reaction, real_user, empty_reaction_ids)
    assert response == True

def test_validate_reaction_user_from_real_user_in_code_review_channel_correct_emoji_request_already_responded():
    code_review_channel_real_author_message = Message(code_review_channel, real_author, '99', '!request review')
    code_review_channel_real_author_message_reaction = Reaction(code_review_channel_real_author_message, "✅")
    response = validate_reaction_user(code_review_channel_real_author_message_reaction, real_user, ['99'])
    assert response == False

def test_validate_reaction_user_from_real_user_in_code_review_channel_correct_emoji_request_second_review():
    code_review_channel_real_author_message = Message(code_review_channel, real_author, '99', '!request review')
    code_review_channel_real_author_message_reaction = Reaction(code_review_channel_real_author_message, "✅")
    response = validate_reaction_user(code_review_channel_real_author_message_reaction, real_user, ['88'])
    assert response == True
