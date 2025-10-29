import pandas as pd

'''read JSON'''

df=pd.read_json('json_data.json')
print(df)
#print(df.to_string())

pd.options.display.max_rows=999
print(df)

'''
json=python dictionary
JSON objects have same format as python dictionaries
'''