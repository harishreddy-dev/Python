# 8-10. Sending Messages: Start with a copy of your program from Exercise
#                         8-9. Write a function called send_messages() 
#                         that prints each text message and moves each 
#                         message to a new list called sent_messages as 
#                         it’s printed. After calling the function, print
#                         both of your lists to make sure the messages 
#                         were moved correctly.

msg = [
    "Hello, World!",
    "Love, World?",
    "Bye, World!"
]

def send_messages(messages):
    """Print each message, move it to sent_messages, and remove it from messages."""
    sent_messages = []
    i = 0 
    while messages:
        print(messages[i])
        sent_messages.append(messages[i])
        messages.pop(i)

    return sent_messages

print(send_messages(msg))
print(msg)
