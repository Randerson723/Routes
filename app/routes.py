from app import app
from flask import render_template

@app.route('/')
def index():
    context = {
        'team_name':'Manchester City',
        'nick_name':'Cytizens',
        'ground':'Etihad',
        'results': [
            {
                'id' : 1,
                'body': 'Manchester City 3 Everton 0'
                
            },
            {
                'id' : 2,
                'body': 'Manchester City 2 Manchester United 0'

            },
            {
                'id' : 3,
                'body': 'Manchester City 0 Crystal Palace 2'

            },
        ]
    }
    return render_template('index.html', **context)

@app.route('/favorites')
def favorites():
   # data = {
       # 'favorite_club': 'Manchester City',
       # 'favorite_player': 'Jao Cancelo',
       # 'favorite_competition': 'Premier League',
       # 'favorite_ground': 'Etihad'
    #}
    return render_template('favorites.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/trophies')
def trophies():
    return render_template('trophy.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

