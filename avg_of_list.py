import functools
import operator

list1 = [1, 2, 5, 9, 12]
list2 = [5, 16, 41, 93, 61]
list3 = [10, 15, -10, -14, -1]


def function(list1):
    return (sum(list1)) / len(list1)


print(function(list1))
print(function(list2))
print(function(list3))

print('')


def function2(list1):
    sum = functools.reduce(operator.add, list1)
    average = sum / len(list1)
    return average


print(function2(list1))
print(function2(list2))
print(function2(list3))

print('')

# Jordan's Solution


def get_average(list1):
    total = functools.reduce(
        (lambda total, element: total + element), list1
    )
    return total / len(list1)


print(get_average(list1))
print(get_average(list2))
print(get_average(list3))
