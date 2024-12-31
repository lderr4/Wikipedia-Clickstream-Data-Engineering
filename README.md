# Wikipedia-Clickstream

### Overview
In this project, I use the [Wikipedia Clickstream Data Dump](https://dumps.wikimedia.org/other/clickstream/) to simulate a real-time data stream. I use Apache Kafka for ingestion, Apache Flink for processing, PostgreSQL for data storage, Metabase for real-time analytics, and Docker-Compose for orchestration. I downloaded the Dutch version of the dataset because the file size is much smaller, although any version should work. Additionally, I used [Random User API](https://randomuser.me/) to generate fake user data, enriching clickstream dataset with realistic user information.

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
   The UI should look like this:
   ![flink ui screenshot](https://github.com/lderr4/Wikipedia-Clickstream-Data-Engineering/blob/main/assets/images/flinkui.png)
 
5. To confirm the entire system is working correctly, check that the database is getting populated with data:
   ```
   make count-rows
   ```
   The users table should have 5000 entries; the clicks table should be getting continually populated.
   ![count rows command](https://github.com/lderr4/Wikipedia-Clickstream-Data-Engineering/blob/main/assets/images/countrows.png)



### Metabase Dashboard
Additionally, I have created a Metabase dashboard which refreshes every minute, showing real-time analytics of the fake data stream. Unfortunately, Metabase dashboards aren't really compatible with github because they are saved as database volumes, so you would have to rebuild this. Regardless, I will share my screenshots here.

![Aggregate dashboard](https://github.com/lderr4/Wikipedia-Clickstream-Data-Engineering/blob/main/assets/images/dashboard1.png)
![filter by country dashboard](https://github.com/lderr4/Wikipedia-Clickstream-Data-Engineering/blob/main/assets/images/dashboard2.png)


### Architecture Diagram

   
