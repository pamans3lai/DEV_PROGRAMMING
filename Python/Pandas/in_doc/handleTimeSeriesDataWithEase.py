# https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html

import pandas as pd 
import matplotlib.pyplot as plt 

air_quality = pd.read_csv("/home/ai/DEV_PROGRAMMING/Python/Pandas/in_doc/air_quality_no2_long.csv")

air_quality = air_quality.rename(columns={"date.utc": "datetime"})

print(air_quality.head())

print(air_quality.city.unique())


print(air_quality.country.unique())

air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])

air_qualtiy["datetime"]

 

pd.read_csv("/home/ai/DEV_PROGRAMMING/Python/Pandas/in_doc/air_quality_no2_long.csv", parse_dates="[datetime"])

air_quality["datetime"].min(), air_quality["datetime"].max()


air_quality["datetime"].min() - air_quality["datetime"].max()
