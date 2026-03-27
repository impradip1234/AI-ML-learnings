dict={
    "name":"Pradip",
    "roll":2438317,
    "subjects":["physics","chemistry","maths"]
}

#Method 01:
print(dict.keys())

#Method 02:
print(dict.values())

#Method 03:
print(dict.items())

#Method 04:
print(dict.get("name"))  #>>>> return None if not found
#print(get("section"))>>>>>return an error if key not found.

#Method 05
print(dict.update({"section":"D"}))
print(dict)