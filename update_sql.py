import psycopg2 as pg2

PASSWORD = 'password to database'

class Sql_update():
    """
    After making the transfer, the data on the current account balance are modified by deducting the amount from the transfer.
    """
    def update(self, customer_id, balance):
        conn = pg2.connect(database='Bank', user='user name',password=PASSWORD, host="localhost", port="5432")
        cur = conn.cursor()
        sql = f""" UPDATE bank_data
                SET balance = '{balance}'
                WHERE customer_id = '{customer_id}' """
        cur.execute(sql)
        conn.commit()
        cur.close()
