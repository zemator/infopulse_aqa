def write_a_song():
    f = open('My_song.txt', 'r')
    f.write('La-la-la-la\n')
    f.write('Tika-boom')
    read_file = f.read()
    f.close()


write_a_song()
