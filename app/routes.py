from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'EdenLeonardo'}
  posts = [
    {
      'author': {'username': 'John'},
      'body': "Beautiful day to devour ribs!"
    },
    {
      'author': {'username': 'Mady'},
      'body': "The Wakandians movie was soooo good!"
    }
  ]
  return render_template('index.html', title="home", user=user, posts=posts)
