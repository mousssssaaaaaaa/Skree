import random
from copy import deepcopy
from code.classes import chain

def depth_first(chain):
    """
    Searches depth first with depth 6 for the best possible folding based on its score.
    """
    while len(chain.folds) < len(chain.aminocode):

        # searh for all possible routes of depth 4
        ways = search(deepcopy(chain), 4, 4, []) 
        if ways == False:
            chain.folds = [(0, 0, 0)]

        # pick best based on score
        else:
            highscore = 0
            best_routes = []
            for way in ways:
                score = way[0]
                if score >= highscore:
                    highscore = score
                    best_routes.append(way[1])

            # take one of the best routes and add first point
            next_point = random.choice(best_routes)[0] 
            chain.build(next_point)

    return chain

def search(chain, depth, state_depth, ways):
    """
    Returns all possibilities and their scores.
    Recursive.
    """  
    #  build every possibilty and save with its score
    if state_depth != 0 :
        options = chain.get_options()
        if len(options) == 0:
            return False
        for coordinate in options:
            chain.build(coordinate)
            _ = search(chain, depth, state_depth-1, ways)	
            
        # after building all in-between points, remove point
        chain.remove_last_point()
    else:
        score = chain.get_score()
        ways.append([score, chain.folds[-depth:]])

        # after building last point, remove point
        chain.remove_last_point()
        
    return ways