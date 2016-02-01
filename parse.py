import csv
import sqlite3
import argparse

db = sqlite3.connect('../ACS.db')

def read(file):
	with open('names.csv') as csvfile:
    	reader = csv.DictReader(csvfile)
    	for row in reader:
        	write(row)
    csvfile.close()
    db.close()

def write(row):
	# TODO: parse specifics of CSV into format for write to db
	sql_statement = 'INSERT INTO acs_data(var_name, value, units, update_time, original_table) VALUES(' + row + '); \n'
	try:
        db.cursor.execute(row)
    except Exception as e:
        print "ERROR"
        print e


# TODO: use argparse to get file name from call of script (ie call "parse.py filename" in command line)