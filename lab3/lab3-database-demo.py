#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");

#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;

#now we create a cursor to work with db
cursor = dbconnect.cursor();
cursor2 = dbconnect.cursor();

#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data table 1
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature'] );

print("");

cursor2.execute('SELECT * FROM sensors');
#print data table 2
for row in cursor2:
    print(row['sensorID'],row['type'],row['zone']);

print("");


cursor2.execute('SELECT type FROM sensors WHERE zone="kitchen"');  
print("display all the sensors in the kitchen");
for row in cursor2:
    print(row['type']);

print("");
cursor2.execute('SELECT zone FROM sensors WHERE type="door"'); 
print("display all the door sensors");
for row in cursor2:
    print(row['zone']);



#close the connection
dbconnect.close();
