import psycopg2

colleges_to_search = ["University", "college"]
program_search = ["Program", "name"]

db_params = {
    "host": "localhost",
    "database": "Grad-Guru",
    "user": "postgres",
    "password": "bunny2aug"
}

def search_college_in_database(input_college_name):
    result = []
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()
    cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    
    for table in cur.fetchall():
        table_name = table[0]
        cur.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
        columns = [col[0] for col in cur.fetchall()]
        
        col_name = None
        prog = None

        for col_name in colleges_to_search:
            if col_name in columns:
                if any(prog_name in columns for prog_name in program_search):
                    prog = next((prog_name for prog_name in program_search if prog_name in columns), None)
                    break
        
        if col_name is not None and prog is not None:
            query = f"SELECT {col_name}, {prog} FROM {table_name} WHERE {prog} ILIKE %s"
            query_params = [f"%{input_college_name}%"]
            cur.execute(query, query_params)
            result = cur.fetchall()

    return result

input_college_name = input("Enter Course: ")
search_results = search_college_in_database(input_college_name)

if search_results:
    for result in search_results:
        print("--------------------")
        print("College Name:", result[0])
        print("Program Name:", result[1])
else:
    print("No matching results found in the database.")
