a = int(input('Enter "a": '))
b = int(input('Enter "b": '))
c = int(input('Enter "c": '))

if a + b > c and a + c > b and c + b > a:
    print('Yes')
else:
    print('No')