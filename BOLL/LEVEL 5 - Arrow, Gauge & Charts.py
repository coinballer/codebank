#TOP SKILL 1: PYTHON CODING - IMPORT AND USE PYTHON LIBRARIES
!pip install plotly
import requests
import plotly.express
import plotly.graph_objects as go
import pandas
from IPython.display import Image, display

#TOP SKILL 2: IMPORTING API DATA
getApiData = requests.get("https://coinballer.io/api/pro-daily/APIKEY")
ApiData = getApiData.json()

#TOP SKILL 3: DECLARE AND SET VARIABLES
#Slice ApiData For Most Recent Date (Today)
ApiData_Today = ApiData[-1]
BollingerUpper = ApiData_Today['bollinger_upper']
BollingerMiddle = ApiData_Today['bollinger_middle']
BollingerLower = ApiData_Today['bollinger_lower']
BitcoinPrice = ApiData_Today['price_close']
BollingerSpread = BollingerUpper - BollingerLower
BollingerPriceSpread = BitcoinPrice - BollingerLower

#TOP SKILL 4: SIMPLE IF STATEMENT
if BitcoinPrice > BollingerUpper:
    BollingerPoints = 100
else: 
  if BitcoinPrice < BollingerLower:
    BollingerPoints = 0
  else: BollingerPoints = round(BollingerPriceSpread / BollingerSpread, 1) * 100

#TOP SKILL 4: SIMPLE IF STATEMENT
if BitcoinPrice > BollingerMiddle:
    Arrow = 'https://i.imgur.com/aCTsoA0.png'
else: Arrow = 'https://i.imgur.com/8Li7d4A.png'
  
#TOP SKILL 4: SIMPLE IF STATEMENT
if BitcoinPrice > BollingerMiddle:
    GaugeColor = 'green'
else: GaugeColor = 'red'

#TOP SKILL: CREATE A CHART USING PLOTLY
Gauge = plotly.express.bar(x=["BOLL Points"], y=[BollingerPoints], text=[BollingerPoints], labels={
                     "x": "",
                     "y": "BOLL Points",
                 })
Gauge.update_traces(marker_color=GaugeColor)
Gauge.update_layout(yaxis_range=[0,100], plot_bgcolor='white', width=300, height=500)
Gauge.update_xaxes(visible=True,showticklabels=False)

#TOP SKILL 3: DECLARE AND SET VARIABLES
#Most Recent 150 Days (Slice Data)
NumberofDays = len(ApiData)
ApiData = ApiData[NumberofDays - 90:NumberofDays]
ApiDataFrame = pandas.DataFrame(ApiData)
MinPrice = min(ApiDataFrame.price_close)
MaxPrice = max(ApiDataFrame.price_close) 
MinDate = min(ApiDataFrame.date)
MaxDate = max(ApiDataFrame.date) 

#TOP SKILL 3: DECLARING VARIABLES (EMPTY BOX)
BOLLColor = []
BOLLPoints = []

#TOP SKILL 2: SETTING VARIABLES WITH A BASIC LOOP (FILL THE EMPTY BOX)
for i in ApiData:
    iBollingerUpper = i['bollinger_upper']
    iBollingerMiddle = i['bollinger_middle']
    iBollingerLower = i['bollinger_lower']
    iBitcoinPrice = i['price_close']
    iBollingerSpread = iBollingerUpper - iBollingerLower
    iBollingerPriceSpread = iBitcoinPrice - iBollingerLower
    if iBitcoinPrice >  iBollingerMiddle:
      iBOLLColor = 'green'
    else: 
      iBOLLColor = 'red'
    BOLLColor.append(iBOLLColor)
    #TOP SKILL 4: SIMPLE IF STATEMENT
    if iBitcoinPrice > iBollingerUpper:
      iBollingerPoints = 100
    else: 
    if iBitcoinPrice < iBollingerLower:
      iBollingerPoints = 0
    else: iBollingerPoints = round(iBollingerPriceSpread / iBollingerSpread, 1) * 100
    BOLLPoints.append(iBollingerPoints)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPrice = plotly.express.bar(x=ApiDataFrame.date, y=ApiDataFrame.price_close, labels={
                     "x": "DATE",
                     "y": "BITCOIN PRICE",
                 })
chartPrice.update_layout(yaxis_range=[MinPrice,MaxPrice], plot_bgcolor='white')
chartPrice.update_traces(marker_color=BOLLColor)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPoints = plotly.express.area(x=ApiDataFrame.date, y=BOLLPoints, labels={
                     "x": "DATE",
                     "y": "BOLL POINTS",
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
    x0=MinDate, y0=50, x1=MaxDate, y1=0,
    line=dict(
        color="red",
        width=2,
    ),
    fillcolor="red", opacity=0.6,
)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartDaily = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.price_close)
chartDaily.update_traces(line=dict(color="black" width=5))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.bollinger_lower, line=dict(color="red", width=5), name="LOWER"))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.bollinger_middle, line=dict(color="grey", width=5, dash='dash'), name="MIDDLE"))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.bollinger_upper, line=dict(color="green", width=5), name="UPPER"))
chartDaily.update_yaxes(showgrid=False, zeroline=False)
chartDaily.update_layout(yaxis_range=[MinPrice,MaxPrice], plot_bgcolor='white', showlegend=False)
chartDaily.update_xaxes(showgrid=False, zeroline=False)

#SHOW SCOREBOARD
print("BOLL", BollingerPoints)
display(Image(Arrow, width = 150, height = 150))
Gauge.show()
chartPrice.show()
chartPoints.show()
chartDaily.show()
