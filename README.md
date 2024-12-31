# Wikipedia-Clickstream

### Overview
In this project, I use the [Wikipedia Clickstream Data Dump](https://dumps.wikimedia.org/other/clickstream/) to simulate a real-time data stream using Apache Kafka for ingestion, Apache Flink for processing, PostgreSQL for data storage, Metabase for real-time analytics, and Docker-Compose for orchestration. Additionally, I used [Random User API](https://randomuser.me/)  to generate fake user data, enriching clickstream dataset with realistic user information.

### How to Run Locally
1. Make sure you have [Docker](https://docs.docker.com/engine/install/) installed on your device.
2. Clone this repository:
   ```
   git clone https://github.com/lderr4/Wikipedia-Clickstream-Data-Engineering.git
   ```
3. Navigate to Project Directory:
   ```
   cd Wikipedia-Clickstream-Data-Engineering
   ```
4. Build and run the project with one command (this should take a few minutes). You will be navigated to the Apache Flink UI. Confirm that the job is running.
   ```
   make run
   ```
 
5. To confirm the entire system is working correctly, check that the database is getting populated with data:
   ```
   make count-rows
   ```
   
