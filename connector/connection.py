import configparser
import os
import sys

settings = configparser.ConfigParser()
print(settings)
cwd = os.getcwd()
settings.read(cwd + '\\connector\\credentials.ini')
settings.sections()

def conn(env):
    try:
        dsn_meta = False
        input_table = False
        output_table =False
        if env == "DEV":
            dsn_meta =settings.get('DEV','LOG_DSN') if settings.has_option('DEV', 'LOG_DSN') else None
            input_table = settings.get('DEV', 'INPUT_TABLE') if settings.has_option('DEV', 'INPUT_TABLE') else None
            output_table = settings.get('DEV', 'OUTPUT_TABLE') if settings.has_option('DEV', 'OUTPUT_TABLE') else None
        elif env == "QA":
            dsn_meta = settings.get('QA', 'LOG_DSN') if settings.has_option('QA', 'LOG_DSN') else None
            input_table = settings.get('QA', 'INPUT_TABLE') if settings.has_option('QA', 'INPUT_TABLE') else None
            output_table = settings.get('QA', 'OUTPUT_TABLE') if settings.has_option('QA', 'OUTPUT_TABLE') else None
        elif env == "UAT":
            dsn_meta = settings.get('UAT', 'LOG_DSN') if settings.has_option('UAT', 'LOG_DSN') else None
            input_table = settings.get('UAT', 'INPUT_TABLE') if settings.has_option('UAT', 'INPUT_TABLE') else None
            output_table = settings.get('UAT', 'OUTPUT_TABLE') if settings.has_option('UAT', 'OUTPUT_TABLE') else None
        elif env == "PROD":
            dsn_meta = settings.get('PROD', 'LOG_DSN') if settings.has_option('PROD', 'LOG_DSN') else None
            input_table = settings.get('PROD', 'INPUT_TABLE') if settings.has_option('PROD', 'INPUT_TABLE') else None
            output_table = settings.get('PROD', 'OUTPUT_TABLE') if settings.has_option('PROD', 'OUTPUT_TABLE') else None

        return dsn_meta,input_table,output_table
    except BaseException as e:
        print(e)
