from flask import Flask, render_template, request
from recommender import random_recommender, MOVIES_LIST

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def homepage():
    return render_template("homepage.html", movies=MOVIES_LIST)


@app.route("/recommendations")
def recommendations():
    form = request.args
    form_dict = dict(request.args)
    results = random_recommender()
    return render_template("recommendations.html", movies = results, votes=form)

if __name__ == '__main__':
    app.run(debug=True)
