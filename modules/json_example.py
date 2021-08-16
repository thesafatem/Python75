"""
JSON stands for JavaScript Object Notation
"""

"""
{
    firstname: 'Dulat',
    lastname: 'Erektybayev',
    age: 30,
    city: 'Almaty'
}
"""

import json

student = {
    'firstname': 'Dulat',
    'lastname': 'Erektybayev',
    'age': 30,
    'city': 'Almaty'
}

json_string = json.dumps(student)
print(student, type(student))
print(json_string, type(json_string))

new_student = json.loads(json_string)
print(new_student, type(new_student))

letters = {
    1: 'a',
    2: 'b',
    26: 'z'
}

json2 = json.dumps(letters)
print(letters)
