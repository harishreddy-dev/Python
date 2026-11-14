# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size
#               and the text of a message that should be printed on the 
#               shirt. The function should print a sentence summarizing 
#               the size of the shirt and the message printed on it.Call
#               the function once using positional arguments to make a 
#               shirt. Call the function a second time using keyword ar-
#               -guments.

def make_shirt(size, message):
    """prints sentences summarizing size and message printed on a T-shirt."""
    print(f"The size of your T-shirt: {size}")
    print(f"The message on your T-shirt: {message}")

make_shirt('M','Hello, World!...')

make_shirt(size= 'XL', message= 'Bye, World!...')
