import argparse

def inputArgs():
    parser = argparse.ArgumentParser(description='This is a books recommender. You can get a list of the genres availables with "--genres" parameter. Then, choose one of them typing "--recommend" and get the top 10 books of that genre ordered by rating.')                 # analizador de argumentos
    grupo = parser.add_mutually_exclusive_group()      # grupo mutuamente excluyente (solo una operacion)

    grupo.add_argument('-g', '--genres', help='Print a list of genres.', action='store_true')
    grupo.add_argument('-r', '--recommend', help='Returns an input box, where you can insert a genre from the previous list. The application will return you a list of 10 books of that genre ordered by rating.', action='store_true')	

    return parser.parse_args()