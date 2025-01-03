# Main Commands

down:
	docker compose down

sleep:
	sleep 10

download-data:
	chmod +x src/data-source/download_data.sh && \
	src/data-source/download_data.sh

run:
	make download-data && \
	make down && \
	make up-stream-only && \
	make up-flink-job-only && \
	make sleep && \
	make reset-db && \
	make run-stream-only && \
	make run-clickstream-job && \
	open http://localhost:8081

metabase:
	docker compose up -d metabase && open http://localhost:3000

# granular commands

up-flink-job-only:
	docker compose up -d postgres jobmanager taskmanager


run-clickstream-job:
	docker exec jobmanager ./bin/flink run --python ./code/flink_orchestration.py

up-stream-only:
	mkdir -p src/postgres/data && docker-compose up -d zookeeper broker postgres data-source

run-stream-only:
	docker-compose exec -d data-source python /app/src/data_stream.py

count-rows:
	docker-compose exec -T postgres psql -U postgres -d postgres -c "\
	SELECT \
	(SELECT COUNT(*) FROM clickstream.clicks) AS num_click, \
	(SELECT COUNT(*) FROM clickstream.users) AS num_users;"

reset-db:
	docker-compose exec -T postgres psql -U postgres -d postgres < ./src/postgres/init.sql
