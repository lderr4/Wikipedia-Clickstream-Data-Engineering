build:
	docker compose up --build -d

up:
	docker compose up -d

down:
	docker compose down

up-flink-job-only:
	docker compose up -d postgres jobmanager taskmanager

run-clickstream-job:
	docker exec jobmanager ./bin/flink run --python ./code/flink_orchestration.py

up-stream-only:
	docker-compose up -d zookeeper broker data-source 

run-stream-only:
	docker-compose exec data-source python /app/data_stream.py

make kafka-control-center:
	docker compose up control-center -d

make testenv:
	make up-stream-only && make up-flink-job-only

make ctest:
	docker exec jobmanager ./bin/flink run --python ./code/postgres_connection.py

run: 
	down up run-clickstream-job

