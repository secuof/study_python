import psycopg2

def pg():
    pgcon = psycopg2.connect("host='192.168.1.226' port='5432' dbname=''")

    pgcur = pgcon.cursor()
    try:
        pgcur.excute("SELECT * from processed")
        for result in pgcur:
            print(result)
        except psycopg2.DatabaseError, e:
            print('%s' % e)
        conn.close()

if __name__ == "__main__":
    pg()

