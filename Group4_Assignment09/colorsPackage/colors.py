## class.py

def connect():
    import requests
    import json
    response = requests.get('https://api.sampleapis.com/csscolornames/colors')
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    print(parsed_json)
    
## Examples: DO NOT USE IN FINAL PROJECT
    #print(parsed_json['data'][0]['description'])
    #print(parsed_json['data'][0]['directionsInfo'])
    
    #total = int(parsed_json['total']) # The number of parks that were returned
    
    #for park in parsed_json['data']:
    #    print (park)
