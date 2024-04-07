'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'abcdstring'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MTM3Mzc2NjMsIm5iZiI6MTcxMjUyODA2MywiZW1haWwiOiJhYmNAeHl6LmNvbSJ9.ucX3x9eRgkfvsyQA6Lo6pKuHxFL-qZx6jL12xAnfZ6g'
EMAIL = 'abc@xyz.com'
PASSWORD = 'mypwd'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
