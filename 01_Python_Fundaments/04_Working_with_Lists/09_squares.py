# 4-9. Squares Comprehension: Use a list comprehension to generate a list 
#                          of the first 10 squares.

squares = [pow(num,2) for num in range(1,11)]

for square in squares:
    print(square)