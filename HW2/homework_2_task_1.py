#Task 1. String includes digit
string_is_integer = '10'
string_is_not_integer = 'spam'

print(f'Is {string_is_integer=} digit?', string_is_integer.isdigit())
print(f'Is {string_is_not_integer=} digit?', string_is_not_integer.isdigit()) 

#Task 2. How many spaces in string
string_with_spaces = ' There are some spaces    '
print(f'There are {string_with_spaces.count(" ")} in string')

#Task 3. How mant dots '.' in string
string_with_dots = 'Good. Evening. We. Are. From. Ukraine.'
print(f'There are {string_with_dots.count(".")} dots in string')

#Task 4. Create string 'Homework' and add forward and backward spaces to rich len == 100
string_homework = 'Homework'
a = b = (100 - len(string_homework)) // 2
string_homework = " " * a + string_homework + " " * b
print(f'There are {string_homework.count(" ")} in string. String len is :', len(string_homework))
print(string_homework)

#Task 5. Make firt letters in each word upper case
string_make_upper = "make love but not with moskolyami"
print(string_make_upper.title())

#Task 6. Check if string has 'ing' in the end
string_ing = 'string'
print(string_ing.endswith('ing'))

#Task 7. Find index of firts 'a'
string_a = "Bayraktar"
print(f'The word is {string_a} with "a" index=',string_a.find('a'))

#Task 8. Split string on lists by space 
string_list = 'There is no goal, there is a way'
print(string_list.split())

#Task 9. Delte forward and backward spaces. Taking string from Task 2
print(string_with_spaces.strip())
