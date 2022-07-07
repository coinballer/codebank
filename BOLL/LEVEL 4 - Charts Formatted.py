#TOP SKILL 1: PYTHON CODING - IMPORT AND USE PYTHON LIBRARIES
!pip install plotly
import requests
import plotly.express
import plotly.graph_objects as go
import pandas

#TOP SKILL 2: IMPORTING API DATA
getApiData = requests.get("https://coinballer.io/api/pro-daily/APIKEY")
ApiData = getApiData.json()

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
chartDaily.update_traces(line=dict(color="black", width=5))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.bollinger_lower, line=dict(color="red", width=5), name="LOWER"))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.bollinger_middle, line=dict(color="grey", width=5, dash='dash'), name="MIDDLE"))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.bollinger_upper, line=dict(color="green", width=5), name="UPPER"))
chartDaily.update_yaxes(showgrid=False, zeroline=False)
chartDaily.update_layout(yaxis_range=[MinPrice,MaxPrice], plot_bgcolor='white', showlegend=False)
chartDaily.update_xaxes(showgrid=False, zeroline=False)

#SHOW SCOREBOARD
chartPrice.show()
chartPoints.show()
chartDaily.show()
