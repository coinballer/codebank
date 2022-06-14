#TOP SKILL #1: IMPORT PYTHON LIBRARIES (PYTHON CODING)
import requests
from IPython.display import Image, display
import plotly.express

#TOP SKILL #2: GET API DATA
getApiData = requests.get("https://coinballer.io/api/technical-indicators-daily/62a6542691df4b00521b5dad")
ApiData = getApiData.json()

#TOP SKILL #3: DECLARE AND SET VARIABLES
#Slice ApiData For Most Recent Date (Today)
ApiData_Today = ApiData[-1]
RSI = ApiData_Today['rsi']

#TOP SKILL #4: SIMPLE IF STATEMENT
if RSI > 50:
    GaugeColor = 'green'
else: GaugeColor = 'red'

#TOP SKILL: CREATE A CHART USING PLOTLY
Gauge = plotly.express.bar(x=["RSI Points"], y=[RSI], text=[RSI], labels={
                     "x": "",
                     "y": "RSI Points",
                 })
Gauge.update_traces(marker_color=GaugeColor)
Gauge.update_layout(yaxis_range=[0,100], plot_bgcolor='white', width=300, height=500)
Gauge.update_xaxes(visible=True,showticklabels=False)

#SHOW SCOREBOARD
Gauge.show()
