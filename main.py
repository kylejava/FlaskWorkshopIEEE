import requests
from flask import Flask, render_template, flash, request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/user' , methods = ['GET', 'POST'])
def user():
    if(request.method == 'POST'):
        name = request.form['name']

    return render_template('user.html', name = name)


if __name__ == "__main__":
    app.run(debug=True)
