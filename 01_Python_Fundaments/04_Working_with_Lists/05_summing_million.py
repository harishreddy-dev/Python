# 4-5. Summing a Million: Make a list of the numbers from one to one mi-
#                         -llion, and then use min() and max() to make 
#                         sure your list actually starts at one and ends
#                         at one million. Also, use the sum() function 
#                         to see how quickly Python can add a million 
#                         numbers.

numbers = [num for num in range(1,100_00_01)]

print(min(numbers))
print(max(numbers))
print(sum(numbers))