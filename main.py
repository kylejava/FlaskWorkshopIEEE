import requests
from flask import Flask, render_template, flash, request

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)
