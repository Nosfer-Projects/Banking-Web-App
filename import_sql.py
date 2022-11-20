import psycopg2 as pg2

PASSWORD = 'password'
class Sql_import():
    def data(self, customer_id):
        customer_data = []
        conn = pg2.connect(database='Bank', user='username',password=PASSWORD, host="localhost", port="5432")
        cur = conn.cursor()
        sql = f''' SELECT * FROM bank_data
                WHERE customer_id = '{customer_id}' '''
        cur.execute(sql)
        data_row = cur.fetchone()
        for i in data_row:
            if str(i).isdigit():
                customer_data.append(i)
            else:   
                i = i.strip(" ")
                customer_data.append(i)
        conn.close()
        cur.close()   
        return customer_data

