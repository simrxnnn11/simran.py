#mysraper.py

import pandas as pd
from playwright.sync_api import sync_playwright

print("starting the automated browser script...")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    print("navigating to the boookstore website...")
    page.go.to("https://books.toscrape.com")

    books = page.query_selector_all(".product_pod")

    titles_list = []
    prices_list = []

    for book in books:
        title_element = book.query_selector("h3 a")
        title = title_element.get_attribute("title")

        price_element = book.query_selector(".price_color")
        price = price_element.inner_text()

        titles_list.append(title)
        prices_list.append(price)


browser.close()

int("Organizing the collecting data into columns...")
scraped_data = {
    "Book name": titles_list,
    "price total": prices_list
}

df = pd.dataframe(scraped_data)

df.to_excel("scraped_books.xlsx", index=False)
print("successfully ! data has been saved to scraped_books.xlsx")


