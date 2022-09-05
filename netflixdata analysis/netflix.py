import numpy as np
import pandas as pd
import plotly.express as px
from textblob import TextBlob

df=pd.read_csv('C:\\Users\\WE\\Desktop\\datasets\\netflix_titles.csv')

#Distribution of Content
z = df.groupby(['rating']).size().reset_index(name='counts')
pieChart = px.pie(z, values='counts', names='rating',
                  title='Distribution of Content Ratings on Netflix',
                  color_discrete_sequence=px.colors.qualitative.Set3)
#graph above will show that the majority of content on netflix is categorized as "TV-MA"
#which mean that most of the content avaliable on netflix is intended for viewing by mature
#and adult audiences.


#Now see Top 5 Directors
df['director']=df['director'].fillna('No director specified')
filtered_directors=pd.DataFrame()
filtered_directors=df['director'].str.split(',',expand=True).stack()
filtered_directors=filtered_directors.to_frame()
filtered_directors.columns=['Director']
directors=filtered_directors.groupby(['Director']).size().reset_index(name='Total Content')
directors=directors[directors.Director !='No Director Specified']
directors=directors.sort_values(by=['Total Content'],ascending=False)
directorsTop5=directors.head()
directorsTop5=directorsTop5.sort_values(by=['Total Content'])
fig1=px.bar(directorsTop5,x='Total Content',y='Director',title='Top 5 Directors on Netflix')
fig1.show()

