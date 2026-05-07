import requests
from bs4 import BeautifulSoup

# The URL of a site designed for scraping practice
url = "http://toscrape.com"

print("Connecting to the website...")
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all book titles
books = soup.find_all("h3")

print("\n--- Book List Found ---")
for book in books:
    title = book.get_text()
    print(f"Book Title: {title}")


