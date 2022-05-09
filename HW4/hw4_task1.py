first_number = input('Enter the first number: ')
second_number = input('Enter the second number: ')
try:
    print(int(first_number) + int(second_number))
except ValueError:
    print(first_number + second_number)
finally:
    print('End of the program.')