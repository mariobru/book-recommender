import sys
import argparse
import subprocess

def inputArgs():
    parser = argparse.ArgumentParser(description='Takes a dataset of books that contains at least title, author and isbn columns. You can add genre info through Google Books API with "--api" option if necessary. Then a list of genres is shown with "--genres" parameter, and you can choose one of them in order to obtain a list of recommendations with "--recommend".')                 # analizador de argumentos
    grupo = parser.add_mutually_exclusive_group()      # grupo mutuamente excluyente (solo una operacion)

    grupo.add_argument('-a', '--api', help='Add a genre column to the dataset through the Google Books API based on the ISBN. Then stores a "booksWithGenre.csv" in the Input directory.', action='store_true')           # action guarda el argumento
    grupo.add_argument('-g', '--genres', help='Print a list of genres. You must choose one of them.', action='store_true')
    grupo.add_argument('-r', '--recommend', help='Insert a genre and the application will return you a list of 10 books of that genre ordered by rating.', action='store_true')	

    return parser.parse_args()