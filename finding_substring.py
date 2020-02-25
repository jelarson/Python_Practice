sentence = 'The quick brown fox jumps over the lazy dog.'

query = sentence.find('qui') # -> if not found, returns a -1
query_two = sentence.index('quick') # -> if not found, returns an error

print(query)
print(query_two)

query_three = 'fox' in sentence

print(query_three) # -> found = true, not found = false

if 'brown' in sentence:
  print('It\'s here!')