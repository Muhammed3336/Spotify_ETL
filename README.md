🎧 Spotify ETL Project using AWS
This project implements an ETL (Extract, Transform, Load) pipeline using AWS Cloud services to extract music data from the Spotify API, transform it using Python, and make it queryable using Amazon Athena.

🚀 Workflow Overview
Extract
extract_code.py fetches raw music data from the Spotify API.
Triggered daily using Amazon CloudWatch.
Data is stored in Amazon S3 (raw zone).

Transform
transform_code.py processes and formats the raw data.
Triggered when new data lands in S3 using S3 Event Triggers.
Transformed data is saved to a new S3 bucket/folder (transformed zone).

Load
AWS Glue Crawler infers schema and updates the Glue Data Catalog.
Amazon Athena is used to query the data directly using SQL.

🛠️ Technologies Used
Programming Language: Python
Data Source: Spotify API
Cloud Platform: AWS
Amazon S3
AWS Lambda
Amazon CloudWatch
AWS Glue
Amazon Athena

📝 Setup Instructions
> Set up Spotify API credentials
> Create an app at Spotify Developer Dashboard
> Get the client_id and client_secret
> Deploy extract_code.py
> Create an AWS Lambda function for extraction.
> Schedule it using Amazon CloudWatch (e.g., daily or every 15 minutes using cron: */15 * * * *).
> Store raw data
> Configure Lambda to push data to S3.
> Set up transformation trigger
> Create another Lambda with transform_code.py
> Configure S3 "Object Created" trigger.
> Configure AWS Glue and Athena
> Set up a Glue Crawler on the transformed S3 bucket.
> Use Amazon Athena to query the data.

📈 Sample Use Cases
Track trending songs
Monitor new releases
Analyze top artists or genres

📎 Architecture Diagram
Refer to spotify_ETL.jpeg in this repository for a visual representation of the pipeline.


