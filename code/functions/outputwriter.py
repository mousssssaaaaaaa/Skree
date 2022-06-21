import csv
import pandas as pd 

def outputwriter(output, aminocode, chain):
    "Convert output to dataframe-csv" 

    directions = []
    
    # compare every point on chain to find direction
    for point in output:
            index = output.index(point)
            if index == (len(output) - 1):
                directions.append(0)
            else: 
                next_point = output[index + 1] 
                current_point = output[index]
                if next_point[1] - current_point[1] == 0: 
                    direction = next_point[0] - current_point[0] 
                else: 
                    direction = (next_point[1] - current_point[1]) * 2

                directions.append(direction)


    # create empty dataframe
    df = pd.DataFrame()
    
    # add results to dataframe/ csv 
    df['amino'] = aminocode
    df['fold'] = directions
    df.loc[''] = ['score', int(chain.get_score())]

    df.to_csv('results/output.csv', index= False)