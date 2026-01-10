import requests

requests.post(
    "http://localhost:7777/start-recording",
    json={"url": "https://naveenautomationlabs.com/opencart/index.php?route=common/home"}
)