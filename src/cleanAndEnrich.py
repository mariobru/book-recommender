import pandas as pd
import os
from dotenv import load_dotenv
import requests
load_dotenv()


def githubRequestAuthorized(isbn):

    # Fuction to get the JSON from Google API validating with a token stored in .env file:

    authToken = os.getenv("GOOGLE_BOOKS_API_TOKEN")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:{}&key={}".format(isbn,authToken)

    res = requests.get(url)
    data = res.json()
    return data



# Cleaning and enriching the DF from Google Books API starts here:

# First I open the dataset I downloaded from Kaggle.com:
df = pd.read_csv("../input/books.csv", error_bad_lines=False)

# Then I clean the columns that are not useful for my purpose:

df = df.drop(['bookID','isbn','language_code','text_reviews_count','ratings_count','Unnamed: 10','Unnamed: 11'], axis=1)
df = df.rename(columns = {'# num_pages':'num_pages'})

# Here I am going create a "Genre" column and ask the Google Books API for the genre of each book using its ISBN13:

for i in range(len(df)) : 
    isbn = df.loc[i, "isbn13"]
    book = githubRequestAuthorized(isbn)
    try:
        df.loc[i, 'Genre'] = book['items'][0]['volumeInfo']['categories'][0]
        
    except:
        df.loc[i, 'Genre'] = 'Others'
        
# Last but not least, I will save the dataset cleaned and enriched with new data in the input directory:

df.to_csv('../input/booksWithGenre.csv')



