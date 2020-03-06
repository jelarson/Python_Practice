# Print out items in a list only if they're less than 10
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 10, 9, -10]


def function(a):
    my_list = []
    for i in a:
        if i >= 10:
            pass
        if i < 10:
            my_list.append(i)
    return my_list


print(function(a))
