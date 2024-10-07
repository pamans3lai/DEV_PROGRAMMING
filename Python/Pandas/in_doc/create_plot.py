import pandas as pd
import matplotlib.pyplot as plt

# https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html

air_quality = pd.read_csv("/home/ai/DEV_PROGRAMMING/Python/Pandas/in_doc/air_quality_no2.csv", index_col=0, parse_dates=True)

print(air_quality)

air_quality.plot()
# plt.show()

air_quality["station_paris"].plot()
plt.show()

