import os
from flask import Flask
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from flask import request, jsonify

app = None
api = None

#Create the Flask App
def create_app():
    app = Flask(__name__)
    CORS(app)

    app.app_context().push()
    return app


app = create_app()





@app.route("/")
def count_word_frequency():
    url = "https://www.geeksforgeeks.org/"
    
    if request.args.get("url"):
        url = request.args.get("url")
        
    req = requests.get(url)

    soup = BeautifulSoup(req.content, "html.parser")

    text_arr = soup.get_text().split()

    symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "

    word_count = {}

    for i in text_arr:
        if i in symbols:
            text_arr.remove(i)
            
        else: 
            if i in word_count:
                word_count[i] += 1
                
            else:
                word_count[i] = 1
                
    return jsonify(word_count)





if __name__ == '__main__':
  # Run the Flask app
  app.run()
