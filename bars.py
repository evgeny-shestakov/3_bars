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
    for bar, bar_type in bars:
        print_bar(bar, bar_type)
                  
                  
if __name__ == '__main__':
    
    if len(sys.argv) <= 1:
        print('error: please add valid json file as 1-st argument:'+ 
            ' ./python pprint_json.py data.json longitude latitude')
        sys.exit(1)
        
    json_input = load_jsonfile(sys.argv[1])
    if json_input is None:
        sys.exit(1)
    bars = [(get_biggest_bar(json_input), 'Biggest'),
            (get_smallest_bar(json_input), 'Smallest')]
    if len(sys.argv) > 3:
        closest_bar = get_closest_bar(json_input, 
                                      float(sys.argv[2]),
                                      float(sys.argv[3]))
        bars.append((closest_bar, 'Nearest'))
    else:
        print('for calculating nearest bar: add 2-st argument and 3-st '+ 
            'argumets: ./python pprint_json.py data.json longitude latitude')
    print_bars_info(bars)
    sys.exit(0)
        
