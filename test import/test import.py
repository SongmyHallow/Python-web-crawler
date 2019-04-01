import imdb_movie as im
import time
try:
    import pandas as pd
except:
    import os
    os.system('pip install pandas')
    import pandas as pd

try:
    import csv
except:
    import os
    os.system('pip install pandas')
    import csv

# columns = ['poster', 'name', 'score', 'time', 'ratings', 'director', 'star',
#                       'movie_length', 'movie_type', 'storyline', 'trailer_embed_link']
# df = pd.read_csv('test_movie.csv', encoding = 'utf-8', header = None, names = columns)
# print(df.name[0])
im.get_movie_details('spider-man into the spider-verse')


# The following works
# read movie name from top 100 list
# infile = open('imdb_top_100_1.csv','r')
# reader = csv.reader(infile)
# for row in reader:
#     print(row[2])
#     try:
#         im.get_movie_details(row[2])
#     except:
#         print("something goes wrong")
#     time.sleep(20)
