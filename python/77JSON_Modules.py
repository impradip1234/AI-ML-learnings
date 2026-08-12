# JSON Modules.......

import json

# 01: json.loads() -> json string to python object
json_str='{"name":"Pradip","isTeacher":true}'
python_obj=json.loads(json_str)
print(python_obj)

# 02: json.dumps() -> python object to json string 
python_obj={'name':'Pradip','isTeacher':True}
json_str=json.dumps(python_obj)
print(json_str)

# 03: json.load() => to read from json file and convert to python object
# with open("77json_modules.json",'r') as f:
#     python_obj=json.load(f)
#     print(python_obj)

# 04: json.dump() => to write in json file and convert to json file
python_obj={
    "name":"Pradip",
    "age":20,
    "isTeacher":False
}
with open("77json_modules.json", "w") as f:
    json.dump(python_obj, f, indent=4 , sort_keys=True)