import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['FLASK_ENV'] = 'testing'
    
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "Comparar países" in response.data.decode('utf-8')

def test_comparar_validos(client):
    response = client.get('/comparar?pais1=bn&pais2=cm')
    assert response.status_code == 200
    assert b"PIB (PPA)" in response.data  # "PIB (PPA)" es ASCII, así que no hay problema

def test_comparar_invalidos(client):
    response = client.get('/comparar?pais1=invalid&pais2=cm')
    assert response.status_code == 400
    assert "No se pudieron obtener los datos de uno o ambos países".encode('utf-8') in response.data
