import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df = world[(world['area'] >= 300000 | (world['population'] >= 2500000)]
    return df[['name', 'population', 'area']]

