# 6-3. Glossary: A Python dictionary can be used to model an actual dic-
#                -tionary. However, to avoid confusion, let’s call it a 
#                glossary.
# • Think of five programming words you’ve learned about in the previous
#   chapters. Use these words as the keys in your glossary, and store t-
#   -heir meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
#   print the word followed by a colon and then its meaning, or print the
#   word on one line and then print its meaning indented on a second line. 
#   Use the newline character (\n) to insert a blank line between each 
#   word-meaning pair in your output. {without aloop.}

glossary ={
    "variable" : "Which gives info of size, range, operations of a data. ",
    "data type" : "Which used to identify the type of data.",
    "list" : "Which is collection of elements in a specify order.",
    "dictionary" : "Which is collection of key-value pairs.",
    "set" : "Which is a unordered collection of unique elements."

}

print(f"Variable: {glossary.get("variable").title()}")
print("\n")
print(f"Data Type: {glossary.get("data type").title()}")
print("\n")
print(f"List: {glossary.get("list").title()}")
print("\n")
print(f"Dictionay: {glossary.get("dictionary").title()}")
print("\n")
print(f"Set: {glossary.get("set").title()}")