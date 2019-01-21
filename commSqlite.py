import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

print("Opened database successfully")

cursor = c.execute("SELECT date, time, ecg from Records where serialno = 23")

index = 0
for row in cursor:
    while index < len(row[2]):
        data = row[2][index] << 6 | row[2][index + 1]    
        print(data+"\n")
        index += 2

print("Operation done successfully")
conn.close()


# for row in cursor:
    # print("Date = ", row[0])
    # print("Time = ", row[1])
    # print("ECG = ", row[2][:2])
    # print("\n")