from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json["message"]
    bot_response = respond(user_message)
    return jsonify({"message": bot_response})

def respond(message):
    # Simple rule-based responses
    if message.lower() in ["hi", "hello"]:
        return "Hello!"
    elif message.lower() in ["bye", "goodbye"]:
        return "Goodbye!"
    else:
        return "I didn't understand that."

if __name__ == "__main__":
    app.run(debug=True)
