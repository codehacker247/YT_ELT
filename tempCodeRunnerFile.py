import requests
import json

API_KEY = "AIzaSyDT-5gXkChsHbZ2gHtomMTR8c_hLEONleY"
CHANNEL_HAndle = "MrBeast"

url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HAndle}&key={API_KEY}"

response  = requests.get(url)

print(response)

data = response.json()

print(json.dumps(data, indent=4))

