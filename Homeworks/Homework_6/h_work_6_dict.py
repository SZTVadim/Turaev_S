student = {
    "name": "ivan",
    "age": 20,
    "course": 2,
    "city": "Moscow",
}

print(student.keys())
print(student.values())

for key, value in student.items():
    print(key, value)

for key, value in student.items():
    print(value)

student_1 = {
    "name": 'ivan',
    "age": 20,
    "course": 2
}
student_2 = {
    "name": 'maria',
    "age": 21,
    "city": 'Saints_petersburg'
}

student_1.update(student_2)
print(student_1, "\n")

student_3 = student_1.copy()
student_3.update(student_2)
print(student_3, "\n")

print(student_1)
print(student_2)
print(student_3)
