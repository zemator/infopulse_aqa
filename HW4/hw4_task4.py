def lalala(lines=3, la_num=3, ending=0):
    a_song = 'la'
    line_num = 0
    for itr in range(lines):
        line_num += 1
        for itr2 in range(la_num-1):
            print(a_song, end='-')
        if line_num == lines and ending:
            print(a_song, end='!')
        elif line_num == lines and not ending:
            print(a_song, end='.')
        else:
            print(a_song)


lalala()
