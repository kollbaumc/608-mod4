#fig06_02.py
"""Tokenizing a string and counting unique words"""
text = ('The story of Chuck Long was an obvious one.  So obvious that no one had written it')
word_counts = {}

#count the number of occurences of each unique word
for word in text.split():
    if word in word_counts:
        word_counts[word] += 1 #update existing key-value pair
    else:
        word_counts[word] = 1 #insert new key-value pair
print (f'{"WORD":<12}COUNT')

for word, count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')

print('\nNumber of unique words:', len(word_counts))
print('Chris Kollbaum')
