#TOP SKILL #1: PYTHON CODING - IMPORT AND USE PYTHON LIBRARIES
!pip install plotly
import requests
import plotly.express
import plotly.graph_objects as go
import pandas

#TOP SKILL #2: IMPORTING API DATA
getApiData = requests.get("https://coinballer.io/api/macd-pro/APIKEY")
ApiData = getApiData.json()

#TOP SKILL #3: DECLARE AND SET VARIABLES
#Most Recent 150 Days (Slice Data)
NumberofDays = len(ApiData)
ApiData = ApiData[NumberofDays - 90:NumberofDays]
ApiDataFrame = pandas.DataFrame(ApiData)
MinPrice = min(ApiDataFrame.price_close)
MaxPrice = max(ApiDataFrame.price_close)
MinDate = min(ApiDataFrame.date)
MaxDate = max(ApiDataFrame.date)  

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPrice = plotly.express.bar(x=ApiDataFrame.date, y=ApiDataFrame.price_close,labels={
                     "x": "DATE",
                     "y": "BITCOIN PRICE",
                 })
chartPrice.update_layout(yaxis_range=[MinPrice,MaxPrice], plot_bgcolor='white')
chartPrice.update_traces(marker_color=ApiDataFrame.macd_pro_color)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPoints = plotly.express.area(x=ApiDataFrame.date, y=ApiDataFrame.points, labels={
                     "x": "DATE",
                     "y": "MACD POINTS",
                 })
chartPoints.update_traces(line=dict(color="white", width=5))
chartPoints.update_layout(yaxis_range=[0,100], plot_bgcolor='black')
chartPoints.update_layout(height=400, yaxis=dict(
        tickmode = 'array',
        tickvals = [0, 50, 100],
        ticktext = ['0', '50','100']
    ))
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
chartWeekly = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.weekly_macd_line, labels={
                     "x": "DATE",
                     "y": "MACD LINE",
                 })
chartWeekly.update_traces(line=dict(color="black", width=5))
chartWeekly.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.weekly_signal_line, fill='tozeroy', line=dict(color="#eeaf12", width=5), name="signal"))
chartWeekly.add_trace(go.Bar(x=ApiDataFrame.date, y=ApiDataFrame.weekly_histogram, marker_color="DeepSkyBlue", name="histogram"))
chartWeekly.update_layout(plot_bgcolor='white', showlegend=False)
chartWeekly.update_yaxes(showgrid=False, zeroline=False)
chartWeekly.update_xaxes(showgrid=False, zeroline=False)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartDaily = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.daily_macd_line, labels={
                     "x": "DATE",
                     "y": "MACD LINE",
                 })
chartDaily.update_traces(line=dict(color="black", width=5))
chartDaily.add_trace(go.Scatter(x=ApiDataFrame.date, y=ApiDataFrame.daily_signal_line, fill='tozeroy', line=dict(color="#eeaf12", width=5), name="signal"))
chartDaily.add_trace(go.Bar(x=ApiDataFrame.date, y=ApiDataFrame.daily_histogram, marker_color="DeepSkyBlue", name="histogram"))
chartDaily.update_layout(plot_bgcolor='white', showlegend=False)
chartDaily.update_yaxes(showgrid=False, zeroline=False)
chartDaily.update_xaxes(showgrid=False, zeroline=False)

#SHOW SCOREBOARD
chartPrice.show()
chartPoints.show()
chartWeekly.show()
chartDaily.show()
