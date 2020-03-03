"""
Do your next EyeQ Challenge.

Solve these Coding Exercises:

# 1) Write a function that generates a random hexadecimal color code
# ex output => #00c274

# 2) Write a function that takes in a string separated by hyphens and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# ex: "green-red-black-white" => "black-green-red-white "
"""

# hexadecimal 0 - 9 and a - f starts with #

import random


def hexi_generator():
    hexi_code = []
    pool = ['1', '2', '3', '4', '5', '6', '7',
            '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    for _ in range(0, 6):
        hexi_code.append(random.choice(pool))
    return hexi_code


print("#" + "".join(hexi_generator()))


# 2
string1 = "green-red-black-white-pink-yellow-orange-blue-brown-grey"


def alphabetizer(string):
    string2 = string.replace('-', ' ')
    string3 = string2.split()
    string4 = sorted(string3)

    return "-".join(string4)


print(alphabetizer(string1))


# Class solution

# 1

def random_hex():
    hex_values = list("ABCDEF") + list(range(10))
    final_hex = []
    i = 1

    while i <= 6:
        final_hex.append(str(hex_values[random.randint(0, 15)]))
        i += 1

    return f"#{''.join(final_hex)}"


print(random_hex())


# 2

def sorter(string):
    split_list = string.split("-")
    split_list.sort()

    return "-".join(split_list)


print(sorter(string1))
