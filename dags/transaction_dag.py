from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime
import os

default_args = {
    "owner": "airflow",
}

def start_pipeline():
    print(f"Transaction pipeline started at {datetime.now()}")

def process_transactions():
    transactions = [120, 300, 450, 200]
    total = sum(transactions)
    count = len(transactions)

    report = f"""Daily Transaction Report 
    Number of transactions: {count} 
    Total amount: {total}"""

    os.makedirs("/data", exist_ok=True)

    with open("/data/transactions_report.txt", "w") as f:
        f.write(report)

    print("Transaction report generated successfully.")


with DAG(
    dag_id="transaction_pipeline_dag",
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/10 * * * *",  
    catchup=False,
) as dag:

    start_task = PythonOperator(
        task_id="start_pipeline",
        python_callable=start_pipeline,
    )

    process_task = PythonOperator(
        task_id="process_transactions",
        python_callable=process_transactions,
    )

    run_script_task = BashOperator(
        task_id="run_external_script",
        bash_command="python /data/process_transactions.py",
    )

    send_email_task = EmailOperator(
        task_id="send_email_report",
        to="jana.habachy@icloud.com",
        subject="Transaction Report",
        html_content="{{ task_instance.xcom_pull(task_ids='process_transactions') }}",
        files=["/data/transactions_report.txt"],
    )

    start_task >> process_task >> run_script_task >> send_email_task