from flask import Flask, render_template, url_for, flash, redirect
import requests
import json
from movieAPI import get_recent_data
# from turbo_flask import Turbo

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        'home.html',
        subtitle='Home Page',
        text='This is the home page')


url = "https://www.scorebat.com/video-api/v1/"
response = requests.get(url)
soccer_info = response.json()
# print(soccer_info[0]['competition'])
# print(get_recent_data())
get_recent_data()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
