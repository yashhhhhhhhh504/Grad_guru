import psycopg2

colleges_to_search = ["University", "College", "college", "institute"]
place = ["location", "Location", "country", "Country"]

db_params = {
    "host": "localhost",
    "database": "Grad-Guru",
    "user": "postgres",
    "password": "bunny2aug"
}

def search_college_in_database(input_college_name):
    results = []

    conn = psycopg2.connect(**db_params)

    try:
        cur = conn.cursor()

        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")

        for table in cur.fetchall():
            table_name = table[0]

            cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
            columns = [col[0] for col in cur.fetchall()]

            if table_name == 'indiancolleges':
                cur.execute(f"SELECT * FROM {table_name} WHERE College ILIKE %s OR abbreviation ILIKE %s", ["%" + input_college_name + "%", "%" + input_college_name + "%"])
                result = cur.fetchall()
                result = list(set([(row[0], 'India', row[12]) for row in result]))
                results.extend(result)
            else:
                col_name = None
                temp = None

                for col_name in colleges_to_search:
                    if col_name in columns:
                        if any(temp_name in columns for temp_name in place):
                            temp = next((temp_name for temp_name in place if temp_name in columns), None)
                            break

                if col_name is not None and temp is not None:
                    query = f"SELECT {col_name}, {temp}, abbreviation FROM {table_name} WHERE "
                    or_conditions = []
                    for col_name in colleges_to_search:
                        if col_name in columns:
                            or_conditions.append(f"{col_name} ILIKE %s")

                    if 'abbreviation' in columns:
                        or_conditions.append("abbreviation ILIKE %s")

                    query += " OR ".join(or_conditions)

                    query_params = [f"%{input_college_name}%"] * len(or_conditions)
                    cur.execute(query, query_params)

                    result = cur.fetchall()
                    results.extend(result)

        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print("Error: ", e)
        results = []

    return results

input_college_name = input("Enter college name: ")
search_results = search_college_in_database(input_college_name)

if search_results:
    for result in search_results:
        print("--------------------")
        print("College Name:", result[0])
        print("Abbreviation:", result[2])
        print("Location/Country:", result[1])
else:
    print("No matching results found in the database.")
