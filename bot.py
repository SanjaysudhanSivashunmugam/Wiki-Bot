from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Function to search Wikipedia
def search_wikipedia(query):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('extract') or "No summary available."
    else:
        return "No results found."

# Endpoint for Zoho Cliq bot
@app.route("/bot", methods=["POST"])
def bot():
    data = request.json
    query = data.get('text')  # Extract the question from the Cliq payload
    if query:
        answer = search_wikipedia(query)
        return jsonify({"text": answer})
    else:
        return jsonify({"text": "Please ask a valid question."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
