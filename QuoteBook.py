from bs4 import BeautifulSoup
import requests

URL_LIST = ["https://quotes.toscrape.com/tag/love/",
            "https://quotes.toscrape.com/tag/inspirational/",
            "https://quotes.toscrape.com/tag/life/",
            "https://quotes.toscrape.com/tag/humor/",
            "https://quotes.toscrape.com/tag/books/",
            "https://quotes.toscrape.com/tag/reading/",
            "https://quotes.toscrape.com/tag/friendship/",
            "https://quotes.toscrape.com/tag/truth/",
            "https://quotes.toscrape.com/tag/friends/",
            "https://quotes.toscrape.com/tag/simile/"]


def save_in_file(text):
    with open("QuotesFromWeb.txt", "a", encoding="UTF-8") as file:
        file.write(text)


for link in URL_LIST:

    response = requests.get(url=link)
    html_doc = response.text

    soup = BeautifulSoup(html_doc, "html.parser")

    for quote in soup.find_all(class_="quote"):

        text = quote.find(class_="text")
        save_in_file(text.getText()+"\n")

        author = quote.find(class_="author")
        save_in_file("     ->  " + author.getText() + "\n\n")






