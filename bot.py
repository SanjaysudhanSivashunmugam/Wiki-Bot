from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

def search_wikipedia(query):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('extract') or "No summary available."
    else:
        return "No results found."


@app.route("/bot", methods=["POST"])
def bot():
    data = request.json
    query = data.get('text')  
    if query:
        answer = search_wikipedia(query)
        return jsonify({"text": answer})
    else:
        return jsonify({"text": "Please ask a valid question."})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

@app.route('/')
def home():
    return "Welcome to the Wikipedia Search Bot!"
