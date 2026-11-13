# 7-3. Multiples of Ten: Ask the user for a number, and then report whe-
#                        -ther the number is a multiple of 10 or not.

number = int(input("Enter a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")