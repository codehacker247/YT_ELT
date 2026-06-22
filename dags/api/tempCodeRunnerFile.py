
API_KEY = Variable.get("API_KEY")
CHANNEL_Handle = Variable.get("CHANNEL_HANDLE")

maxresults = 50

@task
def get_playlist_id():

  try:
    url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_Handle}&key={API_KEY}"
    response  = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    data = response.json()
    # print(json.dumps(data, indent=4))
    channel_items=data["items"][0]
    channel_playlist_id=channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
    #print(channel_playlist_id)
    return channel_playlist_id
  
  except requests.exceptions.RequestException as e:
    return e
