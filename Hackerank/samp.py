import json

def getJSONDiff(json1, json2):
    diff_keys = []
    
    # Parse the JSON strings into dictionaries
    dict1 = json.loads(json1)
    dict2 = json.loads(json2)
    
    # Find the keys that have different values
    for key in dict1.keys():
        if key in dict2.keys() and dict1[key] != dict2[key]:
            diff_keys.append(key)
    
    # Sort the keys in lexicographically ascending order
    diff_keys.sort()
    
    return diff_keys