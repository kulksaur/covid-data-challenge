import threading
import time, sqlite3

# Class to create a thread for Data ingestion of Each County data.
class SQLiteThreadConnector(threading.Thread):

   def __init__(self, countyObject, dbConnection):
       threading.Thread.__init__(self)
       self.countyObject = countyObject
       self.con = dbConnection
       self.cursor = self.con.cursor()

   def run(self):
       # Table create query string
       executeCommandString = f"CREATE TABLE IF NOT EXISTS {self.countyObject.county}(test_date text,new_positives int, cumulative_number_of_positives int, total_number_of_tests int, cumulative_number_of_tests int, load_date text);"
       self.cursor.execute(executeCommandString)
       # Table insert query string
       insertQuery = f"INSERT INTO {self.countyObject.county} VALUES('{self.countyObject.test_date}', {self.countyObject.new_positives} , {self.countyObject.cumulative_number_of_positives}, {self.countyObject.total_number_of_tests} , {self.countyObject.cumulative_number_of_tests}, '{self.countyObject.load_date}');"
       self.cursor.execute(f"{insertQuery}")
