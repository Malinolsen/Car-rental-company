from driver import _get_connection, node_to_json


# Class and functions for Customer entities
class Customer:
    def __init__(self, name, age, customer_ID, address):
        self.name = name
        self.age = age
        self.customer_ID = customer_ID
        self.address = address

def create_Customer(name, age, customer_ID, address):
    with _get_connection.session() as session:
        customers = session.run(
            "CREATE (p:Customer {name:$name, age:$age, customer_ID:$customer_ID, address:$address})", name=name,
            age=age, customer_ID=customer_ID, address=address)

        nodes_json = [node_to_json(record['p']) for record in customers]
        print(nodes_json)
        return nodes_json


def update_Customer(name, age, customer_ID, address):
    with _get_connection.session() as session:
        customers = session.run(
            "MATCH (p:Customer{reg:$reg})set p.name:$name, p.age:$age, p.customer_ID:$customer_ID, p.address:$address})",
            name=name, age=age, customer_ID=customer_ID, address=address)
        nodes_json = [node_to_json(record['p']) for record in customers]
        print(nodes_json)
        return nodes_json


def read_Customer():
    with _get_connection.session() as session:
        customers = session.run("MATCH (a:Customer) Return p;")
        nodes_json = [node_to_json(record["p"]) for record in customers]
        print(nodes_json)
        return nodes_json


def delete_Customer(name, age, customer_ID, address):
    _get_connection().execute_query("MATCH (p:Customer{reg:$reg}}) delete p;", name=name, age=age,
                                    customer_ID=customer_ID, address=address)


#Check customer bookings
def check_customerBookings(customer_ID,car_ID):
     with _get_connection.session() as session:
          car = session.run("MATCH (p:Customer {customer_ID:$customer_ID})-->(a:Car) RETURN a", customer_ID=customer_ID)
          booked_aCar = [record['a'] for record in car]
          return booked_aCar


def create_booking(customer_ID, car_ID):
    with _get_connection.session() as session:
        session.run("MATCH (p:Customer {customer_ID:$customer_ID}), (a:Car {car_ID:$car_ID}) "
                    "CREATE (p)-[r:BOOKED]->(a)", customer_ID=customer_ID, car_ID=car_ID)

