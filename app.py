from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    # Placeholder until real Nortux backend is connected
    return jsonify({
        "response": f"Nortux received: {prompt}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
