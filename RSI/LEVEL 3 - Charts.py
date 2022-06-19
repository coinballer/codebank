#TOP SKILL 1: PYTHON CODING - IMPORT AND USE PYTHON LIBRARIES
!pip install plotly
import requests
import plotly.express
import pandas

#TOP SKILL 2: IMPORTING API DATA
getApiData = requests.get("https://coinballer.io/api/pro-daily/APIKEY")
ApiData = getApiData.json()

#TOP SKILL 3: DECLARE AND SET VARIABLES
#Most Recent 150 Days (Slice Data)
NumberofDays = len(ApiData)
ApiData = ApiData[NumberofDays - 150:NumberofDays]
ApiDataFrame = pandas.DataFrame(ApiData)

#TOP SKILL 3: DECLARING VARIABLES (EMPTY BOX)
RSIColor = []

#TOP SKILL 2: SETTING VARIABLES WITH A BASIC LOOP (FILL THE EMPTY BOX)
for i in ApiData:
    if i['rsi'] > 50:
     iRSIColor = 'green'
    else: 
     iRSIColor = 'red'
     RSIColor.append(iRSIColor)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPrice = plotly.express.bar(x=ApiDataFrame.date, y=ApiDataFrame.price_close)
chartPrice.update_traces(marker_color=RSIColor)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPoints = plotly.express.area(x=ApiDataFrame.date, y=ApiDataFrame.rsi)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartDaily = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.rsi)

#SHOW SCOREBOARD
chartPrice.show()
chartPoints.show()
chartDaily.show()
