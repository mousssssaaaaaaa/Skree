
from sys import argv, exit
import csv
from code.classes import chain as ch
from code.visualisation import visualisation as vis

def main():
    if len(argv) != 2:
        exit(1)

    aminocode = list(argv[1])
    
    chain = ch.Chain(aminocode)

    
    for i in range(len(aminocode) - 1):
        if chain.build() == False:
            chain.aminocode = chain.aminocode[0:i+1]
            break
    
    vis.visualisation(chain)

    # # Outputwritter
    # data = ["test"]
        # if len(argv) != 2:
        # exit(1)

    # # open the file in the write mode
    # with open(argv[1], 'w') as f:

    #     # create the csv writer
    #     writer = csv.writer(f)

    #     # write a row to the csv file
    #     writer.writerow(data)
   

if __name__ == "__main__":
    main()
