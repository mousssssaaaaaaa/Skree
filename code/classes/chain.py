import random
class Chain():
    def __init__(self, aminocode):
        self.folds = [(0,0)]
        self.score = 0
        self.output = () # tuple
        self.aminocode = aminocode

    def build(self):
        # check previous coordinates in folds
        # find next coordinate random

        options = self.get_options()
        print(options)
        if options == []:
            print("I'm stuck")
            return False

        next_point = random.choice(options) 
        print(next_point)

        self.folds.append(next_point)

    def get_options(self):
        """Get all possible options to move to from current point"""

        x, y = self.folds[-1]
        top = (x, y + 1)
        bottom = (x, y - 1)
        left = (x - 1, y)
        right = (x + 1, y)

        all_options = {top, bottom, left, right}

        options = all_options - all_options.intersection(set(self.folds))
        return list(options)


        # append answers tuple (random, chain[i])
        # converter(previous and current)

    # def converter():
    #     # previous and current 
    #     # return direction 

    # def score():
    #     # TODO: count (C)HH bonds

