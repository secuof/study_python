import psycopg2

# Connect to the DB
con = psycopg2.connect(
    host = "192.168.1.226",
    database = "clarity",
    user = "clarity",
    password = "clarity"
)

# Cursor
cur = con.cursor()

# Excute query
cur.execute("select package, version from processed limit 10")

rows = cur.fetchall()

for r in rows:
    print(f"id : {r[0]} || name : {r[1]}")

# Close the cursor
cur.close()

# Close the connection
con.close()
