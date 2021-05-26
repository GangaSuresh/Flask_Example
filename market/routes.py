from market import app
from flask import  render_template
from market.models import Item


#decorator, which url in website
@app.route("/test")
def hello_world():
    return "<h1>Hello, There!</h1>"

#dynamic route
@app.route('/about/<username>')
def about_page(username):
    return f"<h1>This is about page of {username}</h1>"

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')

@app.route("/market")
def market_page():
    items=Item.query.all()
    return render_template('market.html',items=items) #use jinga to use