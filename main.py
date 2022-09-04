import json
from typing import List, Any

from config import app
from models import User, Order, Offer
from service import get_all_users, get_all_orders, get_all_offers, init_db, insert_data_user, update_universal, \
    insert_data_order, insert_data_offer, delete_universal, create_user, create_order, create_offer
from flask import request


@app.route("/users/", methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        return json.dumps(get_all_users()), 200
    elif request.method == 'POST':
        if isinstance(request.json, list):
            user = json.loads(request.data)
            create_user(user)
            return "Данные записаны", 200
        elif isinstance(request.json, dict):
            user = json.loads(request.data)
            create_user(user)
            return "Данные записаны", 200
        else:
            print('Неподдерживаемый  типа данных')


@app.route("/users/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_users(user_id):
    if request.method == 'GET':
        data: list[Any] = get_all_users()
        for item in data:
            if item.get("id") == user_id:
                return json.dumps(item), 200

    elif request.method == 'PUT':
        update_universal(User, user_id, request.json)
        return "Данные обновлены", 200

    elif request.method == 'DELETE':
        delete_universal(User, user_id)
        return "Данные удалены", 200


@app.route("/orders/", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return json.dumps(get_all_orders(), ensure_ascii=False), 200
    elif request.method == 'POST':
        if isinstance(request.json, list):
            order = json.loads(request.data)
            create_order(order)
            return "Данные записаны", 200
        elif isinstance(request.json, dict):
            order = json.loads(request.data)
            create_order(order)
            return "Данные записаны", 200
        else:
            print('Непонятный типа данных')


@app.route("/orders/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_order(user_id):
    if request.method == 'GET':
        data = get_all_orders()
        for item in data:
            if item.get("id") == user_id:
                return json.dumps(item, ensure_ascii=False), 200

    elif request.method == 'PUT':
        update_universal(Order, user_id, request.json)
        return "Данные обновлены", 200

    elif request.method == 'DELETE':
        delete_universal(Order, user_id)
        return "Данные удалены", 200


@app.route("/offers/", methods=['GET', 'POST'])
def get_offers():
    if request.method == 'GET':
        return json.dumps(get_all_offers(), ensure_ascii=False), 200
    elif request.method == 'POST':
        if isinstance(request.json, list):
            offer = json.loads(request.data)
            create_offer(offer)
            return "Данные записаны", 200
        elif isinstance(request.json, dict):
            offer = json.loads(request.data)
            create_offer(offer)
            return "Данные записаны", 200
        else:
            print('Непонятный типа данных')


@app.route("/offers/<int:user_id>", methods=['GET', 'PUT', 'DELETE'])
def get_one_offer(user_id):
    if request.method == 'GET':
        data = get_all_offers()
        for item in data:
            if item.get("id") == user_id:
                return json.dumps(item), 200
    elif request.method == 'PUT':
        update_universal(Offer, user_id, request.json)
        return "Данные обновлены", 200

    elif request.method == 'DELETE':
        delete_universal(Offer, user_id)
        return "Данные удалены", 200


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
