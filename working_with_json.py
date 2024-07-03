import json

with open("code.json","r") as f:
    data = json.load(f)


print("loaded json file",data)

# Printing specific elements
print(f"Device Name: {name}")
print(f"Version: {version}")
print(f"Vendor: {vendor}")
print("Interfaces:")
for interface in interfaces:
    for key, value in interface.items():
        print(f"  {key}: {', '.join(value)}")

# Example of manipulating the data
# Adding a new interface
new_interface = {"Giga": ["interface4", "interface5"]}
data['interface'].append(new_interface)

# Saving the modified data back to the file
with open('data_modified.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Modified data saved to data_modified.json")