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

def read_csv(filename):
    bikes=[]
    with open(filename, encoding="utf-8") as file:
        reader=csv.DictReader(file)
        for row in reader:
            bikes.append(row)
    return bikes

hour_data = read_csv("data/raw/hour.csv")
day_data = read_csv("data/raw/day.csv")

def count_rows(data):
    count=0
    for row in data:
        count+=1
    return count

def count_col(data):
    if not data:
        return 0
    return len(data[0])

def name_col(data):
    if not data:
        return []
    return list(data[0].keys())

def missing_values(data):
    count=0
    for row in data:
        for value in row.values():
            if value=="":
                count+=1
    return count


def get_column_types():
    categorical = [
        "season",
        "yr",
        "mnth",
        "hr",
        "holiday",
        "weekday",
        "workingday",
        "weathersit",
    ]
    numerical = [
        "temp",
        "atemp",
        "hum",
        "windspeed",
        "casual",
        "registered",
        "cnt",
    ]
    date = ["dteday"]
    identifier = ["instant"]
    return categorical, numerical, date, identifier


