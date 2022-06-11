from code.algorithms import Algorithm as alg_r

class Chain():
    def __init__(self, aminocode):
        self.folds = [(0,0)]
        self.score = 0
        self.output = ()
        self.aminocode = aminocode
        self.wrong_option = ()

    def build(self):
        # check previous coordinates in folds
        # find next coordinate random

        options = self.get_options()
        while options == []:
            self.remove_point()
            options = self.get_options()

        next_point = alg_r.algorithm_random(options)

        self.folds.append(next_point)

    def get_options(self):
        """Get all possible options to move to from current point"""

        x, y = self.folds[-1]
        top = (x, y + 1)
        bottom = (x, y - 1)
        left = (x - 1, y)
        right = (x + 1, y)

        all_options = {top, bottom, left, right}

        options = all_options - all_options.intersection(set(self.folds)) - set([self.wrong_option])

        return list(options)

    def remove_point(self):
        self.wrong_option = self.folds[-1]
        self.folds.pop(-1)

        # append answers tuple (random, chain[i])
        # converter(previous and current)

    # def converter():
    #     # previous and current 
    #     # return direction 

    # def score():
    #     # TODO: count (C)HH bonds

