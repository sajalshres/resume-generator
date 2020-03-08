"""Common utility methods for Resume"""

import json

def get_profile(location):
    with open(location) as file:
        if location.endswith('.json'):
            return json.load(file)
    
    print("Unsupported profile file type")
    return None