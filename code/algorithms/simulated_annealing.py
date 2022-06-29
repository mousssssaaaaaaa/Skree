import random
from code.algorithms import random as rnd
from copy import deepcopy
from code.classes import chain as ch
from code.algorithms import greedy_gravity as gg
from code.functions import gravity as g
from code.visualisation import visualisation as vis
from .hill_climber import HillClimber

class SimulatedAnnealing(HillClimber):
    """
    Make small changes to an aminoacid chain and accept the changes based on a slowly decreasing probability. 
    It is allowed to accept changes that decrease the score.
    """
    def __init__(self, chain, n_flips, total_iterations, temperature):
        # Initialize Hill Climber
        super().__init__(chain, n_flips, total_iterations)

        self.tempO = 6
        self.total_iterations = total_iterations
        self.temperature = temperature
        self.probability = 0
        self.iterations = 0

    def get_probability(self, current_score):
        """
        Return probability of acceptance.
        """

        probability = 2 ** ((current_score - self.baseline_score)/ self.temperature)

        # If scores stays the same reduce probability with temperature function
        if current_score == self.baseline_score:
            probability = self.tempO - (self.tempO / self.total_iterations) * self.iterations
        
        self.probability_L.append(probability)

        return probability

    def change_temperature(self, iterations):
        """
        Change the temperature.
        """

        self.temperature = self.tempO - (self.tempO / self.total_iterations) * self.iterations

    def accept_or_fail(self):
        """
        Accept based on probability function.
        """
        current_score = self.copy_chain.get_score()
        self.probability = self.get_probability(current_score)

        if self.probability > random.random():
            self.chain = deepcopy(self.copy_chain)
            self.baseline_score = current_score

    def run(self):
        """
        Run simulated annealing.
        """
        # Initiate copy to make small changes
        self.copy_chain = deepcopy(self.chain)

        # Introduce temperature
        self.temperature = self.tempO

        self.iterations = 1
        while self.iterations < self.total_iterations:
            super().get_random_point()

            # Flip parts of chain of length n_flips if possible
            for _ in range(self.n_flips):

                # Check if not last chain point
                if self.random_point_index <= (len(self.chain.folds) - self.n_flips):

                    # Flip
                    super().get_flip()
                    super().flip()
                    super().set_new_points()

            # Set lowerbound
            if self.temperature < 0.01:
                self.temperature = 0.01

            self.accept_or_fail()

            self.change_temperature(self.iterations)
            self.iterations += 1
            self.iterations_L.append(self.iterations)
