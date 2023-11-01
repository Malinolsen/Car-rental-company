from app import app
from flask import render_template, request, redirect, url_for, jsonify
import json
from models.driver import *
from models.car import *
from models.customer import *
from models.employee import *

#Cars
@app.route('/update_car',methods=['PUT'])
def update_car_info():
    record = json.loads(request.data)
    print(record)

    return update_Car(record['make'],record['model'],record['year'],record['address'],record['car_ID'],record['status'])

@app.route('/create_car', methods='POST')
def create_car_info():
    record=json.loads(request.data)
    print(record)
    return create_Car(record['make'],record['model'],record['year'],record['address'],record['car_ID'],record['status'])

@app.route('/read_car',methods='GET')
def query_records():
    return Read_Cars()

@app.route('/delete_car', methods=['DELETE'])
def delete_car_info():
    record = json.loads(request.data)
    print(record)
    delete_Car(record['reg'])
    return Read_Cars()


#Customer
@app.route('/update_customer',methods=['PUT'])
def update_customer_info():
    record = json.loads(request.data)
    print(record)

    return update_Customer(record['name'],record['age'],record['customer_ID'],record['address'])

@app.route('/create_customer', methods='POST')
def create_customer_info():
    record=json.loads(request.data)
    print(record)
    return create_Customer(record['name'],record['age'],record['customer_ID'],record['address'])

@app.route('/read_customer',methods='GET')
def query_records():
    return read_Customer()

@app.route('/delete_customer', methods=['DELETE'])
def delete_customer_info():
    record = json.loads(request.data)
    print(record)
    delete_Customer(record['reg'])
    return read_Customer()

#Employee
#Customer
@app.route('/update_employee',methods=['PUT'])
def update_employee_info():
    record = json.loads(request.data)
    print(record)

    return update_Employee(record['name'],record['branch'],record['address'])

@app.route('/create_employee', methods='POST')
def create_employee_info():
    record=json.loads(request.data)
    print(record)
    return create_Employee(record['name'],record['branch'],record['address'])

@app.route('/read_employee',methods='GET')
def query_records():
    return read_Employee()

@app.route('/delete_employee', methods=['DELETE'])
def delete_employee_info():
    record = json.loads(request.data)
    print(record)
    delete_Employee(record['reg'])
    return read_Employee()


#Order car
@app.route('/order_car', methods=['POST'])
def order_car():
    customer_id = request.args.get('customer_id')
    car_id = request.args.get('car_id')

    booked_cars = check_customerBookings(customer_id)
    if booked_cars:
        return jsonify({"message": "Customer has already booked a car"}), 404
    
    car_status = check_car_status(car_id)
    if not car_status:
        return jsonify({"message":"Car is not available"}), 404
    
    create_booking(customer_id, customer_id)
    return jsonify({"message":"Car successfully booked."}), 200


