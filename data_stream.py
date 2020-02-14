import urllib.request
import json
import sqlite3
from sqlite3 import Error

class Datastream():
    def __init__(self, api_url, api_location):
        self.timestamp = None
        self.chartname = None
        self.USD_rate = None
        self.EUR_rate = None
        self.api_url = api_url
        self.api_location = api_location

        # all the available api_locations which we can use to access the data
        self.list_of_api_locations = ['coindesk', 'test1', 'test2']

        # here we initialize the database name and the current status of the connection to the database
        self.database = "database.db"
        self.conn = None

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.database)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def close_connection(self):
        self.conn.close()

    # this is the data collection specific for coindesk
    def collect_data_coindesk(self):
       
        btc_data = urllib.request.urlopen(self.api_url).read() 
        btc_data = btc_data.decode()
        btc_data = json.loads(btc_data)

        self.timestamp = btc_data['time']['updated']
        self.chartname = btc_data['chartName']
        self.USD_rate = btc_data['bpi']['USD']['rate']
        self.EUR_rate = btc_data['bpi']['USD']['rate']
    

        print("timestamp = ", self.timestamp)
        print("#########################")
        print("chartname = ", self.chartname)
        print("#########################")
        print("USD_rate = ", self.USD_rate)
        print("#########################")
        print("EUR_rate = ", self.EUR_rate)

    # Here we select which method we are going to use to collect the data
    def collect_data(self):
        if self.api_location == "coindesk":
            self.collect_data_coindesk()

        # here we write other statements and we can write new methods 
        # to collect data from other api's

   
    # def setup_database(self):
    #     c = self.conn.cursor()
    #     #c.execute("""CREATE DATABASE Cryptodata;""")
    #     for item in self.list_of_api_locations:
    #         c.execute("""CREATE TABLE {} (
    #             LastName varchar(255)
    #             );""".format(item))

    def database_push(self):
        pass

def main():
    Agent = Datastream(api_url="https://api.coindesk.com/v1/bpi/currentprice.json", api_location="coindesk")
    Agent.create_connection()
    Agent.collect_data()
    print("##########################")
    print(Agent.api_location)
    #print(Agent.timestamp)
    Agent.close_connection()
    #Agent.database_push()

main()









# def create_connection(db_file):
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
#         dataPush()
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()

# def dataPush(timestamp, chartname, USD_rate, EUR_rate):

# if __name__ == '__main__':
#     create_connection("database.db")