#fig06_02.py
"""Tokenizing a string and counting unique words"""
text =  ('there are still weeks left to go in the 2022 MLB regular season but a few teams mainly the red-hot Los Angeles Dodgers are already looking toward October the Dodgers are on the verge of officially securing a playoff berth now the Houston Astros New York Mets and Atlanta Braves to name a few teams are on track to secure their own postseason spots sooner than their counterparts Meanwhile clubs such as the Seattle Mariners Tampa Bay Rays Philadelphia Phillies and San Diego Padres are battling it out for the remaining wild-card spots Beyond division races there are many storylines to watch as the regular season comes to an end and October begins such as Seattle attempt to break a 21-year playoff drought Aaron Judge race to 62 home runs and Albert Pujols quest for career home runs where do the current playoff matchups stand what series should you be paying attention to in the coming week when will the Dodgers clinch the NL West and what does the playoff schedule look like we have everything you need to know as the regular season winds down')
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
