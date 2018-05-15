'''
Created on 26-Dec-2017

@author: devasish ghosh
'''
from datetime import date, timedelta
def datesequence(span=(0, 10), format=("%a, %d %B", "%Y-%m-%d")):
    """
    Returns a date sequnce with a span and output format 
    @param span: tuple or int. If tuple like (-5, 6) means from 5 days past to 6 days future. if passed tupble both item is compulsory.
    single int also allowed. negative int means past x days.
    @param format: tuple. output dateformat. if set both of the format is compulsory    
    """
    today = date.today()
    arr = []
    
    if not isinstance(span, tuple):
        if span > 0:
            span = (0, span)
        else:
            span = (span, 0)
            
    d = today + timedelta(days=span[0]) 
    
    for i in range(span[0], span[1] + 1):
        arr.append(( d.strftime(format[0]),
            d.strftime(format[1])
        ))
        
        d = d + timedelta(days=1)
        
    return arr


if __name__ == '__main__':
    a = datesequence()
    print(a)
    