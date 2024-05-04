from googleapiclient.discovery import build
import pandas as pd

import json 

api_key='************************'
video_id = "lF9QRXkIgIM" #BDBE lF9QRXkIgIM  #canal-pessoal IxZcdFA8G-w

def video_comments(video_id):
	
  comments = []
  authors = []
  dates = []

  youtube = build('youtube', 'v3', developerKey=api_key)
  
  request=youtube.commentThreads().list(
        part='snippet',
        videoId=video_id
        )
 
  while request:
    response = request.execute()
		
    for item in response['items']:
        
      comment=item['snippet']['topLevelComment']['snippet']['textDisplay']
      comments.append(comment)
      
      author=item['snippet']['topLevelComment']['snippet']['authorDisplayName']
      authors.append(author)
      
      date=item['snippet']['topLevelComment']['snippet']['updatedAt']
      dates.append(date)
      
      request = youtube.commentThreads().list_next(request, response)

  df = pd.DataFrame({'comentarios':comments,'autores':authors,'data':dates})
  
  return df

df = video_comments(video_id)  

df_tatiane = df[(df.comentarios.str.contains('Corrêa') | \
    df.comentarios.str.contains('Correa') | \
    df.comentarios.str.contains('correa') | \
    df.comentarios.str.contains('corrêa') | \
    df.comentarios.str.contains('tatiane') | \
    df.comentarios.str.contains('Tatiane') | \
    df.comentarios.str.contains('Tatiana') | \
    df.comentarios.str.contains('tatiana')
    )
]

print(df_tatiane)
print(list(df_tatiane.autores.drop_duplicates()))
print(len(list(df_tatiane.autores.drop_duplicates())))