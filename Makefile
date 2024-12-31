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
	docker-compose up -d zookeeper broker postgres data-source

run-stream-only:
	docker-compose exec -d data-source python /app/src/data_stream.py

make kafka-control-center:
	docker compose up control-center -d

make testenv:
	make up-stream-only && make up-flink-job-only && make run-stream-only && make run-clickstream-job

run: 
	down up run-clickstream-job

count-rows: # command to confirm the db is working
	docker-compose exec -T postgres psql -U postgres -d postgres -c "\
	SELECT \
	(SELECT COUNT(*) FROM clickstream.clicks) AS num_click, \
	(SELECT COUNT(*) FROM clickstream.users) AS num_users;"

reset-db:
	docker compose up -d postgres && \
	docker exec -i postgres psql -U postgres -d postgres < ./src/postgres/init.sql


