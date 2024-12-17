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
next_url = "https://www.flipkart.com"

create_query = """
                CREATE TABLE IF NOT EXISTS data(
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                features TEXT NOT NULL,
                price BIGINT NOT NULL,
                rating DOUBLE PRECISION NOT NULL,
                ratings_count BIGINT NOT NULL,
                reviews_count BIGINT NOT NULL,
                image TEXT NULL,
                CONSTRAINT unique_title_features UNIQUE(title,features,price)
                )
                """

insert_query = """
               INSERT INTO data(title,features,price,rating,ratings_count,reviews_count,image)
               VALUES(%s,%s,%s,%s,%s,%s,%s)
               ON CONFLICT (title,features,price) DO NOTHING
               """
