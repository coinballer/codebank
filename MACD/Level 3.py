#TOP SKILL #1: PYTHON CODING - IMPORT AND USE PYTHON LIBRARIES
!pip install plotly
import requests
import plotly.express
import pandas

#TOP SKILL #2: IMPORTING API DATA
getApiData = requests.get("https://coinballer.io/api/technical-indicators-daily/APIKEY")
ApiData = getApiData.json()

#TOP SKILL #3: DECLARE AND SET VARIABLES
#Most Recent 150 Days (Slice Data)
NumberofDays = len(ApiData)
ApiData = ApiData[NumberofDays - 150:NumberofDays]
ApiDataFrame = pandas.DataFrame(ApiData)

#TOP SKILL #3: DECLARING VARIABLES (EMPTY BOX)
MACDColor = []

#TOP SKILL #2: SETTING VARIABLES WITH A BASIC LOOP (FILL THE EMPTY BOX)
for i in ApiData:
    if i['daily_points'] > 50:
     iMACDColor = 'green'
    else: 
     iMACDColor = 'red'
     MACDColor.append(iMACDColor)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPrice = plotly.express.bar(x=ApiDataFrame.date, y=ApiDataFrame.price_close)
chartPrice.update_traces(marker_color=MACDColor)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPoints = plotly.express.area(x=ApiDataFrame.date, y=ApiDataFrame.daily_points)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartDaily = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.daily_macd_line, labels={
                     "x": "DATE",
                     "y": "MACD LINE",
                 })
chartDaily.update_traces(line=dict(color="black", width=5))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.daily_signal_line, fill='tozeroy', line=dict(color="#eeaf12", width=5), name="signal"))
chartDaily.add_trace(go.Bar(x=ApiDataFrame.date, y=ApiDataFrame.daily_histogram, marker_color="DeepSkyBlue", name="histogram"))

#SHOW SCOREBOARD
chartPrice.show()
chartPoints.show()
chartDaily.show()
