courses = {}

while True:
    line = input()
    if line == "end":
        break

    data = line.split(" : ")
    course_name = data[0]
    student_name = data[1]

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student_name)

for course_name, students in courses.items():
    total_students = len(students)
    print(f"{course_name}: {total_students}")

    for student in students:
        print(f"-- {student}")