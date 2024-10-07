import pandas as pd

titanic = pd.read_csv("/home/ai/DEV_PROGRAMMING/Python/Pandas/in_doc/titanic.csv")

#print(titanic)

air_quality = pd.read_csv("/home/ai/DEV_PROGRAMMING/Python/Pandas/in_doc/air_quality_long.csv")

#print(air_quality.head())

titanic.sort_values(by="Age").head()

titanic.sort_values(by=["Age", "Pclass"], ascending=False).head()

#print(air_quality)

no2 = air_quality[air_quality["parameter"] == "no2"]
no2_subset = no2.sort_index().groupby(["location"]).head(2)

#print(no2)

# :with expression as target:
# print(air_quality.head()
#
#print(no2.head())

no2_subset.pivot(columns="location", values="value").plot()
#print(no2.head())

no2.pivot(columns="location", values="value").plot()

air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins="True",
)

air_quality.groupby(["parameter", "location"])[["value"]].mean()

no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

print(no2_pivoted.head())

no_2 = no2_pivoted.melt(id_vars="date.utc")

print(no_2.head())



no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)


print(no_2.head())
