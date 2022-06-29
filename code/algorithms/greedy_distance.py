import random
from code.functions import distance_to_H as dh
from copy import deepcopy

class GreedyDistance:
    """
    Build an aminoacid chain based on the distance to the nearest 'H'. Has favor for directions towards 'H' if it builds another 'H'. 
    Does a random choice for building a 'P'.
    """
    def __init__(self, chain):
        self.chain = deepcopy(chain)
        self.index_to_check = 0

    def closest_to_H(self, options):
        """
        Returns coordinate of best option. Option closest to H.
        """
        best_point = random.choice(list(options))
        list_H = self.chain.hydrophobe.copy()
        score = float('inf')

        # remove current point from hydrophobe list
        if self.chain.folds[-1] in self.chain.hydrophobe:
            list_H.remove(self.chain.folds[-1])
        
        # check all options for best score
        self.index_to_check = len(self.chain.folds) - 1
        aminocode = self.chain.aminocode[self.index_to_check]
        if len(list_H) != 0 and aminocode == 'H':
            for point in options:
                distance = dh.distance_to_H(point, list_H)
                if distance < score:
                    best_point = point
                    score = distance

        return best_point

    def add_hydrophobic(self, point):
        """
        Add to hydrophobic collection if H
        """
        if self.chain.aminocode[self.index_to_check + 1] == 'H':
            self.chain.hydrophobe.append(point)


    def run(self):
        """
        Greedy based on best choice. Optimal choice is direction in which an 'H' is closest.
        """
        # check if first aminocode is H and add
        if self.chain.aminocode[0] == 'H':
            self.chain.hydrophobe.append((0,0,0))

        while len(self.chain.folds) < len(self.chain.aminocode):
            
            # get options
            options = self.chain.get_options()
            if len(options) == 0:
                self.chain.folds = [(0, 0, 0)]
            else:
                    # get option closest to H
                if len(self.chain.hydrophobe) != 0:
                    best_point = self.closest_to_H(options)
                else:
                    best_point = random.choice(list(options))
                    
                # add to chain
                self.chain.build(best_point)

                # add if H to list of hydrophoc amino
                self.add_hydrophobic(best_point)
    
    