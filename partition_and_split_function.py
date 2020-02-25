# heading = "Python: an Introduction, and Python: Advanced"

# header, _, subheader = heading.partition(': ')

# print(header)
# print(_)
# print(subheader)

# first, second, third = heading.partition(': ')

# print(first)
# print(second)
# print(third)

tags = 'python,coding,programming,development'

list_of_tags = tags.split(',')

print(list_of_tags)

list_of_tags = tags.split() # -> converts string into a list with one element

print(list_of_tags)

heading = "Python: an Introduction"

heading, subheader = heading.split(': ')

print(heading)
print(subheader)