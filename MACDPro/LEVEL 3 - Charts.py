#TOP SKILL #1: PYTHON CODING - IMPORT AND USE PYTHON LIBRARIES
!pip install plotly
import requests
import plotly.express
import pandas

#TOP SKILL #2: IMPORTING API DATA
getApiData = requests.get("https://coinballer.io/api/macd-pro/APIKEY")
ApiData = getApiData.json()

#TOP SKILL #3: DECLARE AND SET VARIABLES
#Most Recent 150 Days (Slice Data)
NumberofDays = len(ApiData)
ApiData = ApiData[NumberofDays - 90:NumberofDays]
ApiDataFrame = pandas.DataFrame(ApiData)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPrice = plotly.express.bar(x=ApiDataFrame.date, y=ApiDataFrame.price_close)
chartPrice.update_traces(marker_color=ApiDataFrame.macd_pro_color)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPoints = plotly.express.area(x=ApiDataFrame.date, y=ApiDataFrame.daily_points)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartWeekly = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.daily_macd_line)
chartWeekly.update_traces(line=dict(color="black", width=5))
chartWeekly.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.daily_signal_line, fill='tozeroy', line=dict(color="#eeaf12", width=5), name="signal"))
chartWeekly.add_trace(go.Bar(x=ApiDataFrame.date, y=ApiDataFrame.daily_histogram, marker_color="DeepSkyBlue", name="histogram"))

#TOP SKILL: CREATE A CHART USING PLOTLY
chartDaily = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.daily_macd_line)
chartDaily.update_traces(line=dict(color="black", width=5))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.daily_signal_line, fill='tozeroy', line=dict(color="#eeaf12", width=5), name="signal"))
chartDaily.add_trace(go.Bar(x=ApiDataFrame.date, y=ApiDataFrame.daily_histogram, marker_color="DeepSkyBlue", name="histogram"))

#SHOW SCOREBOARD
chartPrice.show()
chartPoints.show()
chartWeekly.show()
chartDaily.show()
