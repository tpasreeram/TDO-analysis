This is my attempt at "automating" the visualization of TDO data
in the Sullivan lab at UF.

Files:

## clean.py

Will clean the data from a certain .csv file given to it as a
command line argument

The code assumes there are 25 columns, with columns 23, 24, 25 
(W, X, Y in excel, or 22, 23, 24 when counting from 0) reserved
for comments. I have not yet added an example .csv for I do not
know the policies on posting group data on a public website.

The line
'df.rename(columns={"Live_ME_(experemental)2/29/2024": "Live_ME_(experimental)"}, inplace=True)'

exists mostly only for my sanity and can be commented out, but
make sure to change the corresponding line in graph.py when
needed.

For now, all comments are dropped into a text file, but I 
may change that in a later date so that the comment data can 
be stored closer to the actual data that it is associated with.

This program will create a folder with the name of the input
file (e.g. "example.csv" becomes the directory "example/"), and
all ramps will be placed in this new directory. Ramps are
calculated based off of the location of the comments in row 25
(Y in excel, and 24 when counting from 0). These comments are
not read, so anything in that row will trigger the creation of a
new ramp file. For now, it is on the user to discard any ramps
that are not useful (For example, there was a ramp that I 
believe was ended after 10 minutes to start something else).

## graph.py

Uses data from a given .csv file given to it as a command line
argument. This data is assumed to be the cleaned ramp data that
was output by clean.py

As of right now, 'tl' and 'th' must be input by the user by
editting the python script itself. tl need not be higher than
th, there is code to make sure that it is fine regardless of
whether or not th>tl. The 'tol' is the tolerance i have set for
the finding of setpoints, since the setpoints themselves do not
land on perfect decimal values. This can be changed, but make
sure you look at the raw data before messing with it.

The 'xaxis', and 'yaxis2' values can be changed, and must be
done by actually modifying the values in the script. A planned
future update is to make it so that no editing of the code is
necessary for the user.

This code scales the yaxis for both the y1 and y2 by 20%, and
this value can be changed by adjusting the scaling factor on
'y1r' and 'y2r'.

More can be done to pretty-fy the graph, as well as make the
user experience better, and these are things I plan to rectify
in the future.

Feedback welcome!
