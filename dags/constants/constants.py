from datetime import timedelta

default_args = {
    "owner": "Sachin Prasanth",
    "retries": 5,
    "retry_delay": timedelta(minutes=2),
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.flipkart.com/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

base_url = "https://www.flipkart.com/search?q=mobile+phones&sort=popularity"
