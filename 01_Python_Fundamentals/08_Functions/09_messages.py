# 8-9. Messages: Make a list containing a series of short text messages.
#                Pass the list to a function called show_messages(), wh-
#                -ich prints each text message.

msg = [
    "Hello, World!",
    "Love, World?",
    "Bye, World!"
]
 
def show_messages(messages):
    """Prints a short text messages."""
    for message in messages:
        print(message)

show_messages(msg)