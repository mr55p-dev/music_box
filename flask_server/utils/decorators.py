from functools import wraps
from flask import current_app
from flask_login import current_user
from flask_server.database.models import User, Box


def ownership_required(func):
    """
    Wrapper to specify that the userID must
    own the boxID in question before a page 
    can be accessed. Should be used with 
    @login_rquired decorator as well as this
    contains some extra checks (ie if the app
    configuration is changed to not use 
    authentication).

    Can be used as a standard decorator.
    Can only be used on functions which 
    possess a boxID in the URL.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Old mehtod.
        # current_box = Box.query.filter_by(box_id=kwargs["boxID"]).first()
        # if current_box.owner_id is not current_user.id:
        if int(kwargs["boxID"]) not in [box.box_id for box in current_user.user_boxes]:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)
    return wrapper

def trace(func):
    """
    Allows you to see the arguments and name of the decorated function
    in realtime with a small wrapper
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'''
        Trace: function {func.__name__}\n
        With args: {args}\n
        Keyword arguments: {kwargs}''')

        ret = func(*args, **kwargs)

        print(f'''
            Trace: function {func.__name__}\n
            Returned: {ret}
            ''')
        return func(*args, **kwargs)

