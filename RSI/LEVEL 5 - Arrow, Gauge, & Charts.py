#TOP SKILL 1: PYTHON CODING - IMPORT AND USE PYTHON LIBRARIES
!pip install plotly
import requests
import plotly.express
import pandas
from IPython.display import Image, display

#TOP SKILL 2: IMPORTING API DATA
getApiData = requests.get("https://coinballer.io/api/pro-daily/APIKEY")
ApiData = getApiData.json()

#TOP SKILL 3: DECLARE AND SET VARIABLES
#Slice ApiData For Most Recent Date (Today)
ApiData_Today = ApiData[-1]
RSI = ApiData_Today['rsi']
if RSI > 90:
  RSIPoints = 100
elif RSI < 10:
  RSIPoints = 0
else: 
  RSIPoints = round(((RSI - 10) / 80) * 100, 1)

#TOP SKILL 4: SIMPLE IF STATEMENT
if RSI > 50:
    Arrow = 'https://i.imgur.com/aCTsoA0.png'
else: Arrow = 'https://i.imgur.com/8Li7d4A.png'

#TOP SKILL 4: SIMPLE IF STATEMENT
if RSI > 50:
    GaugeColor = 'green'
else: GaugeColor = 'red'

#TOP SKILL: CREATE A CHART USING PLOTLY
Gauge = plotly.express.bar(x=["RSI Points"], y=[RSIPoints], text=[RSIPoints], labels={
                     "x": "",
                     "y": "RSI Points",
                 })
Gauge.update_traces(marker_color=GaugeColor)
Gauge.update_layout(yaxis_range=[0,100], plot_bgcolor='white', width=300, height=500)
Gauge.update_xaxes(visible=True,showticklabels=False)

#TOP SKILL 3: DECLARE AND SET VARIABLES
#Most Recent 150 Days (Slice Data)
NumberofDays = len(ApiData)
ApiData = ApiData[NumberofDays - 90:NumberofDays]
ApiDataFrame = pandas.DataFrame(ApiData)

#TOP SKILL 3: DECLARING VARIABLES (EMPTY BOX)
RSIColor = []
RSIPoints = []

#TOP SKILL 2: SETTING VARIABLES WITH A BASIC LOOP (FILL THE EMPTY BOX)
for i in ApiData:
    if i['rsi'] > 50:
     iRSIColor = 'green'
    else: 
     iRSIColor = 'red'
    RSIColor.append(iRSIColor)
    if i['rsi'] > 90:
     iRSIPoints = 100
    elif i['rsi'] < 10:
     iRSIPoints = 0
    else: 
     iRSIPoints = round(((i['rsi'] - 10) / 80) * 100, 1)
    RSIPoints.append(iRSIPoints)

MinPrice = min(ApiDataFrame.price_close)
MaxPrice = max(ApiDataFrame.price_close) 
MinDate = min(ApiDataFrame.date)
MaxDate = max(ApiDataFrame.date) 

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPrice = plotly.express.bar(x=ApiDataFrame.date, y=ApiDataFrame.price_close, labels={
                     "x": "DATE",
                     "y": "BITCOIN PRICE",
                 })
chartPrice.update_layout(yaxis_range=[MinPrice,MaxPrice], plot_bgcolor='white')
chartPrice.update_traces(marker_color=RSIColor)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPoints = plotly.express.area(x=ApiDataFrame.date, y=RSIPoints, labels={
                     "x": "DATE",
                     "y": "RSI POINTS",
                 })
chartPoints.update_layout(yaxis_range=[0,100], plot_bgcolor='black')
chartPoints.update_layout(height=400, yaxis=dict(
        tickmode = 'array',
        tickvals = [0, 50, 100],
        ticktext = ['0', '50','100']
    ))
chartPoints.update_traces(line=dict(color="white", width=5))
chartPoints.update_yaxes(showgrid=False, zeroline=False)
chartPoints.update_xaxes(showgrid=False, zeroline=False)
chartPoints.add_shape(type="rect",
    x0=MinDate, y0=50, x1=MaxDate, y1=100,
    line=dict(
        color="green",
        width=2,
    ),
    fillcolor="green", opacity=0.6,
)
chartPoints.add_shape(type="rect",
    x0=MinDate, y0=50, x1=MaxDate, y1=00,
    line=dict(
        color="red",
        width=2,
    ),
    fillcolor="red", opacity=0.6,
)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartDaily = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.rsi, labels={
                     "x": "DATE",
                     "y": "RSI",
                 })
chartDaily.update_traces(line=dict(color="white", width=5), name="rsi")
chartDaily.add_hline(y=70, line_color="green")
chartDaily.add_hline(y=30, line_color="red")
chartDaily.update_yaxes(showgrid=False, zeroline=False)
chartDaily.update_layout(yaxis_range=[10,90], plot_bgcolor='black', yaxis=dict(
        tickmode = 'array',
        tickvals = [10, 30, 50, 70, 90],
        ticktext = ['10', '30','50','70', '90']
    ))
chartDaily.update_xaxes(showgrid=False, zeroline=False)
chartDaily.add_shape(type="rect",
    x0=MinDate, y0=50, x1=MaxDate, y1=90,
    line=dict(
        color="green",
        width=2,
    ),
    fillcolor="green", opacity=0.6,
)
chartDaily.add_shape(type="rect",
    x0=MinDate, y0=50, x1=MaxDate, y1=10,
    line=dict(
        color="red",
        width=2,
    ),
    fillcolor="red", opacity=0.6,
)

#SHOW SCOREBOARD
print("RSI", RSI)
display(Image(Arrow, width = 150, height = 150))
Gauge.show()
chartPrice.show()
chartPoints.show()
chartDaily.show()
