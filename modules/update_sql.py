import psycopg2 as pg2

PASSWORD = 'pass'

class Sql_update():
    def update(self, customer_id, balance):
        conn = pg2.connect(database='Bank', user='postgres',password=PASSWORD, host="localhost", port="5432")
        cur = conn.cursor()
        sql = f""" UPDATE bank_data
                SET balance = '{balance}'
                WHERE customer_id = '{customer_id}' """
        cur.execute(sql)
        conn.commit()
        cur.close()