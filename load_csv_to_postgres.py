import psycopg2
import csv

conn = psycopg2.connect(dbname="postgres", user='postgres', password='postgres', host='172.27.0.2')
conn.autocommit = True

cur = conn.cursor()
cur.execute("CREATE DATABASE housing")
conn.close()

conn = psycopg2.connect(dbname="housing", user='postgres', password='postgres', host='172.27.0.2')
conn.autocommit = True
cur = conn.cursor()


state_list = ['al', 'ak', 'ar', 'az', 'ca', 'co', 'ct', 'de', 'dc', 'fl', 'ga', 'hi', 'id', 'il', 'in_', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi' ,'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd' , 'oh', 'ok', 'or_', 'pa', 'ri', 'sc', 'sd', 'tn', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

for state in state_list:
    with conn.cursor() as cur:
        cur.execute("CREATE TABLE " + state + "(price_usd integer, price_baht bigint,\
                        bed integer, bath integer,sqft integer, sq_wah double precision,\
                        house_type varchar, address varchar, link varchar)")
            
    with conn.cursor() as cur:
        with open('/usr/src/app/csv_files/housing_' + state + '.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                cur.execute("INSERT INTO " + state + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", row)
                
    with conn.cursor() as cur:
        sql = "SELECT count(*) FROM" + state + ";"
        cur.execute(sql)
        result = cur.fetchone()
        print(state, "table has", result, "rows")