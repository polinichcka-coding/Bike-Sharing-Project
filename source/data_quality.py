from load_data import (
    read_csv, 
    count_rows,
    count_col,
    name_col,
    missing_values, 
    get_column_types
)
from validate_data import (
    convert_row,
    validate_count,
    validate_hour,
    validate_month,
    validate_season,
    validate_weather,
    validate_total_count,
)

data = read_csv("data/raw/hour.csv")
def report(data):
    print("Data Quality Report")
    print(f"Number of rows: {count_rows(data)}")
    print(f"Number of columns: {count_col(data)}")
    print(f"Missing values: {missing_values(data)}")
    invalid_hour=0
    invalid_month=0
    invalid_season=0
    invalid_weather=0
    invalid_total_count=0
    inv_row=0
    list_inv_hr=[]
    for row in data:
        try:
            d=convert_row(row)
        except ValueError:
            inv_row+=1
            continue
        if validate_hour(d["hr"])==False:
                list_inv_hr.append(d["hr"])
        if validate_season(d["season"])==False:
                invalid_season+=1
        if validate_month(d["mnth"])==False:
                invalid_month+=1
        if validate_weather(d["weathersit"])==False:
                invalid_weather+=1
        if validate_total_count(d["casual"], d["registered"], d["cnt"])==False:
                invalid_total_count+=1


    return {
        "rows": count_rows(data),
        "columns": count_col(data),
        "missing": missing_values(data),
        "invalid_hours": len(list_inv_hr),
        "invalid_months": invalid_month,
        "invalid_seasons": invalid_season,
        "invalid_weather": invalid_weather,
        "invalid_total_counts": invalid_total_count,
        "conversion_errors": inv_row,
    }

result = report(data)

print("Data Quality Report")
print(f"Rows: {result['rows']}")
print(f"Columns: {result['columns']}")
print(f"Missing values: {result['missing']}")
print(f"Invalid hours: {result['invalid_hours']}")
print(f"Invalid months: {result['invalid_months']}")
print(f"Invalid seasons: {result['invalid_seasons']}")
print(f"Invalid weather: {result['invalid_weather']}")
print(f"Invalid total counts: {result['invalid_total_counts']}")
print(f"Conversion errors: {result['conversion_errors']}")