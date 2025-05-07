import requests

query = input("Enter the topic you want to search for: ")

api = "7c2c2eaf1e894f17aacdee9c822dc540"

url =f"https://newsapi.org/v2/everything?q={query}&from=2025-03-27&sortBy=publishedAt&apiKey={api}"

print(url)

r = requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(article["title"])
    print(article["description"])
    print(article["url"])
    print(article["publishedAt"])
    print("\n**************************************************************************\n")