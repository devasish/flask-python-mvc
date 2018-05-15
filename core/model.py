'''
Created on 21-Aug-2017

@author:devas
'''
import pyodbc  # @UnresolvedImport
import datetime
from . import config
class Base(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
#         self.dbcon = pyodbc.connect("Driver={" + config.DATABASES['default']['OPTIONS']['driver'] + "};Server={" + config.DATABASES['default']['HOST'] + "};Database=" + config.DATABASES['default']['NAME'] + ";Uid=" + config.DATABASES['default']['USER'] + ";Pwd=" + config.DATABASES['default']['PASSWORD'])
        self.__dbcons = {}
        self.__con()
        

    def __con(self):
#         self.dbcon = pyodbc.connect("Driver={" + config.DATABASES['default']['OPTIONS']['driver'] + "};Server={" + config.DATABASES['default']['HOST'] + "};Database=" + config.DATABASES['default']['NAME'] + ";Uid=" + config.DATABASES['default']['USER'] + ";Pwd=" + config.DATABASES['default']['PASSWORD'])
        connection_alias_names = list(config.DATABASES.keys())
        for connection_alias in connection_alias_names:
            self.__dbcons[connection_alias] = pyodbc.connect("Driver={" + config.DATABASES[connection_alias]['OPTIONS']['driver'] + "};Server={" + config.DATABASES[connection_alias]['HOST'] + "};Database=" + config.DATABASES[connection_alias]['NAME'] + ";Uid=" + config.DATABASES[connection_alias]['USER'] + ";Pwd=" + config.DATABASES[connection_alias]['PASSWORD'], autocommit=True)
        
        
    def cursor(self, alias = 'default'):
        return self.__dbcons[alias].cursor()
    
    def assoc(self, cursor, dateasstr = True):
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        if dateasstr == True:
            return [dict(zip(columns, [str(item) if isinstance(item, (datetime.date, datetime.time)) else item for item in row])) for row in rows]
        else:
            return [dict(zip(columns, row)) for row in rows]
