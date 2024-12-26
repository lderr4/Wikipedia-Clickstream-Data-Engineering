from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

from constants import StreamJobConfig, KafkaConfig, PostgresConfig
from jinja2 import Environment, FileSystemLoader
from dataclasses import asdict
from typing import Tuple



def get_sql_query(
    entity: str,
    type: str = 'source',
    template_env: Environment = Environment(loader=FileSystemLoader("/opt/flink/code/")),
) -> str:
    config_map = {
        'kafka_connection': KafkaConfig(),
        'postgres_connection': PostgresConfig()

    }

    params = config_map.get(entity, None)
    if params is None: 
        params = {}
    else:
        params = asdict(params)


    return template_env.get_template(f"{type}/{entity}.sql").render(
        params
    )



def run_clickstream_job(t_env: StreamTableEnvironment,get_sql_query=get_sql_query) -> None:
    # Create Source DDLs
    query = get_sql_query('kafka_connection', "source")
    print(query)
    t_env.execute_sql(query)

    query = get_sql_query('postgres_connection', 'sink')
    print(query)
    t_env.execute_sql(query)

    query = get_sql_query("clickstream", "process")    

    print(query)
    t_env.execute_sql(query)

def get_execution_environment(
    config: StreamJobConfig,
) -> tuple[StreamExecutionEnvironment, StreamTableEnvironment]:
    
    s_env = StreamExecutionEnvironment.get_execution_environment()
    for jar in config.jars:
        s_env.add_jars(jar)
        print(f"{jar} added to execution environment.")
    # start a checkpoint every 10,000 ms (10 s)
    s_env.enable_checkpointing(config.checkpoint_interval * 1000)
    # make sure 5000 ms (5 s) of progress happen between checkpoints
    s_env.get_checkpoint_config().set_min_pause_between_checkpoints(
        config.checkpoint_pause * 1000
    )
    # checkpoints have to complete within 5 minute, or are discarded
    s_env.get_checkpoint_config().set_checkpoint_timeout(
        config.checkpoint_timeout * 1000
    )
    execution_config = s_env.get_config()
    execution_config.set_parallelism(config.parallelism)
    t_env = StreamTableEnvironment.create(s_env)
    job_config = t_env.get_config().get_configuration()
    job_config.set_string("pipeline.name", config.job_name)
    return s_env, t_env

if __name__ == "__main__":
    _, t_env = get_execution_environment(StreamJobConfig())
    run_clickstream_job(t_env)