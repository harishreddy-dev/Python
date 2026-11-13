# 6-4. Glossary 2: Now that you know how to loop through a dictionary, 
#                  clean up the code from Exercise 6-3 by replacing your
#                  series of print() calls with a loop that
#                  runs through the dictionary’s keys and values. When 
#                  you’re sure that your loop works, add five more Python
#                  terms to your glossary. When you run your program ag-
#                  -ain, these new words and meanings should automatically
#                  be included in the output.

glossary ={
    'variable' : 'which gives info of size, range, operations of a data.',
    'data type' : 'which used to identify the type of data.',
    'list' : 'which is collection of elements in a specify order.',
    'dictionary' : 'which is collection of key-value pairs.',
    'set' : 'which is a unordered collection of unique elements.',
    'string' :'which is a collection of characters',
    'conditions' : 'which is used evaluate a statement and based on result perform actions.',
    'boolean values' : 'both True or False are known as boolean values.',
    'key' : 'which is a unique value in dictionary which is associated with a value.',
    'key-pair values' : 'which means both the key and its associated value in a dictionary.'


}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning.title()}")
    print("\n")