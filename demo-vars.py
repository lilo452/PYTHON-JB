# this is a literal string that cannot be replaced
stringA= 'word'
stringB= f"word {stringA}"
#this is a string replace example
# it's possible because of the 'f' keyword and usage of doublequotes ""
# good for printing logs and debugging
print(stringB)

literalparagraph= '''hello mister postman
hii hii mister postman'''

paragraph = f"""hello mister postman
hi hi hi hi mister postman {stringA}"""

print(literalparagraph)
print(paragraph)