from app import db
from models.item import Item
from models.list import List 
from models.user import User
from models.user_list import UserList
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Item.query.delete()
    List.query.delete()
    list_of_items = [
    Item(name='apple', category='fruits', price=0.39),
    Item(name='banana', category='fruits', price=0.29),
    Item(name='orange', category='fruits', price=0.49),
    Item(name='watermelon', category='fruits', price=2.39),
    Item(name='grapes', category='fruits', price=1.99),
    Item(name='strawberry', category='fruits', price=0.69),
    Item(name='pineapple', category='fruits', price=1.89),
    Item(name='kiwi', category='fruits', price=1.49),
    Item(name='pear', category='fruits', price=0.89),
    Item(name='mango', category='fruits', price=1.79),
    Item(name='pear', category='fruits', price=0.59),
    Item(name='peach', category='fruits', price=0.79),
    Item(name='plum', category='fruits', price=0.59),
    Item(name='apricot', category='fruits', price=0.49),
    Item(name='blueberry', category='fruits', price=0.99),
    Item(name='raspberry', category='fruits', price=1.29),
    Item(name='blackberry', category='fruits', price=1.19),
    Item(name='cherry', category='fruits', price=0.89),
    Item(name='lemon', category='fruits', price=0.69),
    Item(name='lime', category='fruits', price=0.79),
    Item(name='grapefruit', category='fruits', price=1.39),

    Item(name='milk', category='diary', price=1.29),
    Item(name='cheese', category='diary', price=2.40),
    Item(name='yogurt', category='diary', price=0.99),
    Item(name='butter', category='diary', price=1.89),
    Item(name='eggs', category='diary', price=2.19),
    Item(name='cream', category='diary', price=1.49),
    Item(name='cottage cheese', category='diary', price=1.59),
    Item(name='sour cream', category='diary', price=1.29),
    Item(name='milk chocolate', category='diary', price=1.99),
    Item(name='whipping cream', category='diary', price=1.79),
    Item(name='mozzarella', category='diary', price=2.59),
    Item(name='feta cheese', category='diary', price=2.09),
    Item(name='gouda', category='diary', price=2.29),
    Item(name='cheddar', category='diary', price=2.49),
    Item(name='parmesan', category='diary', price=2.79),
    Item(name='cream cheese', category='diary', price=1.89),
    Item(name='ricotta', category='diary', price=1.99),
    Item(name='brie', category='diary', price=2.79),
    Item(name='greek yogurt', category='diary', price=1.39),
    Item(name='swiss cheese', category='diary', price=2.69),

    Item(name='beef', category='meat', price=4.39),
    Item(name='chicken', category='meat', price=4.09),
    Item(name='pork', category='meat', price=3.99),
    Item(name='lamb', category='meat', price=6.29),
    Item(name='bacon', category='meat', price=3.79),
    Item(name='sausages', category='meat', price=2.99),
    Item(name='ground beef', category='meat', price=4.19),
    Item(name='ham', category='meat', price=3.49),
    Item(name='turkey', category='meat', price=5.39),
    Item(name='venison', category='meat', price=7.89),
    Item(name='duck', category='meat', price=6.49),
    Item(name='salami', category='meat', price=3.99),
    Item(name='veal', category='meat', price=5.29),
    Item(name='quail', category='meat', price=8.99),
    Item(name='rabbit', category='meat', price=6.79),
    Item(name='corned beef', category='meat', price=4.99),
    Item(name='bison', category='meat', price=9.29),
    Item(name='pork chops', category='meat', price=4.89),
    Item(name='pepperoni', category='meat', price=3.59),
    Item(name='ground turkey', category='meat', price=3.99),

    Item(name='rice', category='grains', price=1.99),
    Item(name='wheat', category='grains', price=2.49),
    Item(name='oats', category='grains', price=1.79),
    Item(name='cornmeal', category='grains', price=1.59),
    Item(name='barley', category='grains', price=2.19),
    Item(name='quinoa', category='grains', price=3.29),
    Item(name='bulgur', category='grains', price=2.79),
    Item(name='millet', category='grains', price=2.09),
    Item(name='rye', category='grains', price=2.99),
    Item(name='couscous', category='grains', price=2.39),
    Item(name='amaranth', category='grains', price=3.49),
    Item(name='teff', category='grains', price=3.59),
    Item(name='farro', category='grains', price=2.89),
    Item(name='spelt', category='grains', price=2.69),
    Item(name='wild rice', category='grains', price=4.29),
    Item(name='buckwheat', category='grains', price=2.99),
    Item(name='amaranth flour', category='grains', price=3.99),
    Item(name='corn flour', category='grains', price=1.49),
    Item(name='millet flour', category='grains', price=2.79),
    Item(name='rye flour', category='grains', price=2.69),

    Item(name='cinnamon', category='spices', price=1.99),
    Item(name='turmeric', category='spices', price=2.49),
    Item(name='cumin', category='spices', price=1.79),
    Item(name='paprika', category='spices', price=1.59),
    Item(name='coriander', category='spices', price=2.19),
    Item(name='cloves', category='spices', price=3.29),
    Item(name='nutmeg', category='spices', price=2.79),
    Item(name='cardamom', category='spices', price=2.09),
    Item(name='ginger', category='spices', price=2.99),
    Item(name='mustard seeds', category='spices', price=2.39),
    Item(name='fennel seeds', category='spices', price=3.49),
    Item(name='dill seeds', category='spices', price=3.59),
    Item(name='poppy seeds', category='spices', price=2.89),
    Item(name='fenugreek', category='spices', price=2.69),
    Item(name='allspice', category='spices', price=4.29),
    Item(name='chili flakes', category='spices', price=2.99),
    Item(name='saffron', category='spices', price=3.99),
    Item(name='sumac', category='spices', price=1.49),
    Item(name='vanilla bean', category='spices', price=2.79),
    Item(name='star anise', category='spices', price=2.69),

    Item(name='ketchup', category='condiments', price=2.49),
    Item(name='mayonnaise', category='condiments', price=1.99),
    Item(name='mustard', category='condiments', price=1.79),
    Item(name='relish', category='condiments', price=1.59),
    Item(name='soy sauce', category='condiments', price=2.19),
    Item(name='barbecue sauce', category='condiments', price=3.29),
    Item(name='hot sauce', category='condiments', price=2.79),
    Item(name='tahini', category='condiments', price=2.09),
    Item(name='horseradish', category='condiments', price=2.99),
    Item(name='hoisin sauce', category='condiments', price=2.39),
    Item(name='chili sauce', category='condiments', price=3.49),
    Item(name='soy paste', category='condiments', price=3.59),
    Item(name='apple cider vinegar', category='condiments', price=2.89),
    Item(name='balsamic glaze', category='condiments', price=2.69),
    Item(name='wasabi', category='condiments', price=4.29),
    Item(name='pickle relish', category='condiments', price=2.99),
    Item(name='teriyaki sauce', category='condiments', price=3.99),
    Item(name='oyster sauce', category='condiments', price=1.49),
    Item(name='fish sauce', category='condiments', price=2.79),
    Item(name='chutney', category='condiments', price=2.69),
    
    Item(name='dish soap', category='household', price=2.99),
    Item(name='laundry detergent', category='household', price=5.49),
    Item(name='toilet paper', category='household', price=3.99),
    Item(name='paper towels', category='household', price=4.29),
    Item(name='trash bags', category='household', price=2.59),
    Item(name='cleaning wipes', category='household', price=2.79),
    Item(name='fabric softener', category='household', price=3.49),
    Item(name='bathroom cleaner', category='household', price=2.89),
    Item(name='window cleaner', category='household', price=2.39),
    Item(name='floor cleaner', category='household', price=3.99),
    Item(name='sponges', category='household', price=1.49),
    Item(name='dustpan and brush', category='household', price=2.09),
    Item(name='oven cleaner', category='household', price=3.79),
    Item(name='garbage bin', category='household', price=6.99),
    Item(name='broom', category='household', price=4.59),
    Item(name='mop', category='household', price=5.29),
    Item(name='vacuum cleaner bags', category='household', price=3.29),
    Item(name='feather duster', category='household', price=1.99),
    Item(name='microfiber cloths', category='household', price=2.49),
    Item(name='air freshener', category='household', price=2.19),

    Item(name='bread', category='bakery', price=1.99),
    Item(name='bagels', category='bakery', price=2.49),
    Item(name='croissants', category='bakery', price=1.79),
    Item(name='muffins', category='bakery', price=1.69),
    Item(name='cupcakes', category='bakery', price=2.29),
    Item(name='doughnuts', category='bakery', price=1.99),
    Item(name='cookies', category='bakery', price=1.49),
    Item(name='brownies', category='bakery', price=1.89),
    Item(name='tarts', category='bakery', price=2.99),
    Item(name='pie', category='bakery', price=3.49),
    Item(name='sourdough', category='bakery', price=2.79),
    Item(name='ciabatta', category='bakery', price=2.59),
    Item(name='rolls', category='bakery', price=1.29),
    Item(name='crackers', category='bakery', price=1.99),
    Item(name='pretzels', category='bakery', price=1.69),
    Item(name='biscuits', category='bakery', price=1.49),
    Item(name='cake', category='bakery', price=3.99),
    Item(name='pancakes', category='bakery', price=2.49),
    Item(name='waffles', category='bakery', price=2.79),
    Item(name='croutons', category='bakery', price=1.29)
    ]

    for item in list_of_items:
        db.session.add(item) 

    list_1 = List(name='Grocery', budget=20)
    list_2 = List(name='Tuesday dinner', budget=15)
    list_3 = List(name='Big eating', budget=25)
    list_4 = List(name='Cooking for bunch', budget=45)

    db.session.add(list_1)
    db.session.add(list_2)
    db.session.add(list_3)
    db.session.add(list_4)
    
    list_of_users = [
    User(fullname="Gerald of Rivia"),
    User(fullname="Solid Snake"),
    User(fullname="Lara Croft"),
    User(fullname="Agent 47"),
    User(fullname="Kratos"),
    User(fullname="Joel"),
    User(fullname="Agent 47"),
    User(fullname="Nathan Drake"),
    User(fullname="Duke Nukem"),
    User(fullname="Niko Bellic")
    ]
    for user in list_of_users:
        db.session.add(user)

    

    db.session.commit()