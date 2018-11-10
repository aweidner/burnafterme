import time
import re

def get_key(response):
    return re.match(r'http://localhost/([a-zA-Z0-9].*)', response.data.decode('utf-8')).group(1)


def test_adding_data(client):
    response = client.put('/', data = 'Hello World')
    assert response.status == '200 OK'
    assert re.match(r'http://localhost/[a-zA-Z0-9].*', response.data.decode('utf-8'))


def test_getting_data(client):
    key = get_key(client.put('/', data = 'Hello World'))
    client.get(f'/{key}').data == b'Hello World'


def test_multiple_keys_can_be_used(client):
    hello = get_key(client.put('/', data = 'Hello World'))
    goodbye = get_key(client.put('/', data = 'Goodbye World'))

    assert client.get(f'/{hello}').data == b'Hello World'
    assert client.get(f'/{goodbye}').data == b'Goodbye World'


def test_data_is_deleted_after_first_access(client):
    hello = get_key(client.put('/', data = 'Hello World'))

    assert client.get(f'/{hello}').data == b'Hello World'
    assert client.get(f'/{hello}').status == '404 NOT FOUND'


def test_returns_404_when_key_not_found(client):
    assert client.get('/something_never_found').status == '404 NOT FOUND'


def test_data_is_deleted_after_timeout_without_access(client):
    key = get_key(client.put('/?t=1s', data = 'Hello World'))
    time.sleep(2)
    assert client.get(f'/{key}').status == '404 NOT FOUND'
