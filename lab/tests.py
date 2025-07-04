import random
from math import expm1
from multiprocessing.context import set_spawning_popen

import pytest

from project import Server, Client


def test_send_ugly():
    server = Server(80)
    server.start()
    assert server.status == True
    client = Client(80)
    message = "Test message"
    response = client.send(message)
    assert response == f"Server: {message}"

# ------------------8<------------------------------

# pripravi testovaciu spravu a ocakávanu odpoved
# vytvori sa len raz pre celu testovaciu session (vsetky testy)
@pytest.fixture(scope="session")
def data_message():
    message = "Test Message"
    expected = f"Server: {message}"
    return message, expected

# pre kazdy test novy port?? ze nebudu dva rovnake porty v dvoch portoch - kolizia
@pytest.fixture(scope="function")
def data_port():
    return random.randint(1,100)

# vytvori a spusti server - system under test
@pytest.fixture()
def sut_server(data_port):
    server = Server(data_port) # vytv server s nahodnym portom
    server.start() # spusti server
    yield server # odovzda server testu
    server.stop() # po teste sa server zastavi, uvolni sa port

# vytvori klienta pripojeneho na rovn port ako server
@pytest.fixture()
def sut_client(data_port):
    client = Client(data_port)
    return client


def test_send_fixtures(sut_server, sut_client, data_message):
    response = sut_client.send(data_message[0])
    assert response == data_message[1]