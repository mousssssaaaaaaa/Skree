
class Chain():
    def __init__(self):
        self.folds = [(0,0)]
        self.score = 0
        self.output = () # tuple

    def build(self):
        # check previous coordinates in folds
        # find next coordinate random

        x, y = self.folds[-1]
        x_new = x + 1
        y_new = y + 1
        print(x_new, y_new)

        self.folds.append((x_new, y_new))

        # append answers tuple (random, chain[i])
        # converter(previous and current)

    # def converter():
    #     # previous and current 
    #     # return direction 

    # def score():
    #     # TODO: count (C)HH bonds

