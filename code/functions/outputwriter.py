import csv
import pandas as pd 

def outputwriter(output, aminocode, chain_result):
    "Convert output to dataframe-csv" 

    directions = []
    
    # Compare every point on chain to find direction
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

    # Create empty dataframe
    df = pd.DataFrame()
    
    # Add results to dataframe/ csv 
    df['amino'] = list(aminocode)
    df['fold'] = directions
    df.loc[''] = ['score', int(chain_result)]

    df.to_csv('results/output?.csv', index= False)