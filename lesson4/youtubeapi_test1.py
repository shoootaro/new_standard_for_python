import requests

youtube_api = "https://www.googleapis.com/youtube/v3/search"
apikey = "AIzaSyBJWXDWje2MJjLj5iN5FOFJf89g5GW9B6U"

keyword = "富士山"
params = {"part": "snippet", "q": keyword, "type": "video","maxResults": "5", "key": apikey}

results = requests.get(youtube_api, params=params).json()

for item in results["items"]:
    print("■ id: ", item["id"]["videoId"])
    print("title:", item["snippet"]["title"])
    print("desc:", item["snippet"]["description"])
    print("thumbnail:", item["snippet"]["thumbnails"]["default"]["url"])