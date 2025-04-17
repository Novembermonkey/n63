import threading
import requests
import json



urls = [
    "https://dummyjson.com/users",
    "https://dummyjson.com/products",
    "https://dummyjson.com/posts",
    "http://www.youtube.com",
    "http://www.facebook.com",
    "http://www.baidu.com",
    "http://www.yahoo.com",
    "http://www.amazon.com",
    "http://www.wikipedia.org",
    "http://www.qq.com",
    "http://www.google.co.in",
    "http://www.twitter.com",
    "http://www.live.com",
]

threads = []

def get_data(url: str, index: int, filename: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Connection to url{index} failed")
    data = response.json()
    with open(f"json/{filename}", "w") as f:
        json.dump(data, f, indent=4)
    print(f"Url{index} was saved successfully")

for index, url in enumerate(urls, 1):
    thread = threading.Thread(target=get_data, args=(url,index, f"file{index}.json"))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

