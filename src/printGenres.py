import pandas as pd

def printGenres():

    df = pd.read_csv('./input/booksWithGenre.csv', index_col=0)

    dfgb = df.groupby(['Genre']).count()

    dfsorted = dfgb.sort_values(['title'], ascending=[False]).head(20)

    print("Please choose one of those genres: \n")
    
    print(dfsorted[['title']])


