import random

weighted_random = ['winning'] * 1 + ['break_even'] * 2 + ['losing'] * 3

print(random.choice(weighted_random))

weights = {
    'winning': 1,
    'break_even': 2,
    'losing': 3,
}

# print(weighted_lottery(weights))


weights_dictionary = {
    'winning': 2,
    'break_even': 1,
    'losing': 5
}

# Edwin's solution


def weighted_lottery(dictionary):
    result_list = []
    times_winning = dictionary['winning']
    even_break = dictionary['break_even']
    times_losing = dictionary['losing']

    for _ in range(times_winning):
        result_list.append('winning')
        for _ in range(even_break):
            result_list.append('break even')
            for _ in range(times_losing):
                result_list.append('losing')

    return random.choice(result_list)


print(weighted_lottery(weights_dictionary))

# Jordan's Solution


def weighted_lottery1(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)
    return random.choice(container_list)


print(weighted_lottery1(weights))

# My Solution

rando = random.choice(list(range(10)))
print(rando)


def weighted_lottery2(weights):
    if rando <= 2:
        return 'winning'
    if rando < 5 > 2:
        return 'break-even'
    if rando >= 5:
        return 'losing'


print(weighted_lottery2(weights))
