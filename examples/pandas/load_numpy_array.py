import pandas as pd

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame
df = pd.read_csv('test.csv')

# https://pandas.pydata.org/pandas-docs/stable/reference/arrays.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy
df.iloc[:,1].to_numpy()
print(df.to_json())
print(df.to_string())
