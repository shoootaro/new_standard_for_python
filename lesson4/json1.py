import os
import json

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "customers.json")
in_file = open(path, "r")

# JSONファイルをロード
json_obj = json.load(in_file)
print(json_obj)

for customer in json_obj["customers"]:
    print(customer["name"], str(customer["age"]) + "才", customer["gender"])
in_file.close()