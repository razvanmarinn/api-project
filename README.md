# api_project
![Untitled design](https://user-images.githubusercontent.com/60939601/194404729-c9a0abc5-619a-42ff-97f4-b963150dcd88.png)


The project is based on twitter and coinmarketcap APIS from where I extract data. Furthermore, using Apache Airflow DAGS for operating my python functions I use the apis and get data on number of tweets on the subject "BITCOIN" and "ETH" and the price of them and store the result in a csv file in my amazon s3 bucket.


![Screenshot_3](https://user-images.githubusercontent.com/60939601/194404737-da97f28a-cbd6-4552-a1af-108ea5a0fc07.png) - > Picture with succesfully working DAG.
![image](https://user-images.githubusercontent.com/60939601/194405350-b7a23996-24e5-42d2-905e-942bb37ea5c6.png) - > Picture with the files saved on my S3 Bucket.

