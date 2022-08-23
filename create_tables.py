import sqlite3

conn = sqlite3.connect('school.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE students
          (id INTEGER PRIMARY KEY ASC,
           timestamp DATETIME NOT NULL,
           first_name VARCHAR(250) NOT NULL,
           last_name VARCHAR(250) NOT NULL,           
           username VARCHAR(20) NOT NULL
          )
          ''')

conn.commit()
conn.close()
