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
    CREATE TABLE IF NOT EXISTS tuitionCost (
        name varchar(255),
        state varchar(255),
        state_code varchar(255),
        type varchar(255),
        degree_length varchar(255),
        room_and_board varchar(255),
        in_state_tuition varchar(255),
        in_state_total varchar(255),
        out_of_state_tuition varchar(255),
        out_of_state_total varchar(255)
    );
'''

cursor.execute(create_table_query)
conn.commit()

with open('C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets/tuitionCost.csv', 'r', encoding='utf-8') as f:
    cursor.copy_expert("COPY tuitionCost FROM stdin WITH CSV HEADER", f)

conn.commit()
cursor.close()
