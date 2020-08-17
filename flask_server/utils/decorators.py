from functools import wraps
from flask import current_app
from flask_login import current_user
from flask_server.database.models import User, Box

<<<<<<< HEAD
def ownership_required(func):
=======
def requiresOwnership(func):
>>>>>>> 890cd43b145d9a827f846ae5ec28e8d3e5934c2b
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
<<<<<<< HEAD
        # Old mehtod.
        # current_box = Box.query.filter_by(box_id=kwargs["boxID"]).first()
        # if current_box.owner_id is not current_user.id:
        if int(kwargs["boxID"]) not in [box.box_id for box in current_user.user_boxes]:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)


        
            
=======
        current_box = Box.query.filter_by(boxID=kwargs["boxID"]).first()
        if current_box.userID is not current_user.id:
            return current_app.login_manager.unauthorized()
        # print(f'Trace: function {func.__name__}\nWith args: {args}\nKeyword arguments: {kwargs}')
        return func(*args, **kwargs)
>>>>>>> 890cd43b145d9a827f846ae5ec28e8d3e5934c2b
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
        
