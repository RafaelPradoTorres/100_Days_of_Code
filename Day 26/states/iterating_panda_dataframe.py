student_dict = {
    "student": ["rafa", "joao", "otavio"],
    "score": [65, 70, 80],
}
print(student_dict)
#
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)


# loopong a dataframe
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# column
for (key, value) in student_data_frame.items():
    print(value)

# rows
for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row)
    print(row.student)