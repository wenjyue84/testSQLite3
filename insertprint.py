import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("INSERT INTO stocks VALUES ('2023-03-27', 'BUY', 'AAPL', 100, 130.00)")
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

conn.close()
