import json
from models import *
from config import db


def insert_data_user(input_data):
    """вставляет данные в базу построчно, JSON -> dict"""

    for row in input_data:
        db.session.add(User(
            id=row.get("id"),
            first_name=row.get("first_name"),
            last_name=row.get("last_name"),
            age=row.get("age"),
            email=row.get("email"),
            role=row.get("role"),
            phone=row.get("phone")))

    db.session.commit()


def insert_data_order(input_data):
    """вставляет данные в базу построчно, JSON -> dict"""

    for row in input_data:
        db.session.add(Order(
            id=row.get("id"),
            name=row.get("name"),
            description=row.get("description"),
            start_date=row.get("start_date"),
            end_date=row.get("end_date"),
            address=row.get("address"),
            price=row.get("price"),
            customer_id=row.get("customer_id"),
            executor_id=row.get("executor_id")))

    db.session.commit()

def insert_data_offer(input_data):
    """вставляет данные в базу построчно, JSON -> dict"""

    for row in input_data:
        db.session.add(Offer(
            id=row.get("id"),
            order_id=row.get("order_id"),
            executor_id=row.get("executor_id")))

    db.session.commit()


def get_all_users():
    """получает всех пользователей"""

    result = []
    for item in User.query.all():
        result.append(item.to_dict())

    return result

def get_all_orders():
    """получает все заказы в виде словаря"""

    result = []
    for item in Order.query.all():
        result.append(item.to_dict())

    return result

def get_all_offers():
    """получает все предложения в виде словаря"""

    result = []
    for item in Offer.query.all():
        result.append(item.to_dict())

    return result

def init_db():
    db.drop_all()  # удаляем все таблицы
    db.create_all()  # создаем их заново и отправляем данные из файлов

    with open("data/user.json") as file:
        data = json.load(file)
        insert_data_user(data)

    with open("data/order.json", encoding='utf-8') as file:
        data = json.load(file)
        insert_data_order(data)

    with open("data/offer.json") as file:
        data = json.load(file)
        insert_data_offer(data)

def update_universal(model,user_id,values):
    """обновляет данные, подходит для всех вьюшек"""

    try:

        db.session.query(model).filter(model.id == user_id).update(values)
        db.session.commit()

    except Exception:
        return {}

def delete_universal(model,user_id):
    """удаляет данные, подходит для всех вьюшек"""

    try:

        db.session.query(model).filter(model.id == user_id).delete()
        db.session.commit()

    except Exception:
        return {}

def insert_data_universal(model, input_data):
    """универсальная функция для добавления данных из джейсон в базу"""

    for row in input_data:
        db.session.add(
            model(**row)
        )

    db.session.commit()

def create_user(user):
    """добавляет в базу одного пользователя, для метода POST"""

    new_user_obj = User(
        first_name=user['first_name'],
        last_name=user['last_name'],
        age=user['age'],
        email=user['email'],
        role=user['role'],
        phone=user['phone']
    )
    db.session.add(new_user_obj)
    db.session.commit()
    db.session.close()
    return "Пользователь добавлен в базу"

def create_order(order):
    """добавляет в базу один заказ, для метода POST"""

    new_order_obj = Order(
        name=order['name'],
        description=order['description'],
        start_date=order['start_date'],
        end_date=order['end_date'],
        address=order['address'],
        price=order['price'],
        customer_id=order['customer_id'],
        executor_id=order['executor_id']
    )
    db.session.add(new_order_obj)
    db.session.commit()
    db.session.close()
    return "Заказ добавлен в базу"

def create_offer(offer):
    """добавляет в базу одно предложение, для метода POST"""

    new_offer_obj = Offer(
        order_id=offer['order_id'],
        executor_id=offer['executor_id']
    )
    db.session.add(new_offer_obj)
    db.session.commit()
    db.session.close()
    return "Заказ добавлен в базу"