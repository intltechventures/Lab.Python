#*****************************************************************************
# load_numpy_array.py 
#
# Inspired to explore this simple problem, based on this LinkedIn post:
# https://www.linkedin.com/feed/update/urn:li:activity:6559093931026509824
#
# ...and Vaibhav Desai's (https://www.linkedin.com/in/vaibhav-desai-8b0ba8b6/)
# elegant answer 
# https://www.linkedin.com/feed/update/urn:li:activity:6559093931026509824?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A6559093931026509824%2C6559100506214625280%29
#
#
# Source Code:
#
# On Github
# https://github.com/intltechventures/Lab.Python/blob/master/examples/pandas/load_numpy_array.py
#
# test.csv
# https://github.com/intltechventures/Lab.Python/blob/master/examples/pandas/test.csv
# First row includes column headers
# Columns (numbered based on Python indexing):
#    0 - Greeting
#    1 - Language
#    2 - Country
#    3 - Currency Conversion Rate, as of 2019-07-22
#
# Goals:
# 1) Load a CSV file into a Pandas dataframe, and experiment with methods to transform the fourth column (Currency Conversion Rate) to a NumPy array
# 2) Experiment with loading UTF-8 encoded mixed character set data, and...
# 3) Dump the contents of the dataframe as JSON
# 4) Dump the contents of the dataframe as a string (i.e. in a console-friendly tabular output)
#
#
# International Technology Ventures, Inc.
# https://www.intltechventures.com
#
# Author: Kelvin D. Meeks
# Email: kmeeks@intltechventures.com 
#
# Created: 2019-07-22
#*****************************************************************************
#
import pandas as pd


#*****************************************************************************
# Program Start
#
print("\n\nProgram Start: load_numpy_array.py\n")



#*****************************************************************************
# Useful background reading/references on read_csv() processing...
# NOTE: The test.csv file has some UTF-8 encoded entries with characters (e.g. `Dzień Dobry`) - which will result in an error when trying to print to_string() - if you don't specify an encoding of 'mbcs' on the read_csv()
#
# https://docs.python.org/3/library/codecs.html#standard-encodings
# NOTE: mbcs: "Windows only: Encode operand according to the ANSI codepage (CP_ACP)"
#
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame
#
# https://www.datacamp.com/community/tutorials/python-numpy-tutorial
# https://www.datacamp.com/community/tutorials/pandas-read-csv
#
# https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
#
# https://medium.com/@ericvanrees/pandas-series-objects-and-numpy-arrays-15dfe05919d7
# 
# https://jrogel.com/python-3-pandas-encoding-issues/
# 
# https://stackoverflow.com/questions/30462807/encoding-error-in-panda-read-csv
# https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python
#
df = pd.read_csv('test.csv', encoding='mbcs')

print("\n\ndf, 4th column, Before:\n", df.iloc[:,3])


#*****************************************************************************
# https://pandas.pydata.org/pandas-docs/stable/reference/arrays.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy
#


#****************************************************************************
# Although you might consider using .values, note the v0.24.0 release notes comment:
#   "We haven’t removed or deprecated Series.values or DataFrame.values, but we highly recommend and using .array or .to_numpy() instead."
#   https://pandas-docs.github.io/pandas-docs-travis/whatsnew/v0.24.0.html#accessing-the-values-in-a-series-or-index
#
print("\n\nUsing .to_numpy():\n", df.iloc[:,3].to_numpy())

print("\n\nUsing .array:\n", df.iloc[:,3].array)


print("\n\nUsing .values:\n", df.iloc[:,3].values)


# TO-DO: Some additional ideas to explore...
#   https://stackoverflow.com/questions/17241004/how-do-i-convert-a-pandas-series-or-index-to-a-numpy-array/54324513#54324513
#   https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array
#




print("\n\ndf, 4th column, After:\n", df.iloc[:,3])


#*****************************************************************************
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json
#
print("\n\n.to_json():\n", df.to_json())


#*****************************************************************************
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string
#
print("\n\n.to_string():\n", df.to_string())


#*****************************************************************************
# Program End
#
print("\n\nProgram End: load_numpy_array.py\n")

