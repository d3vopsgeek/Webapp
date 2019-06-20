import psycopg2
# It is the most standard library to connect to PostgreSQL

DB_NAME = "ISAC"
DB_USER = "postgres"
DB_PASS = "123456"
DB_HOST = "localhost"
DB_PORT = "5432"


# conn = psycopg2.connect(
#    database="ISAC",
#    user="postgres",
#    password="123456",
#    host="localhost",
#    port="5432"
# ()

try:
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
    cur = conn.cursor()
    # cur.execute("INSERT INTO locations (locationid, locationdesc) VALUES (1,'Puebla')")
    cur.execute("SELECT locationid, locationdesc from locations")

    rows = cur.fetchall()
    for r in rows:
        print(f"locationid: {r[0]} locationdesc: {r[1]} ")
    # conn.commit()
    # close the cursor
    cur.close()
    conn.close()
except psycopg2.OperationalError as e:
    print("Unable to connect or something went wrong during connection")
