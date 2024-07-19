import pandas as pd
import logging
from datetime import datetime
import pytz
import os
import sys
import snowflake.connector
from connector import connection
from connector import aws_secret
import warnings


log = logging.getLogger("logger")
print(log)

def data_quality_check(arg):
    job_start_time = datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone('US/Central')).strftime('%Y-%m-%d %H:%M:%S')
    print(job_start_time)

    args =arg[1].split(',')
    workstream_name = args[0]
    data_src_name = args[1]
    env = args[2]
    rule_master_id = args[3] if len(args) > 3 else ''

    try:
        dsn_meta, input_table, output_table = connection.conn(env)
        log_dsn_name = aws_secret.get_dsn(dsn_meta)

        # connecting to snowflake account
        print("Connecting to Snowflake....")
        conn = snowflake.connector.connect(user = log_dsn_name['id'], password =log_dsn_name['secret'], account =log_dsn_name['host'], database = log_dsn_name['database'])

        if not conn:
            log.info("Credentials provide to connect to Snowflake is incorrect")
            sys.exit("Credentials provide to connect to Snowflake is incorrect")
        else:
            log.info("Connected to Snowflake")



    except BaseException as e:
        print(e)


data_quality_check(sys.argv)
