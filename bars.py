import json
import sys
from math import sqrt


def load_jsonfile(filepath):
    try:
        with open(filepath, 'r', encoding='cp1251', 
                errors='ignore') as file_handler:              
            return json.load(file_handler)
    except FileNotFoundError:
        print('file: {0} not found'.format(filepath))
    except ValueError:
        print('file: {0} is not valid json file'.
            format(filepath))
        


def get_biggest_bar(json_input):
    return max(json_input, key=lambda bar: bar['SeatsCount'])
    
    
def get_smallest_bar(json_input):
    return min(filter(lambda bar: bar['SeatsCount'] > 0, json_input),
               key=lambda bar: bar['SeatsCount'])
               

def get_closest_bar(json_input, longitude, latitude):
    return min(json_input, key=lambda bar: sqrt(
                    (longitude - float(bar['Longitude_WGS84']))**2 + 
                    (latitude - float(bar['Latitude_WGS84']))**2))


def print_bar(bar, type):
    print('{0} bar is: "{1}" with ID: {2}, seats: {3}'
          .format(type, bar['Name'], bar['ID'],
                  str(bar['SeatsCount'])))
                  
                  
def print_bars_info(bars):
    for bar, type in bars:
        print_bar(bar, type)
                  
                  
if __name__ == '__main__':
    
    try: 
        json_input = load_jsonfile(sys.argv[1])
        longitude = float(sys.argv[2])
        latitude = float(sys.argv[3]) 
    except IndexError:
        print('warning: please add valid json file as 1-st argument:'+ 
            ' ./python pprint_json.py data.json longitude latitude')
    else:
        bars = [(get_biggest_bar(json_input), 'Biggest'),
            (get_smallest_bar(json_input), 'Smallest'),
            (get_closest_bar(json_input, longitude, latitude),
                'Nearest')]
        print_bars_info(bars)
                 
