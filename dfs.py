# Python script to read some CSVs and give us the Traces we want for our plotly javascripts
# Donut plot scripting done by Corey Clippinger

# Imports
import pandas as pd
import numpy as np
import json

from sqls import city_data

# For Corey!
import random

# Set the directory as a variable because laziness
directory = 'static/data/'

# Read in and reprepare (csv's don't play nicely with groupbys?) Chris Prabhu's excellently cleaned data for our scatter plot
delays = pd.read_csv(directory + 'airport_delays.csv')
delays = delays.groupby(['DESTINATION_AIRPORT', 'MONTH', 'DAY']).sum()
delays = delays["ARRIVAL_DELAY"]

# Get our list of cities that are in the US, because our airport data is all American baby!
cities = city_data()
city_list = []
for city in cities:
    if (city['country'] == 'United States'):
        city_list.append(city['city_name'])

# Prepare our airports data to be combed
airports = pd.read_csv(directory + 'airports.csv')

# Function to pull out our airport codes from the city name
def find_airports(city):
    airport_list = airports[['IATA_CODE']][airports['CITY'] == city].to_dict('list')['IATA_CODE']
    return airport_list

def prepare_delays(airports, month):
    month = int(month)
    if len(airports) == 1:
        delay_list = delays[[airports[0]]][month].tolist()
        return delay_list
    elif len(airports) == 2:
        print(airports)
        delay_list = (delays[airports[0]][month] + delays[airports[1]][month]).tolist()
        return delay_list
#TODO Finish this up with making the trace for the scatter plot

def csv_timeseries_data(city, month, files):
    traces = []
    for filename in files:
        df = pd.read_csv(directory + filename + '.csv')
        df = time_warp(df)
        df = df[[f'{city}', 'datetime']][(df['Year'] == '2015') & (df['Month'] == month)]
        df = df.to_dict('list')
        trace = {
            'x': df['datetime'],
            'y': df[city],
            'type': 'scatter',
            'name': city + ' Timeseries',
            'mode': 'lines',
            'line': {'color': '#123456'}
        }
        traces.append(trace)
    return traces

def csv_scatter_data(city, month, filename):
    df = pd.read_csv(directory + filename[0] + '.csv')
    df = time_warp(df)
    df = df[[f'{city}', 'datetime']][(df['Year'] == '2015') & (df['Month'] == month)]
    df = df.to_dict('list')
    airports = find_airports(city)
    print(airports)
    df2 = prepare_delays(airports, month)
    print(df2)
    trace = {
        'x': df[city],
        'y': df2,
        'type': 'scatter',
        'name': f'{city} {filename[0]} vs {city} Count of Airport Delays',
        'mode': 'markers',
        'marker': {'size': 12,
                'symobl': 'star',
                'color': 'purple'},
        'text': df['datetime']
    }
    return [trace]

def donut_data(city, month):
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
    dynamically create color codes from weather descriptions, probably ugly colors too
    '''
    color_codes = []
    snow_counter = 0
    storm_counter = 0
    rain_counter = 0
    clear_counter = 0
    cloud_counter = 0
    for value in weather_list:
        try:
            if 'snow' in value:
                color_codes.append("rgb(159,255,203)")
                if snow_counter >= 1:
                    color_codes.append(f"rgb(159,255,{203 + snow_counter * 10})")
                snow_counter += 1
            elif 'storm' in value:
                color_codes.append("rgb(16,79,85)")
                if storm_counter >= 1:
                    color_codes.append(f"rgb({16 + storm_counter * 10},{79 + snow_counter * 10},85)")
                storm_counter += 1

            elif 'rain' in value:
                color_codes.append("rgb(160,210,219)")
                if rain_counter >= 1:
                    color_codes.append(f"rgb({160 - rain_counter * 20},{210 - rain_counter * 20},{219 + rain_counter*20})")
                rain_counter += 1

            elif 'clear' in value:
                color_codes.append("rgb(251,237,99)")
                if clear_counter >= 1:
                    color_codes.append(f"rgb(251,237,{99 + clear_counter})")
                clear_counter += 1
                print('clear:', value)
            elif 'clouds' in value:
                color_codes.append("rgb(114,172,170)")
                if cloud_counter >= 1:
                    code = f"rgb({114 - cloud_counter * 25},{172 - cloud_counter * 25},{170 - cloud_counter * 15})"
                    color_codes.append(code)
                    print(code)
                cloud_counter += 1
                print('clouds:', value, cloud_counter)
            elif 'haze' in value:
                color_codes.append("rgb(197,211,119)")
            elif 'mist' in value:
                color_codes.append("rgb(247,189,178)")
            else:
                color_codes.append(f"rgb({random.randint(50,200)},{random.randint(50,200)},{random.randint(50,100)})")
            
        except:
            print('nan')
    return color_codes

def get_pic_urls(city):
    """
    queries the pic urls json file and returns a random sampling of them
    
    No guarenttees for trying to get more than 6 pics, so dont' change the random sample selection!!!
    """
    with open(directory + 'city_pics_urls.json', 'r') as f:
        data = json.loads(f.read())
        city_urls = data[city]
        return random.sample(list(city_urls),6)


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
