import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
    100,
    83,
    220,
    40,
    100,
    400,
    10,
    1,
    3,
]


def median(list):
    sorted_list = sorted(list)
    length_of_list = len(list)
    to_middle = math.floor((length_of_list-1)/2)
    median = sorted_list[(to_middle):-(to_middle)]

    return median


print(median(sale_prices))


def median1(list1):
    sorted_list = sorted(list1)
    for items in range(len(sorted_list)):
        if len(sorted_list) > 2:
            sorted_list.pop(-1)
            sorted_list.pop(0)
        if len(sorted_list) == 2:
            new_list = (sum(sorted_list)/2)
            return new_list
        if len(sorted_list) == 1:
            return sorted_list


print(median1(sale_prices))

# sorted_list = sorted(sale_prices)
# num_of_sales = len(sorted_list)
# half_slice = math.floor(num_of_sales/2)
# first_sales_items = sorted_list[:half_slice]
# last_sales_items = sorted_list[-(half_slice):]
# median = sorted_list[half_slice:(half_slice + 1)]

# print(sorted_list)
# print(num_of_sales)
# print(first_sales_items)
# print(last_sales_items)
# print(median)
