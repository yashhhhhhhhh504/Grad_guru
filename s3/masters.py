import psycopg2
import re

conn = psycopg2.connect(
    dbname="Grad-Guru",
    user="postgres",
    password="bunny2aug",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS masters (
        name VARCHAR(255),
        college VARCHAR(255),
        location VARCHAR(255)
    );
'''

cursor.execute(create_table_query)
conn.commit()

with open('C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets/masters.csv', 'r', encoding='utf-8') as f:
    cursor.copy_expert("COPY masters FROM stdin WITH CSV HEADER", f)

conn.commit()
cursor.close()
