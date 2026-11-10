# 3-8. Seeing the World: Think of at least five places in the world you-
#                        -’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabe-
#   -tical order. 
# • Print your list in its original order. Don’t worry about printing t-
#   -he list neatly just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modif-
#   -ying the actual list.
# • Show that your list is still in its original order by printing it. 
# • Use sorted() to print your list in reverse-alphabetical order witho-
#   -ut changing the order of the original list.
# • Show that your list is still in its original order by printing it a-
#   -gain. 
# • Use reverse() to change the order of your list. Print the list to s-
#   -how that its order has changed.
# • Use reverse() to change the order of your list again. Print the list
#  to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order.
#  Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetic-
# -al order.Print the list to show that its order has changed.

places = ['New York','Vinland','Scotland','London','Himalayas']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)