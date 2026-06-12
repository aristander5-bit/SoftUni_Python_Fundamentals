def add(list_of_lessons: list, title:str) -> list:
    if title not in list_of_lessons:
        list_of_lessons.append(title)
    return list_of_lessons

def insert(list_of_lessons: list, title:str, insert_index:int) -> list:
    if title not in list_of_lessons:
        list_of_lessons.insert(insert_index, title)
    return list_of_lessons

def remove(list_of_lessons: list, title:str) -> list:
    if title in list_of_lessons:
        list_of_lessons.remove(title)
        if f"{title}-Exercise" in list_of_lessons:
            list_of_lessons.remove(f"{title}-Exercise")
    return list_of_lessons

def swap(list_of_lessons: list, first_lesson:str, second_lesson:str) -> list:
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_position = list_of_lessons.index(first_lesson)
        second_position = list_of_lessons.index(second_lesson)
        list_of_lessons[first_position], list_of_lessons[second_position] = \
            list_of_lessons[second_position], list_of_lessons[first_position]
        first_has_exercise = f"{first_lesson}-Exercise" in list_of_lessons
        second_has_exercise = f"{second_lesson}-Exercise" in list_of_lessons
        if first_has_exercise and second_has_exercise:
            list_of_lessons[first_position+1], list_of_lessons[second_position+1] = \
                list_of_lessons[second_position+1], list_of_lessons[first_position+1]
        elif first_has_exercise and not second_has_exercise:
            list_of_lessons.insert(second_position+1, list_of_lessons.pop(first_position+1))
        elif second_has_exercise and not first_has_exercise:
            list_of_lessons.insert(first_position + 1, list_of_lessons.pop(second_position + 1))

    return list_of_lessons

def exercise(list_of_lessons: list, title:str) -> list:
    exercise_name = f"{title}-Exercise"
    if title in list_of_lessons and exercise_name not in list_of_lessons:
        lesson_index = list_of_lessons.index(title)
        list_of_lessons.insert(lesson_index+1, exercise_name)
    elif title not in list_of_lessons:
        list_of_lessons.append(title)
        list_of_lessons.append(exercise_name)
    return list_of_lessons

lessons = input().split(", ")
command = input().split(":")

while len(command) > 1:
    action = command[0]
    lesson_title = command[1]
    if action == "Add":
        lessons = add(lessons, lesson_title)
    elif action == "Insert":
        index = int(command[2])
        lessons = insert(lessons, lesson_title, index)
    elif action == "Remove":
        lessons = remove(lessons, lesson_title)
    elif action == "Swap":
        second_title = command[2]
        lessons = swap(lessons, lesson_title, second_title)
    elif action == "Exercise":
        lessons = exercise(lessons, lesson_title)
    command = input().split(":")
for index, lesson_title in enumerate(lessons):
    print(f"{index+1}.{lesson_title}")
