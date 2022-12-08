import psycopg2
import sys
import boto3
import os

# importante!! pasar datos de acceso a un modulo a parte en un gitignore

ENDPOINT="dev-db.ccxwezilmsaz.us-east-1.rds.amazonaws.com"
PORT="5432"
USER="udata"
PASSWORD="kYUi#wTs&wzq3pZ9xW&tm)oy"
REGION="us-east-1"
DBNAME="pickle_rick"

#gets the credentials from .aws/credentials
#session = boto3.Session(profile_name='RDSCreds')
#client = session.client('rds')

#token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION, password=PASSWORD)

try:
    conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USER, password=PASSWORD, sslrootcert="SSLCERTIFICATE")
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e)) 