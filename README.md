# Airflow Transaction Pipeline DAG

<img width="1919" height="984" alt="image" src="https://github.com/user-attachments/assets/b50e6989-b604-4c51-b95c-d801f04c2b59" />


## Overview
This project implements an Apache Airflow DAG that simulates a transaction processing pipeline running every 10 minutes.

## Workflow
1. Start pipeline message with timestamp
2. Process transactions and generate report
3. Run external Python script to append processing timestamp
4. Send email with the final report

## Technologies
- Apache Airflow
- Python
- BashOperator
- EmailOperator

## DAG Schedule
Runs every 10 minutes (`*/10 * * * *`)

## Output
Report saved in: "/data/transactions_report.txt"


## How to Run
1. Start Airflow
2. Trigger DAG or wait for schedule

## Author
Jana Habachy
