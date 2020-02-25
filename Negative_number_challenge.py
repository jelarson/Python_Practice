pos_num = 50

neg_num = pos_num - (pos_num + 1)

neg_mult = pos_num * -1

neg_div = pos_num / -1


num = 50

if num > 0:
  num =num * -1
  print(num)
else:
  print(num)

print(neg_num)
print(neg_mult)
print(neg_div)

def switch_sign(my_integer):
  if my_integer > 0:
    my_integer = my_integer * -1
    print(my_integer)
  else:
    print(my_integer)

switch_sign(-5)