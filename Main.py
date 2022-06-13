
from sys import argv, exit
import csv
import pandas as pd 
from code.classes import chain as ch
from code.visualisation import visualisation as vis

def main():
    if len(argv) != 3:
        exit(1)

    aminocode = list(argv[1])
    
    chain = ch.Chain(aminocode)

    while len(chain.folds) < len(aminocode):
        chain.build()
    
    vis.visualisation(chain)

    #convert output to dataframe-csv
    output = chain.folds
    print(output)
    
    df = pd.Dataframe()

    # df = pd.DataFrame(output, columns = ['x', 'y'])
    # df['amino'] = aminocode

    # df['fold'] = chain.folds
    df.to_csv('out.csv', index_label = 'step')
    
    
    
if __name__ == "__main__":
    main()
