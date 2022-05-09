# 1
def input_number():
    while True:
        enter_number = input('Enter a number: ')
        if input_number.isdigit():
            break
        else:
            print('You should enter the number.')
            continue
    return enter_number


# 2
def input_word():
    while True:
        enter_word = input("Enter a word: ").strip()
        if " " in enter_word:
            print('No spaces in word')
            continue
        else:
            break
    return enter_word


# 3
def is_year_leap(year):
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        return True
    else:
        return False


# 4
def is_triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False


# 5
def is_triangle_type(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        if a == b == c:
            return 'Equilateral triangle '
        elif a == b or a == c:
            return 'Isosceles triangle'
        else:
            return "Versatile triangle"
    else:
        return 'Not a triangle'

# 6
def distance():
    xa = int(input('Enter x1: '))
    ya = int(input('Enter y1: '))
    xb = int(input('Enter x2: '))
    yb = int(input('Enter y2: '))
    from math import sqrt
    distance_length = sqrt(((xb - xa) ** 2) + ((yb - ya)**2))
    return distance_length


# 7
def del_not_letter(some_str):
    letters_only = ''
    for symbol in some_str:
        if symbol.isalpha():
            letters_only += symbol
        else:
            continue
    return letters_only

print(del_not_letter('Some12Test_!'))