from flask import Flask, jsonify
import pandas as pd
from out import output
movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
allmovies=movies_data[['original_title','release_date','poster_link','runtime','weighted_rating']]

# variables to store data
liked=[]
disliked=[]
watch_later=[]
# method to fetch data from database
def getmovies():
  movie_data={
    'original_title':allmovies.iloc[0,0],'release_date':allmovies.iloc[0,1],'poster_link':allmovies.iloc[0,2],'runtime':allmovies.iloc[0,3],'weighted_rating':allmovies.iloc[0,4]
  }
  return movie_data

# /movies api
@app.route('/')
def showmovies():
  mdata=getmovies()
  return jsonify({
    'data':mdata,'statues':'success'
  })
# /like api
@app.route('/like')
def likes():
  global allmovies
  mdata=getmovies()
  liked.append(mdata)
  allmovies.drop([0],inplace=True)
  allmovies=allmovies.reset_index(drop=True)
  return jsonify({
    'statues':'success'
  })
@app.route('/liked')
def likeds():
  global liked
  return jsonify({
    'data':liked,'statues':'success'
  })
# /dislike api
@app.route('/dislike')
def dislikes():
  global allmovies
  mdata=getmovies()
  disliked.append(mdata)
  allmovies.drop([0],inplace=True)
  allmovies=allmovies.reset_index(drop=True)
  return jsonify({
    'statues':'success'
  })

# /did_not_watch api
@app.route('/watch_later')
def unwatch():
  global allmovies
  mdata=getmovies()
  watch_later.append(mdata)
  allmovies.drop([0],inplace=True)
  allmovies=allmovies.reset_index(drop=True)
  return jsonify({
    'statues':'success'
  })

@app.route('/popular')
def pop():
  popularmovie=[]
  for i, row in output.iterrows():
    popmovie={'original_title':row['original_title'],'release_date':row['release_date'],'poster_link':row['poster_link'],'runtime':row['runtime'],'weighted_rating':row['weighted_rating']}
    popularmovie.append(popmovie)
  return jsonify({
    'data':popularmovie,
    'statues':'success'
  })
if __name__ == "__main__":
  app.run()