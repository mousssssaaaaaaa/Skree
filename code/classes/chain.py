from code.algorithms import Algorithm as alg_r

class Chain():
    def __init__(self, aminocode):
        self.folds = [(0,0)]
        self.score = 0
        self.aminocode = aminocode

    def build(self, point):
        self.folds.append(point)

    def get_options(self):
        """Get all possible options to move to from current point"""

        all_options = self.get_neighbours(self.folds[-1])
        options = all_options - all_options.intersection(set(self.folds))

        return options

    def validate_option(self):
        """
        Check if placed amino acid is next to other existing amino acid
        Requirement:
        - Happens after fold is appended
        - Set threshold of when to start validation, otherwise
        the chain would only spiral (when len(chain.folds) > 7?).
        - Do not include covalent bond into the condition.
        - Minesweeper-method (Nienke)
        - Alternatief: zwaartepunt-method ("gemiddelde" van coordinates)
        """

        if len(chain.folds) < 0.3 * len(chain.aminocode):
            return True
        else:
            pot_neighbour = self.get_neighbours(self.folds[-1])
                            + self.get_diag_neighbours(self, point)
            val_neighbour = pot_neighbour - self.folds[-1]

    # def get_diag_neighbours(self, point):
    #     x, y = point
    #     t_left = (x - 1, y + 1)
    #     t_right = (x + 1, y + 1)
    #     b_left = (x - 1, y - 1)
    #     b_right = (x + 1, y - 1)

        # return {}

    def get_neighbours(self, point):
        x, y = point
        top = (x, y + 1)
        bottom = (x, y - 1)
        left = (x - 1, y)
        right = (x + 1, y)

        return {top, bottom, left, right}

    def remove_last_point(self):
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
