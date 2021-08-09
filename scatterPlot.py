import pandas as pd
import plotly.express as px
#data=[[1,2,3,4,5],[23,43,324,43,45]]
df=pd.read_csv("data.csv")
#df=pd.DataFrame(data)
print(df)
fig = px.scatter(df, x="date", y="cases", color="country", title='Covid Cases')
fig.show()   