# 3.21 -> 3.99 or 3.95 or 3.00
# (3.20, 99) or (3.20, .99) = 3.99


def pretty_price(price, decimal):
    price = int(price)

    if decimal < 0:
        return "Invalid Input"
    if decimal < 1:
        new_price = price + decimal
        return new_price
    if decimal > 99:
        return "Invalid Input"
    else:
        new_price = price + decimal / 100
        return new_price


print(pretty_price(3.20, .99))
print(pretty_price(3.20, 99))
print(pretty_price(3.20, 296))
print(pretty_price(3.20, -40))

print('')

# Jordan's Solution


def pretty_price1(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * .01

    return int(gross_price) + extension


print(pretty_price1(3.20, .99))
print(pretty_price1(3.20, 99))

# Ternary


def pretty_price2(gross_price, extension):
    extension = extension * 0.01 if isinstance(extension, int) else extension

    return int(gross_price) + extension


print('')
print(pretty_price2(3.20, 99))
print(pretty_price2(3.20, .99))
