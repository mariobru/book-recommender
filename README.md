# book-recommender

## Introduction:

For this project I have taken the "GoodReads" dataset from Kaggle and I have fed it with information from Google Books API with the intention of making a book recommender by genre.

Ref1: https://www.kaggle.com/jealousleopard/goodreadsbooks

Ref2: https://developers.google.com/books/docs/v1/using

## Description:

- The original dataset contains information like "Title", "Author", "ISBN", "Rating", "Number of pages", etc.
- Using the ISBN I can obtain a JSON from Google Books API which contains the genre of the book. For that I need to register a project in Google API and create an auth token. That token is saved in my ".env" directory (not present in GitHub for obvious reasons).
- Then I clean and order this new dataset so I can group by genre.
- Finally, the user can obtain a list of genres through the application an choose one of them, in order to get a list of the best 10 ranked books of that genre.

## How to use book-recommender:



