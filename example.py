import requests
res = requests.get("https://ucsd-catalogue-api.onrender.com/departments/code/DSC/courses/10/sections")
print(res.json())