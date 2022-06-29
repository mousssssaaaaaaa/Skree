import csv

def read_scores(file):
    """
    Open file and return list of stability scores
    """
    results = []
    with open(file, newline='') as f:
        for row in csv.reader(f):
            results.append(int(row[0]))

    return results
