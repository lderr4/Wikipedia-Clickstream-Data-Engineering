# flink 1.18; scala 2.12; java 11 (January 2024) 
FROM flink:1.17.0

ENV FLINK_LIB_DIR=/opt/flink/lib

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/*


RUN wget https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/1.17.0/flink-sql-connector-kafka-1.17.0.jar \
&& wget https://repo.maven.apache.org/maven2/org/apache/flink/flink-connector-jdbc/3.0.0-1.16/flink-connector-jdbc-3.0.0-1.16.jar \
&& wget https://jdbc.postgresql.org/download/postgresql-42.6.0.jar


RUN ln -s /usr/bin/python3 /usr/bin/python

COPY requirements.txt /opt/flink/
RUN pip install --no-cache-dir -r /opt/flink/requirements.txt