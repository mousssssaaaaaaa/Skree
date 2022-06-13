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

        all_options = self.get_neighbours(self.folds[-1])

        options = all_options - all_options.intersection(set(self.folds)) - set([self.wrong_option])

        return list(options)

    def get_neighbours(self, point):
        x, y = point
        top = (x, y + 1)
        bottom = (x, y - 1)
        left = (x - 1, y)
        right = (x + 1, y)

        return {top, bottom, left, right}

    def remove_point(self):
        self.wrong_option = self.folds[-1]
        self.folds.pop(-1)

    def get_score(self):
        score = 0
        dictionary = dict(zip(self.folds, self.aminocode))

        for point in dictionary:
            if dictionary[point] == 'H':
                neighbours = self.get_neighbours(point)
                for neighbour in neighbours:
                    covalent = self.get_covalent(point)
                    if dictionary.get(neighbour) == 'H' and neighbour not in covalent:
                        score += 1
        return score/2

    def get_covalent(self, point):
        index = self.folds.index(point)

        if index == 0:
            return [self.folds[index + 1]]
        elif index == len(self.aminocode) - 1:
            return [self.folds[index-1]]
        else: 
            return [self.folds[index-1], self.folds[index + 1]]
