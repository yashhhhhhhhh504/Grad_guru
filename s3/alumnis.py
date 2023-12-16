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
    CREATE TABLE IF NOT EXISTS alumnis (
        name VARCHAR(255),
        college VARCHAR(255),
        email VARCHAR(255)
    );
'''

cursor.execute(create_table_query)
conn.commit()

with open('C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets/alumnis.csv', 'r', encoding='latin1') as f:
    cursor.copy_expert("COPY alumnis FROM stdin WITH CSV HEADER", f)

conn.commit()
cursor.close()
