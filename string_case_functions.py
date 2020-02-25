#sentence -> variable
#'The quick brown fox jumps' -> string
#= -> performing the variable assignment

sentence = 'The quick brown fox jumps'#.upper()

sentence_two = sentence.upper()

print(sentence)
print(sentence_two)

sentence = 'the quick brown fox jumps'.capitalize()#capitalize first letter of first word
print(sentence)

sentence = 'the quick brown fox jumps'.title()#capitalize first letter of every word
print(sentence)

sentence = 'the Quick Brown fOX JUmPs'.lower()#makes everything lowercase
print(sentence) #or print(sentence.lower())
