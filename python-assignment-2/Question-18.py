import json
with open('user.json','w') as file:
         json.dump({
            "name": "Foo Bar",
            "age": 78,
            "friends": ["Jane","John"],
            "balance": 345.80,
            "other_names":("Doe","Joe"),
            "active":True,
            "spouse":None
        }, file, sort_keys=True, indent=4)
with open('user.json', 'r') as file:
        user_data = json.load(file)
print(user_data)
