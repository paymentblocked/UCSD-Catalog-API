import requests
res = requests.get("https://ucsd-catalogue-api.onrender.com/departments")
print(res.json())