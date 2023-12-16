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
    CREATE TABLE IF NOT EXISTS salaryPotential (
        rank INT,
        name varchar(255),
        state_name varchar(255),
        early_career_pay varchar(255),
        mid_career_pay varchar(255),
        make_world_better_percent varchar(255),
        stem_percent varchar(255)
    );
'''

cursor.execute(create_table_query)
conn.commit()

with open('C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets/salaryPotential.csv', 'r', encoding='utf-8') as f:
    cursor.copy_expert("COPY salaryPotential FROM stdin WITH CSV HEADER", f)

conn.commit()
cursor.close()
