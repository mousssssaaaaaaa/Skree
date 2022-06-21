import random
from code.functions import distance_to_H as dh

def greedy_distance(chain):
    """
    Greedy based on best choice. Optimal choice is direction in which an 'H' is closest.
    """

    # check if first aminocode is H and add
    if chain.aminocode[0] == 'H':
        chain.hydrophobe.append((0,0,0))
        

    while len(chain.folds) < len(chain.aminocode):
        
        options = chain.get_options()
        if len(options) == 0:
            chain.folds = [(0, 0, 0)]

        score = float('inf')
        best_point = random.choice(list(options))

        index_to_check = 0 

        #print(best_point)
        if len(chain.hydrophobe) != 0:

            list_H = chain.hydrophobe.copy()
            # remove current point from hydrophobe list
            if chain.folds[-1] in chain.hydrophobe:
                list_H.remove(chain.folds[-1])
            
            # check all options for best score
            index_to_check = len(chain.folds) - 1
            aminocode = chain.aminocode[index_to_check]
            if len(list_H) != 0 and aminocode != 'H':
                for point in options:
                    distance = dh.distance_to_H(point, list_H)
                    if distance < score:
                        best_point = point
                        score = distance

        chain.build(best_point)

        # add if H to list
        if chain.aminocode[index_to_check + 1] == 'H':
            chain.hydrophobe.append(best_point)

    return chain