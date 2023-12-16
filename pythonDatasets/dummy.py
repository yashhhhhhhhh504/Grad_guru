import random
import faker
import csv

with open(r'C:\Users\aditi\OneDrive\Documents\Grad-guru\pythonDatasets\universities.txt', 'r', encoding='utf-8') as file:
    universities = [line.strip() for line in file.readlines()]

fake = faker.Faker()

alumni_data = []

def generate_unique_email(existing_emails):
    while True:
        email = fake.email()
        if email not in existing_emails:
            existing_emails.add(email)
            return email

generated_emails = set()

for _ in range(500):  
    name = fake.name()
    college = random.choice(universities)
    email = generate_unique_email(generated_emails)
    alumni_data.append([name, college, email])

with open('alumni_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'College', 'Email']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(alumni_data)

print("Alumni data has been generated and saved to 'alumni_data.csv'.")
