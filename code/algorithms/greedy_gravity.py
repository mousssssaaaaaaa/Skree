import random
from copy import deepcopy
from code.functions import distance as d
from code.functions import gravity as g
from code.functions import distance_to_H as dh

class GreedyGravity():

    def __init__(self, chain):
        self.chain = deepcopy(chain)

    def closest_to_gravity(self, options):
        """
        Returns point closest to center of gravity of chain.
        """
        score = 100

        # calculate center of gravity for current protein
        gravity_value = g.get_gravity(self.chain.folds)

        # calculate distance (Pythagoras)
        for point in options:
            gravity_distance = d.distance(point, gravity_value)
            if gravity_distance < score:
                score = gravity_distance
                best_point = point
        return best_point

    def run(self):
        """
        Pick random coordinate as option on grid and
        see if proposed chain elongation is valid.
        """
        while len(self.chain.folds) < len(self.chain.aminocode):
            options = self.chain.get_options()

            if len(options) == 0:
                self.chain.folds = [(0, 0, 0)]

            best_point = random.choice(list(options))
            if len(self.chain.folds) < 6:
                best_point = random.choice(list(options))
            else:
                best_point = self.closest_to_gravity(options)
            
            self.chain.build(best_point)
