import socket
from threading import Thread
from pyonr.converter import convert, PYON, OBJ
from pyonr import read
from os import listdir
from os.path import split, join

def algorithm(documents, _filter):
   return [d for d in documents if sum(1 for k, v in d.items() if _filter.get(k)==v) >= len(_filter)]

def findDatabases(path:str):
   return list(map(lambda e:join(path, e), filter(lambda e:e.endswith('.sdb'), listdir(path))))

def findDatabasePath(databases:list, dbname):

   for db in databases:
      dbFilename = split(db)[1]
      
      if dbFilename == dbname:
         return db

def send(data, adress):
   pass

def readfile(filepath):
   return read(filepath).read

def UDPServer(server:socket.socket, dbsPath:str):
   BUFFERSIZE = 1024
   ENCODING = ENCODING
   while True:
      dataLength, address = server.recvfrom(1024)

      if dataLength:
         data, address = server.recvfrom(int(dataLength))
         data = convert(PYON, OBJ, data.decode(ENCODING))

         dbName = data['dbName']

         if not dbName.endswith('.sdb'):
            dbName += '.sdb'

         dbs = findDatabases(dbsPath)
         dbRelPath = findDatabasePath(dbs, dbName)

         if data['type'] == 'get':
            _filter = data['data']

            with open(dbRelPath, 'r', encoding=ENCODING) as file:
               filedata = readfile(dbRelPath)
               wantedData = algorithm(filedata['__docs'], _filter)
               wantedData = None if not wantedData else wantedData[0]
               wantedData = str(wantedData).encode(ENCODING)
               server.sendto(wantedData, address)

         if data['type'] == 'getMany':
            _filter = data['data']

            with open(dbRelPath, 'r') as file:
               pass

def RunUDPServer(databasesPath:str, local:bool=True, port:int=5440):
   HOST = '0.0.0.0' if not local else '127.0.0.1'
   PORT = port
   ADDR = (HOST, PORT)

   server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   server.bind(ADDR)

   UDPServer(server, databasesPath)