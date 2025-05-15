from flask import Blueprint, render_template, request, redirect, url_for
from .models import InventoryItem
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def index():
    items = InventoryItem.query.all()
    return render_template('index.html', items=items)


@views.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        new_item = InventoryItem(
            name=name, category=category, quantity=quantity, price=price)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('views.index'))
    return render_template('create.html')


@views.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = InventoryItem.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.category = request.form['category']
        item.quantity = int(request.form['quantity'])
        item.price = float(request.form['price'])
        db.session.commit()
        return redirect(url_for('views.index'))
    return render_template('update.html', item=item)


@views.route('/delete/<int:id>')
def delete(id):
    item = InventoryItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('views.index'))
