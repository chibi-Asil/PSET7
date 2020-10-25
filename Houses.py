## TODO
# In import.py, write a program that imports data from a CSV spreadsheet.
# Implement a program that identifies a person based on their DNA, per the below.
import cs50 
from cs50 import SQL
# Documentation for argparse can be found at: https://docs.python.org/3.3/library/argparse.html
# Python's sys module gives you access to sys.argv for command-line arguments
import sys
from sys import argv, exit
# Python's csv module has reader and DictReader
import csv 
from csv import writer, reader

def main():
    i = import_csv()

def import_csv():
    # Your program should accept the name of a CSV file as a command-line argument.
    if (len(argv) != 2):
        print("Please provide me with the csv file.")
        sys.exit(1)
    # We will also want to open the database
    # https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
    open("students.db", "w").close()
    db = SQL("sqlite:///students.db")
    
    # If they input in the correct csv file, it should open
    # We included "w" instead of "r" because we want to change the middle_inital if it is empty
    with open(argv[1], "r") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = ",")
    # According to the Lecture Notes, we will need to iterate over the rows so that when there is no middle name, we will need to put it down as a NULL character
        for row in csv_reader:
        # We should create an empty list so we can populate the missing data. When I went over SELECT * FROM students, it was missing data
            name = row["name"]
            delination_name = []
        # From the looks of it, we will need to split the names based on the first 3 - based on space and then populate the middle if there is no value
        for splitting_names in row["name"].split(" "):
            delination_name.append(splitting_names)
        
        # After this, we will need to input it into the database
        # The code should come from Lecture 7
        if len(delination_name) == 2:
            first_name = delination_name[0]
            surname = delination_name[1]
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first_name, None, surname, row["house"], row["birth"])
            
        elif len(delination_name) == 3:
            first_name = delination_name[0]
            middle_name = delination_name[1]
            surname = delination_name[2]
            db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first_name, middle_name, surname, row["house"], row["birth"])


if __name__ == "__main__":
    main()
