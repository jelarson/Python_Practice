"""
remove_first_and_last(list_to_clean)

html = ['h1', 'some content', '</h1>']

html_2 = ['h1', 'some content', 'more', '</h1>']

remove_first_and_last(html)
=> ['some content']

remove_first_and_last(html_2)
=> ['some content', 'more']
"""

# Create function takes in list
# check length
# pop off last element
# remove first element

html = ['h1', 'some content', '</h1>']
html_2 = ['h1', 'some content', 'more', '</h1>']
html_3 = ['hi', 'there']
html_4 = ['hi']


def remove_first_and_last(og_list):
    if len(og_list) == 2:
        return "List is now empty"
    if len(og_list) < 2:
        return "List is too short"
    else:
        return og_list[1: -1]


print(remove_first_and_last(html))
print(remove_first_and_last(html_2))
print(remove_first_and_last(html_3))
print(remove_first_and_last(html_4))

print("")

# Jordan's solution

one, *two, three = [1, 2, 3, 4, 5]


def remove_first_and_last1(list_to_clean):
    _, *content, _ = list_to_clean
    return content


print(remove_first_and_last1(html))
print(remove_first_and_last1(html_2))
