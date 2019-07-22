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
# Goals:
# 1) Load a CSV file into a Pandas dataframe, and load the second column as a NumPy array
# 2) Dump the contents of the dataframe as JSON
# 3) Dump the contents of the dataframe as a string (i.e. in a console-friendly tabular output)
# 
# Source Code:
#
# On Github
# https://github.com/intltechventures/Lab.Python/blob/master/examples/pandas/load_numpy_array.py
#
# test.csv
# https://github.com/intltechventures/Lab.Python/blob/master/examples/pandas/test.csv
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

import pandas as pd


#*****************************************************************************
# Useful background reading/references on read_csv() processing...
# NOTE: The test.csv file has UTF-8 encoded characters - which will result in an error when trying to print to_string() - if you don't specify an encoding of 'mbcs' on the read_csv()
#
# https://docs.python.org/3/library/codecs.html#standard-encodings
# NOTE: mbcs: "Windows only: Encode operand according to the ANSI codepage (CP_ACP)"
#
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame
# https://jrogel.com/python-3-pandas-encoding-issues/
# https://stackoverflow.com/questions/30462807/encoding-error-in-panda-read-csv
# https://stackoverflow.com/questions/18171739/unicodedecodeerror-when-reading-csv-file-in-pandas-with-python
# https://www.datacamp.com/community/tutorials/pandas-read-csv
# https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
#
df = pd.read_csv('test.csv', encoding='mbcs')


#*****************************************************************************
# https://pandas.pydata.org/pandas-docs/stable/reference/arrays.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy
#
df.iloc[:,1].to_numpy()


#*****************************************************************************
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json
#
print(df.to_json())

#*****************************************************************************
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string
#
print(df.to_string())
