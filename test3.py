# importing json library.
import json

# data which going to b serialize and deserialize in other file name check.json.
students ={
           "id":"9607",
           "name": "Sunny",
           "department":"Computer",
           "compiled" : "None",
           }

# Serialization in json format using dump.
with open("check.json", "w") as file:
    student_json = json.dump(students, file, indent= 4)
print(file)

# Deserialization from json to back in python using load.
f = open("check.json")
data = json.load(f)
print(data)




