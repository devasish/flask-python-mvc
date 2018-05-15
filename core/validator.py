'''
Created on 23-Aug-2017

@author: devasish ghosh
'''
import re
import datetime

class Operation(object):
    def __init__(self):
        pass
    
    @staticmethod
    def trim():
        pass

class String(object):
    
    def __init__(self):
        '''
        constructor
        '''
    @staticmethod
    def default_value(rules):
        return rules.get('default', "")
    
    @staticmethod
    def check(rules, value):
        op = {}
        required = rules.get('required', False)
        
        # Take care when it is None. str(None) returns 'None' so on trying this no exception will generate         
        if value  is None:
            if required is True:
                return False, {'type_error' : 'not a string'}, None
            else:
                return True, {'warning' : 'default value set'}, String.default_value(rules)
        
        try:
            value = str(value)
        except:
            # case: when not a string convertible input
            if required is True:
                return False, {'type_error' : 'not a string'}, None
            else:
                return True, {'warning' : 'default value set'}, String.default_value(rules)
        else:
            # Case : when a valid string is input
            is_valid = isinstance(value, str)
            if required is True or (isinstance(value, str) and len(value) > 0) :
                
                if rules.get('max_length', None) is not None:
                    is_max_length_valid = String.max_length(rules['max_length'], value)
                    is_valid = is_valid and is_max_length_valid
                    if not is_max_length_valid:
                        op['max_length_error'] = 'maximum length allowed is ' + str(rules['max_length']) 
                
                if rules.get('min_length', None) is not None:
                    is_min_length_valid = String.min_length(rules['min_length'], value)
                    is_valid = is_valid and is_min_length_valid
                    if not is_min_length_valid:
                        op['min_length_error'] = 'minimum length allowed is ' + str(rules['min_length'])
                
                return is_valid, op, value
            else:
                # If not compulsory field just check max length
                if rules.get('max_length', None) is not None:
                    is_max_length_valid = String.max_length(rules['max_length'], value)
                    is_valid = is_valid and is_max_length_valid
                    if not is_max_length_valid:
                        op['max_length_error'] = 'maximum length allowed is ' + str(rules['max_length'])
                    
                    return is_valid, op, value
                else:        
                    return True, {}, value
    
    
    @staticmethod    
    def max_length(max_len, value):
        return True if isinstance(value, str) and len(value) <= max_len else False
        
    @staticmethod
    def min_length(min_len, value):
        return True if isinstance(value, str) and len(str(value)) >= min_len else False

class Int(object):
    
    def __init__(self):
        '''
            constructor
        '''
        
    @staticmethod
    def default_value(rules):
        return rules.get('default', 0)
    
    @staticmethod
    def operation():
        pass
    
    @staticmethod
    def check(rules, value):
        op = {}
        required = rules.get('required', False)
        
        try:
            value = int(value)
        except:
            # case: when not a integer convertible input
            if required is True:
                return False, {'type_error' : 'Not an integer', 'value' : str(value)}, None
            else:
                return True, {'warning' : 'default value set'}, Int.default_value(rules) 
        else:
            is_valid = True
            
            if rules.get('max', None) is not None:
                is_max_valid = Int.max(rules['max'], value)
                is_valid = is_valid and is_max_valid
                if not is_max_valid:
                    op['max_val_error'] = 'maximum value allowed is ' + str(rules['max'])
            
            if rules.get('min', None) is not None:
                is_min_valid = Int.min(rules['min'], value)
                is_valid = is_valid and is_min_valid
                if not is_min_valid:
                    op['min_val_error'] = 'minimum value allowed is ' + str(rules['min'])
            
            return is_valid, op, value
    
    @staticmethod
    def max(max_val, value):
        return True if value <= max_val else False
    
    @staticmethod
    def min(min_val, value):
        return True if value >= min_val else False

class Float(object):
    
    def __init__(self):
        '''
            constructor
        '''
    @staticmethod
    def default_value(rules):
        return rules.get('default', 0)
    
    @staticmethod
    def operation():
        pass
    
    @staticmethod
    def check(rules, value):
        op = {}
        required = rules.get('required', False)
        
        try:
            value = float(value)
        except:
            if required is True:
                return False, {'type_error' : 'Not a float'}, None
            else:
                return True, {'warning' : 'default value set'}, Float.default_value(rules)
        else:
            is_valid = True
            
            if rules.get('max', None) is not None:
                is_max_valid = Float.max(rules['max'], value)
                is_valid = is_valid and is_max_valid
                if not is_max_valid:
                    op['max_val_error'] = 'maximum value allowed is ' + str(rules['max'])
            
            if rules.get('min', None) is not None:
                is_min_valid = Float.min(rules['min'], value)
                is_valid = is_valid and is_min_valid
                if not is_min_valid:
                    op['min_val_error'] = 'minimum value allowed is ' + str(rules['min'])
            
            return is_valid, op, value
    
    @staticmethod
    def max(max_val, value):
        return True if value <= max_val else False
    
    @staticmethod
    def min(min_val, value):
        return True if value >= min_val else False
        
class Date(object):
    
    @staticmethod
    def default_value(rules):
        return rules.get('default', "")
    
    @staticmethod
    def operation():
        pass
    
    @staticmethod    
    def check(rules, value):
        required = rules.get('required', False)
        if not isinstance(value, str):
            if required is True:
                return False, {'type_error' : 'not a string'}, value
            else:
                return True, {'warning' : 'default value set'}, Date.default_value(rules) 
        
        if required is False and value is "":
            return True, {'warning' : 'default value set'}, Date.default_value(rules)
        
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
            return True, {}, value
        except:
            return False, { 'type_error' : 'invalid date format'}, value

class Regex(object):
    @staticmethod
    def default_value(rules):
        return rules.get('default', "")
    
    @staticmethod
    def operation():
        pass
    
    @staticmethod
    def check(rules, value):
        required = rules.get('required', False)
        if not isinstance(value, str):
            if required is True:
                return False, {'type_error' : 'not a string'}
            else:
                return True, {'warning' : "default value set"}, Regex.default_value(rules)
        
        if required is False and value is "":
            return True, {'warning' : "default value set"}, Regex.default_value(rules)
        
        try:
            if rules.get('case', True) is True:
                matched = re.match(rules.get('regex'), value)
            else:
                matched = re.match(rules.get('regex'), value, re.IGNORECASE)
                
            if matched is not None and matched.group() == value:
                return True, {}, value
            else:
                return False, {'error' : rules.get('msg', "invalid data")}, value
        except:
            return False, { 'semantic_error' : 'invalid regex'}, value

class Email(object):
    
    @staticmethod
    def check(rules, value):
        tmp_rules = {
            'type' : 'Regex',
#             'regex': r'[\w.-]+@[\w.-]+\.\w+',
            'regex': r'^[\w.-]+@[\w]+(\.[\w]+)+$',
            'msg': rules.get('msg',"invalid email")
        }
        
        rules.update(tmp_rules)
        
        return Regex.check(rules, value)

class Mobile(object):
    
    @staticmethod
    def check(rules, value):
        tmp_rules = {
            'type' : 'Regex',
            'regex': r'[0-9]{10}',
            'msg': rules.get('msg',"invalid mobile number")
        }
        
        rules.update(tmp_rules)
        
        return Regex.check(rules, value)
    

class Pin(object):
    @staticmethod
    def check(rules, value):
        tmp_rules = {
            'type' : 'Regex',
            'regex': r'[0-9]{6}',
            'msg': rules.get('msg',"Invalid Pin - Must be a valid PIN ")
        }
        
        rules.update(tmp_rules)
        
        return Regex.check(rules, value)
    
class Set(object):
    @staticmethod
    def check(rules, value):
        regx = "|".join(rules.get('set'))
        regx = "^("+ regx + "){1}$"
        
        tmp_rules = {
            'type' : 'Regex',
            'regex': regx,
            'msg': rules.get('msg',"Unknown input. Must be in set (" + ", ".join(rules.get('set')) + ")")
        }
        
        rules.update(tmp_rules)
        
        return Regex.check(rules, value)

class Bit(object):
    @staticmethod
    def check(rules, value):
        tmp_rules = {
            'type' : 'Regex',
            'regex': r'(0|1){1}',
            'default' : rules.get('default', '1'),
            'msg': rules.get('msg',"Unknown input. Must be either 0 or 1")
        }
        
        rules.update(tmp_rules)
        
        return Regex.check(rules, value)