# Imports
import pandas as pd
import numpy as np

# Set variables the directory
directory = 'static/data/'

def timeseries_data(city, month, filename):
    df = pd.read_csv(directory + filename + '.csv')
    df = time_warp(df)
    df = df[[f'{city}', 'datetime']][(df['Year'] == '2015') & (df['Month'] == month)]
    df = df.to_dict('list')
    trace = {
        'x': df['datetime'],
        'y': df[city],
        'type': 'scatter',
        'name': city + ' ' + filename,
        'mode': 'lines',
        'line': {'color': '#123456'}
    }
    return trace

def scatter_data(city, month, filename1, filename2):
    df = pd.read_csv(directory + filename1 + '.csv')
    df = time_warp(df)
    df = df[[f'{city}', 'datetime']][(df['Year'] == '2015') & (df["Month"] == month)]
    df = df.to_dict('list')
    df2 = pd.read_csv(directory + filename2 + '.csv')
    df2 = time_warp(df2)
    df2 = df2[[f'{city}', 'datetime']][(df2['Year'] == '2015') & (df2["Month"] == month)]
    df2 = df2.to_dict('list')
    trace = {
        'x': df[city],
        'y': df2[city],
        'type': 'scatter',
        'name': f'{city} {filename1} vs {city} {filename2}',
        'mode': 'markers',
        'marker': {'size': 12,
                'symobl': 'star',
                'color': 'purple'},
        'text': df['datetime']
    }
    return trace

def donut_data(city, month, filename):
    return 0

def time_warp(df):
    # Takes in a pandas DataFrame, splits a YYYY-MM-DD format datetime column into a Year, Month, and Day column while retaining the original column for later use
    df['Year']=[d.split('-')[0] for d in df.datetime]
    df['Month']=[d.split('-')[1] for d in df.datetime]
    df['Day']=[d.split('-')[2] for d in df.datetime]
    return df
# OK so things I need to have
# A function in the app that goes to cityvar/monthvar/xvar/yvar or something
# to feed the front end dropdowns

# Functions to prepare the data for each selection
#     so...
#     Scatter:
#         the trace
#             x: variable from the weather,
#             y: airport delays or w/e,
#             mode: 'markers',
#             type: 'scatter',
#         layout
#             title: `${x} vs Airplane Delays or W/E`
#     Timeseries:
#         the trace
#             x: date column,
#             y: temp/humidity/wind speed,
#             type: 'scatter',
#             mode: 'lines',
#             name: the table it's from or w/e,
#             line: dict(
#                 color: '#nicecolor'
#             )
#     Donut:
#         the trace
#             values: numbers from the weather descriptors based on city for that month
#             labels: labels from weather descriptors etc
#             type: 'pie'
#         layout
#             height: a number,
#             width: another number
    
# For each of these, the right csv needs to be loaded, and the data needs to 
# be first paired down to just the city, then just the month that was selected
