from source.load_data import (
    read_csv, 
    count_rows,
    count_col,
    name_col,
    missing_values, 
    get_column_types
)
from source.validate_data import (
    convert_row,
    validate_count,
    validate_hour,
    validate_month,
    validate_season,
    validate_weather,
    validate_total_count,
)


def validate_row(row):
    return (
        validate_count(row["cnt"]) and validate_hour(row["hr"])
        and validate_month(row["mnth"]) and validate_season(row["season"])
        and validate_weather(row["weathersit"]) and validate_total_count(
        row["casual"], row["registered"], row["cnt"],)
    )


hour_data = read_csv("data/raw/hour.csv")
print(count_rows(hour_data))
print(count_col(hour_data))
print(name_col(hour_data))
print(missing_values(hour_data))
print(get_column_types())
row = convert_row(hour_data[0])
print(row)
print(validate_row(row))