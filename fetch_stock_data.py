import requests
import psycopg2
from datetime import datetime

def fetch_and_store():
    url = "https://dummyjson.com/products/1"  # replace with real stock API
    response = requests.get(url)
    data = response.json()

    conn = psycopg2.connect(
        dbname="airflow",
        user="airflow",
        password="airflow",
        host="postgres",
        port="5432"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_data (
            id SERIAL PRIMARY KEY,
            date_time TIMESTAMP,
            stock_info JSONB
        )
    """)

    cur.execute(
        "INSERT INTO stock_data (date_time, stock_info) VALUES (%s, %s)",
        (datetime.utcnow(), data)
    )

    conn.commit()
    cur.close()
    conn.close()
