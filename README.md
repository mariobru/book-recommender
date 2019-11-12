# book-recommender

## Introduction:

For this project I have taken the "GoodReads" dataset from Kaggle and I have fed it with information from Google Books API with the intention of making a book recommender by genre.

Ref1: https://www.kaggle.com/jealousleopard/goodreadsbooks

Ref2: https://developers.google.com/books/docs/v1/using

## Description:

- The original dataset contains information like "Title", "Author", "ISBN", "Rating", "Number of pages", etc.

- Using the ISBN I can obtain a JSON from Google Books API which contains the genre of the book. With a loop, I have added these values to a new "genre" column in the dataframe. For this step, you need to register a project in Google API and create an auth token. My token is saved in my ".env" directory (not present in GitHub for obvious reasons). You can check `cleanAndEnrich.py` to see how I did it.

- Then I clean and order this new dataset so I can group by genre.

- Finally, the user can obtain a list of genres through the application and choose one of them, in order to get a recommendation list of the best 10 ranked books for that genre.

## How to use book-recommender:

1- Fork this repo and clone it locally and give execution permissions to main.py.

2- Run `./main.py --help`


    optional arguments:

    -h, --help       show this help message and exit

    -g, --genres     Print a list of genres.

    -r, --recommend  Returns an input box, where you can insert a genre
                   from the previous list. The application will return you a
                   list of 10 books of that genre ordered by rating.


3- You can only choose one option at the same time, so pick first `--genres`. It will prompt a list of genres and the number of titles that the dataset has for each genre.

4- Then you can get a recommendation with `--recommend` option. This flag returns an input question like this:

    `Please insert a genre from the list above:`

You must insert one of the genres from the list. IMPORTANT: You must type it exactly as it is shown on the list.




