def trigrams(filename):
    f = open(filename, 'r')
    sets = {}
    all_words = []

    for line in f:
        words = line.split()
        for word in words:
            all_words.append(word)

    print(all_words)
    print(len(all_words))

    for i in range(len(all_words) - 2):
        set_key = all_words[i] + " " + all_words[i+1]
        sets[set_key] = all_words[i+2]

    print(sets)

trigrams("sherlock_small.txt")
