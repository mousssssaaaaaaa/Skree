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
        # set placeholder score
        old_distance = 100

        # calculate center of gravity for protein of current state
        gravity_value = g.get_gravity(self.chain.folds)

        # calculate distance between center of gravity and available options
        for point in options:
            gravity_distance = d.distance(point, gravity_value)

            # compare and replace if smaller
            if gravity_distance < old_distance:
                old_distance = gravity_distance
                best_point = point

        return best_point

    def run(self):
        """
        Pick random coordinate as option on grid and
        see if proposed chain elongation is valid.
        """

        # set how many times to build randomly for variability
        threshold = round(len(self.chain.aminocode) / 4)

        while len(self.chain.folds) < len(self.chain.aminocode):

            # obtain options to build the next amino acid
            options = self.chain.get_options()

            # restart when no options are present
            if len(options) == 0:
                self.chain.folds = [(0, 0, 0)]
                continue
            else:
                # select option closest to gravity or random when chain is short
                if len(self.chain.folds) < threshold:
                    best_point = random.choice(list(options))
                else:
                    best_point = self.closest_to_gravity(options)

            # add to chain
            self.chain.build(best_point)
