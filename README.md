# 📈 Dockerized Stock Data Pipeline with Apache Airflow

This project implements a **data pipeline** that fetches stock market data and stores it in a **PostgreSQL database**, orchestrated using **Apache Airflow**.  
It is fully containerized with **Docker Compose** for easy setup.

---

## 🚀 Features
- Fetches stock data via a custom Python script (`fetch_stock_data.py`).
- Orchestrates daily/hourly ETL jobs with **Airflow DAGs**.
- Stores results in **PostgreSQL** with schema & indexes (`init.sql`).
- Fully containerized with **Docker Compose**.
- Persistent PostgreSQL storage volume.

---

## 🛠️ Project Structure
stock_pipeline_project/
│── airflow/
│ └── dags/
│ └── stock_data_dag.py # Airflow DAG definition
│── fetch_stock_data.py # Python script for fetching stock data
│── init.sql # SQL schema for stock_data table
│── docker-compose.yml # Docker services configuration
│── .env # Environment variables (DB, API key, Airflow secrets)
│── README.md # Documentation (this file)


---

## ⚙️ Setup Instructions

### 1️⃣ Clone this repository
```bash
git clone https://github.com/YOUR_USERNAME/stock_pipeline_project.git
cd stock_pipeline_project

2️⃣ Configure environment variables

Create a .env file in the project root (already provided in this repo):

POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow
ALPHA_VANTAGE_API_KEY=your_api_key_here
FERNET_KEY=your_fernet_key_here


Generate a Fernet key if needed:

python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

3️⃣ Start Docker containers
docker-compose up -d --build

4️⃣ Initialize Airflow database
docker-compose run airflow-webserver airflow db migrate

5️⃣ Create Airflow admin user
docker-compose run airflow-webserver airflow users create \
    --username airflow \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password airflow

6️⃣ Access services

Airflow Web UI → http://localhost:8080

Postgres DB → localhost:5432

▶️ Usage

Login to Airflow (airflow / airflow if you used defaults).

Enable the DAG stock_data_pipeline.

Trigger it manually or wait for the schedule.

Check stored data inside Postgres:

docker exec -it stock_pipeline_project-postgres-1 \
    psql -U airflow -d airflow -c "SELECT * FROM stock_data LIMIT 10;"

🛑 Stopping the Services
docker-compose down -v

📌 Notes

Update fetch_stock_data.py with your desired stock API endpoint & parsing logic.

Adjust the DAG schedule in stock_data_dag.py (@daily, @hourly, etc.).

Persistent Postgres storage is configured via the postgres_data Docker volume.
