import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# Get the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"User: {user_message}\nBot:",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot_message = response.choices[0].text.strip()
    return jsonify({"message": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
