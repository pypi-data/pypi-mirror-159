import snowflake.connector
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.utils import int_from_bytes
import os

USER = os.getenv('SNOWFLAKE_USER')
PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
RSA_KEY = os.getenv('SNOWFLAKE_RSA_Key')

ACCOUNT = os.getenv('DEV_SNOWFLAKE_ACCOUNT')
WAREHOUSE = os.getenv('DEV_SNOWFLAKE_WAREHOUSE')
DATABASE = os.getenv('DEV_SNOWFLAKE_DATABASE')
SCHEMA = os.getenv('DEV_SNOWFLAKE_SCHEMA')
 

def connection_info():
    print(USER,ACCOUNT,WAREHOUSE,DATABASE,SCHEMA)

def snowflake_connection( USER=USER , RSA_KEY=RSA_KEY ,PASSWORD=PASSWORD, DATABASE=DATABASE, SCHEMA=SCHEMA, ACCOUNT=ACCOUNT,WAREHOUSE=WAREHOUSE):
    try:
        private_rsa_key = bytes(RSA_KEY.encode()) 
        p_key= serialization.load_pem_private_key(
            private_rsa_key,
            password=PASSWORD.encode(),
            backend=default_backend())
        pkb = p_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption())
        # Connection string
        cnxn = snowflake.connector.connect(
            user= USER,
            account= ACCOUNT,
            private_key=pkb,
            warehouse= WAREHOUSE,
            database= DATABASE,
            schema= SCHEMA
        )
        return cnxn
    except Exception as e:
        print(f"Error in connecting to snowflake {e}")
        
        
def snowflake_execute(sql_query):
    con = snowflake_connection()
    cur = con.cursor()
    try:    
        cursor = cur.execute(sql_query)
        print("snowflake query executed successfully!")
        return cursor
    except Exception as e:
        print(f"Error in execution of snowflake query :{e}")