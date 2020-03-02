list1 = [1, 6, 11, 16]

# for num in range(0, 21):
#     for num1 in list1:
#         if num == list1:
#             print(num)
#         else:
#             print(num1)


# def funct(list1):

#   list2 = []

#   for num in range(0, 21):
#      if num != list1:
#         list2.append(num)
#         return(list2)
#       if num == list1:
#         return(null)
# print(funct(list1))

def remove_nums(list1):
    num_list = list(range(21))

    for num in num_list:
        if num in list1:
            num_list.remove(num)

    return num_list


print(remove_nums(list1))


def remove_nums2(omit):
    new_list = [num for num in range(21) if num not in omit]

    return new_list


print(remove_nums2([1, 2, 3]))
