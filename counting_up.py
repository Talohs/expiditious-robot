def first_odds():
    #prints odd numbers
    hundred = list(range(1, 101))
    for odds in hundred:
        if odds%2 != 0:
            print(odds)