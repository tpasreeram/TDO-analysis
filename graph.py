import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

def main():
    filename = sys.argv[1]
    print(filename)
    
    df = pd.read_csv(filename, sep=',')

    fig, ax1 = plt.subplots()

    ax1.plot(df['offset'], df['DC_X'], 'b')
    ax1.axis((7500,30000, -20, 220))
    ax2 = ax1.twinx()
    ax2.plot(df['offset'], df['Live_ME_(experimental)'], 'r')
    ax2.axis((7500,30000,-2.5e6,-1.0e6))
    plt.show()
    
    th = 0
    tl = 1

    if tl == th:
        th += 0.1
    elif tl > th:
        tempth = th
        th = tl
        tl = tempth


    # x-axis : offset, temperature
    # y-axis_1 : DC_X
    # y-axis_2 : Live_ME_..., f_dot/f
    xaxis = "offset", "temperature"
    yaxis1 = "DC_X"
    yaxis2 = "Live_ME_(experimental)", "f"
    extraaxis = "fdot"

    closest_tl = df.loc[(df["Setpoint"] - tl).abs().idxmin()]
    x_low = closest_tl[xaxis]

    closest_th = df.loc[(df["Setpoint"] - th).abs().idxmin()]
    x_high = closest_th[xaxis]

    return 0

main()
