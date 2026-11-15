# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call
#                          the function send_messages() with a copy of the
#                          list of messages. After calling the function,
#                          print both of your lists to show that the or-
#                          -iginal list has retained its messages.

msg = [
    'Hello, World!',
    'Love, World?',
    'Bye, World!'
]

def send_messages(messages):
    """Print each message, move it to sent_messages, and remove it from the copy of messages."""
    sent_messages = []
    i = 0 
    while messages:
        print(messages[i])
        sent_messages.append(messages[i])
        messages.pop(i)

    return sent_messages

print(send_messages(msg[:]))
print(msg)
