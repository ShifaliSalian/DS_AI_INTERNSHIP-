# # File handling in Python
# file = open("sample.txt","w")
# file.write("Hello, this is a file handling example.")
# file.close()

# file = open("sample.txt","r")
# content = file.read()
# print(content)
# file.close()

# # context manager
# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)

# # Error handling with try/except
# try:
#     with open("missing.txt","r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found. Please check the filename.")

# # CSV file handling
# import csv
# with open("data.csv","r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[0])  

# #excel file handling using openpyxl library
# import openpyxl
# workbook = openpyxl.load_workbook("data1.xlsx")
# sheet = workbook.active  
# for row in sheet.iter_rows(values_only=True):
#     print(row)

# # Task 1
# name = input("Enter your name: ")
# goal = input("Enter your daily goal: ")

# with open("journal.txt", "a") as file:
#     file.write(name + " - " + goal + "\n")

# # Task 2
# import csv
# with open("students.csv","r") as file:
#     reader=csv.reader(file)
#     print("Students who passed:")
#     for row in reader:
#         if row[2] == "Pass":
#             print(row[0])

# Task 3
filename = input("Enter the filename to open: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        print("File contents:\n")
        print(content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")