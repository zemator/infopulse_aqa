# user`s string is "This is my string."
USER_STR = "This is my string."
user_string = input('Enter a string: ')
print(
    "line #1: " + user_string[2], 
    "line #2: " + user_string[-2], 
    "line #3: " + user_string[:6],
    "line #4: " + user_string[:-2],
    "line #5: " + user_string[0::2],
    "line #6: " + user_string[1::2],
    "line #7: " + user_string[::-1],
    "line #8: " + user_string[-1::-2],
    "line #9: " + user_string[-2::-2],
    "line #10: " + user_string[-2:0:-1],
    "line #11: " + str(len(user_string)),
    sep='\n')
