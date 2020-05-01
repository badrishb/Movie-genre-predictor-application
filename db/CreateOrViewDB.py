import sqlite3

# """
# this is the code for
# creating the USER TABLE
# """
# conn = sqlite3.connect('db/movie.db')
# conn.execute('''CREATE TABLE login
#          (
#          EMAILID TEXT  NOT NULL,
#          PASSWORD TEXT NOT NULL,
#          PRIMARY KEY(EMAILID));''')
# conn.commit()

# conn = sqlite3.connect('db/movie.db')
# conn.execute('''INSERT into login values('admin@gmail.com','redwood');''')
# conn.commit()

# conn.execute('''CREATE TABLE USER
#          (EMAIL TEXT PRIMARY KEY     NOT NULL,
#          FIRSTNAME           TEXT    NOT NULL,
#          LASTNAME           TEXT    NOT NULL,
#          PHONE            INT     NOT NULL,
#          PASSWORD        TEXT    NOT NULL
#          );''')

# print("User table created successfully")
# """
# this is the code for
# creating the SCHEDULE TABLE
# """
# conn = sqlite3.connect('db//exam.db')

# conn.execute('''CREATE TABLE fdbk
#          (EMAIL TEXT PRIMARY KEY     NOT NULL,
#          name           TEXT    NOT NULL,
#          feedBack          TEXT    NOT NULL
#          );''')
# conn.commit()

# print("User table created successfully")
# conn = sqlite3.connect('db//exam.db')
# cl=conn.cursor()
# cl.execute('''
# select * from fdbk
#          ''')
# print(cl.fetchone())
# """
# this is the code for
# creating the SCHEDULE TABLE
# """
# conn = sqlite3.connect('exam.db')
# #
# conn.execute('''CREATE TABLE SCHEDULE
#          (EMAIL TEXT    NOT NULL,
#          EDATE  TEXT    NOT NULL,
#          ETIME  TEXT    NOT NULL,
#          EID    Text    NOT NULL,
#          SLOT   TEXT    NOT NULL
#          );''')
# #
# print("Schedule table created successfully")

# """
# this is the code for
# creating the AVAILABILITY TABLE
# """
# conn = sqlite3.connect('exam.db')
# #
# conn.execute('''CREATE TABLE AVAILABILITY
#          (EMAIL TEXT  NOT NULL,
#          EXAMID TEXT  NOT NULL,
#          SLOT TEXT NOT NULL,
#          AVAILABLE  TEXT    NOT NULL,
#          PRIMARY KEY(EMAIL, EXAMID, SLOT));''')
# #
# print("Availability table created successfully")

# """
# this is the code for
# displaying the USER TABLE
# """
# conn = sqlite3.connect('exam.db')
#
# cursor = conn.execute("SELECT EMAIL,FIRSTNAME,LASTNAME,PHONE,PASSWORD from USER")
# #
# no = 0
# for row in cursor:
#     print(f"User {no+1}:")
#     print("EMAIL = ", row[0])
#     print("FIRSTNAME = ", row[1])
#     print("LASTNAME = ", row[2])
#     print("PHONE = ", row[3])
#     print("PASSWORD = ", row[4], "\n\n")
#     no += 1

# """
# this is the code for
# displaying the SCHEDULE TABLE
# """
# conn = sqlite3.connect('exam.db')
# #
# cursor = conn.execute("SELECT EMAIL,EDATE,ETIME,EID,SLOT from SCHEDULE")
# #
# for row in cursor:
#     print("EMAIL = ", row[0])
#     print("EDATE = ", row[1])
#     print("ETIME = ", row[2])
#     print("EID = ", row[3])
#     print("SLOT = ", row[4], "\n\n")

# """
# this is the code for
# displaying the Availability TABLE
# """
# conn = sqlite3.connect('exam.db')

# cursor = conn.execute("SELECT EMAIL,EXAMID,SLOT,AVAILABLE from AVAILABILITY")
#
# for row in cursor:
#     print("EMAIL = ", row[0])
#     print("EXAMID = ", row[1])
#     print("SLOT = ", row[2])
#     print("AVAILABLE = ", row[3], "\n\n")

# """
# this is the code for
# droping tables
# """
# conn = sqlite3.connect('exam.db')
# conn.execute("DROP TABLE AVAILABILITY;")
# conn.commit()
# """
# this is the code for
# displaying the Availability TABLE
# """
# conn = sqlite3.connect('exam.db')
# #
# cursor = conn.execute("SELECT EMAIL,name,feedback from fdbk")
# #
# for row in cursor:
#     print("EMAIL = ", row[0])
#     print("name = ", row[1])
#     print("feedback = ", row[2], "\n\n")


# conn = sqlite3.connect('exam.db')
# conn = sqlite3.connect('exam.db')

# conn.execute('''CREATE TABLE REQUEST
#          (EMAILF TEXT NOT NULL,
#          EMAILT TEXT NOT NULL,
#          EXAMID TEXT NOT NULL,
#          DATE  TEXT NOT NULL,
#          TIME INT NOT NULL,
#          SLOT TEXT NOT NULL,
#          APPROVED TEXT NOT NULL,
#          PRIMARY KEY(EMAILF, EMAILT, DATE, TIME, SLOT));''')
#
# cursor = conn.execute("SELECT * from REQUEST")
# for row in cursor:
#     print('Email from: ', row[0])
#     print('Email to: ', row[1])
#     print('Exam: ', row[2])
#     print('date: ', row[3])
#     print('time: ', row[4])
#     print('slot: ', row[5])
#     print('approved: ', row[6])
#
#
# conn = sqlite3.connect('exam.db')
# conn.execute("DELETE FROM REQUEST;")
# conn.commit()


# conn = sqlite3.connect('exam.db')
# conn.execute("DROP TABLE REQUEST;")
# conn.commit()
