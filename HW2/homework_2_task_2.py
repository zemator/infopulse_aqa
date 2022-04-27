#Task 1. Find hypotenuse with sides 367 and 127
print('Hypotenuse is:', (((367**2) + (127**2)) ** 0.5 ))

#Task 2. Find number of tens in the number
number = 42
print(number // 10, f'tens in {number}')

#Task 3. Given number. Find sum of all number
number = 432
result = sum(map(int, str(number)))
print(result)

#Task 4. Print next evel number after number 
number = 42
print('given number is:', number)
number += 1
while True:
    if number % 2 == 0:
        print('Next evel number is:', number)
        break
    else:
        number += 1

#Task 5. Fraction from float 
number = 123.45
str_number = str(number)
split_number = str_number.split('.')
print('Full number is:', number, '\nFaction is:', split_number[1])

#Task 6. Print first fraction number. Get vars from Task 5
print('First fraction number is:', split_number[1][0])

