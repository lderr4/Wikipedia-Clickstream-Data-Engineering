build:
	mkdir -p src/postgres/data && \
	docker compose up --build -d

down:
	docker compose down

sleep:
	sleep 10

make run:
	make down && \
	make up-stream-only && \
	make up-flink-job-only && \
	make sleep && \
	make run-stream-only && \
	make run-clickstream-job && \
	open http://localhost:8081

make metabase:
	docker compose up -d metabase && open http://localhost:3000

# Commands I made for Debugging 

up-flink-job-only:
	docker compose up -d postgres jobmanager taskmanager

run-clickstream-job: # run flink job
	docker exec jobmanager ./bin/flink run --python ./code/flink_orchestration.py

up-stream-only: 
	mkdir -p src/postgres/data && docker-compose up -d zookeeper broker postgres data-source

run-stream-only: # run the data stream by itself
	docker-compose exec -d data-source python /app/src/data_stream.py

count-rows: # command to confirm the db is populating with data
	docker-compose exec -T postgres psql -U postgres -d postgres -c "\
	SELECT \
	(SELECT COUNT(*) FROM clickstream.clicks) AS num_click, \
	(SELECT COUNT(*) FROM clickstream.users) AS num_users;"

reset-db: # command to delete the contents of both data tables
	docker compose up -d postgres && \
	docker exec -i postgres psql -U postgres -d postgres < ./src/postgres/init.sql


