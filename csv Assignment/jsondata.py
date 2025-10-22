
print("------------------------------------------------------")


# PART A

import json

# Step 1: Create and write student details to a JSON file
students = {
    "students": [
        {"name": "nazia", "age": 20, "marks": 85},
        {"name": "yaram", "age": 22, "marks": 65},
        {"name": "Aazia", "age": 19, "marks": 90},
    ]
}

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)

# Step 2: Read JSON and print students with marks > 70
with open("students.json", "r") as f:
    data = json.load(f)

print("Students with marks > 70:")
for student in data["students"]:
    if student["marks"] > 70:
        print(student)

# Step 3: Convert JSON to string and print
json_string = json.dumps(data, indent=4)
print("\nJSON String:\n", json_string)







# PART B




import csv

# Step 1: Create and write product details to a CSV file
products = [
    {"id": 1, "name": "Laptop", "price": 1200, "quantity": 5},
    {"id": 2, "name": "Mouse", "price": 25, "quantity": 50},
    {"id": 3, "name": "Keyboard", "price": 45, "quantity": 30},
    {"id": 4, "name": "Monitor", "price": 700, "quantity": 8},
]

with open("products.csv", "w", newline="") as f:
    fieldnames = ["id", "name", "price", "quantity"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print(" products.csv created successfully!")

# Step 2: Read the CSV and calculate total values
total_value = 0
print("\nAll Products:")
with open("products.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        qty = int(row["quantity"])
        value = price * qty
        total_value += value
        print(f"{row['name']} → price: {price}, quantity: {qty}, total: {value}")

print(f"\n Total value of all products: {total_value}")

# Step 3: Print products with price > 500
print("\nProducts with price > 500:")
with open("products.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if float(row["price"]) > 500:
            print(row)

# Step 4: Append a new product
new_product = {"id": 5, "name": "Printer", "price": 400, "quantity": 10}
with open("products.csv", "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "price", "quantity"])
    writer.writerow(new_product)

print("\n New product appended successfully!")




# PART C



import csv
import json

# Create a CSV file with user details
users = [
    {"name": "Ali", "email": "ali@example.com", "age": 17},
    {"name": "Ayesha", "email": "ayesha@example.com", "age": 22},
    {"name": "Bilal", "email": "bilal@example.com", "age": 19},
    {"name": "Hina", "email": "hina@example.com", "age": 16},
]

with open("users.csv", "w", newline="") as f:
    fieldnames = ["name", "email", "age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(users)

print("users.csv created successfully!")

#  Read the CSV and select users with age > 18
selected_users = []

with open("users.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["age"]) > 18:
            selected_users.append(row)

#  Write filtered users to users.json
with open("users.json", "w") as f:
    json.dump(selected_users, f, indent=4)

print("\n Users with age > 18 written to users.json successfully!")

#  Display the written data
print("\nFiltered Users:")
for user in selected_users:
    print(user)