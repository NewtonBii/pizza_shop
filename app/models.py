from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    role = db.relationship("Roles", backref="user", lazy="dynamic")
    order = db.relationship("Order", backref="user", lazy="dynamic")


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

class Roles(db.Model):
    """Class that creates roles for the users of the app"""
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Pizza(db.Model):
    """Class for creating the pizza object"""

    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    image_pic_path = db.Column(db.String())
    price = db.Column(db.Integer)
    order = db.relationship("Order", backref="pizza", lazy="dynamic")

class Order(db.Model):
    """Class that stores the different orders and their prices"""

    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    price = db.Column(db.Integer)
    pizza_id= db.Column(db.Integer, db.ForeignKey("pizza.id"))



class Toppings(db.Model):
    """Class that has the different type of toppings and their prices"""
    __tablename__ = 'toppings'

    id = db.Column(db.Integer, primary_key = True)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizza.id"))
    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    image_pic_path = db.Column(db.String())
