from app import db
from models.item import Item
from models.list import List 
from models.user_list import UserList
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Item.query.delete()
    List.query.delete()
    item_1 = Item(name='apple', category='fruits', price=0.39)
    item_2 = Item(name='orange', category='fruits', price=0.49)
    item_3 = Item(name='milk', category='diary', price=1.29)
    item_4 = Item(name='cheese', category='diary', price=2.40)
    item_5 = Item(name='beef', category='meat', price=4.39)
    item_6 = Item(name='chicken', category='meat', price=4.09)
    item_7 = Item(name='flour', category='grains', price=1.19)
    item_8 = Item(name='coriander', category='spices', price=0.89)
    item_9 = Item(name='soy sauce', category='condiments', price=2.39)

    list_1 = List(name='Grocery', budget=20)
    list_2 = List(name='Tuesday dinner', budget=15)
    list_3 = List(name='Big eating', budget=25)
    list_4 = List(name='Cooking for bunch', budget=45)

    db.session.add(item_1)
    db.session.add(item_2)
    db.session.add(item_3)
    db.session.add(item_4)
    db.session.add(item_5)
    db.session.add(item_6)
    db.session.add(item_7)
    db.session.add(item_8)
    db.session.add(item_9)


    db.session.add(list_1)
    db.session.add(list_2)
    db.session.add(list_3)
    db.session.add(list_4)

    db.session.commit()