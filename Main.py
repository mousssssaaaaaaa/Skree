
from sys import argv, exit
import csv
import pandas as pd 
from code.classes import chain as ch
from code.visualisation import visualisation as vis

def main():
    if len(argv) != 2:
        print("Error not right amount arguments")
        exit(1)

    

    aminocode = list((argv[1]).upper())
    
    chain = ch.Chain(aminocode)

    while len(chain.folds) < len(aminocode):
        chain.build()
    
    vis.visualisation(chain)

    #convert output to dataframe-csv
    output = chain.folds

    directions = []
    
    for point in output:
            index = output.index(point)
            if index == (len(output) - 1):
                directions.append(0)
            else: 
                next_point = output[index + 1] 
                current_point = output[index]
                if next_point[1] - current_point[1] == 0: 
                    direction = next_point[0] - current_point[0] 
                else: 
                    direction = (next_point[1] - current_point[1]) * 2

                directions.append(direction)

    df = pd.DataFrame()
    df['amino'] = aminocode
    df['fold'] = directions

    df.to_csv('out.csv', index_label = 'index')
    
if __name__ == "__main__":
    main()
