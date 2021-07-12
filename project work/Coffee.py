import pandas as pd
import plotly.express as px
import numpy as num
import csv

def getDataSrc():
    file_data={}
    coffee=[]
    sleep=[]
    with open("Coffee.csv") as f:
        reader = csv.DictReader(f)
        file_data = reader
        for row in file_data:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return {'cof' : coffee , 'sle' : sleep}

def correlation():
    data=getDataSrc()
    correlation = num.corrcoef(data['cof'],data['sle'])
    print("The correlation of the given data is =" , correlation[0][1])

def chart():
    plotData = pd.read_csv('Coffee.csv')
    fig = px.scatter(plotData,x="Coffee in ml",y="sleep in hours")
    fig.show()

correlation()
chart()