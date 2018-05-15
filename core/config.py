'''
Created on 21-Aug-2017

@author: devasish ghosh
'''
import os

ENV_PRODUCTION = False
DATABASES = {
    'default': {
        'NAME': 'dbname1',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': '192.168.5.235',
        'USER': 'abc',
        'PASSWORD': 'xyz',
        'OPTIONS' : {
            'driver' : 'SQL Server Native Client 11.0'
        }
    },
    'another': {
        'NAME': 'dbname2',
        'ENGINE': 'sql_server.pyodbc',
        'HOST': '192.168.5.235',
        'USER': 'abc',
        'PASSWORD': 'xyz',
        'OPTIONS' : {
            'driver' : 'SQL Server Native Client 11.0'
        }
    }
}
 
HOST = os.environ.get('API_HOST') or '127.0.0.1'
PORT = 5050

