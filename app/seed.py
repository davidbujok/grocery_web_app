from app import db
from app.models.item import Item
from app.models.list import List 
from app.models.category import Category
from app.models.user import User
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():

    Item.query.delete()
    List.query.delete()


    list_of_categories = [
        Category(name='fruit'),
        Category(name='diary'),
        Category(name='meat'),
        Category(name='grains'),
        Category(name='spices'),
        Category(name='condiments'),
        Category(name='household'),
        Category(name='bakery')
    ]

    for category in list_of_categories:
        db.session.add(category)
    


    list_of_items = [
    Item(name='apple', category=1, price=0.39),
    Item(name='banana', category=1, price=0.29),
    Item(name='orange', category=1, price=0.49),
    Item(name='watermelon', category=1, price=2.39),
    Item(name='grapes', category=1, price=1.99),
    Item(name='strawberry', category=1, price=0.69),
    Item(name='pineapple', category=1, price=1.89),
    Item(name='kiwi', category=1, price=1.49),
    Item(name='pear', category=1, price=0.89),
    Item(name='mango', category=1, price=1.79),
    Item(name='pear', category=1, price=0.59),
    Item(name='peach', category=1, price=0.79),
    Item(name='plum', category=1, price=0.59),
    Item(name='apricot', category=1, price=0.49),
    Item(name='blueberry', category=1, price=0.99),
    Item(name='raspberry', category=1, price=1.29),
    Item(name='blackberry', category=1, price=1.19),
    Item(name='cherry', category=1, price=0.89),
    Item(name='lemon', category=1, price=0.69),
    Item(name='lime', category=1, price=0.79),
    Item(name='grapefruit', category=1, price=1.39),

    Item(name='milk', category=2, price=1.29),
    Item(name='cheese', category=2, price=2.40),
    Item(name='yogurt', category=2, price=0.99),
    Item(name='butter', category=2, price=1.89),
    Item(name='eggs', category=2, price=2.19),
    Item(name='cream', category=2, price=1.49),
    Item(name='cottage cheese', category=2, price=1.59),
    Item(name='sour cream', category=2, price=1.29),
    Item(name='milk chocolate', category=2, price=1.99),
    Item(name='whipping cream', category=2, price=1.79),
    Item(name='mozzarella', category=2, price=2.59),
    Item(name='feta cheese', category=2, price=2.09),
    Item(name='gouda', category=2, price=2.29),
    Item(name='cheddar', category=2, price=2.49),
    Item(name='parmesan', category=2, price=2.79),
    Item(name='cream cheese', category=2, price=1.89),
    Item(name='ricotta', category=2, price=1.99),
    Item(name='brie', category=2, price=2.79),
    Item(name='greek yogurt', category=2, price=1.39),
    Item(name='swiss cheese', category=2, price=2.69),

    Item(name='beef', category=3, price=4.39),
    Item(name='chicken', category=3, price=4.09),
    Item(name='pork', category=3, price=3.99),
    Item(name='lamb', category=3, price=6.29),
    Item(name='bacon', category=3, price=3.79),
    Item(name='sausages', category=3, price=2.99),
    Item(name='ground beef', category=3, price=4.19),
    Item(name='ham', category=3, price=3.49),
    Item(name='turkey', category=3, price=5.39),
    Item(name='venison', category=3, price=7.89),
    Item(name='duck', category=3, price=6.49),
    Item(name='salami', category=3, price=3.99),
    Item(name='veal', category=3, price=5.29),
    Item(name='quail', category=3, price=8.99),
    Item(name='rabbit', category=3, price=6.79),
    Item(name='corned beef', category=3, price=4.99),
    Item(name='bison', category=3, price=9.29),
    Item(name='pork chops', category=3, price=4.89),
    Item(name='pepperoni', category=3, price=3.59),
    Item(name='ground turkey', category=3, price=3.99),

    Item(name='rice', category=4, price=1.99),
    Item(name='wheat', category=4, price=2.49),
    Item(name='oats', category=4, price=1.79),
    Item(name='cornmeal', category=4, price=1.59),
    Item(name='barley', category=4, price=2.19),
    Item(name='quinoa', category=4, price=3.29),
    Item(name='bulgur', category=4, price=2.79),
    Item(name='millet', category=4, price=2.09),
    Item(name='rye', category=4, price=2.99),
    Item(name='couscous', category=4, price=2.39),
    Item(name='amaranth', category=4, price=3.49),
    Item(name='teff', category=4, price=3.59),
    Item(name='farro', category=4, price=2.89),
    Item(name='spelt', category=4, price=2.69),
    Item(name='wild rice', category=4, price=4.29),
    Item(name='buckwheat', category=4, price=2.99),
    Item(name='amaranth flour', category=4, price=3.99),
    Item(name='corn flour', category=4, price=1.49),
    Item(name='millet flour', category=4, price=2.79),
    Item(name='rye flour', category=4, price=2.69),

    Item(name='cinnamon', category=5, price=1.99),
    Item(name='turmeric', category=5, price=2.49),
    Item(name='cumin', category=5, price=1.79),
    Item(name='paprika', category=5, price=1.59),
    Item(name='coriander', category=5, price=2.19),
    Item(name='cloves', category=5, price=3.29),
    Item(name='nutmeg', category=5, price=2.79),
    Item(name='cardamom', category=5, price=2.09),
    Item(name='ginger', category=5, price=2.99),
    Item(name='mustard seeds', category=5, price=2.39),
    Item(name='fennel seeds', category=5, price=3.49),
    Item(name='dill seeds', category=5, price=3.59),
    Item(name='poppy seeds', category=5, price=2.89),
    Item(name='fenugreek', category=5, price=2.69),
    Item(name='allspice', category=5, price=4.29),
    Item(name='chili flakes', category=5, price=2.99),
    Item(name='saffron', category=5, price=3.99),
    Item(name='sumac', category=5, price=1.49),
    Item(name='vanilla bean', category=5, price=2.79),
    Item(name='star anise', category=5, price=2.69),

    Item(name='ketchup', category=6, price=2.49),
    Item(name='mayonnaise', category=6, price=1.99),
    Item(name='mustard', category=6, price=1.79),
    Item(name='relish', category=6, price=1.59),
    Item(name='soy sauce', category=6, price=2.19),
    Item(name='barbecue sauce', category=6, price=3.29),
    Item(name='hot sauce', category=6, price=2.79),
    Item(name='tahini', category=6, price=2.09),
    Item(name='horseradish', category=6, price=2.99),
    Item(name='hoisin sauce', category=6, price=2.39),
    Item(name='chili sauce', category=6, price=3.49),
    Item(name='soy paste', category=6, price=3.59),
    Item(name='apple cider vinegar', category=6, price=2.89),
    Item(name='balsamic glaze', category=6, price=2.69),
    Item(name='wasabi', category=6, price=4.29),
    Item(name='pickle relish', category=6, price=2.99),
    Item(name='teriyaki sauce', category=6, price=3.99),
    Item(name='oyster sauce', category=6, price=1.49),
    Item(name='fish sauce', category=6, price=2.79),
    Item(name='chutney', category=6, price=2.69),
    
    Item(name='dish soap', category=7, price=2.99),
    Item(name='laundry detergent', category=7, price=5.49),
    Item(name='toilet paper', category=7, price=3.99),
    Item(name='paper towels', category=7, price=4.29),
    Item(name='trash bags', category=7, price=2.59),
    Item(name='cleaning wipes', category=7, price=2.79),
    Item(name='fabric softener', category=7, price=3.49),
    Item(name='bathroom cleaner', category=7, price=2.89),
    Item(name='window cleaner', category=7, price=2.39),
    Item(name='floor cleaner', category=7, price=3.99),
    Item(name='sponges', category=7, price=1.49),
    Item(name='dustpan and brush', category=7, price=2.09),
    Item(name='oven cleaner', category=7, price=3.79),
    Item(name='garbage bin', category=7, price=6.99),
    Item(name='broom', category=7, price=4.59),
    Item(name='mop', category=7, price=5.29),
    Item(name='vacuum cleaner bags', category=7, price=3.29),
    Item(name='feather duster', category=7, price=1.99),
    Item(name='microfiber cloths', category=7, price=2.49),
    Item(name='air freshener', category=7, price=2.19),

    Item(name='bread', category=8, price=1.99),
    Item(name='bagels', category=8, price=2.49),
    Item(name='croissants', category=8, price=1.79),
    Item(name='muffins', category=8, price=1.69),
    Item(name='cupcakes', category=8, price=2.29),
    Item(name='doughnuts', category=8, price=1.99),
    Item(name='cookies', category=8, price=1.49),
    Item(name='brownies', category=8, price=1.89),
    Item(name='tarts', category=8, price=2.99),
    Item(name='pie', category=8, price=3.49),
    Item(name='sourdough', category=8, price=2.79),
    Item(name='ciabatta', category=8, price=2.59),
    Item(name='rolls', category=8, price=1.29),
    Item(name='crackers', category=8, price=1.99),
    Item(name='pretzels', category=8, price=1.69),
    Item(name='biscuits', category=8, price=1.49),
    Item(name='cake', category=8, price=3.99),
    Item(name='pancakes', category=8, price=2.49),
    Item(name='waffles', category=8, price=2.79),
    Item(name='croutons', category=8, price=1.29)
    ]

    for item in list_of_items:
        db.session.add(item) 
    
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