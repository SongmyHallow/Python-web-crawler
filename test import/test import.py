import imdb_movie as im
try:
    import pandas as pd
except:
    import os
    os.system('pip install pandas')
    import pandas as pd

columns = ['poster', 'name', 'score', 'time', 'ratings', 'director', 'star',
                      'movie_length', 'movie_type', 'storyline']
df = pd.read_csv('test_movie.csv', encoding = 'utf-8', header = None, names = columns)
print(df.name)
im.get_movie_details('The Dark Knight')