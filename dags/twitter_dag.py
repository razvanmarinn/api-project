from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from include.coinbase_api import api_pull_coinbase
from include.twitter_api import twitter_bitcoin_pull, twitter_eth_pull
# from include.twitter_api import twitter_bitcoin_pull, twitter_eth_pull


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}


dag = DAG(
    'twitter_dag',
    default_args = default_args,
    description = 'twitter dag'
)
run_etl_twitter_btc = PythonOperator(
    task_id = 'twitter_etl_btc',
    python_callable = twitter_bitcoin_pull,
    dag=dag,
)
run_etl_twitter_eth = PythonOperator(
    task_id = 'twitter_etl_eth',
    python_callable = twitter_eth_pull,
    dag=dag,
)
run_etl_coinbase = PythonOperator(
    task_id = 'twitter_etl_coinbase',
    python_callable = api_pull_coinbase,
    dag=dag,
)
run_etl_coinbase >> run_etl_twitter_btc >> run_etl_twitter_eth