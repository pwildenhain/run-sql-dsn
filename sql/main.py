import pyodbc
from tabulate import tabulate

# Remember to start dev server before running script
# password is postgres
conn = pyodbc.connect("dsn=PostgreSQL30")

cursor = conn.cursor()

result = cursor.execute("select * from test_db.public.example_table").fetchall()

col_names = [column[0] for column in cursor.description]

col_names

print(tabulate(result, headers=col_names, tablefmt="grid"))

# think through what functions should look like, then think through basic tests
