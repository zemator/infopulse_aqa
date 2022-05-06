# from 0 to 10
number1 = 1
number2 = 20

while number1 <= 10:
    print(number1)
    number1 += 1

while number2 >= 1:
    print(number2, end=' ')
    number2 -= 1

print()
number3 = int(input('Enter the number: '))
devision_times = 0
while number3 % 2 == 0:
    number3 //= 2
    devision_times += 1

print("Number was devided {} times.".format(devision_times))
