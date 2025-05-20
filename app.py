from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
import requests

load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").lower()
        
        if any(word in user_message for word in ["sad", "depressed", "unhappy"]):
            bot_response = "I'm sorry to hear you're feeling this way. Remember it's okay to feel sad sometimes. Would you like to talk more about what's bothering you?"
        elif any(word in user_message for word in ["stress", "stressed", "overwhelmed"]):
            bot_response = "Stress can be really challenging. Try taking 5 deep breaths. Would it help to brainstorm solutions together?"
        elif any(word in user_message for word in ["help", "suicide", "kill myself"]):
            bot_response = "I'm really concerned about you. Please contact a trusted person or call the National Suicide Prevention Lifeline at 988 (US) immediately."
        else:
            bot_response = "Thank you for sharing. How has this been affecting your daily life?"
            
        return jsonify({
            "response": bot_response,
            "status": "success"
        })
        
    except Exception as e:
        return jsonify({
            "response": f"Sorry, I'm having trouble understanding. Could you rephrase that?",
            "status": "error"
        })

if __name__ == "__main__":
    app.run(debug=True, port=5000)

    