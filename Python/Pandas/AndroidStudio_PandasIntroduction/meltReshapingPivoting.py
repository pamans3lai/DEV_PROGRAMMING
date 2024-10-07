import pandas as pd 

#Sample DataFrame (wide format)

data = {
    "ID": [1, 2, 3],
    "Temperature": [23,21,25],
    "Humidity": [45, 50, 40]
}

df = pd.DataFrame(data)

print("Original Data Frame (wide format):")
print(df)

melted_df = pd.melt(
    df, id_vars="ID", value_vars=["Temperature", "Humidity"], var_name="Variable", value_name="Value"
)

print("\Melted Data Frame (long format):")
print(melted_df)

udara = {
    "ID": [1, 2, 3, 1, 2, 3],
    "Variable": ["Temperature", "Temperature", "Temperature", "Humidity", "Humidity", "Humidity"],
    "Value": [23, 21, 25, 45, 50, 40],
}

ud =pd.DataFrame(udara)

print("Original Data Frame (format panjang):")
print(ud)

#membuat pivot data

pivoted_ud = ud.pivot(index="ID", 
                      columns="Variable", values="Nilai")

print(pivoted_ud)

