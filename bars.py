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
            bar['SeatsCount'] < small_bar['SeatsCount']):
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


if __name__ == '__main__':
    json_input = None;
    
    try: 
        json_input = load_jsonfile(sys.argv[1])
    except IndexError:
        print('warning: please add valid json file as argument: ' + 
            'python pprint_json.py data.json')
            
    if json_input is not None:
        biggest_bar = get_biggest_bar(json_input)
        smallest_bar = get_smallest_bar(json_input)
        print('Biggest bar is: "{0}" with ID: {1}, seats: {2}'
            .format(biggest_bar['Name'], biggest_bar['ID'],
                    str(biggest_bar['SeatsCount'])))
        print('Smallest bar is: "{0}", with ID: {1}, seats: {2}'
            .format(smallest_bar['Name'], smallest_bar['ID'],
                    str(smallest_bar['SeatsCount'])))
        try:
            closest_bar = get_closest_bar(json_input, float(sys.argv[2]),
                                          float(sys.argv[3]))
            print('Nearest bar is: "{0}" with ID: {1}, seats: {2}'
                  .format(closest_bar['Name'], closest_bar['ID'],
                          str(closest_bar['SeatsCount'])))
        except (IndexError, ValueError):
            print('warning: please add valid longitude latitude'
                 'as arguments, like:' +
                 'python bars.py data.json longitude latitude')
