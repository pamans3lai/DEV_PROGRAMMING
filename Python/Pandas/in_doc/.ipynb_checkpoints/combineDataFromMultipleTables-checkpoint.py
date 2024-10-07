import pandas as pd

air_quality_no2 = pd.read_csv("/home/ai/DEV_PROGRAMMING/Python/Pandas/in_doc/air_quality_no2_long.csv", parse_dates=True)

air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]


print(air_quality_no2.head())

air_quality_pm25 = pd.read_csv("/home/ai/DEV_PROGRAMMING/Python/Pandas/in_doc/air_quality_pm25_long.csv", parse_dates=True)

air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]

print(air_quality_pm25.head())

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)

print(air_quality.head())

print('Shape of the ``air_quality_pm25`` table: ', air_quality_pm25.shape)

print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)

print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)


air_quality = air_quality.sort_values("date.utc")

print(air_quality.head())               


air_quality_ = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])

print(air_quality_.head())