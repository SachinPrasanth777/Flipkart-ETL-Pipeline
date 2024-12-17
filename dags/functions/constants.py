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

BUCKET_NAME = "bucket"
CSV_FILE_NAME = "data.csv"
PATH = "http://localhost:9090/api/v1/download-shared-object/aHR0cDovLzEyNy4wLjAuMTo5MDAwL2J1Y2tldC9kYXRhLmNzdj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPVVVNlY1TjE4N1pFUkpTWUVLQ1pRJTJGMjAyNDEyMTclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjE3VDEzMzAxM1omWC1BbXotRXhwaXJlcz00MzIwMCZYLUFtei1TZWN1cml0eS1Ub2tlbj1leUpoYkdjaU9pSklVelV4TWlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKaFkyTmxjM05MWlhraU9pSlZWVFpXTlU0eE9EZGFSVkpLVTFsRlMwTmFVU0lzSW1WNGNDSTZNVGN6TkRRM05UWTBNaXdpY0dGeVpXNTBJam9pWVdseVpteHZkekV5TXpRaWZRLlJ4clJBM1U1dU9rc2c3M0NaSkViVHNQeHZxWHMyVkxBQWdnVTdGSGZ5R2V5dHVhYVRWZTkzd0Q3eThaRGtzVnJvTFl5YmNaRHpWV2xUR1liRXN3NGJ3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZ2ZXJzaW9uSWQ9bnVsbCZYLUFtei1TaWduYXR1cmU9OGQ0ZTgxNzYxNmU0MTA5NjMyMTJiODgyYmFjMmFmNTYyNTQyZWI2MWRmYzViNTQ1YmNlYzc3ZDdmNmQ0NTVhNw"
