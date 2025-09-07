file_name = "./weather_data.csv"

# with open(file_name, 'r') as file:
#     data = file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

# DATAFRAME & SERIES

data = pandas.read_csv(file_name)
print(data)
print(type(data))
print(data["temp"])
print(type(data["temp"]))


data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# getting data in columns
avr_temp = sum(temp_list) / len(temp_list)
print(avr_temp)

print(data["temp"].mean())
print(data["temp"].max())

print(data.temp.mean())

#getting data in rows
print(data[data.day == "Monday"])
max_temp = data.temp.max()
print(data[data.temp == max_temp])

print('\n')
# getting an element
monday = data[data.day == "Monday"]
print(monday.temp)

#creating a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")