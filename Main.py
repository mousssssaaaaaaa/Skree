
from sys import argv, exit
import csv
from Class_Chain import Chain
from Visualization import visualization 

def main():
    if len(argv) != 2:
        exit(1)

    aminocode = list(argv[1])
    
    chain = Chain()

    
    for i in range(len(aminocode) - 1):
        chain.build()
    
    print(chain.folds)
    visualization(chain)

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
