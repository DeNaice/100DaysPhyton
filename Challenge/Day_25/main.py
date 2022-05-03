# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature_list = []
#     for row in data:
#         if row[1] != "temp":
#             temperature_list.append(int(row[1]))
#     print(temperature_list)

import pandas

# data = pandas.read_csv("weather_data.csv")
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#  print(type(data))
#  print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
# einfach durchschnitt ausrechnen
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
# ODER
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
# Get data rows where day is Monday
# print(data[data.day == "Monday"])
# row of hottest day
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_print_f = monday_temp * 9 / 5 + 32
# print(monday_print_f)
# Create Dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# EICHHÖRNCHEN
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
