import csv

with open("files/weather.csv", 'r') as file_r:
    data = list(csv.reader(file_r))

city = input("Enter country: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])