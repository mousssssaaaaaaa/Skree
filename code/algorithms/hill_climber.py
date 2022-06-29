import random
from code.algorithms import random as rnd
from copy import deepcopy
from code.classes import chain as ch
from code.algorithms import greedy_gravity as gg
from code.functions import gravity as g


class HillClimber:
    """
    Hill climber algorithm that makes small changes to an aminoacid chain.
    """
    def __init__(self, chain, n_flips, upperbound_fails):
        self.chain = chain
        self.copy_chain = deepcopy(self.chain)

        self.n_flips = n_flips
        self.fails = 0
        self.upperbound_fails = upperbound_fails
        self.baseline_score = self.chain.get_score()

        # Initiate copy to make small changes
        self.copy_chain = deepcopy(self.chain)

        self.random_point_index = 0
        self.random_point = (0, 0)
        self.middle = (0, 0)

    def get_random_point(self):
        """
        Get a random point in the aminoacid chain.
        """
        self.random_point_index = random.randint(0,len(self.copy_chain.folds)-1)
        self.random_point = self.copy_chain.folds[self.random_point_index]

    def get_flip(self):
        """
        Make flips in a random part of the chain of length n_flip if possible.
        """
        # Find next point
        next_point = self.copy_chain.folds[self.random_point_index + 2]

        # Find middle point
        self.middle = list(self.copy_chain.folds[self.random_point_index + 1])

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
            dif_middle_dim1 = self.middle[dim1] - self.random_point[dim1]

            if dif_middle_dim1 == differences_end[dim1]:
                self.middle[dim1] = self.random_point[dim1]
                self.middle[dim2] = self.random_point[dim2] + differences_end[dim2]
            else:
                self.middle[dim1] = self.random_point[dim1] + differences_end[dim1]
                self.middle[dim2] = self.random_point[dim2]
      
    def flip(self):
        """
        Flip if point to flip to is not in chain. Do nothing otherwise.
        """
        if tuple(self.middle) not in self.copy_chain.folds:
            self.copy_chain.folds[self.random_point_index + 1] = tuple(self.middle)

    def set_new_points(self):
        """
        Move to new set of points in amino acid chain to flip again.
        """
        self.random_point = self.copy_chain.folds[self.random_point_index + 1]
        self.random_point_index += 1

    def accept_or_fail(self):
        """
        Compare score to baseline. Only accept improving score.
        """
        new_score = self.copy_chain.get_score()

        if new_score > self.baseline_score:
            self.chain = deepcopy(self.copy_chain)
            self.baseline_score = new_score
        else:
            self.fails += 1

    def run(self):
        """
        Run Hill Climber.
        """
        # Initiate copy to make small changes
        self.copy_chain = deepcopy(self.chain)

        # Run until no improvements
        while self.fails < self.upperbound_fails:
            self.get_random_point()

            # Flip parts of chain of length n_flips if possible
            for _ in range(self.n_flips):

                # Check if not last chain point
                if self.random_point_index <= (len(self.chain.folds) - self.n_flips):

                    # Flip
                    self.get_flip()
                    self.flip()
                    self.set_new_points()

            # Accept or fail depending on score
            self.accept_or_fail()
