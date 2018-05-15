'''
Created on 18-Aug-2017

@author: devasish ghosh
'''
from core import model
class Friend(model.Base):
    '''
    classdocs
    '''
    validation_rules = {
        'field1' : {
            'type' : 'String',
            'max_length' : 5,
            'min_length' : 1,
            'operation' : ['trim', 'upper', 'lower'],
            'msg' : 'must be an string',
            'required' : False,
            'default' : None
        },
        'field2': {
            'type' : 'Int',
            'max' : 100,
            'min' : 10 ,
            'operation' : ['floor', 'ceiling'],
            'msg' : 'must be a real number'
        },
        'field3' : {
            'type' : 'Email',
            'required': True
        },
        'field4' : {
            'type' : 'Regex',
            'regex' : r'[0-9]{3}',
            'msg' : 'Must be a 3 digit number',
            'required': True
        },
        'field5' : {
            'type' : 'Custom',
            'validator' : lambda x: x 
        },
        'field6' : {
            'type' : 'Pin',
            'required' : True
        },
        'field7' : {
            'type' : 'Set',
            'set'  : {'a', 'b', 'hello', '1', '234'},
            'case' : False,
            'default': 'a'
        },
        'field8' : {
            'type' : 'Bit'
        },
        'field9' : {
            'type' : 'Mobile',
            'required': True
        },
                        
    }
    
    validation_rules2 = {
        'f1' : {
            'type' : 'Bit'
        },
        'f2' : {
            'type' : 'Mobile',
            'required': True
        },
    }

    def __init__(self):
        '''
        Constructor
        '''
        model.Base.__init__(self)
        
        
    
    def test(self):
        cursor = self.cursor('ssspl')
        query = "SELECT * FROM SSSPL.Kiosk.tblKiosk"
        cursor.execute(query)
        return self.assoc(cursor)
        rows = cursor.fetchall()
    
        return [list(row) for row in rows]
        