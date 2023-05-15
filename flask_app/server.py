from flask import Flask, render_template
import random
import datetime
import requests


app = Flask(__name__)


@app.route("/")
def homepage():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year,)


@app.route("/guess/<name>")
def api_pages(name):
    parameters = {
        "name": name
    }
    response1 = requests.get("https://api.agify.io", params=parameters)
    response2 = requests.get("https://api.genderize.io", params=parameters)
    user_name = name
    user_age = response1.json()["age"]
    user_gender = response2.json()["gender"]
    return render_template("guess.html",  age=user_age, gender=user_gender, name=user_name)


@app.route("/blog")
def blog():
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    all_data = response.json()
    return render_template("blog.html", data=all_data)


if __name__ == "__main__":
    app.run(debug=True)