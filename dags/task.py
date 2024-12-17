from datetime import datetime
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from functions.functions import scrape_all_pages
from functions.constants import create_query, default_args


@dag(
    dag_id="setup_soup",
    default_args=default_args,
    start_date=datetime(2024, 12, 15),
    schedule_interval="@hourly",
)
def scrape_data():

    @task()
    def fetch_all_products():
        all_products = scrape_all_pages(max_pages=25)
        return all_products

    @task()
    def create_table():
        pg_hook = PostgresHook(postgres_conn_id="postgres_local")
        pg_hook.run(create_query)

    create_table_task = create_table()
    products = fetch_all_products()
    create_table_task >> products


scrape_data()
