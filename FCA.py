from flask import Flask
import json
app = Flask(__name__)

class Forum():
    @app.route("/snippets")
    def get():
        return {"name":"recipe", "expires_in": 30, "snippet":"1 apple"}

    @app.route("/recipe")
    def post(data):
        return data

if  __name__=="__main___":
    app.run(debug=True)