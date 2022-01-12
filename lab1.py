import requests

print(requests.__version__)

print(requests.get("https://raw.githubusercontent.com/vyomea/cmput404-lab1/main/lab1.py").text)