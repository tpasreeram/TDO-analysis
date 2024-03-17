import pandas as pd
import sys
import os
import numpy as np

def clean(filename):
    df = pd.read_csv(filename, sep=',', dtype={"Unnamed: 24": str})   # Iniitializes dataframe
    
    df.rename(columns=lambda x: x.strip(), inplace=True)     # Removes leading/trailing whitespace
    df.columns = df.columns.str.replace(' ', '_')
    
    # Shortening certain column names
    df.rename(columns={"Live_ME_(experemental)2/29/2024": "Live_ME_(experimental)"}, inplace=True)

    df.dropna(axis=1, how='all', inplace=True)              # Drops columns with all NaN
    df = df.loc[:, (df != 0).any(axis=0)]                   # Drops columns with all 0
    df.drop(df.columns[[1]], axis=1, inplace=True)          # Drops N(GPIB)
    df.dropna(subset="T_(top)", inplace=True)               # Drops rows with NaN values
    comments = df.filter(df.iloc[:,-3:], axis=1)            # Filters out comment data into a separate dataframe
    df.drop(df.iloc[:,-3:], axis=1, inplace=True)           # Drops the 3 final comment columns

    # Make an offset column
    t0 = df.iloc[0]['time']
    df["offset"] = df["time"] - t0
    col = df.pop("offset")
    df.insert(1, col.name, col)

    temp = comments.dropna(axis=0, how='any')
    indices = np.array([0])
    for ind in temp.index:
        if ind != 0:
            indices = np.append(indices, ind)

    dir = filename.replace('.csv', '') + '/'
    os.mkdir(dir)

    j = 0;
    for i in range(indices.size + 1):
        ramp = "-ramp" + str(i - 1) + ".csv";
        fname = dir + filename.replace('.csv', ramp)
        if i == indices.size:
            df.loc[j:df.tail(1).index.item()].to_csv(fname, index=False)
        elif (indices[i] != 0) and (indices[i] - 1 != 0):
            df.loc[j:indices[i]-1].to_csv(fname,index=False)
            j = indices[i]

    comments.dropna(axis=0, how='all', inplace=True)            
    commentfile = dir + "notes.txt" 
    comments.to_csv(commentfile, sep='\t')

def main():
    filename = sys.argv[1]
    isfile = os.path.isfile(filename)

    if isfile:
        clean(filename)
    else:
        print("It doesn't seem like the file you are looking for exists. Try again.")
    return 0

main()
