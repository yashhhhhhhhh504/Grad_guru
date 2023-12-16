import subprocess

print("Welcome to Grad-Guru Trial Version")
print("""Choose an action:
1. Search University
2. Search Course
3. Compare Universities
4. Career Exploration
5. Admission Requirements
6. Fee Structure
""")

choice = input("Enter choice: ")

if choice == '1':
    subprocess.run(['python', 'backend\searchAlgo.py'])
elif choice == '2':
    subprocess.run(['python', 'backend\programSearch.py'])