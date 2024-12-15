import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.flipkart.com/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

base_url = "https://www.flipkart.com/search?q=mobile+phones&sort=popularity"


def get_soup(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    else:
        print(f"Failed to fetch page: {url}, Status code: {response.status_code}")
        return None


def fetch_mobile_titles(soup):
    product_containers = soup.find_all("div", {"class": "_75nlfW"})
    products = []

    for container in product_containers:
        title_element = container.find("div", {"class": "KzDlHZ"})
        rating_element = container.find("div", {"class": "XQDdHH"})
        price = container.find("div", {"class": "Nx9bqj _4b5DiR"})
        features = container.find("div", {"class": "_6NESgJ"})
        reviews = container.find("span", {"class": "Wphh3N"})
        image = container.find("img", {"class": "DByuf4"})

        if title_element:
            title_text = title_element.text
            rating_text = rating_element.text if rating_element else "No rating"
            price_text = price.text
            features_text = features.text
            reviews_text = reviews.text if reviews else "No reviews"
            image_url = image["src"]

            products.append(
                {
                    "title": title_text,
                    "rating": rating_text,
                    "price": price_text,
                    "features": features_text,
                    "reviews": reviews_text,
                    "image": image_url,
                }
            )

    if products:
        print("Fetched the following product titles and ratings:")
        for product in products:
            print(
                product["title"],
                product["rating"],
                product["price"],
                product["features"],
                product["reviews"],
                product["image"],
            )
    else:
        print("No product titles found.")

    return products


def scrape_all_pages():
    next_page_url = base_url
    all_products = []

    while next_page_url:
        soup = get_soup(next_page_url)
        if soup is None:
            break

        products = fetch_mobile_titles(soup)
        all_products.extend(products)

        next_button = soup.find("a", {"class": "_9QVEpD"})
        if next_button:
            next_page_url = "https://www.flipkart.com" + next_button["href"]
        else:
            print("No more pages to scrape.")
            next_page_url = None

    print(f"Scraped a total of {len(all_products)} products.")


scrape_all_pages()
