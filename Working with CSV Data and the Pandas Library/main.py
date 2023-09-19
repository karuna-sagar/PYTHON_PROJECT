# with open("Day_25 Working with CSV Data and the Pandas Library/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
# with open("Day_25 Working with CSV Data and the Pandas Library/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
import math
import pandas
# data = pandas.read_csv("Day_25 Working with CSV Data and the Pandas Library/weather_data.csv")
# print(data)
# print(data["temp"])
# list = data["temp"].to_list()
# print(list)
# list_len = len(list)
# print(list_len)
# sum = 0
# for item in list:
#     sum +=item
#     avg = sum/list_len
# print(avg)


############################# ************** bawaal cheez hai bc****************
# print(data["temp"].mean())
# print(data.condition) 
# print(data[data.day == "Monday"])
# print(data[data.temp==data.temp.max()])


# create a dataframe from scratch 

# data_dict ={
#     "student" : ["Amy","James","Angela"],
#     "scores" : [50,30,62]
# } 
# data = pandas.DataFrame(data_dict)
# print(data)

# data.to_csv("new_Data.csv")


data = pandas.read_csv("Day_25 Working with CSV Data and the Pandas Library/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrel = data[data["Primary Fur Color"]=="Gray"]
# print(grey_s quirrel)
cinnamon_squirrel_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
print(cinnamon_squirrel_count)
Black_squirrel_count = len(data[data["Primary Fur Color"]=="Black"])
print(Black_squirrel_count)
grey_squirrel_count = len(data[data["Primary Fur Color"]=="Gray"])
print(grey_squirrel_count)

data_dict = {
    "Fur Color":["Gray","Cinnamon","Red"],
    "Count" : [grey_squirrel_count,Black_squirrel_count,cinnamon_squirrel_count]
}
# print(data_dict)
# df = pandas.DataFrame(data_dict)
# df.to_csv("Squirrel_count.csv")

