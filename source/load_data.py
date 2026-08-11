import csv
# First variant of csv reading
'''def read_hour(filename):
    bikes = []

    with open(filename, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(",")

            bike = (
                parts[0],
                parts[1],
                parts[2],
                parts[3],
                parts[4],
                parts[5],
                parts[6],
                parts[7],
                parts[8],
                parts[9],
                parts[10],
                parts[11],
                parts[12],
                parts[13],
                parts[14],
                parts[15],
                parts[16],
            )

            bikes.append(bike)

    return bikes'''

def read_hours(filename):
    bikes=[]
    with open(filename, encoding="utf-8") as file:
        reader=csv.DictReader(file)
        for row in reader:
            bikes.append(row)
    return row
