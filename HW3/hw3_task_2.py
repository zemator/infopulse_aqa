# user input "House of the rising sun."
user_input = input('Enter the phrase: ')
user_str_len = len(user_input)

half = round(user_str_len / 2)
part_one = user_input[:half]
part_two = user_input[half:]

print(part_two+part_one)