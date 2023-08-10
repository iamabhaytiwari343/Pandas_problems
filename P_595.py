import pandas as pd


def big_countries(data: pd.DataFrame) -> pd.DataFrame:
    big_countries = data[(data['area'] >= 3000000) |
                         (data['population'] >= 25000000)]
    result = big_countries[['name', 'population', 'area']]
    d = pd.DataFrame(result)
    return d
