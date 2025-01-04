# // Implement a simple prototype service to find the difference between two JSON
# // To keep the prototype simple,a JSON will contain only key-value pairs and no nested objects or arrays in it
# // Given two JSON strings json1 and json2, find the list of keys for which the values are different. 
# // If a key is present in only one of the JSONs, it should not be considered in the result. The list of keys should be sorted in lexicographically ascending order.

# // Example
# json1={
#     "hello": "world",
#     "hi":'hello',
#     "you":"me"
# }
# json2={
#     "hello": "world",
#     "hi":'hello',
#     "you":"me"
# }

# // The only difference between the two JSONs is the value of the key "hi". The result is ["hi"].

# // Function Description
# // Complete the function findJSONDIFF below
# // findJSONDIFF has the following parameter(s):
# //     string json1: a JSON string
# //     string json2: a JSON string

# // Returns:
# # //     string[]: sorted a list of keys for which the values are different between the two JSONs

# // solution
# function findJSONDIFF(json1, json2) {
#     // Write your code here
#     let obj1 = JSON.parse(json1);
#     let obj2 = JSON.parse(json2);
#     let result = [];
#     for (let key in obj1) {
#         if (obj1[key] !== obj2[key]) {
#             result.push(key);
#         }
#     }
#     return result.sort();
# }

# in python
import json

def getJSONDIFF(json1, json2):
    obj1 = json.loads(json1)
    obj2 = json.loads(json2)
    result = []
    for key in obj1:
        if obj1[key] != obj2[key]:
            result.append(key)
    return sorted(result)

json1 = {
    "hello": "world",
    "hi":'hello',
    "you":"me"
}
json2 = {
    "hello": "world",
    "hi":'hello',
    "you":"me"
}

print(findJSONDIFF(json1, json2)) # ["hi"]

