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