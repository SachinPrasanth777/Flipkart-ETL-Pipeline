import requests
from bs4 import BeautifulSoup
from functions.constants import headers, base_url, next_url

def get_soup(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    else:
        print(f"Failed to fetch page: {url}, Status code: {response.status_code}")
        return None

def fetch_product_data(container):
    title = extract_title(container)
    rating = extract_rating(container)
    price = extract_price(container)
    features = extract_features(container)
    ratings_count, reviews_count = extract_reviews(container)
    image = extract_image(container)

    return {
        "title": title,
        "rating": rating,
        "price": price,
        "features": features,
        "ratings_count": ratings_count,
        "reviews_count": reviews_count,
        "image": image,
    }

def extract_title(container):
    title_element = container.find("div", {"class": "KzDlHZ"})
    return title_element.text if title_element else "No title"

def extract_rating(container):
    rating_element = container.find("div", {"class": "XQDdHH"})
    return rating_element.text if rating_element else "No rating"

def extract_price(container):
    price_element = container.find("div", {"class": "Nx9bqj _4b5DiR"})
    return price_element.text if price_element else "No price"

def extract_features(container):
    features_element = container.find("div", {"class": "_6NESgJ"})
    return features_element.text if features_element else "No features"

def extract_reviews(container):
    reviews_element = container.find("span", {"class": "Wphh3N"})
    ratings_count = "No ratings"
    reviews_count = "No reviews"
    
    if reviews_element:
        reviews_text = reviews_element.text.strip()
        parts = reviews_text.split('&')
        if len(parts) == 2:
            ratings_count = parts[0].strip()
            reviews_count = parts[1].strip()
        else:
            reviews_count = reviews_text

    return ratings_count, reviews_count

def extract_image(container):
    image_element = container.find("img", {"class": "DByuf4"})
    return image_element["src"] if image_element else "No image"

def fetch_mobile_titles(soup):
    product_containers = soup.find_all("div", {"class": "_75nlfW"})
    products = []

    for container in product_containers:
        product_data = fetch_product_data(container)
        products.append(product_data)

    return products

def scrape_all_pages(max_pages=25):
    next_page_url = base_url
    all_products = []
    page_count = 0

    while next_page_url and page_count < max_pages:
        soup = get_soup(next_page_url)
        if soup is None:
            break

        products = fetch_mobile_titles(soup)
        all_products.extend(products)

        next_button = soup.find("a", {"class": "_9QVEpD"})
        if next_button:
            next_page_url = next_url + next_button["href"]
            page_count += 1
        else:
            break

    return all_products
