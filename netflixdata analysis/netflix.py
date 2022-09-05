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

#Now see Top 5 Actors
df['cast']=df['cast'].fillna('No Cast Specified')
filtered_cast=pd.DataFrame()
filtered_cast=df['cast'].str.split(',',expand=True).stack()
filtered_cast=filtered_cast.to_frame()
filtered_cast.columns=['Actor']
actors=filtered_cast.groupby(['Actor']).size().reset_index(name='Total Content')
actors=actors[actors.Actor !='No Cast Specified']
actors=actors.sort_values(by=['Total Content'],ascending=False)
actorsTop5=actors.head()
actorsTop5=actorsTop5.sort_values(by=['Total Content'])
fig2=px.bar(actorsTop5,x='Total Content',y='Actor', title='Top 5 Actors on Netflix')
fig2.show()

#Next thing is to analyze from this data is the trend of production over the years on netflix
df1=df[['type','release_year']]
df1=df1.rename(columns={"release_year": "Release year"})
df2=df1.groupby(['Release year','type']).size().reset_index(name='Total content')
df2=df2[df2['Release year']>=2010]
fig3 = px.line(df2,x="Release year",y="Total content",color='type',title='Trend on content produce over the years on Netfilx')
fig3.show()

