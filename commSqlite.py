import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

print("Opened database successfully")

cursor = c.execute("SELECT date, time, ecg from Records where serialno = 23")

for row in cursor:
    print("ECG = ", row[2][:14])
    print("\n")

print("Operation done successfully")
conn.close()


    # print("Date = ", row[0])
    # print("Time = ", row[1])