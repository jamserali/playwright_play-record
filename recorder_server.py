from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/start-recording", methods=["POST"])
def start_recording():
    data = request.get_json()
    url = data["url"]

    subprocess.Popen([
        "playwright",
        "codegen",
        "--target=python",
        url
    ])

    return jsonify({"status": "Recording started"}), 200

# if __name__ == "__main__":
#     app.run(port=7777)

app.run(port=7777)







