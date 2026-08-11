def convert_row(row):
    return {
        "instant": int(row["instant"]),
        "dteday": row["dteday"],
        "season": int(row["season"]),
        "yr": int(row["yr"]),
        "mnth": int(row["mnth"]),
        "hr": int(row["hr"]),
        "holiday": int(row["holiday"]),
        "weekday": int(row["weekday"]),
        "workingday": int(row["workingday"]),
        "weathersit": int(row["weathersit"]),
        "temp": float(row["temp"]),
        "atemp": float(row["atemp"]),
        "hum": float(row["hum"]),
        "windspeed": float(row["windspeed"]),
        "casual": int(row["casual"]),
        "registered": int(row["registered"]),
        "cnt": int(row["cnt"]),
    }


def validate_count(count):
    return count>=0

def validate_hour(hour):
    return 0<=hour<=23

def validate_month(month):
    return 1<=month<=12

def validate_season(season):
    return season in {1,2,3,4}

def validate_weather(weather):
    return weather in {1,2,3,4}

def validate_total_count(casual, registered, count):
    return casual+registered==count