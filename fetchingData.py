import requests


def fetchAndSave(url, path):
    r = requests.get(url=url)
    with open(path, "w", encoding="UTF-8") as file:
        file.write(r.text)

url = "https://quotes.toscrape.com/"

fetchAndSave(url, "ScrapedQuotes.html")