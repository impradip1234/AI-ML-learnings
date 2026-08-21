# Ques: 04 Create a python dictionary of 3 cities and their populations. Save it to "cities.json".
    # 1. Then load the JSON ans print each city and its population.
    # 2. Ask the user for a new city & its population - update this info in the json file.

import json

cities = {
    "Deoria": 100000,
    "Khukhundoo": 50000,
    "Sonughat": 75000
}

# Save the dictionary to JSON file
with open("81cities.json", "w") as f:
    json.dump(cities, f, indent=4) #save cities info in file f with the indentation 4


# Load the JSON file
with open("81cities.json", "r") as f:
    data = json.load(f)

# Print each city and its population
print("Cities and their populations:")

for city, population in data.items():
    print(city, ":", population)


# Ask user for a new city and its population
city = input("Enter a new city: ")
population = int(input("Enter its population: "))

# Update the dictionary
data[city] = population

# Save the updated dictionary back to JSON
with open("81cities.json", "w") as f:
    json.dump(data, f, indent=4)

print("City added successfully!")