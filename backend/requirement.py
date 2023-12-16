import psycopg2
import re

conn = psycopg2.connect(
    dbname="Grad-Guru",
    user="postgres",
    password="bunny2aug",
    host="localhost",
    port="5432"
)

TOEFL = 100
GRE = 300
GMAT = 300
IELTS = 6

query = """select University, Program, Country from (
    select University, Program, Country, TOEFL, GRE, GMAT, IELTS from abroad
    union
    select college as University, name as Program, location as Country, NULL as TOEFL, NULL as GRE, NULL as GMAT, NULL as IELTS from masters
    union
    select college as University, name as Program, location as Country, NULL as TOEFL, NULL as GRE, NULL as GMAT, NULL as IELTS from phd
    union
    select University, Program, location as Country, NULL as TOEFL, NULL as GRE, NULL as GMAT, NULL as IELTS from bachelors
) as t
where TOEFL::float >= %(TOEFL)s or GRE::float >= %(GRE)s or GMAT::float >= %(GMAT)s or IELTS::float >= %(IELTS)s and TOEFL is not null or GRE is not null or GMAT is not null or IELTS is not null
order by University, Program, Country;
"""

cursor = conn.cursor()
cursor.execute(query, {'TOEFL': TOEFL, 'GRE': GRE, 'GMAT': GMAT, 'IELTS': IELTS})
result = cursor.fetchall()
for row in result:
    print('-----------------')
    print(row[0])
    print(row[1])
    print(row[2])
conn.commit()
cursor.close()
