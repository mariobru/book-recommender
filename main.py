#!/usr/bin/env python3 
import src.inputArgs as ia
import src.printGenres as pg
import src.recommendation as rc

def main():

    args = ia.inputArgs()

    print(args)

    if args.genres:

        pg.printGenres()

    if args.recommend:

        genre = input('Please insert a genre from the list above: ')
        rc.recommendation(genre)

if __name__=="__main__":
    main()