# 4-10. Slices: Using one of the programs you wrote in this chapter, add
#               several lines to the end of the program that do the fol-
#               -lowing:
# • Print the message The first three items in the list are:. Then use a
#   slice to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:. Then
#   use a slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:. Then use a 
#   slice to print the last three items in the list.

# example :

squares = [pow(num,2) for num in range(1,11)]

# Manually
print(squares[0])
print(squares[1])
print(squares[2])

# using slice.
for num in squares[0:3]:
    print(num)

print(squares[4])
print(squares[5])
print(squares[6])

for num in squares[4:7]:
    print(num)

print(squares[7])
print(squares[8])
print(squares[9])

for num in squares[7:10]:
    print(num)