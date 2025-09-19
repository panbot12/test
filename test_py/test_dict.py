# Create a dictionary
my_dictionary = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupations": ["Engineer", "Developer"]
}

# 1. Print the entire dictionary
print("--- Printing the entire dictionary ---")
print(my_dictionary)

# 2. Print a specific value by its key
print("\n--- Printing a specific value ---")
print("Name:", my_dictionary["name"])
print("Age:", my_dictionary["age"])

# 3. Iterate and print keys
print("\n--- Printing only keys ---")
for key in my_dictionary:
    print(key)

# 4. Iterate and print values
print("\n--- Printing only values ---")
for value in my_dictionary.values():
    print(value)

# 5. Iterate and print key-value pairs
print("\n--- Printing key-value pairs ---")
for key, value in my_dictionary.items():
    print(f"{key}: {value}")

# 6. Using pprint for pretty printing (especially for nested dictionaries)
import pprint
print("\n--- Pretty printing with pprint ---")
pprint.pprint(my_dictionary)

# 7. Using json.dumps for formatted string output
import json
print("\n--- Formatted string output with json.dumps ---")
json_string = json.dumps(my_dictionary, indent=4)
print(json_string)
