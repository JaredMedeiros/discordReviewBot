from const import CODE_REVIEW_CHANNEL_ID

def validate_reaction_user(reaction, user, reaction_ids):

    # Check if the reaction was added to a message in the code review channel
    if reaction.message.channel.id != CODE_REVIEW_CHANNEL_ID or reaction.message.author.bot:
        return False
    
    # Check if the reaction is the "done" emoji
    if str(reaction.emoji) != "✅":
        return False
    
    # Check if the user who added the reaction is not a bot
    if user.bot:
        return False
    
    # Check if the message that was reacted to contains a request message
    if "!request" not in reaction.message.content.lower():
        return False
    
    # Check if the message ID is in the list of IDs that the user has already reacted to
    if reaction.message.id in reaction_ids:
        return False
    
    return True