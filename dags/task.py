from datetime import datetime
from airflow.decorators import dag, task
from bs4 import BeautifulSoup
import requests
from constants.constants import default_args, headers, base_url


@dag(
    dag_id="setup_soup",
    default_args=default_args,
    start_date=datetime(2024, 12, 15),
    schedule_interval="@hourly",
)
def scrape_data():

    @task()
    def get_soup(url):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            print(f"Failed to fetch page: {url}, Status code: {response.status_code}")
            return None

    get_soup(base_url)


scrape_data()
