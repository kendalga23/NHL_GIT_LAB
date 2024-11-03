"""

Description: A simple script to query the NHL API and generate simple 
documentation

License: MIT, see LICENSE file for more details

"""

import requests
import xmltodict
import json

__author__ = 'Drew Hynes'
__copyright__ = 'Copyright 2024, NHL API Documentation'
__credits__ = ['Kevin Sidwar','Jon Ursenbach']
__license__ = 'MIT'
__version__ = '0.0.1'
__maintainer__ = 'Drew Hynes'
__email__ = 'drew.hynes@gmail.com'
__status__ = 'Alpha'

url = "https://api-web.nhle.com/application.wadl?detail=true"
attributes = [
    "@path",
    "@base",
    "@href",
    "@id",
    "@itsn",
    "@jersey",
    "@mediaType",
    "@name",
    "@path",
    "@style",
    "@title",
    "@type",
    "@xml",
    "@xmlns"
]

def remove_at_symbols(data):
    if isinstance(data, dict):
        # Process each key-value pair in the dictionary
        new_data = {}
        for key, value in data.items():
            # Remove @ symbol from the key
            new_key = key.lstrip('@')
            new_data[new_key] = remove_at_symbols(value)
        return new_data
    elif isinstance(data, list):
        # Process each item in the list
        return [remove_at_symbols(item) for item in data]
    else:
        # Return data as-is if it's not a dict or list
        return data    
    
reps = []
for a in attributes:
    line_item = {"target":f"{a}", "new":f"{a[1:]}"}
    reps.append(line_item) 

res_plain = requests.get(url)
res_cleaned = res_plain.text.replace("@", "")

for l in reps:
    res_cleaned = res_cleaned.replace(f'{l["target"]}', f'{l["new"]}')

new_json = xmltodict.parse(res_cleaned)
cleaned = remove_at_symbols(new_json)

i = 0
for line in cleaned['application']['resources']['resource']:
    for item in line:
        if item == "path":
            print(f"{i}: {line['path']}")
        elif item == "resource" and isinstance(line[item], list):
            print(f"{item}")
            for sub_item in line[item]:
                print(f"\t{sub_item['path']}")
                print(f"\tExample: {line['path']}/{sub_item['path']}\n")
        else:
            print(f"{item}")
    print("\n++++++++++++++++++\n")
    i += 1
    