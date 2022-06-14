import random

def algorithm_random(chain):
    wrong_option = ()

    while len(chain.folds) < len(chain.aminocode):

        # check previous coordinates in folds
        options = chain.get_options()
        while options == []:
            wrong_option = chain.folds[-1]
            chain.remove_last_point()
            options = chain.get_options() - set([wrong_option])

        # find next coordinate random
        next_point = random.choice(options)
        chain.build(next_point)

    return chain