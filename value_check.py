sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'


# does not work with upper and lowercase letters
if word in sentence:
    print('The word is in the sentence')
else:
    print('The word is not in the sentence')


# Formats data to account for upper and lowercase letters
if word.lower() in sentence.lower():
    print('The word is in the sentence')
else:
    print('The word is not in the sentence')


nums = [1, 2, 3, 4]

if 3 in nums:
    print('The number was found')
else:
    print('The number was not found')


if 0 in nums:
    print('The number was found')
else:
    print('The number was not found')
