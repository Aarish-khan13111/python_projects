import numpy as np
import pandas as pd
import plotly.express as px
from textblob import TextBlob

df=pd.read_csv('C:\\Users\\WE\\Desktop\\datasets\\netflix_titles.csv')

z = df.groupby(['rating']).size().reset_index(name='counts')
pieChart = px.pie(z, values='counts', names='rating',
                  title='Distribution of Content Ratings on Netflix',
                  color_discrete_sequence=px.colors.qualitative.Set3)
pieChart.show()



