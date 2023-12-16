import psycopg2
import csv
import re

conn = psycopg2.connect(
    dbname="Grad-Guru",
    user="postgres",
    password="bunny2aug",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS qsranking (
    s_no VARCHAR(255),
    key VARCHAR(255),
    rank_2020 VARCHAR(255),
    rank_2019 VARCHAR(255),
    institute VARCHAR(255),
    country VARCHAR(255)
);
'''

cur.execute(create_table_query)

conn.commit()

csv_file_path = "C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets/qsranking.csv"  

with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        s_no, key, rank_2020, rank_2019, institute, country = row
        cur.execute(
            'INSERT INTO qsranking (s_no, key, rank_2020, rank_2019, institute, country) VALUES (%s, %s, %s, %s, %s, %s)',
            (s_no, key, rank_2020.replace(' ', ''), rank_2019.replace(' ', ''), institute, country)
        )

conn.commit()

cur.close()
conn.close()
