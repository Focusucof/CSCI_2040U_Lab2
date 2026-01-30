import csv

# wrapper functions for CSV interaction
# ======================================================
def read_csv(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        data = [row for row in csv_reader]
    return data

# Appends an array as a new row to the CSV file
def append_csv(file_path, row):
    with open(file_path, mode='a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(row)
# ======================================================

# read
def get_data():
    return read_csv('db.csv')

# add array as new row to CSV
# create
def add_data(row):
    append_csv('db.csv', row)

# update a specific row by index
# update
def update_data(index, new_row):
    data = read_csv('db.csv')
    if 0 <= index < len(data):
        data[index] = new_row
        with open('db.csv', mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

# delete
def delete_data(index):
    data = read_csv('db.csv')
    if 0 <= index < len(data):
        del data[index]
        with open('db.csv', mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)

def load_through():
    catalog = []
    with open ("db.csv", newline = "", encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            catalog.append({
                "genre": row["Genre"],
                "title": row["Movie Title"],
                "release_year": int(row["Release Date"])
            })
    print(catalog)

def display_catalog():
    data = get_data()
    header, *rows = data
    print(f"{header[0]:<5}{header[1]:<15}{header[2]}")
    print ("-" * 40)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<15}{row[2]}")