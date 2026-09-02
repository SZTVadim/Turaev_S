student = {
    "name": 'ivan',
    "age": 20,
    "course": 2,
    "city": 'Moscow'
}

print(student.keys())
print(student.values(), "\n")

for key, value in student.items():
    print(key, value)
for value in student.values():
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

student_3 = student_1 | student_2

print(student_3)

student_1.update(student_2)

print("student1:", student_1)
print("student2:", student_2)
print("student3:", student_3)
