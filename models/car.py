from driver import _get_connection, node_to_json

class Car:
    def __init__(self, make, model, year, address, car_ID, status):
        self.make = make
        self.model = model
        self.year = year
        self.address = address
        self.car_ID = car_ID
        self.status = status


def create_Car(make, model, year, address, car_ID, status):
    with _get_connection.session() as session:
        cars = session.run(
            "CREATE (a:Car {make: $make, model:$model, year:$year, address:$address, car_ID:$car_ID, status:$status})",
            make=make, model=model, year=year, address=address, car_ID=car_ID, status=status)

        nodes_json = [node_to_json(record['a']) for record in cars]
        print(nodes_json)
        return nodes_json


def update_Car(make, model, year, address, car_ID, status):
    with _get_connection.session() as session:
        cars = session.run(
            "MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year=$year, a.address=$address, a.car_ID=$car_ID, a.status=$status RETURN a;",
            make=make, model=model, year=year, address=address, car_ID=car_ID, status=status)
        print(cars)
        nodes_json = [node_to_json(record['a']) for record in cars]
        print(nodes_json)
        return nodes_json


def delete_Car(make, model, year, address, car_ID, status):
    _get_connection().execute_query(
        "MATCH (a:Car{reg:$reg}) set a.make=$make, a.model=$model, a.year=$year, a.address=$address, a.car_ID=$car_ID, a.status=$status delete a;",
        make=make, model=model, year=year, address=address, car_ID=car_ID, status=status)


def Read_Cars():
    with _get_connection.session() as session:
        cars = session.run("MATCH (a:Car) Return a;")
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json


def check_car_status(car_ID):
    with _get_connection.session() as session:
        car_status = session.run("MATCH(a:Car {car_ID:$car_ID, status: 'available'})set a.status='booked' RETURN a",
                                 car_ID=car_ID)
        return car_status.single()
