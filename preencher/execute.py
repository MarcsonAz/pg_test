import psycopg2
import dbinfo
import helper

query = helper.SQL
conn = dbinfo.conn

cur = conn.cursor()

for i in helper.teste:
    cur.execute(query,helper.new_data())

cur.execute("select * from covid19onlinebeta")

rows = cur.fetchall()

for r in rows:
   print(r)


# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()