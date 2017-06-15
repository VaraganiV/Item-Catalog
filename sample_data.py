
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem
from flask import Flask, render_template, request, redirect, url_for, jsonify


engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


## Delete the tables
session.query(Category).delete()
session.query(CategoryItem).delete()

## Add categories
sample_categories = ['Services', 'Inventory', 'Non Inventory']

for category_name in sample_categories:
    category = Category(category_name)
    session.add(category)
session.commit()

## Add items
sample_items = {'Laundry': 1, 'Mobiles': 2, 'Mother Board': 3}

for item_title, item_category in sample_items.iteritems():
    item = CategoryItem(item_title, item_title + ": description", item_category)
    session.add(item)
session.commit()
