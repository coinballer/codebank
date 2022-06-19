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
WLPR = ApiData_Today['wlpr']
WLPRPoints = 100 + ApiData_Today['wlpr']

#TOP SKILL 4: SIMPLE IF STATEMENT
if WLPR > -50:
    Arrow = 'https://i.imgur.com/aCTsoA0.png'
else: Arrow = 'https://i.imgur.com/8Li7d4A.png'

#TOP SKILL #4: SIMPLE IF STATEMENT
if WLPR > -50:
    GaugeColor = 'green'
else: GaugeColor = 'red'

#TOP SKILL: CREATE A CHART USING PLOTLY
Gauge = plotly.express.bar(x=["WLPR Points"], y=[WLPRPoints], text=[WLPRPoints], labels={
                     "x": "",
                     "y": "WLPR Points",
                 })
Gauge.update_traces(marker_color=GaugeColor)
Gauge.update_layout(yaxis_range=[0,100], plot_bgcolor='white', width=300, height=500)
Gauge.update_xaxes(visible=True,showticklabels=False)
  
#TOP SKILL 3: DECLARE AND SET VARIABLES
#Most Recent 150 Days (Slice Data)
NumberofDays = len(ApiData)
ApiData = ApiData[NumberofDays - 150:NumberofDays]
ApiDataFrame = pandas.DataFrame(ApiData)
MinPrice = min(ApiDataFrame.price_close)
MaxPrice = max(ApiDataFrame.price_close) 
MinDate = min(ApiDataFrame.date)
MaxDate = max(ApiDataFrame.date) 

#TOP SKILL 3: DECLARING VARIABLES (EMPTY BOX)
WLPRColor = []
WLPRPoints = []

#TOP SKILL 2: SETTING VARIABLES WITH A BASIC LOOP (FILL THE EMPTY BOX)
for i in ApiData:
    if i['wlpr'] > -50:
     iWLPRColor = 'green'
    else: 
     iWLPRColor = 'red'
     WLPRColor.append(iWLPRColor)
    iWLPRPoints = 100 + i['wlpr']
    WLPRPoints.append(iWLPRPoints)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPrice = plotly.express.bar(x=ApiDataFrame.date, y=ApiDataFrame.price_close,labels={
                     "x": "DATE",
                     "y": "BITCOIN PRICE",
                 })
chartPrice.update_layout(yaxis_range=[MinPrice,MaxPrice], plot_bgcolor='white')
chartPrice.update_traces(marker_color=WLPRColor)

#TOP SKILL: CREATE A CHART USING PLOTLY
chartPoints = plotly.express.area(x=ApiDataFrame.date, y=WLPRPoints,labels={
                     "x": "DATE",
                     "y": "WLPR POINTS",
                 })
chartPoints.update_layout(yaxis_range=[0,100], plot_bgcolor='black')
chartPoints.update_layout(height=400, yaxis=dict(
        tickmode = 'array',
        tickvals = [0, 20, 50, 80, 100],
        ticktext = ['0', '20','50','80', '100']
    ))
chartPoints.update_traces(line=dict(color="white", width=5))
chartPoints.add_hline(y=80, line_color="green")
chartPoints.add_hline(y=20, line_color="red")
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
chartDaily = plotly.express.line(x=ApiDataFrame.date, y=ApiDataFrame.wlpr,labels={
                     "x": "DATE",
                     "y": "WLPR",
                 }))
chartDaily.update_traces(line=dict(color="white", width=5))
chartDaily.add_hline(y=-80, line_color="red")
chartDaily.add_hline(y=-20, line_color="green")
chartDaily.update_yaxes(showgrid=False, zeroline=False)
chartDaily.update_layout(yaxis_range=[-100,-0], plot_bgcolor='black', yaxis=dict(
        tickmode = 'array',
        tickvals = [-100, -80, -50, -20, -0],
        ticktext = ['-100', '-80','-50','-20', '0']
    ))
chartDaily.update_xaxes(showgrid=False, zeroline=False)
chartDaily.add_shape(type="rect",
    x0=MinDate, y0=-50, x1=MaxDate, y1=-0,
    line=dict(
        color="green",
        width=2,
    ),
    fillcolor="green", opacity=0.6,
)
chartDaily.add_shape(type="rect",
    x0=MinDate, y0=-50, x1=MaxDate, y1=-100,
    line=dict(
        color="red",
        width=2,
    ),
    fillcolor="red", opacity=0.6,
)

#SHOW SCOREBOARD
print("WLPR", WLPR)
display(Image(Arrow, width = 150, height = 150))
Gauge.show()
chartPrice.show()
chartPoints.show()
chartDaily.show()
