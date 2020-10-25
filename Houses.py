# TODO - IMPORT.PY
# https://cs50.harvard.edu/x/2020/psets/7/houses/
# In import.py, write a program that imports data from a CSV spreadsheet.
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
    db = SQL("sqlite:///students.db")
    
    # If they input in the correct csv file, it should open
    # We didn't include the "r" because the default is "r"
    with open(argv[1]) as csv_file:
        csv_reader = csv.DictReader(csv_file)
    # According to the Lecture Notes, we will need to iterate over the rows so that when there is no middle name, we will need to put it down as a NULL character
        for row in csv_reader:
        # We should split the row["name"] 
            name = row["name"]
            delination_name = name.split()
        
        # After this, we will need to input it into the database
        # The code should come from Lecture 7
            if len(delination_name) == 2:
                first_name = delination_name[0]
                surname = delination_name[1]
                db.execute("INSERT INTO students ('first', 'middle', 'last', 'house', 'birth') VALUES(?, ?, ?, ?, ?)", first_name, None, surname, row["house"], row["birth"])
            
            elif len(delination_name) == 3:
                first_name = delination_name[0]
                middle_name = delination_name[1]
                surname = delination_name[2]
                db.execute("INSERT INTO students ('first', 'middle', 'last', 'house', 'birth') VALUES(?, ?, ?, ?, ?)", first_name, middle_name, surname, row["house"], row["birth"])
            


if __name__ == "__main__":
    main()

# TODO - ROSTER.PY
# https://cs50.harvard.edu/x/2020/psets/7/houses/
# In roster.py, write a program that prints a list of students for a given house in alphabetical order.

import cs50
from cs50 import SQL
import sys
from sys import argv, exit
import csv 
from csv import reader

def main():
    i = roster()
    
def roster():
    # Your program should accept the name of a house as a command-line argument.
    if len(argv) != 2: 
        print("Please input in the correct House name.")
        sys.exit(1)
    
    # We will also want to open the database. Code could be found from Lecture 7 notes
    # Your program should query the students table in the students.db database for all of the students in the specified house.
    db = SQL("sqlite:///students.db")
    
    # It looks like we do not need to set a argv[1] other than setting it as a house name. Tried to put it argv2 but it would not let me. So I'm assuming that when we do the check, python roster.py <house_name>, the house name will be argv[1]
    # We want to make it case sensitive in case someone puts down GRYFFINDOR / gryffindor instead of Gryffindor
    house_name = argv[1].islower()
    
    # Your program should then print out each student’s full name and birth year (formatted as, e.g., Harry James Potter, born 1980 or Luna Lovegood, born 1981).
    students_info = db.execute("SELECT DISTINCT * FROM students WHERE house = (?) ORDER BY last, first ASC", argv[1])
    
    # We need to print out the values
    for row in students_info: 
        if row["middle"] == None:
            print(row["first"] + " " + row["last"] + ", " + "born" + " " + str(row["birth"]))
        
        else:
            print(row["first"] + " " + row["middle"] + " " + row["last"] + ", " + "born" + " " + str(row["birth"]))
    

if __name__ == "__main__":
    main()

 
