import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
df=pd.read_csv("tsunami.csv")
df1=df.drop(columns=['DAY','MINUTE','HOUR','MINUTE','MONTH','LOCATION_NAME','REGION','CAUSE','HOUSES_TOTAL_DESCRIPTION','TS_INTENSITY','DAMAGE_TOTAL_DESCRIPTION','URL','COMMENTS'])
df2=df1.sort_values(by=['YEAR']).head()
fig=px.line_3d(df2,x='YEAR',y='LATITUDE',z='LONGITUDE',title='Tsunami')
fig.show()

