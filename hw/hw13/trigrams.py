import random

file = open("sherlock.txt", "r")
lines = file.readlines()
file.close()

words = []
trigrams = {}

for line in lines:
    line = line.replace('--', ' ').replace('\n', '').replace('(', '')
    line = line.replace(')', '').replace('-', ' ').replace(',', '')
    line = line.replace('"', '').replace("'", '')
    words += line.split(' ')

for i in range(len(words) - 2):
    key = words[i] + ' ' + words[i + 1]
    if key in trigrams:
        trigrams[key].append(words[i + 2])
    else:
        trigrams[key] = [words[i + 2]]

start = random.choice(list(trigrams.keys()))
trigram = start + ' ' + random.choice(trigrams[start])

book = "" + trigram
trigram = trigram.split()
nextkey = trigram[1] + ' ' + trigram[2]

count = 0

while (count < 225) and (nextkey in trigrams.keys()):
    nextword = random.choice(trigrams[nextkey])
    book = book + ' ' + nextword
    nextkey = nextkey.split()
    if len(nextkey) > 1:
        nextkey = nextkey[1] + ' ' + nextword
    else:
        nextkey = random.choice(list(trigrams.keys()))
    count = count + 1

if book[-1:] != '.':
    book = book + '.'

print(book)
