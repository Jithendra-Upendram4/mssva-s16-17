from flask import Flask, request, jsonify
from processor import process_artifact

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "no file"}), 400

    path = f"/tmp/{file.filename}"
    file.save(path)

    result = process_artifact(path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
