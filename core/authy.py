from flask_httpauth import HTTPDigestAuth, HTTPBasicAuth
from functools import wraps

auth = HTTPBasicAuth()


users = {
    "userone": "12345",
    "usertwo": "12345",
    "user2": "12345"
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


def apigate(f):
    """
    Used as a gate to every API. Authentication, authorization etc. can be
    implemented in this section.
    """
    @wraps(f)
#     @auth.login_required
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
