# Merge test

from sys import argv, exit
import csv


def main():

    if len(argv) != 2:
        exit(1)
    
    data = ["test"]

    # open the file in the write mode
    with open(argv[1], 'w') as f:

        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv file
        writer.writerow(data)


if __name__ == "__main__":
    main()
