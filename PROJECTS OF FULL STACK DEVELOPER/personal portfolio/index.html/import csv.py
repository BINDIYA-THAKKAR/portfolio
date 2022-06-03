import csv
with open('compton 30.csv', 'r') as csvfile:
rows = csv.reader(csvfile)
for row in rows:
print(row)