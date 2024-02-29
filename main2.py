import files
import json

# json.dumps(dict)  # convierte un dict en un str formato JSON
# json.loads(str)  # convierte un str formato JSON a dict

user = {
    "username": "alfredoa",
    "name": "Alfredo",
    "last_name": "Altamirano",
    "password": "ksks",
}

user1 = {
    "username": "alfredoa1",
    "name": "Alfredo1",
    "last_name": "Altamirano1",
    "password": "ksks1",
}

user_list = [user,user1]

print(user_list)

json_user_list = json.dumps(user_list)

python_user_list = json.loads(json_user_list)

files.create('samples.txt', json_user_list)
