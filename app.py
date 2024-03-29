# Simple Flask Backend that shows news feed

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

load_dotenv()

news_api_key = os.getenv('NEWS_API_KEY')


@app.route('/ipl', methods=['GET'])
def home_landing():
    return  jsonify(message="Hello, my fellow IPL fans!! This is also a hello from heroku :wink: !!")

@app.route('/ipl/news/<string:news_type>', methods=['GET'])
def ipl_news(news_type):
    url = f"https://newsapi.org/v2/everything?q={news_type}&from=2024-03-27&to=2024-03-28&apiKey={news_api_key}"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    app.run(debug=True)