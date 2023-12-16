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
    CREATE TABLE IF NOT EXISTS abroad (
        University varchar(255),
        City varchar(255),
        Country varchar(255),
        Program varchar(255),
        Deadline varchar(255),
        Fees varchar(255),
        TOEFL varchar(255),
        GRE varchar(255),
        GMAT varchar(255),
        IELTS varchar(255)
    );
'''

cursor.execute(create_table_query)
conn.commit()

with open('C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets/abroad.csv', 'r', encoding='utf-8') as f:
    cursor.copy_expert("COPY abroad FROM stdin WITH CSV HEADER", f)

conn.commit()
cursor.close()
