#Example (want to find all DSC10 lecture sections)
import requests

res = requests.get("https://ucsd-catalogue-api.onrender.com/departments/code/DSC/courses/10/sections")

for class_ in res.json():
    if class_['meeting_type'] == 'LE':
        print(class_)


"""
Results:
{'building': 'PCYNH', 'course_id': 2490, 'days': 'MWF', 'id': 4264, 'instructor': 'Tiefenbruck, Janine LoBue', 'meeting_type': 'LE', 'room': '106', 'section': 'A00', 'section_id': '', 'time': '9:00a-9:50a'}
{'building': 'PCYNH', 'course_id': 2491, 'days': 'MWF', 'id': 4268, 'instructor': 'Tiefenbruck, Janine LoBue', 'meeting_type': 'LE', 'room': '106', 'section': 'B00', 'section_id': '', 'time': '10:00a-10:50a'}
{'building': 'PCYNH', 'course_id': 2492, 'days': 'MWF', 'id': 4272, 'instructor': 'Tiefenbruck, Janine LoBue', 'meeting_type': 'LE', 'room': '106', 'section': 'C00', 'section_id': '', 'time': '11:00a-11:50a'}
{'building': 'PODEM', 'course_id': 2493, 'days': 'MWF', 'id': 4276, 'instructor': 'Chi, Peter Benjamin', 'meeting_type': 'LE', 'room': '1A19', 'section': 'D00', 'section_id': '', 'time': '9:00a-9:50a'}
"""