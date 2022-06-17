class Chain():
    def __init__(self, aminocode):
        self.folds = [(0,0,0)]
        self.score = 0
        self.aminocode = aminocode
        self.hydrophobe = []

    def build(self, point):
        self.folds.append(point)

    def get_options(self):
        """Get all possible options to move to from current point"""

        all_options = self.get_neighbours(self.folds[-1])
        options = all_options - all_options.intersection(set(self.folds))

        return options

    def get_neighbours(self, point):
        x, y, z = point
        top = (x, y + 1, z)
        bottom = (x, y - 1, z)
        left = (x - 1, y, z)
        right = (x + 1, y, z)
        up = (x, y, z + 1)
        down = (x, y, z - 1)

        return {top, bottom, left, right, up, down}

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
