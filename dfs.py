# Python script to read some CSVs and give us the Traces we want for our plotly javascripts
# Donut plot scripting done by Corey Clippinger

# Imports
import pandas as pd
import numpy as np

# For Corey!
import random

# Set the directory as a variable because laziness
directory = 'static/data/'

def timeseries_data(city, month):
    avg_df = pd.read_csv(directory + 'daily_avg_temps.csv')
    df = time_warp(avg_df)
    df = df[[f'{city}', 'datetime']][(df['Year'] == '2015') & (df['Month'] == month)]
    df = df.to_dict('list')
    avg_trace = {
        'x': df['datetime'],
        'y': df[city],
        'type': 'scatter',
        'name': city + ' ' + "Daily Average Temperatures",
        'mode': 'lines',
        'line': {'color': '#87D68D'}
    }

    min_df = pd.read_csv(directory + 'daily_min_temps.csv')
    df = time_warp(min_df)
    df = df[[f'{city}', 'datetime']][(df['Year'] == '2015') & (df['Month'] == month)]
    df = df.to_dict('list')
    min_trace = {
        'x': df['datetime'],
        'y': df[city],
        'type': 'scatter',
        'name': city + ' ' + "Daily Min Temperatures",
        'mode': 'lines',
        'line': {'color': '#87A0B2'}
    }

    max_df = pd.read_csv(directory + 'daily_max_temps.csv')
    df = time_warp(max_df)
    df = df[[f'{city}', 'datetime']][(df['Year'] == '2015') & (df['Month'] == month)]
    df = df.to_dict('list')
    max_trace = {
        'x': df['datetime'],
        'y': df[city],
        'type': 'scatter',
        'name': city + ' ' + "Daily Max Temperatures",
        'mode': 'lines',
        'line': {'color': '#D95D39'}
    }


    return [avg_trace, min_trace, max_trace]

def scatter_data(city, month, filename1, filename2):
    df = pd.read_csv(directory + filename1 + '.csv')
    df = time_warp(df)
    df = df[[f'{city}', 'datetime']][(df['Year'] == '2015') & (df['Month'] == month)]
    df = df.to_dict('list')
    df2 = pd.read_csv(directory + filename2 + '.csv')
    df2 = time_warp(df2)
    df2 = df2[[f'{city}', 'datetime']][(df2['Year'] == '2015') & (df2['Month'] == month)]
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
    return [trace]

def donut_data(city, month, filename):
    # My take on Coreys code
    df = pd.read_csv(directory + 'weather_description.csv')
    df = time_warp(df)
    df = df[[f'{city}', 'datetime']][(df['Year'] == '2015') & (df['Month'] == month)]
    df = df[city].value_counts(ascending=False)
    color_codes = create_color_codes(df.index)
    trace = {
        'type': 'pie',
        'name': str(df.name),
        'labels': [x for x in df.index],
        'values': [int(x) for x in df.values],
        'marker': {'colors' : color_codes},
        'hole': 0.4,
        'textinfo': 'labels'
    }
    return [trace]

def time_warp(df):
    # Takes in a pandas DataFrame, splits a YYYY-MM-DD format datetime column into a Year, Month, and Day column while retaining the original column for later use
    df['Year']=[d.split('-')[0] for d in df.datetime]
    df['Month']=[d.split('-')[1] for d in df.datetime]
    df['Day']=[d.split('-')[2] for d in df.datetime]
    return df

# Corey's code!  But maybe I can make it work a little bit more like mine, so I'm stealing this and reworking it in an above function.  Thanks!
def get_descriptions(arrival, city):
    import json
    '''
    takes in a date and city and gives a json string of 
    the value counts of the weather descriptions for that month
    result json also includes dynamically changing color codes
    
    arrival: datetime as a string, 
    city: column that corresponds to the weather_description.csv
    '''
    
    df = pd.read_csv(directory + 'weather_description.csv',
                     parse_dates=['datetime'], index_col='datetime')
    time_frame = df.loc[pd.date_range(arrival, periods=30, freq='D').values, :]
    weather_descriptions = time_frame[city].value_counts(ascending=False)
    #results = weather_descriptions.to_json(orient='split')
   # print(weather_descriptions.to_json(orient='split'))
    # create color codes
    color_codes= create_color_codes(weather_descriptions.index)
    final_json = {
        "name":str(weather_descriptions.name),
        "index":[x for x in weather_descriptions.index],
        "data":[int(x) for x in weather_descriptions.values],
        "color_codes": color_codes
        }
    return json.dumps(final_json)

# Corey's color function
def create_color_codes(weather_list):
    '''
    dynamically create color codes from weather descriptions
    '''
    color_codes = []
    snow_counter = 0
    storm_counter = 0
    rain_counter = 0
    clear_counter = 0
    for value in weather_list:
        try:
            if 'snow' in value:
                color_codes.append("rgb(159,255,203)")
                if snow_counter > 1:
                    color_codes.append(f"rgb(159,255,{203 + snow_counter * 2})")
                snow_counter += 1
            elif 'storm' in value:
                color_codes.append("rgb(16,79,85)")
                if storm_counter > 1:
                    color_codes.append(f"rgb({16 + storm_counter},{79 + snow_counter},85)")
                storm_counter += 1

            elif 'rain' in value:
                color_codes.append("rgb(160,210,219)")
                if rain_counter > 1:
                    color_codes.append(f"rgb(160,{210 - rain_counter * 4},219)")
                rain_counter += 1

            elif 'clear' in value:
                color_codes.append("rgb(251,237,99)")
                if clear_counter > 1:
                    color_codes.append(f"rgb(251,237,{99 + clear_counter})")
                clear_counter += 1
            else:
                color_codes.append(f"rgb({random.randint(1,150)},{random.randint(1,50)},99)")
            
        except:
            print('nan')
    return color_codes



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
