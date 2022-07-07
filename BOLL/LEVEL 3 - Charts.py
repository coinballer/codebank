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
chartPrice = plotly.express.bar(x=ApiDataFrame.date, y=ApiDataFrame.price_close)
chartPrice.update_traces(marker_color=BOLLColor)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPoints = plotly.express.area(x=ApiDataFrame.date, y=BOLLPoints)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartDaily = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.price_close)
chartDaily.update_traces(line=dict(color="black"))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.bollinger_lower, line=dict(color="red", width=5), name="LOWER"))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.bollinger_middle, line=dict(color="grey", width=5, dash='dash'), name="MIDDLE"))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.bollinger_upper, line=dict(color="green", width=5), name="UPPER"))

#SHOW SCOREBOARD
chartPrice.show()
chartPoints.show()
chartDaily.show()
