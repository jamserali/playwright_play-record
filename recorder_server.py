# from flask import Flask, request, jsonify
# import subprocess
#
# app = Flask(__name__)
#
# @app.route("/start-recording", methods=["POST"])
# def start_recording():
#     data = request.get_json()
#     url = data["url"]
#
#     subprocess.Popen([
#         "playwright",
#         "codegen",
#         "--target=python",
#         url
#     ])
#
#     return jsonify({"status": "Recording started"}), 200
#
# if __name__ == "__main__":
#     app.run(port=7777)
#
# # app.run(port=7777)
# # app.run(host="0.0.0.0", port=7777)
#
#
#
#
#
#
#
#

from flask import Flask, request, jsonify
import subprocess
import sys
import os

app = Flask(__name__)

# Path to the Python that runs this Flask app (this is the venv python)
PYTHON = sys.executable

@app.route("/start-recording", methods=["POST"])
def start_recording():
    data = request.get_json()
    url = data["url"]

    # Use: python -m playwright instead of playwright.exe
    subprocess.Popen([
        PYTHON,
        "-m",
        "playwright",
        "codegen",
        "--target=python",
        url
    ], cwd=os.getcwd())

    return jsonify({"status": "Recording started"}), 200


@app.route("/health", methods=["GET"])
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="localhost", port=7777)
