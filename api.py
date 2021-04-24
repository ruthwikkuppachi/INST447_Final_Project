
'''
Importing Libraries
'''
import pandas as pd
import numpy as np 
import requests
import matplotlib.pyplot as plt

URL = 'https://opendata.arcgis.com/datasets/9fa34e198ad240358c7c36bc063d2058_40.geojson'

data = requests.get(URL)

print(data.status_code)

#RID/Race/offesce type/offense/severity - is the severity of similar crimes the same by race?

#cases by race - how many cases are there per race

#type by age and gender

#Race/offense type/sentence type/sentence imposted month - are sentences given similar for similar crimes by race?