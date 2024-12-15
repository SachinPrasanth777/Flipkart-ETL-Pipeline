from datetime import datetime, timedelta
from airflow.decorators import dag, task
from functions.functions import scrape_all_pages

@dag(
    dag_id="setup_soup",
    default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    start_date=datetime(2024, 12, 15),
    schedule_interval="@hourly",
)
def scrape_data():

    @task()
    def fetch_all_products():
        all_products = scrape_all_pages(max_pages=25)
        return all_products

    fetch_all_products()

scrape_data()
