import pytest
import pandas as pd
from source.transform_data import(
    time_of_day,
    rush_hour, 
    demand,
    add_features
)
def test_time_of_day():
    assert time_of_day(12) == "Afternoon"
    assert time_of_day(23) == "Night" 
    assert time_of_day(10)!="Evening"

def test_rush_hour():
    working_days=[1,1,1,0]
    hours=[8, 12, 18, 8]
    expected=[1,0,1,0]
    assert rush_hour(working_days, hours)==expected

def tests_demand():
    count=10
    median=9
    assert demand(10, 9)==1

def test_add_features():
    input=pd.DataFrame({
        "hr": [8,18,23],
        "cnt": [10,30,100],
        "workingday": [1,1,0]
    })
    result=add_features(input)
    assert "time_of_day" in result.columns
    assert "high_demand" in result.columns
    assert "rush_hour" in result.columns
    assert list(result["time_of_day"]) == ["Morning", "Evening", "Night"]
    assert list(result["high_demand"]) == [0, 0, 1]
    assert list(result["rush_hour"]) == [1, 1, 0]