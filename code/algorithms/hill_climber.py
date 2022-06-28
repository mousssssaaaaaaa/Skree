import random
from code.algorithms import random as rnd
from copy import deepcopy
from code.classes import chain as ch
from code.algorithms import greedy_gravity as gg
from code.functions import gravity as g


class HillClimber:
    """
    Hill climber algorithm that starts with Greedy Gravity
    """
    def __init__(self, chain, n_flips, upperbound_fails):
        self.chain = chain
        self.copy_chain = deepcopy(self.chain)
        self.n_flips = n_flips
        self.upperbound_fails = upperbound_fails
        self.random_point_index = 0
        self.random_point = (0, 0)

    def beginning_chain(self):
        """
        Begin with a greedy gravity chain.
        """
        greedy_gravity = gg.GreedyGravity(self.chain)
        greedy_gravity.run()
        self.chain = deepcopy(greedy_gravity.chain)

    def get_random_point(self):
        self.random_point_index = random.randint(0,len(self.copy_chain.folds)-1)
        self.random_point = self.copy_chain.folds[self.random_point_index]

    def flip(self):
        """
        Make flips in a random part of the chain of length n_flip if possible.
        """
        # Find next point
        next_point = self.copy_chain.folds[self.random_point_index + 2]
    

        # Find middle point
        middle = list(self.copy_chain.folds[self.random_point_index + 1])

        dif_end_x = next_point[0] - self.random_point[0]
        dif_end_y = next_point[1] - self.random_point[1]
        dif_end_z = next_point[2] - self.random_point[2]

        differences_end = (dif_end_x, dif_end_y, dif_end_z)

        # check which dimension to ignore
        if dif_end_x == 0:
            dim1 = 1
            dim2 = 2

        elif dif_end_y == 0:
            dim1 = 0
            dim2 = 2

        else:
            dim1 = 0
            dim2 = 1

        # Check if not straight line (if only one coordinate)
        if differences_end[dim1] != 0 and differences_end[dim2] != 0:

            # Calculate coordinates new point (invert change):

            dif_middle_dim1 = middle[dim1] - self.random_point[dim1]

            if dif_middle_dim1 == differences_end[dim1]:
                middle[dim1] = self.random_point[dim1]
                middle[dim2] = self.random_point[dim2] + differences_end[dim2]
            else:
                middle[dim1] = self.random_point[dim1] + differences_end[dim1]
                middle[dim2] = self.random_point[dim2]

        # Check if point in fold
        if tuple(middle) not in self.copy_chain.folds:
            self.copy_chain.folds[self.random_point_index + 1] = tuple(middle)

        # Set new random points
        self.random_point = self.copy_chain.folds[self.random_point_index + 1]
        self.random_point_index += 1 

    def run(self):
        """
        Run Hill Climber based on greedy gravity.
        """

        # Get folded chain
        self.beginning_chain()

        # Get a baseline score
        baseline_score = self.chain.get_score()

        # Initiate copy to make small changes
        self.copy_chain = deepcopy(self.chain)
        fails = 0

        # Run until no improvements
        while fails < self.upperbound_fails:
            self.get_random_point()

            # Flip parts of chain
            for _ in range(self.n_flips):

                # Check if not last chain point
                if self.random_point_index <= (len(self.chain.folds) - self.n_flips):
                    self.flip()

            new_score = self.copy_chain.get_score()

            # Compare score to baseline
            if new_score > baseline_score:
                self.chain = deepcopy(self.copy_chain)
                baseline_score = new_score
            else:
                fails += 1
