import psycopg2

db_params = {
    'dbname': 'Grad-Guru',
    'user': 'postgres',
    'password': 'bunny2aug',
    'host': 'localhost',
    'port': '5432',
}

fee = 43000  

conn = psycopg2.connect(**db_params)

cur = conn.cursor()

delete_query = """
    DELETE FROM abroad
    WHERE Fees LIKE '%%Cr%%';
"""

cur.execute(delete_query)
conn.commit()

update_query = """
    UPDATE abroad
    SET Fees = REPLACE(Fees, ',', '')::float * CASE
        WHEN Fees ~ E'^\\d+\\.\\d+$' THEN 100000 
        ELSE 1
    END;
"""

cur.execute(update_query)
conn.commit()

query = """
    SELECT University, Country, Fees
    FROM (
        SELECT University, Country, avg(Fees::numeric) as Fees
        FROM abroad
        GROUP BY University, Country
        UNION
        SELECT name as University, 'usa' as Country, in_state_total::numeric * 80 as Fees
        FROM tuitionCost
    ) as a
    WHERE Fees >= %s;
"""

cur.execute(query, (fee,))

results = cur.fetchall()

for row in results:
    university, country, fees = row
    print('---------------------------')
    print(university)
    print(country)
    print(fees)

cur.close()
conn.close()
