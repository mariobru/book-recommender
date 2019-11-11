def recommendation(genre):
        
    df = pd.read_csv('../input/booksWithGenre.csv', index_col=0)

    selection = df.loc[df['Genre'] == genre].sort_values(['average_rating'], ascending=[False]).head(10)

    finaldf = selection.drop(['isbn13'], axis=1)

    finaldf.to_csv("./output/recommendation.csv")
    
    print(finaldf)
