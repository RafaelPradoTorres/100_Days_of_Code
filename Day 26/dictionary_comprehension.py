from random import randint

names = ["alex", "beth", "caroline", "dave", "elanor", "freddie"]

students_scores = {student:randint(1, 100) for student in names}
print(students_scores)

passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
print(passed_students)