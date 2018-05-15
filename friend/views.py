from flask import Blueprint, request
from friend import model
from core.io import inp, out, err
from core.authy import apigate
from core.email import sendmail
from flask.json import jsonify

friend = Blueprint('friend', __name__)

@friend.route('/create', methods=['POST'])
@apigate
def create():
    inp.register_request(request)
    inp.set_rules(model.Friend.validation_rules)
    valid, op = inp.validate()
    
    return out({"validation" : op, 'valid' : valid, 'data' : inp.post()})
    
    if valid is True:
        return out({"validation" : op, 'valid' : valid, 'data' : inp.post()})
    else:
        return err({"validation" : op, 'valid' : valid, 'data' : inp.post()})
    

    
@friend.route('/list', methods=['GET', 'POST', 'PUT', 'DELETE'])
@apigate
def list():
    inp.register_request(request)
    if request.method == 'POST':
        return out({'body' : inp.post(), 'head' : dict(request.headers)})
    else:
        return out({'body' : inp.get(), 'head' : dict(request.headers)})

@friend.route('/devas', methods=['POST'])
@apigate
def devas():
    inp.register_request(request, copyheader=['Header-One', 'Header-Two'])
#     d = request.get_json()
#     print(request.headers.get('Content-Type'))
#     inp.set_rules(model.Friend.validation_rules)
#     valid, op = inp.validate()
    
    return out({'data' : inp.post()})

@friend.route('/ui', methods=['GET', 'POST', 'PUT', 'DELETE'])
@apigate
def ui():
    inp.register_request(request)
    data = inp.post()
    
    return out({"body" : data, "head" : inp.headers()}, msg='successfully', status=2000)

@friend.route('/email', methods=['GET'])
@apigate
def email():
    resp = sendmail(to = ['dghosh2@sastasundar.com'], 
                    body = {"header" : "1233"}, 
                    subject = "mail test",
                    template="template2")
    
    return out(resp)

@friend.route('/partvalidate', methods=['POST'])
@apigate
def partvalidate():
    inp.register_request(request)
    inp.set_rules(model.Friend.validation_rules, ['field1', 'field2'])
    valid, op = inp.validate()
    
    
    inp.set_rules(model.Friend.validation_rules2, ['f1', 'f2'])
    valid, op = inp.validate()
    
    
    return out({"validation" : op, 'valid' : valid, 'data' : inp.post()})

@friend.route('/testdel/<int:id>', methods=['GET', 'DELETE'])
@apigate
def testdel(id):
    inp.register_request(request)
    print(inp.post(), id)
    return out(inp.post())


@friend.route('/posti', methods=['POST'])
@apigate
def posti():
    inp.register_request(request)
    return out({"data" : inp.post()})
    
@friend.route('/restclient', methods=['GET', 'POST'])
@apigate
def restclient():
    from core import restclient as rc
    url = 'http://192.168.5.63:5050/abc/ui'
    url = 'http://stage-cartapi.sastasundar.com/index.php/payment/genu_payment_process/app_payment_processing'
    url = 'http://192.168.5.69:4040/search/service/search?q=blood'
    authdata = {
        'type' : 'basic',
        'username' : 'admin',
        'password' : '1234' 
    }
    
    cont, req = rc.get(url, data = {'q' : 'dettol', "sdf" : 5656}, headers={'qq' : "67"}, authdata=authdata)
    return out(cont)

@friend.route('/memory1', methods=['GET'])
@apigate
def memory1():
    x = y = 4
    z = 5
    return out({"body" : hex(id(z)) }, msg='successfully', status=2000)
    #