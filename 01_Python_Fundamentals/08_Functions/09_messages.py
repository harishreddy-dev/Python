# 8-9. Messages: Make a list containing a series of short text messages.
#                Pass the list to a function called show_messages(), wh-
#                -ich prints each text message.

mgs = [
    'hello, world!',
    'love, world?',
    'bye, world!'
]
 
def show_messages(messages):
    """Prints a short text messages."""
    for message in messages:
        print(message.title())

show_messages(mgs)