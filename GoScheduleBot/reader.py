import os
import psycopg2

from psycopg2 import Error

USER = os.environ.get('POSTGRES_GOBOT_USER')
PASS = os.environ.get('POSTGRES_GOBOT_PASS')

class DbReader:
    def __init__(
        self,
        database='postgres',
        host='127.0.0.1',
        port='5432'
    ):
        self.database = database
        self.host = host
        self.port = port


    # TODO: Makes sense to have this be a decorator
    def open_connection(self, username, password):
        '''
        Return a Postgres connection object.
        '''
        connection = None

        try:
            connection = psycopg2.connect(database=self.database, user=username, password=password, host=self.host, port=self.port)
            return connection

        except (Exception, psycopg2.Error) as e:
            print("Error attempting to connect to Postgres:", e)
            if connection:
                connection.close()


    def read_routes(self):
        conn = None

        try:
            conn = self.open_connection(USER, PASS)
            cursor = conn.cursor()
            cursor.execute('select * from gobot.routes_test')
            all_routes = cursor.fetchall()

            for r in all_routes:
                print(r[0], r[1], r[2], "\n")
        finally:
            if conn:
                conn.close()


    def update_routes(self):
        pass


    def read_stops(self):
        pass


    def update_stops(self):
        pass


    def read_times(self):
        pass


    def update_times(self):