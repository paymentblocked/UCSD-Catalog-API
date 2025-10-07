# UCSD-Catalog-API


## Endpoints:
 * ### GET /health -> simple health check
 ```
 #Example
 import requests
 res = requests.get("https://ucsd-catalogue-api.onrender.com/health")
 print(res.json())

 ...

 {status: ok}
 ```
 * ### GET /departments -> list of departments (returns id, name, code)
 ```
 #Example
 import requests
 res = requests.get("https://ucsd-catalogue-api.onrender.com/departments")
 print(res.json())

 ...

 [{'code': '', 'id': 1, 'name': 'Asian American &Pacific Islander'}, {'code': 'AAPI', 'id': 2, 'name': 'Asian Am & Pacific Islander St'}, {'code': 'AAS', 'id': 3, 'name': 'African American Studies'}, {'code': 'AIP', 'id': 4, 'name': 'Academic Internship Program'}, {'code': 'ANES', 'id': 5, 'name': 'Anesthesiology'}, ...]
 ```
 * ### GET /search?q=term -> basic search across course titles and department names
 ```
 #Example
 import requests
 res = requests.get("https://ucsd-catalogue-api.onrender.com/search?q=Data+Science")
 print(res.json())

 ...

 [{'course_id': 1828, 'course_number': '9', 'department': 'Cognitive Science', 'title': 'Introduction to Data Science ( 4 Units)'}, {'course_id': 1847, 'course_number': '108', 'department': 'Cognitive Science', 'title': 'Data Science in Practice ( 4 Units)'}, ...]
 ```
 * ### GET /departments/by-code/<dept_code> -> lookup a department object by its code (case-insensitive)
 ```
 #Example
 import requests
 res = requests.get("https://ucsd-catalogue-api.onrender.com//departments/by-code/DSC")
 print(res.json())

 ...

 {'code': 'DSC', 'id': 59, 'name': 'Data Science'}
 ```
 * ### GET /departments/code/<dept_code>/courses -> list courses for the department identified by code
 ```
 #Example
 import requests
 res = requests.get("https://ucsd-catalogue-api.onrender.com/departments/code/DSC/courses")
 print(res.json())

 ...

 [{'course_number': '10', 'id': 2490, 'title': 'Principles of Data Science ( 4 Units)'}, {'course_number': '10', 'id': 2491, 'title': 'Principles of Data Science ( 4 Units)'}, {'course_number': '10', 'id': 2492, 'title': 'Principles of Data Science ( 4 Units)'}, ...]
 ```
 * ### GET /departments/code/<dept_code>/courses/<course_number>/sections -> list sections for the given department code and course_number. If multiple course rows share the same course_number in the DB, sections from all matching course rows will be returned and each section will include the numeric `course_id`.
```
#Example
 import requests
 res = requests.get("https://ucsd-catalogue-api.onrender.com/departments/code/DSC/courses/10/sections")
 print(res.json())

 ...

 [{'building': 'PCYNH', 'course_id': 2490, 'days': 'MWF', 'id': 4264, 'instructor': 'Tiefenbruck, Janine LoBue', 'meeting_type': 'LE', 'room': '106', 'section': 'A00', 'section_id': '', 'time': '9:00a-9:50a'}, ...]
 ```