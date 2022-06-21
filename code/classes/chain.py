class Chain():
    """
    The Chain class represents an aminoacid chain with aminocode.
    """
    def __init__(self, aminocode):
        self.folds = [(0,0,0)]
        self.score = 0
        self.aminocode = aminocode
        self.hydrophobe = []

    def build(self, point):
        """
        Append a point to the chain.
        """
        self.folds.append(point)

    def get_options(self):
        """
        Get all possible options to move to from current point.
        """

        # get all neighbours and remove points already in the chain
        all_options = self.get_neighbours(self.folds[-1])
        options = all_options - all_options.intersection(set(self.folds))

        return options

    def get_neighbours(self, point):
        """
        Get all neighbouring points.
        """
        x, y, z = point
        top = (x, y + 1, z)
        bottom = (x, y - 1, z)
        left = (x - 1, y, z)
        right = (x + 1, y, z)
        up = (x, y, z + 1)
        down = (x, y, z - 1)

        return {top, bottom, left, right, up, down}

    def remove_last_point(self):
        """
        Remove last point from current chain.
        """
        self.folds.pop(-1)

    def get_score(self):
        """
        Calculate score of the current structure. 
        Neighbouring hydrophobic points that are not covalently connected equals 1 point.
        """
        score = 0
        dictionary = dict(zip(self.folds, self.aminocode[0: len(self.folds)]))

        # check all neighbours of hydrophobic point
        for point in dictionary:
            if dictionary[point] == 'H':
                neighbours = self.get_neighbours(point)
                for neighbour in neighbours:
                    covalent = self.get_covalent(point)

                    # score a point if neighbour is hydrophobic and not covalent
                    if dictionary.get(neighbour) == 'H' and neighbour not in covalent:
                        score += 1

        # halve score since two hydrophobic neighbours equals 1 point, not 2
        return score/2

    def get_covalent(self, point):
        """
        Get covalent connections from point.
        """
        index = self.folds.index(point)
    
        if index == 0:
            return [self.folds[index + 1]]
        elif index == len(self.aminocode[0: len(self.folds)]) - 1:
            return [self.folds[index-1]]
        else:
            return [self.folds[index-1], self.folds[index + 1]]
