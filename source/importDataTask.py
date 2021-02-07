import urllib.request as request
import json
from County import County
import datetime
import ssl
import sqlite3
from SQLiteThreadConnector import SQLiteThreadConnector

# Fetch data from the URL
def fetchDataFromApi(url):
    context = ssl._create_unverified_context()
    with request.urlopen(url, context=context) as response:
        source  = response.read()
        fetchDataResponse = json.loads(source)
    return fetchDataResponse

# Get and return all the Column list from the meta Object of Response
def getAllColumnsFromResponse(metaObject):
    columnObjectList = metaObject["view"]["columns"]
    columnNameList = []
    for column in columnObjectList:
        columnNameList.append(str(column["fieldName"]))
    return columnNameList


# Construct and return data dictionary for easier iteration and creation of County objects
def constructRequiredDataDictionary(dataObject,allColumnList, actualColumnStartIndex):
    dataDictionary = {"columns":allColumnList[actualColumnStartIndex:], "data": []}
    for row in dataObject:
        dataDictionary["data"].append(row[actualColumnStartIndex:])
    return dataDictionary


# Return a Object Mapping dictionary with Key as County Name and County Object List as value
# Using a County Object List as value if needs a scaling w.r.t adding Historic data as well in the DB
def getCountyObjectMapping(dataDictionary):
    countyObjectMapping = {}
    for rowData in dataDictionary["data"]:
        rowData[0] = rowData[0].replace("T", " ")
        testDate = datetime.datetime.strptime(rowData[0], "%Y-%m-%d %H:%M:%S")
        currentDate = datetime.datetime.now()
        if abs(currentDate - testDate).days == 2:
            countyData = {}
            for index, row in enumerate(rowData):
                countyData[dataDictionary["columns"][index]] = row
            # Add the today's date for Load date
            countyData["load_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            countyData["county"] = countyData["county"].replace(" ","").replace(".","")
            county = County(**countyData)
            # Remove any extra spaces in the countyName
            if not county.__getattribute__("county") in countyObjectMapping.keys():
                countyObjectMapping[county.__getattribute__("county")] = [county]
            elif not county in countyObjectMapping[county.__getattribute__("county")]:
                countyObjectMapping[county.__getattribute__("county")].append(county)

    return countyObjectMapping
   
# Create and return a SqLite connection object and treat it as a Inmemory, pass it to Multithreaded function for shared use
def getSQLiteConnection():
    conn = sqlite3.connect('file:CoviData?mode=memory&cache=shared', uri=True, check_same_thread=False, isolation_level=None)
    return conn


# Start threading and ingest data in Inmemory database
def startThreadsForIngestingData(countyObjectMapping, dbConnection):
    listThreads = []
    for countyObjectList in countyObjectMapping.values():
        thread = SQLiteThreadConnector(countyObjectList[0], dbConnection)
        thread.start()
        listThreads.append(thread)

    print("*********Threads for all the counties have been started to create and insert data*********")

    for t in listThreads:
        print(f"Data has been loaded for the county: {t.countyObject.county}")
        t.join()

    print("*********All the threads have finished their execution*********")


# Close the DB Connection once all the threads complete execution
def closeDbConnection(dbConnection):
    dbConnection.close()

if __name__ == "__main__":
    # Fetch the Data and constuct a data structure for Ingesting into DB
    fetchDataResponse = fetchDataFromApi("https://health.data.ny.gov/api/views/xdss-u53e/rows.json?accessType=DOWNLOAD")
    allColumnList = getAllColumnsFromResponse(fetchDataResponse["meta"])
    actualColumnStartIndex = len(allColumnList) - 6
    dataObject = fetchDataResponse["data"]
    dataDictionary = constructRequiredDataDictionary(dataObject, allColumnList, actualColumnStartIndex)
    countyObjectMapping = getCountyObjectMapping(dataDictionary)
    dbConnection = getSQLiteConnection()
    startThreadsForIngestingData(countyObjectMapping, dbConnection)
    closeDbConnection(dbConnection)

