from flask import Flask , render_template , jsonify
import csv
import random
import pprint
import config
import requests
app = Flask(__name__)


@app.route("/")
def Home():
      with open('netflix_titles.csv',encoding="utf8") as f:
            read = csv.reader(f)
            row = random.choice(list(read))
      movie = {
        'id': row[0],
        'category': row[1],
        'title': row[2],
        'director': row[3],
        'cast': row[4],
        'country': row[5],
        'date_added': row[6],
        'release_year': row[7],
        'maturity': row[8],
        'duration': row[9],
        'genre': row[10],
        'description': row[11],
        # default poster just so we see something
        'image': 'https://live.staticflickr.com/4422/36193190861_93b15edb32_z.jpg',
        'imdb': 'Not Available'
        
                   }
      
      url =  f"http://www.omdbapi.com/?t={movie['title']}/&apikey={config.API_KEY}"

      
      response = requests.request("GET", url)

      mdata = response.json()

      
      if 'Poster' in mdata:
            movie['image'] = mdata['Poster']
      
      # print(movie)

      return render_template('home.html' , data = movie)


      



app.run(debug=True)

