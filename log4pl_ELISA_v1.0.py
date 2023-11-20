# -*- coding: utf-8 -*-
"""
Created on 12 Nov 2023

@author: Billy Shen

## Description

Filename : 'log4pl_ELISA_v1.0.py'

This is an ELISA Tool as an application to analyze data generated from ELISA. 
The application will allow users to input generated data, for example, 
concentration (x) and absorbance results (y) and use libraries such as NumPy, 
SciPy, Matplotlib, and Pandas for data processing and analysis. The application 
will use the ‘curve_fit’ function in SciPy to fit a 4-parameter logistic 
regression model to the input data. The data and visualization of the predicted 
model are built using functions from the Matplotlib library and will present a 
sigmoid curve.

After the graph is presented, the application will provide an option for the 
user to input measured absorbance results and use the modeled function to 
interpolate the unknown concentration as output. 

A final report will be generated summarizeing all the results and date stamped 
for good laboratory practices. A second output uses the Plotly graphing library 
to present an interactive graph, improving data analysis.
"""
import numpy as np
from scipy.optimize import curve_fit #This will do the actual curve fitting
import matplotlib.pyplot as plt
import pandas as pd
import sys
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

### example dataset 1 #########################################################
# x = [1.0, 0.5, 0.25, 0.125, 0.0625]
# y = [9.0, 8.0, 5.0, 2.0, 1.0]

### example dataset 2 #########################################################
# x = [1.95,3.91,7.81,15.63,31.25,62.5,125,250,500,1000]
# y = [0.274, 0.347, 0.392, 0.420, 0.586, 1.115, 1.637, 2.227, 2.335, 2.372]

### example dataset 3 #########################################################
# x = [62.5,125,250,500,1000]
# y = [1.115, 1.637, 2.227, 2.335, 2.372]

# Define function
concs=[]
def serial_dilution(n, factor, start):
    """
    This function create list of concentrations from start and decrease by factor.
    
    Parameters
    ----------
    n : TYPE int
        Number of points to create.
    factor : TYPE float
        Decreasing factor.
    start : TYPE float
        Starting concentration.
    Returns
    -------
    concs : TYPE list
        A list of concentrations.
        
    """
    concs.append(start)
    if n == 1:   # Terminate recursion
        return concs            
    else:
        start = start / factor
        serial_dilution(n - 1, factor, start)   # Recursive call

# prompt user for data input
while True:
    try:
        start_conc = float(input('What is the starting concentration of the reference standard?\n'))
        break
    except ValueError:
        print("That wasn't a valid number!\n")
while True:    
    try:
        serial_factor = float(input('What is the serial dilution factor?\n'))
        break
    except ValueError:
        print("That wasn't a valid number!\n")
while True:        
    try:
        num_points = int(input('How many points for the Reference Standard? (min 5 req.)\n'))
        if num_points > 4:
            break
        print("Minimum 5 points required.\n")
    except ValueError:
        print("That wasn't a valid number!\n")

# calculate concentration series based on user input
serial_dilution(num_points,serial_factor,start_conc)

# get readings and store in list
readings=[]
for i in range(0, num_points):
    while True: 
        try:
            read = float(input(f'What is the reading for reference standard at concentration {concs[i]}?\n'))
            break
        except ValueError:
            print("That wasn't a valid number!\n")
    readings.append(read)

x = concs
y = readings
# create dataframe
df_std = pd.DataFrame(data={'concentration':x, 'reference standard results':y})
print("\nResult Summary:")
print(df_std.to_string(index=False))
# variables to store data features and create new x for curve fit
x = df_std['concentration'].tolist()
x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)
serial_dilution(4, 2, min(x))
step = min(concs)
x_new = np.arange(x_min, x_max, step)

### Define functions
# define 4pl model
def log4pl_y(x, A, B, C, D):
    """
    This function defines the 4pl model fit parameters A, B, C and D, in 'y='.
    
    Parameters
    ----------
    x : TYPE float
        Concentration (x value).
    A : TYPE float
        Bottom.
    B : TYPE float
        Slope.
    C : TYPE float
        EC50.
    D : TYPE float
        Top.
    Returns
    -------
    (((A-D)/(1.0+((x/C)**B))) + D) : TYPE float
        output (y value).
        
    """
    return (((A-D)/(1.0+((x/C)**B))) + D)

# calculate 'x' using defined 4pl model
def log4pl_x(y, A, B, C, D):
    """
    This function defines the same 4pl model fit parameters A, B, C and D, in 'x='.
    
    Parameters
    ----------
    y : TYPE float
        Reading (y value).
    A : TYPE float
        Bottom.
    B : TYPE float
        Slope.
    C : TYPE float
        EC50.
    D : TYPE float
        Top.
    Returns
    -------
    (C*((-A + y)/(D - y))**(1/B)) : TYPE float
        Concentration (x value).
        
    """
    return (C*((-A + y)/(D - y))**(1/B))

### Calculate

# curve fit
try:
    params, _ = curve_fit(log4pl_y, x, y)
except RuntimeError:
    print("\nRuntimeError!\n***4PL model cannot fit into data***\n")
    # plot result
    plt.plot(x, y, 'bo',label="Reference Standard")
    plt.title('Result')
    plt.xlabel('Concentration')
    plt.ylabel('Reading')
    plt.xscale("log")
    plt.legend(loc='best', fancybox=True, shadow=True)
    plt.grid(True)
    plt.savefig('log4pl_plot.png')
    plt.show()
    sys.exit()
    
# get and show the parameters    
A,B,C,D = params[0], params[1], params[2], params[3]
print("\n4PL parameters: A = " + str(round(A,4)) + 
      ", B = " + str(round(B,4)) + 
      ", C = " + str(round(C,4)) + 
      ", D = " + str(round(D,4))) 

# Calculate and print the R-squared value
residuals = y - log4pl_y(x, *params)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y - np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)
print("R-squared value:", round(r_squared, 4), '\n')

# calculate points to plot curve fit result
yfit1 = log4pl_y(x_new, *params)

# Plot reference standard results and curve fit
plt.plot(x, y, 'bo')
plt.plot(x_new, yfit1, 'blue',label="Reference Standard")
plt.title('Standard Curve')
plt.xlabel('Concentration')
plt.ylabel('Reading')
plt.xscale("log")
plt.legend(loc='best', fancybox=True, shadow=True)
plt.grid(True)
plt.savefig('log4pl_plot.png')
plt.show()

# calculate sample
print("Enter 'end' to exit.\n")
sample_x, sample_y = [], []
df_sample = pd.DataFrame()
while True:
    yn = input('Predict sample concentration using reading? (y/n) ')
    if yn == 'n' or yn == 'end':
        print('***end program***')
        break
    elif yn == 'y':
        while True:
            sample_read = input('Enter your sample reading: ')
            if sample_read == "end":
                print('***end program***\n')
                yn = 'end'
                break
            try:
                sample_read = float(sample_read)
                if y_min < sample_read < y_max:
                    sample_conc = log4pl_x(sample_read, *params)
                    print("Based upon a reading of " + str(sample_read) + ", your concentration is " + str(round(sample_conc, 3)) + " units")
                    sample_x += [sample_conc]
                    sample_y += [sample_read]
                else:
                    print("***Values outside the reference standard minimum and maximum readings are invalid for prediction.***")
            except ValueError:
                print("That wasn't a valid number!\n")
        df_sample = pd.DataFrame(data={'sample reading':sample_y, 'concentration':list(np.around(np.array(sample_x),3))})
        print('Result Summary:')
        print(df_sample.to_string(index=False))
        break
    else:
        print("That wasn't a valid input!  'y' yes. 'n' no or 'end' to exit")

# create interactive plot
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=x_new, y=yfit1,
                         mode='lines',
                         line=dict(color='blue'),
                         name='Reference Standard'))
fig.add_trace(go.Scatter(x=x, y=y,
                         mode='markers', 
                         marker=dict(color='blue'),
                         showlegend=False))
fig.update_xaxes(type="log")
fig.update_layout(title='Standard Curve',
                   xaxis_title='Concentration',
                   yaxis_title='Reading')
fig.update_layout(showlegend=True)
fig.write_html("log4pl_plot.html")

# get current date and time
from datetime import datetime
now = datetime.today()

# output to html
with open('index.html', 'w') as f:
    f.write('<h1 style="text-align:center;">Result Summary</h1>')
    f.write('<p>Report created on: '+now.strftime("%d %b %Y  %H:%M:%S")+'</p>')
    f.write('<img src="log4pl_plot.png"/>')
    f.write('<h2 style="text-align:left;">Reference Standard Results</h2>')
    f.write(df_std.to_html(index=False))
    if not df_sample.empty:
        f.write('<h2 style="text-align:left;">Sample Results</h2>')
        f.write(df_sample.to_html(index=False))
