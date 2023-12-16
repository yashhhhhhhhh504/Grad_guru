import csv
import os
import psycopg2
import subprocess

folder_path = 'C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets/'

with open('missing.txt', 'r') as f:
    for line in f:
        line = line.strip()
        file = line + '.csv'
        file_path = os.path.join(folder_path, file)

        if os.path.exists(file_path):
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                try:
                    header = next(reader)
                    columns = header
                    with open(f'C:/Users/aditi/OneDrive/Documents/Grad-guru/s3/{line}.py', 'w') as f:
                        f.write(f'import psycopg2\n')
                        f.write(f"""conn = psycopg2.connect(
                                    dbname="Grad-Guru",
                                    user="postgres",
                                    password="bunny2aug",
                                    host="localhost",
                                    port="5432"
                                )\n""")
                        f.write(f'cursor = conn.cursor()\n')
                        f.write(f'create_table_query = """CREATE TABLE IF NOT EXISTS {line} ({", ".join([f"{column} varchar(255)" for column in columns])})"""\n')
                        f.write(f'cursor.execute(create_table_query)\n')
                        f.write(f'conn.commit()\n')
                        f.write(f'with open("C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets/{file}", "r", encoding="latin1") as f:\n')
                        f.write(f'    cursor.copy_expert("COPY {line} FROM stdin WITH CSV HEADER", f)\n')
                        f.write(f'cursor = conn.cursor()\n')
                        f.write(f'alter_table_query = """ALTER TABLE {line}\n')
                        f.write(f'ADD COLUMN IF NOT EXISTS abbreviation VARCHAR(255);"""\n')
                        f.write(f'cursor.execute(alter_table_query)\n')
                        f.write(f'conn.commit()\n')
                        f.write(f'cursor.execute("SELECT University FROM {line}")\n')
                        f.write(f'college_names = cursor.fetchall()\n')
                        f.write(f'ignore_words = ["of", "and", "in", "for", "the", "a", "an", "on"]\n')
                        f.write(f'for name in college_names:\n')
                        f.write(f'    full_name = name[0]\n')
                        f.write(f'    full_name = re.sub(r"\\(.*?\\)", "", full_name)\n')
                        f.write(f'    words = re.findall(r"\\b\\w+\\b", full_name)\n')
                        f.write(f'    abbreviation = "".join(word[0].upper() for word in words if word.lower() not in ignore_words)\n')
                        f.write(f'    cursor.execute("UPDATE {line} SET abbreviation = %s WHERE University = %s", (abbreviation, name[0]))\n')
                        f.write(f'conn.commit()\n')
                        f.write(f'cursor.close()\n')
                        print(f"Created {line}.py")
                except StopIteration:
                    print(f"No header found in {file}")
        else:
            print(f"File not found: {file}")
        pythonpath = f'C:/Users/aditi/OneDrive/Documents/Grad-guru/s3/{line}.py'
        subprocess.run(['python', pythonpath])
