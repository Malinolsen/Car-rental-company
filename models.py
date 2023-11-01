from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json 

URI = "Your URI"
AUTH = ("neo4j", "YOUR-AUTH-KEY")

def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()

    return driver

def node_to_json(node):
     node_properties = dict(node.items())
     return node_properties

#Class and functions for Car entities

class Car:
    def __init__(self, make, model, year, address, car_ID, status):
        self.make = make 
        self.model = model 
        self.year = year
        self.address = address 
        self.car_ID = car_ID
        self.status = status
    
def create_Car(make,model,year,address, car_ID, status):
        with _get_connection.session() as session:
            cars = session.run(
                "CREATE (a:Car {make: $make, model:$model, year:$year, address:$address, car_ID:$car_ID, status:$status})",
                make=make, model=model, year=year, address=address, car_ID=car_ID, status=status)
            
            nodes_json = [node_to_json(record['a'])for record in cars]
            print(nodes_json)
            return nodes_json
    
def update_Car(make, model, year, address, car_ID, status):
        with _get_connection.session() as session:
            cars = session.run("MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year=$year, a.address=$address, a.car_ID=$car_ID, a.status=$status RETURN a;", make=make, model=model, year=year,address=address, car_ID=car_ID, status=status)
            print(cars)
            nodes_json = [node_to_json(record['a'])for record in cars]
            print(nodes_json)
            return nodes_json

def delete_Car(make, model, year, address, car_ID, status):
     _get_connection().execute_query("MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year=$year, a.address=$address, a.car_ID=$car_ID, a.status=$status delete a;", make=make, model=model, year=year,address=address, car_ID=car_ID, status=status)

def Read_Cars():
     with _get_connection.session() as session:
          cars = session.run("MATCH (a:Car) Return a;")
          nodes_json = [node_to_json(record["a"])for record in cars]
          print(nodes_json)
          return nodes_json


#Class and functions for Customer entities
class Customer:
    def __init__(self,name,age, customer_ID, address):
         self.name = name
         self.age = age
         self.customer_ID = customer_ID
         self.address = address

def create_Customer(name,age, customer_ID, address):
     with _get_connection.session() as session:
          customers = session.run("CREATE (p:Customer {name:$name, age:$age, customer_ID:$customer_ID, address:$address})", name=name, age=age, customer_ID=customer_ID, address=address)
          
          nodes_json = [node_to_json(record['p'])for record in customers]
          print(nodes_json)
          return nodes_json

def update_Customer(name, age,customer_ID, address):
          with _get_connection.session() as session:
               customers = session.run("MATCH (p:Customer{reg:$reg})set p.name:$name, p.age:$age, p.customer_ID:$customer_ID, p.address:$address})", name=name, age=age, customer_ID=customer_ID, address=address)
               nodes_json = [node_to_json(record['p'])for record in customers]
               print(nodes_json)
               return nodes_json

def read_Customer():
      with _get_connection.session() as session:
        customers = session.run("MATCH (a:Customer) Return p;")
        nodes_json = [node_to_json(record["p"])for record in customers]
        print(nodes_json)
        return nodes_json


def delete_Customer(name, age, customer_ID, address):
     _get_connection().execute_query("MATCH (p:Customer{reg:$reg}}) delete p;", name=name, age=age,customer_ID=customer_ID, address=address)


#Class and functions for Employee entities
class Employee:
    def __init__(self,name,branch,address):
         self.name = name
         self.branch = branch
         self.address = address

def create_Employee(name,branch, address):
     with _get_connection.session() as session:
          employees = session.run("CREATE (e:Employee {name:$name, branch:$branch, address:$address})", name=name, branch=branch, address=address)
          
          nodes_json = [node_to_json(record['e'])for record in employees]
          print(nodes_json)
          return nodes_json

def update_Employee(name, branch, address):
          with _get_connection.session() as session:
               employees = session.run("MATCH (e:Employee{reg:$reg})set e.name:$name, e.branch:$branch, e.address:$address})", name=name, branch=branch, address=address)
               nodes_json = [node_to_json(record['e'])for record in employees]
               print(nodes_json)
               return nodes_json

def read_Employee():
      with _get_connection.session() as session:
        employees= session.run("MATCH (e:Employee) Return e;")
        nodes_json = [node_to_json(record["e"])for record in employees]
        print(nodes_json)
        return nodes_json


def delete_Employee(name, branch, address):
     _get_connection().execute_query("MATCH (e:Employee{reg:$reg}}) delete e;", name=name, branch=branch, address=address)


#Check customer bookings
def check_customerBookings(customer_ID):
     with _get_connection.session() as session:
          car = session.run("MATCH (p:Customer {customer_ID:$customer_ID})-->(a:Car) RETURN a", customer_ID=customer_ID)
          booked_aCar = [record['a'] for record in car]
          return booked_aCar

def check_car_status(car_ID):
     with _get_connection.session() as session:
          car_status = session.run("MATCH(a:Car {car_ID:$car_ID, status: 'available'})set a.status='booked' RETURN a", car_ID= car_ID )
          return car_status.single()

def create_booking(customer_ID, car_ID):
     with _get_connection.session() as session:
          session.run("MATCH (p:Customer {customer_ID:$customer_ID}), (a:Car {car_ID:$car_ID}) "
                      "CREATE (p)-[:BOOKED]->(a)", customer_ID=customer_ID, car_ID=car_ID)

