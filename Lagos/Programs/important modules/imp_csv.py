import csv

""" Sample demonstration for the important module csa"""

with open("names.csv", 'r') as file:
    data = list(csv.reader(file))

print(data)
for name in data[1:]:
    if name[0] == 'Victor':
        print(name[1])