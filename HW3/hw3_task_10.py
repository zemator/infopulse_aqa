str1 = """
We are not what we should be!
We are not what we need to be.
But at least we are not what we used to be
 (Football Coach)
"""
# 1
print('Number of words: ', len(str1.split()))

# 2
new_str1 = ''
for itr in str1:
    new_str1 += itr.strip('!.()')
print(new_str1)

# 3
sorted_list = str1.split()
sorted_list.sort()
print(sorted_list)

# 4*
numer_of_words = {}
for itr in new_str1.split():
    numer_of_words[f'{itr}'] = 0
for itr in numer_of_words.keys():
    count_words = str1.count(itr)
    numer_of_words[f'{itr}'] = count_words

print('Number of words:', numer_of_words)



