
from sys import argv, exit
from code.classes import chain as ch
from code.visualisation import visualisation as vis
from code.functions import outputwriter as out

def main():
    if len(argv) != 2:
        print("Error not right amount arguments")
        exit(1)

    aminocode = list((argv[1]).upper())
    
    chain = ch.Chain(aminocode)

    while len(chain.folds) < len(aminocode):
        chain.build()
    
    vis.visualisation(chain)

    out.outputwriter(chain.folds, aminocode, chain)
    
if __name__ == "__main__":
    main()
