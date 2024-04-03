## class.py
'''*******************************************************************************************
# Name: Anna Bowers, Alyssa Battaglia, Duncan Ward                                           *
# email: bowersas@mail.uc.edu, battagaa@mail.uc.edu, ward2dc@mail.uc.edu                     *
# Assignment Number: Assignment 09                                                           *
# Due Date: 4/4/24                                                                           *
# Course/Section: IS4010-001                                                                 *
# Semester/Year: Spring 2024                                                                 *
# Brief Description of the assignment: Research APIs and build a URL with a data request     *
                                                                                             *
# Brief Description of what this module does: Learn about APIs                               *
# Citations: https://sampleapis.com/api-list/csscolornames                                   *
# Anything else that's relevant:                                                             *
*******************************************************************************************'''
def connect():
    import requests
    import json
    response = requests.get('https://api.sampleapis.com/csscolornames/colors')
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    print(parsed_json)
    
    
    #total = int(parsed_json['total']) # The number of parks that were returned
    
    #    for park in parsed_json['data']:
    #    print (park)
    
    print("Colors containing blue :")
    for color in parsed_json:
        if 'blue' in color['name'].lower():
            print(color['name'])
    print("Colors containing Green :")
    for color in parsed_json:
        if 'green' in color['name'].lower():
            print(color['name'])
            
