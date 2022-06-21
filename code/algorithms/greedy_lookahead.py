import random
from copy import deepcopy
from code.classes import chain

def depth_first(chain, depth, state_depth, ways):
    """
    Returns all possibilities and their scores with depth
    """  
    
    if state_depth != 0 :
        options = chain.get_options()
        if len(options) == 0:
            return False
        for coordinate in options:
            chain.build(coordinate)
            _ = depth_first(chain, depth, state_depth-1, ways)	
            
        chain.remove_last_point()
    else:
        score = chain.get_score()
        ways.append([score, chain.folds[-depth:]])
        chain.remove_last_point()
        
    
    return ways

def greedy_lookahead(chain):

    while len(chain.folds) < len(chain.aminocode):
        ways = depth_first(deepcopy(chain), 4, 4, []) 
        
        if ways == False:
            chain.folds = [(0, 0, 0)]
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