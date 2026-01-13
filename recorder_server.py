from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/start-recording", methods=["POST"])
def start_recording():
    data = request.get_json()

    url = data["url"]
    client_ip = data["client_ip"]

    try:
        r = requests.post(
            f"http://{client_ip}:7777/start",
            json={"url": url},
            timeout=5
        )
        return jsonify({"status": "Forwarded", "target": client_ip}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)


# from flask import Flask, request, jsonify
# import subprocess
# import sys
# import os
#
# app = Flask(__name__)
#
# # Path to the Python that runs this Flask app (this is the venv python)
# PYTHON = sys.executable
#
# @app.route("/start-recording", methods=["POST"])
# def start_recording():
#     data = request.get_json()
#     url = data["url"]
#
#     # Use: python -m playwright instead of playwright.exe
#     subprocess.Popen([
#         PYTHON,
#         "-m",
#         "playwright",
#         "codegen",
#         "--target=python",
#         url
#     ], cwd=os.getcwd())
#
#     return jsonify({"status": "Recording started"}), 200
#
#
# @app.route("/health", methods=["GET"])
# def health():
#     return "OK", 200
#
#
# if __name__ == "__main__":
#     app.run(host="localhost", port=7777)


# from flask import Flask, request, jsonify
# import requests
# import subprocess
# import sys
# import os
#
# app = Flask(__name__)
#
# PYTHON = sys.executable
#
#
# @app.route("/start-recording", methods=["POST"])
# def start_recording():
#     data = request.get_json()
#
#     url = data["url"]
#     client_ip = data["client_ip"]
#
#     try:
#         # 1️⃣ Check that the laptop is online
#         health = requests.get(f"http://{client_ip}:7777/health", timeout=3)
#         if health.status_code != 200:
#             return jsonify({"error": "Client not reachable"}), 400
#
#         # 2️⃣ Start Playwright Codegen on THIS machine
#         subprocess.Popen([
#             PYTHON,
#             "-m",
#             "playwright",
#             "codegen",
#             "--target=python",
#             url
#         ], cwd=os.getcwd())
#
#         return jsonify({
#             "status": "Recorder started",
#             "client": client_ip
#         }), 200
#
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
#
#
# @app.route("/health")
# def health():
#     return "OK", 200
#
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8888)
