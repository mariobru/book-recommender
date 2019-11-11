#!/usr/bin/env python3 

from src.inputArgs import inputArgs
from src.cleanAndEnrich import cleanAndEnrich
from src.printGenres import printGenres
from src.githubRequestAuthorized import githubRequestAuthorized

def main():

    args = inputArgs()

    print(args)

    if args.api:

        input = input('Please insert the path where your books dataset CSV file is stored: ')
        
        src.cleanAndEnrich(input)

    if args.genres:
        src.printGenres()







if __name__=="__main__":
    main()