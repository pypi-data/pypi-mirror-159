import mysql.connector
import pandas as pd
from typing import List
import time


class MySqlConnection:
    def __init__(self, user: str = 'root', password: str = 'password', host: str = '127.0.0.1', database: str = 'sys',
                 print_session_details: bool = False):
        self.__connection = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.__cursor_connection = self.__connection.cursor()
        self.__user = user
        self.__password = password
        self.__host = host
        self.__database = database
        self.__print_session_details = print_session_details
        self.__q_name = None
        self.__start = None
        self.__finish = None

    def __calculate_time(self, query_name):
        result = round(self.__finish - self.__start, 2)
        print(f'|| --------- Query Name: {query_name}, Finished in {result} second(s) --------- ||')
        return result

    def __cursor_connection_test(self):
        try:
            if self.__connection.is_connected():
                return
            else:
                self.__connection = mysql.connector.connect(user=self.__user, password=self.__password,
                                                            host=self.__host, database=self.__database)
                self.__cursor_connection = self.__connection.cursor()
        except Exception as e:
            print(e)

    def get_data(self, query: str, q_name: str = None, return_data_frame: bool = False, close_connection: bool = False):
        try:
            self.__start = time.perf_counter()
            self.__cursor_connection_test()
            self.__cursor_connection.execute(query)
            data_result = list(self.__cursor_connection.fetchall())
            if close_connection:
                self.close_connection()
            self.__finish = time.perf_counter()
            if self.__print_session_details:
                self.__calculate_time(query_name=q_name)
            if not return_data_frame:
                return data_result, self.__cursor_connection.column_names
            else:
                return pd.DataFrame(data=data_result, columns=self.__cursor_connection.column_names)
        except Exception as e:
            raise print(e, query)

    def manipulate_data(self, query: str, q_name: str = None, data: List[tuple] = None, is_list: bool = True,
                        update_data: bool = False, close_connection: bool = False):
        try:
            self.__start = time.perf_counter()
            self.__cursor_connection_test()
            if is_list and not update_data:
                self.__cursor_connection.executemany(query, data)
            elif not update_data:
                self.__cursor_connection.execute(query, data)
            else:
                self.__cursor_connection.execute(query)
            self.__connection.commit()
            if close_connection:
                self.close_connection()
            self.__finish = time.perf_counter()
            if self.__print_session_details:
                self.__calculate_time(query_name=q_name)
        except Exception as e:
            self.close_connection()
            raise print(e)

    def close_connection(self):
        try:
            self.__connection.close()
        except Exception as e:
            raise print(e)
