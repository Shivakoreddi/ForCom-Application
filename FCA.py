from flask import Flask,render_template,url_for
import json
app = Flask(__name__)

posts = [
    {
        "title":"Forum post 1",
        "author": "shiva Koreddi",
        "date_posted":"04/19/2021",
        "content":"First post content"

    },
    {
        "title":"Forum Post 2",
        "author": "Sravani",
        "date_posted": "04/19/2021",
        "content":"Second post content"

    }
]
class Forum():
    @app.route("/home")
    def home():
        return render_template('home.html',posts= posts)

    @app.route("/about")
    def about():
        return render_template('about.html')
    @app.route("/snippets")
    def get():
        return {"name":"recipe", "expires_in": 30, "snippet":"1 apple"}

    @app.route("/recipe")
    def post(self):
        return self.content
if  __name__=="__main___":
    app.run(debug=True)