#The quick brown fox jumped
#T -> 0
#h -> 1
#e -> 2
#' ' -> 3
#q -> 4 etc.
starter_sentence = 'The quick brown fox jumps'
#starter_sentence[12] = 'A' -> error - strings are immutable, can't change a string - only a list 

# first = starter_sentence[0]
# second = starter_sentence[1]
# third = starter_sentence[2]
# new_sentence = first + second + third
# print(new_sentence)

# first_word = starter_sentence[0:3]
# new_sentence = first_word

new_sentence = 'Thy' + starter_sentence[3:]
print(new_sentence)