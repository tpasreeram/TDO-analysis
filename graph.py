import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

def main():
    filename = sys.argv[1]
    
    df = pd.read_csv(filename, sep=',')

    tl = 106        # Temp 1
    th = 107.3      # Temp 2 (Temp2 > Temp1 need not be true)
    tol = 0.001     # Tolerance for setpoint temps

    if tl == th:
        th += 0.1
    elif tl > th:
        tempth = th
        th = tl
        tl = tempth

    # x-axis : offset, temperature
    # y-axis_1 : DC_X
    # y-axis_2 : Live_ME_..., f_dot/f
    xaxis = "offset"
    yaxis1 = "DC_X"
    yaxis2 = "Live_ME_(experimental)"
    
    # Low End
    templ = df.loc[df["Setpoint"].between(tl - tol, tl + tol)]
    firstl = df.loc[templ["offset"].idxmin()]

    # High End
    temph = df.loc[df["Setpoint"].between(th - tol, th + tol)]
    firsth = df.loc[temph["offset"].idxmin()]

    # firstl.name, firsth.name
    graphr = df.loc[firstl.name:firsth.name]

    xmin = graphr[xaxis].min()
    xmax = graphr[xaxis].max()

    y1r = (graphr[yaxis1].max() - graphr[yaxis1].min()) * 0.2
    y1min = np.floor(graphr[yaxis1].min() - y1r)
    y1max = np.ceil(graphr[yaxis1].max() + y1r)

    y2r = (graphr[yaxis2].max() - graphr[yaxis2].min()) * 0.2
    y2min = np.floor(graphr[yaxis2].min() - y2r)
    y2max = np.ceil(graphr[yaxis2].max() + y2r)

    fig, ax1 = plt.subplots()

    ax1.plot(df['offset'], df['DC_X'], 'b')
    ax1.axis((xmin,xmax, y1min, y1max))
    ax2 = ax1.twinx()
    ax2.plot(df['offset'], df['Live_ME_(experimental)'], 'r')
    ax2.axis((xmin,xmax,y2min,y2max))
    plt.show()
    
    return 0

main()
