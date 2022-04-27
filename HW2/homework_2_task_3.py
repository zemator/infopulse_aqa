my_list = ['You', 'only', 'leave', 'once']
print('My list:', my_list)
#Task 1. Print 3rd word from the list 
print('Task 1:', my_list[-3])

#Task 2. Print 1st symbol from the second word
print('Task 2:', my_list[1][0])

#Task 3. Print the last symbol from the last word
print('Task 3:', my_list[-1][-1])

#Task 4. Add one more word in the end of list 
my_list.append('!')

#Task 5. Add in the middle of the list one more word
my_list.insert(int(len(my_list)/2), 'new')

#Task 6. Delete first word
my_list.pop(0)

#Task 7. Remove word 'word' if it is in the list
if 'word' in my_list:
    my_list.remove('word')
else:
    print('There is no "word" in the list')

