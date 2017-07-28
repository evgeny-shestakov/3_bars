import json
import sys
import os.path
from math import sqrt


def load_jsonfile(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='cp1251', 
                errors='ignore') as file_handler:
            try:              
                return json.load(file_handler)
            except ValueError:
                return None
    else:
        print('no file: {0}'.format(filepath))


def get_biggest_bar(json_input):
    big_bar = None
    for bar in json_input:
        if (big_bar is None or
            bar['SeatsCount'] > big_bar['SeatsCount']):
            big_bar = bar
    
    return big_bar
    
    
def get_smallest_bar(json_input):
    small_bar = None
    for bar in json_input:
        if (small_bar is None or
            (bar['SeatsCount'] < small_bar['SeatsCount']
                and bar['SeatsCount'] > 0)):
            small_bar = bar
    
    return small_bar


def get_closest_bar(json_input, longitude, latitude):
    closest_bar = None
    min_distance  = 0
    for bar in json_input:
        distance = sqrt((longitude - float(bar['Longitude_WGS84']))**2 + 
                        (latitude - float(bar['Latitude_WGS84']))**2)
        if (closest_bar is None or
            distance < min_distance):
            closest_bar = bar
            min_distance = distance
    return closest_bar


def print_bar(bar, type):
    print('{0} bar is: "{1}" with ID: {2}, seats: {3}'
          .format(type, bar['Name'], bar['ID'],
                  str(bar['SeatsCount'])))
                  
                  
def print_bars_info(json_input):
    print_bar(get_biggest_bar(json_input), 'Biggest')
    print_bar(get_smallest_bar(json_input), 'Smallest') 

    try:
        closest_bar = get_closest_bar(json_input, float(sys.argv[2]),
                                      float(sys.argv[3]))
        print_bar(closest_bar, 'Nearest')

    except (IndexError, ValueError):
        print('warning: please add valid longitude latitude'
              'as arguments for calculate nearest bar, like:' +
              './python bars.py data.json longitude latitude')

                  
                  
if __name__ == '__main__':
    json_input = None;
    
    try: 
        json_input = load_jsonfile(sys.argv[1])
    except IndexError:
        print('warning: please add valid json file as argument: ' + 
            'python pprint_json.py data.json')
            
    if json_input is not None:
        print_bars_info(json_input)
                 
