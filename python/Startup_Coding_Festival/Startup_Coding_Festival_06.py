# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# SOLVED

class Content():
    def __init__(self, played, genre, g_p, row, col):
        self.played = played
        self.genre = genre
        self.genre_prefer = g_p
        self.row = row
        self.col = col

prefer = input().split()
genre_alpha = ['A','B','C','D','E']

genre_prefer ={}
for i, genre in zip(prefer, genre_alpha):
    genre_prefer[genre] = i
    
row, col = input().split()

row = int(row)
col = int(col)
played = []
genre = []
contents = []

for i in range(row):
    played.append(input())
for i in range(row):
    genre.append(input())

for i in range(row):
    for j in range(col):
        if played[i][j] == 'W':
            continue
        contents.append(Content(played[i][j], genre[i][j], genre_prefer[genre[i][j]], i, j))


contents.sort(key = lambda o : (o.played, o.genre_prefer), reverse=True)
for a in contents:
    print("{} {} {} {}".format(a.genre, a.genre_prefer, a.row, a.col))    

