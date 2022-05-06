# 1
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while num_list:
    print(num_list.pop(0))

# 2
str_str = 'Bandera'
while str_str:
    print(str_str[0], str_str, sep=' ---> ')
    str_str = str_str[1:]

# 3
num_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while num_list1:
    print(max(num_list1), num_list1, sep=" ---> ")
    num_list1.remove(max(num_list1))

# 4
