from dataclasses import dataclass, field
from typing import List

REQUIRED_JARS = [
    "file:///opt/flink/flink-sql-connector-kafka-1.17.0.jar",
    "file:///opt/flink/flink-connector-jdbc-3.0.0-1.16.jar",
    "file:///opt/flink/postgresql-42.6.0.jar",
]


@dataclass(frozen=True)
class StreamJobConfig:
    job_name: str = 'checkout-attribution-job'
    jars: List[str] = field(default_factory=lambda: REQUIRED_JARS)
    checkpoint_interval: int = 10
    checkpoint_pause: int = 5
    checkpoint_timeout: int = 5
    parallelism: int = 2

@dataclass(frozen=True)
class KafkaConfig:
    connector: str = 'kafka'
    bootstrap_servers: str = 'broker:29092'
    scan_stratup_mode: str = 'earliest-offset'
    consumer_group_id: str = 'flink-consumer-group-1'
    topic: str = 'clickstream'
    format: str = 'json'


@dataclass(frozen=True)
class PostgresConfig:
    schema_name: str = 'clickstream'
    table_name: str = 'clicks'
    port: str = "5432"
    host: str = 'postgres'
    username: str = 'postgres'
    password: str = 'postgres'

