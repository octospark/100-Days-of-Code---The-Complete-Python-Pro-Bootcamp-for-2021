#
#
# with open("weather_data.csv", 'r') as file:
#     data = file.readlines()
#
# print(data)
# import csv
#
# with open("weather_data.csv", 'r') as data_file:
#     data = list(csv.reader(data_file))
#     temperatures = []
#     for row_index in range(1, len(data)):
#         temperature = int(data[row_index][1])
#         temperatures.append(temperature)
#     print(temperatures)


# data = pandas.read_csv("weather_data.csv")
# temperatures = data["temp"].mean()
# max_temp = data["temp"].max()
# print(temperatures)
# print(max_temp)
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp * 9 / 5 + 32)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
new_dict = {"Fur Color":[], "Count":[]}

for entry in data["Primary Fur Color"].to_list():
    if isinstance(entry, str):
        if entry in new_dict["Fur Color"]:
            new_dict["Count"][new_dict["Fur Color"].index(entry)] += 1
        else:
            new_dict["Fur Color"].append(entry)
            new_dict["Count"].append(1)

new_data = pandas.DataFrame(new_dict)
new_data.to_csv("new_data.csv")
new_data = pandas.read_csv("new_data.csv")
print(new_data)
