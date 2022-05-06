from cgitb import reset


a = int(input('Enter "a": '))
b = int(input('Enter "b": '))
c = int(input('Enter "c": '))

num_list = [a, b, c]

result = 0
for number in num_list:
    if num_list.count(number) == 1:
        result = 0
    elif num_list.count(number) == 2:
        result = 2
    elif num_list.count(number) == 3:
        result = 3

print(result)