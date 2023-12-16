import psycopg2

conn = psycopg2.connect(
    dbname="Grad-Guru",
    user="postgres",
    password="bunny2aug",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

create_table_query = '''
    CREATE TABLE IF NOT EXISTS scholarship (
        sign INT,
        title varchar(255),
        degrees varchar(255),
        funds varchar(255),
        date varchar(255),
        location varchar(255)
    );
'''

cursor.execute(create_table_query)
conn.commit()

# Use psycopg2's COPY_FROM to load data from the CSV file
with open('C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets/scholarship.csv', 'r', encoding='utf-8') as f:
    cursor.copy_expert("COPY scholarship FROM stdin WITH CSV HEADER", f)

conn.commit()
cursor.close()
