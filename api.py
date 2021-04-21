
'''
Importing Libraries
'''
import pandas as pd
import numpy as np 
import requests
import matplotlib.pyplot as plt
%matplotlib inline

URL = 'https://opendata.arcgis.com/datasets/9fa34e198ad240358c7c36bc063d2058_40.geojson'

data = requests.get(URL)

# print html response object
print(data.request)