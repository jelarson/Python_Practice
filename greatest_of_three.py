import random

one = random.randint(0, 99)
two = random.randint(0, 99)
three = random.randint(0, 99)
print(one, two, three)


def funkyfunc(one, two, three):
    if one >= two and one >= three:
        return one
    if two >= one and two >= three:
        return two
    if three >= one and three >= two:
        return three


print(funkyfunc(one, two, three))
