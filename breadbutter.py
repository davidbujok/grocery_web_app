from app import app, db
from app.models.category import Category
from app.models.item import Item
from app.models.list import List
from app.models.store import Store
from app.models.user import User
from app.models.user_layouts import UserLayouts
from app.models.user_list import UserList

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Category': Category, 'Item': Item, 'List': List, 'Store': Store, 'UserLayouts': UserLayouts, 'UserList': UserList}


