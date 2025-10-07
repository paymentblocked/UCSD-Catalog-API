import requests
import json


res = requests.get("https://ucsd-catalogue-api.onrender.com/departments/code/DSC/courses/10/sections")

t = res.json()

print(res)