#!/usr/bin/env python3 

import src.inputArgs as ia
import src.cleanAndEnrich as ce
import src.printGenres as pg
import src.recommendation as rc

def main():

    args = ia.inputArgs()

    print(args)

    if args.api:

        path = input('Please insert the path where your books dataset CSV file is stored: ')
        
        ce.cleanAndEnrich(path)

    if args.genres:

        path = input('Please insert the path where your books dataset CSV file with genres info is stored: ')
        pg.printGenres(path)

    if args.recommend:

        genre = input('Please insert a genre from the list above: ')
        rc.recommendation(genre)








if __name__=="__main__":
    main()