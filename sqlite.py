import sqlite3
import re

conn = sqlite3.connect('counts.sqlite')  # create a new db

cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Counts''')

cur.execute('''
    CREATE TABLE Counts (org TEXT, count INTEGER)
''')

fname = input('Enter file name: ')

fh = open(fname, 'r')

for line in fh:
    org = re.findall(r'From: \S*@(\S*)', line)

    if not org:
        continue

    org = org[0]

    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))

    row = cur.fetchone()

    if row is None:
        cur.execute('''
            INSERT INTO Counts(org, count)
            VALUES (?, 1)
        ''', (org,))
    else:
        cur.execute('''
            UPDATE Counts
            SET count = count + 1
            WHERE org = ?
        ''', (org,))

conn.commit()
cur.close()
