
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out

def main():
    if len(argv) != 2:
        print("Error not right amount arguments")
        exit(1)

    # capitalize argument input
    aminocode = list((argv[1]).upper())

    # build protein chain
    chain = ch.Chain(aminocode)

    while len(chain.folds) < len(aminocode):
        chain.build()

    # visualize protein chain
    vis.visualisation(chain)

    # store protein data into csv
    out.outputwriter(chain.folds, aminocode, chain)

if __name__ == "__main__":
    main()
