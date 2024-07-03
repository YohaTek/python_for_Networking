import json

with open("code.json","r") as f:
    data = json.load(f)


print("loaded json file",data)

