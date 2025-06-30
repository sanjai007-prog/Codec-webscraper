import requests
from bs4 import BeautifulSoup
import schedule
import time
import csv


def extract_quotes():
    site_url = "https://quotes.toscrape.com/" 
    site_response = requests.get(site_url)
    html_soup = BeautifulSoup(site_response.text, "html.parser")

    quote_blocks = html_soup.find_all("div", class_="quote")

    with open("quotes.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Quote", "Author"])

        for quote in quote_blocks:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            writer.writerow([text, author])

    print("Scraped data successfully and saved to quotes.csv!")


schedule.every(1).minutes.do(extract_quotes)

print("Scheduler is running...")
while True:
    schedule.run_pending()
    time.sleep(1)