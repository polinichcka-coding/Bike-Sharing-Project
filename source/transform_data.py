def time_of_day(hour):
    if 5<=hour<12:
        return "Morning"
    elif 12<=hour<17:
        return "Afternoon"
    elif 17<=hour<22:
        return "Evening"
    else:
        return "Night"

def rush_hour(workingday, hr):
    rush_hour=[]
    for day, hr in zip(workingday, hr):
        if day==1 and ((7<=hr<=9) or (17<=hr<=19)):
            rush_hour.append(1)
        else:
            rush_hour.append(0)
    return rush_hour

def demand(count, median):
    if count>median:
        return 1
    return 0

def add_features(data):
    data=data.copy()
    data["time_of_day"]=data["hr"].apply(time_of_day)
    median=data["cnt"].median()
    data["high_demand"]=data["cnt"].apply(lambda count: demand(count, median))
    data["rush_hour"]=rush_hour(data["workingday"], data["hr"])
    return data
