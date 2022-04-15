my_dict = {'title': 'borshch', 'price': 40, 'ingredients':['kartoshka', 'burychok', 'morkovka']}

#Task 1. Add description
my_dict['description'] = 'Do not forget SALO!'

#Task 2. Increase the price
my_dict['price'] += 100

#Task 3. Add one more ingredient
my_dict['ingredients'].append('myaso')

#Task 4. Show number of ingredients 
print('The number of ingredietns is:', len(my_dict['ingredients']))

#Task 5. Delete key with name 'Description'
my_dict.pop('description')

