from . import db


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)


class Store(db.Model):
    __tablename__ = "store"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    create = db.Column("create", db.DateTime)
    active = db.Column("active", db.Boolean)

    user = db.relationship("User", foreign_keys=user_id)


class Order(db.Model):
    __tablename__ = "order"
    id = db.Column("id", db.Integer, primary_key=True)
    create = db.Column("create", db.DateTime)
    order_status_id = db.Column(
        "order_status_id", db.Integer, db.ForeignKey("order_status.id")
    )
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    address_id = db.Column(
        "address_id", db.Integer, db.ForeignKey("address.id")
    )

    order_status = db.relationship("OrderStatus", foreign_keys=order_status_id)
    store = db.relationship("Store", foreign_keys=store_id)
    user = db.relationship("User", foreign_keys=user_id)
    address = db.relationship("Address", foreign_keys=address_id)


class OrderStatus(db.Model):
    __tablename__ = "order_status"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)


class CategoryToStore(db.Model):
    __tablename__ = "category_to_store"
    id = db.Column("id", db.Integer, primary_key=True)
    category_id = db.Column(
        "category_id", db.Integer, db.ForeignKey("category.id")
    )
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))

    category = db.relationship("Category", foreign_keys=category_id)
    store = db.relationship("Store", foreign_keys=store_id)


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
    price = db.Column("price", db.Float)
    quantity = db.Column("quantity", db.Unicode)
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))

    store = db.relationship("Store", foreign_keys=store_id)


class OrderHistory(db.Model):
    __tablename__ = "order_history"
    id = db.Column("id", db.Integer, primary_key=True)
    create = db.Column("create", db.DateTime)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))

    order = db.relationship("Order", foreign_keys=order_id)


class OrderProduct(db.Model):
    __tablename__ = "order_product"
    id = db.Column("id", db.Integer, primary_key=True)
    quantity = db.Column("quantity", db.Integer)
    product_id = db.Column(
        "product_id", db.Integer, db.ForeignKey("product.id")
    )
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))

    product = db.relationship("Product", foreign_keys=product_id)
    order = db.relationship("Order", foreign_keys=order_id)


class Payment(db.Model):
    __tablename__ = "payment"
    id = db.Column("id", db.Integer, primary_key=True)
    payment = db.Column("payment", db.Integer)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))
    payment_status_id = db.Column(
        "payment_status_id", db.Integer, db.ForeignKey("payment_status.id")
    )

    order = db.relationship("Order", foreign_keys=order_id)
    payment_status = db.relationship(
        "PaymentStatus", foreign_keys=payment_status_id
    )


class Address(db.Model):
    __tablename__ = "address"
    id = db.Column("id", db.Integer, primary_key=True)
    zip = db.Column("zip", db.Unicode)
    country = db.Column("country", db.Unicode)
    address = db.Column("address", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))

    user = db.relationship("User", foreign_keys=user_id)


class PaymentStatus(db.Model):
    __tablename__ = "payment_status"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)
