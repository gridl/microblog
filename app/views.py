from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Eric'}  # a fake user

    # populate some fake posts

    posts = [
                {'author': {'nickname':'John'},
                 'body': 'Beautiful day in Boston!'},
                 
                {'author':{'nickname':'Susan'},
                 'body': 'The Avengers movie was so cool!'}
    ]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)