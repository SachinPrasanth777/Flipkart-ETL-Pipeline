from datetime import datetime
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from functions.functions import scrape_all_pages
from functions.constants import (
    create_query,
    default_args,
    insert_query,
    BUCKET_NAME,
    CSV_FILE_NAME,
    PATH,
)
from airflow.datasets import Dataset
from io import StringIO
import csv

path = Dataset(PATH)


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

    @task()
    def insert_table(products):
        pg_hook = PostgresHook(postgres_conn_id="postgres_local")
        for product in products:
            pg_hook.run(
                insert_query,
                parameters=(
                    product["title"],
                    product["features"],
                    product["price"],
                    product["rating"],
                    product["ratings_count"],
                    product["reviews_count"],
                    product["image"],
                ),
            )

    @task(outlets=[path])
    def convert_to_csv():
        pg_hook = PostgresHook(postgres_conn_id="postgres_local")
        query = "SELECT * FROM data"
        connection = pg_hook.get_conn()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]
        csv_buffer = StringIO()
        writer = csv.writer(csv_buffer, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        for row in rows:
            clean_row = [str(item) if item is not None else "" for item in row]
            writer.writerow(clean_row)
        csv_buffer.seek(0)
        cursor.close()
        connection.close()
        return csv_buffer.getvalue()

    @task()
    def upload_to_minio(csv_data):
        s3_hook = S3Hook(aws_conn_id="minio_conn")
        s3_hook.load_string(
            string_data=csv_data,
            key=CSV_FILE_NAME,
            bucket_name=BUCKET_NAME,
            replace=True,
        )

    create_table_task = create_table()
    products = fetch_all_products()
    insert_table_task = insert_table(products)
    csv_data = convert_to_csv()
    upload_task = upload_to_minio(csv_data)

    create_table_task >> products >> insert_table_task >> csv_data >> upload_task


scrape_data()
