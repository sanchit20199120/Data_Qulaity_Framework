import base64
import json
import boto3
from botocore.exceptions import Clienterror

# hard coded credentials -- in future will use secret manager to get the credential details
def get_dsn(dsn_name: str):
    if dsn_name == "SNOWFLAKE_DEV":
        return({"host" : "", "id" : "", "secret" : "", "database" : "", "schema" : " ", "table" : " "})
    elif dsn_name == "SNOWFLAKE_QA":
        return ({"host": "", "id": "", "secret": "", "database": "", "schema": " ", "table": " "})




