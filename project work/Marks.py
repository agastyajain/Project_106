import pandas as pd
import plotly.express as px
import numpy as num
import csv

def getDataSrc():
    file_data={}
    days=[]
    marks=[]
    with open("Marks.csv") as f:
        reader = csv.DictReader(f)
        file_data = reader
        for row in file_data:
            days.append(float(row['Days Present']))
            marks.append(float(row['Marks In Percentage']))
    return {'day' : days , 'per' : marks}

def correlation():
    data=getDataSrc()
    correlation = num.corrcoef(data['day'],data['per'])
    print("The correlation of the given data is =" , correlation[0][1])

def chart():
    plotData = pd.read_csv('Marks.csv')
    fig = px.scatter(plotData,x="Days Present",y="Marks In Percentage")
    fig.show()

correlation()
chart()