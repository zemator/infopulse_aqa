# 1
def is_year_leap(year):
    if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
        return True
    else:
        return False

print(is_year_leap(1988))

# 2
def is_triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        return True
    else:
        return False

print(is_triangle(3, 3, 3))