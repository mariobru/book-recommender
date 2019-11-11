import pandas as pd
import githubRequestAuthorized

def cleanAndEnrich(inputPath):

    # Loading environment variables


    df = pd.read_csv(inputPath, error_bad_lines=False)

    df = df.drop(['bookID','isbn','language_code','text_reviews_count','ratings_count','Unnamed: 10','Unnamed: 11','Unnamed: 12'], axis=1)
    df = df.rename(columns = {'# num_pages':'num_pages'})

    
    for i in range(len(df)) : 
        isbn = df.loc[i, "isbn13"]
        book = githubRequestAuthorized(isbn)
        try:
            df.loc[i, 'Genre'] = book['items'][0]['volumeInfo']['categories'][0]
            
        except:
            df.loc[i, 'Genre'] = 'Others'
            

    df.to_csv('../input/booksWithGenre.csv')
