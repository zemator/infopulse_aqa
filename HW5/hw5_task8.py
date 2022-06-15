def read_file_song():
    with open('My_song.txt', 'r') as f1:
        f_old = ''
        for line in f1:
            f_old += line.strip() + '!\n'
        f1.close()
    with open('My_new_song.txt', 'w') as f2:
        f2.write(f_old)

read_file_song()