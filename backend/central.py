import os
import subprocess

folder_path = 'C:/Users/aditi/OneDrive/Documents/Grad-guru/Datasets' 
python_folder = 'C:/Users/aditi/OneDrive/Documents/Grad-guru/s3'

files = os.listdir(folder_path)
codes = os.listdir(python_folder)

csv_files = [file for file in files if file.endswith('.csv')]
python_files = [file for file in codes if file.endswith('.py')]

with open('C:/Users/aditi/OneDrive/Documents/Grad-guru/backend/missing.txt', 'w') as f:
    for csv_file in csv_files:
        csv = csv_file.split('.')[0]
        python = csv + '.py'
        if python not in python_files:
            f.write(csv + '\n')

path = 'C:/Users/aditi/OneDrive/Documents/Grad-guru/backend/missing.py'

if os.path.getsize(path) != 0:
    subprocess.run(['python', path])
