def calculate_love_score(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    names = name1+name2
    print(f'{names}')
    word1 = 'true'
    word2 = 'love'
    counter1 = 0
    counter2 = 0
    for letter1 in word1:
        for letter2 in names:
            if letter1 == letter2:
                counter1 += 1

    for letter1 in word2:
        for letter2 in names:
            if letter1 == letter2:
                counter2 += 1

    counter = str(counter1) + str(counter2)

    print(counter)


calculate_love_score('Kanye West', 'Kim Kardashian')
