a = int(input('Enter "a": '))
b = int(input('Enter "b": '))
c = int(input('Enter "c": '))

if c > a:
    a, c = c, a
if b > a:
    a, b = b, a
if c > b:
    b, c = c, b

print(f'{a=}, {b=}, {c=}')