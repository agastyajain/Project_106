import pandas as pd
import plotly.express as px
import numpy as num
import csv

def getDataSrc():
    file_data={}
    temperature=[]
    icecream=[]
    with open("IceCream.csv") as f:
        reader = csv.DictReader(f)
        file_data = reader
        for row in file_data:
            temperature.append(float(row['Temperature']))
            icecream.append(float(row['Ice-cream Sales']))
    return {'tem' : temperature , 'ice' : icecream}

def correlation():
    data=getDataSrc()
    correlation = num.corrcoef(data['tem'],data['ice'])
    print("The correlation of the given data is =" , correlation[0][1])

correlation()