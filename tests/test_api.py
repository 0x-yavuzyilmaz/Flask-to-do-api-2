import pytest
from main import app # Ana uygulama dosyamızdan 'app' nesnesini import ediyoruz

@pytest.fixture
def client():
    # Bu fixture, her test fonksiyonu çalışmadan önce,
    # uygulamamızın bir test istemcisini (test client) oluşturur.
    # Bu, sunucuyu gerçekten başlatmadan, istek gönderebilen sihirli bir araçtır.
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client # yield, return gibidir ama test bittikten sonra temizlik yapılmasına izin verir.

# --- Test Fonksiyonları ---

def test_get_all_todos(client):
    """
    GET /api/todos endpoint'ini test eder.
    - Başarılı bir 200 OK durum kodu dönmeli.
    - Dönen veri bir liste olmalı.
    - Listenin içinde en az 3 eleman olmalı (başlangıç verimiz).
    """
    # 1. Adım: Eylem (Act)
    # Test istemcisini kullanarak endpoint'e bir GET isteği gönder.
    response = client.get('/api/todos')

    # 2. Adım: Doğrulama (Assert)
    # Gelen cevabın özelliklerinin beklediğimiz gibi olup olmadığını kontrol et.
    # 'assert' anahtar kelimesi, bir koşulun 'True' olup olmadığını kontrol eder.
    # Eğer koşul 'False' ise, test başarısız olur.
    assert response.status_code == 200
    assert response.is_json
    json_data = response.get_json()
    assert isinstance(json_data, list)
    assert len(json_data) == 2

def test_get_single_todo_found(client):
    """
    Var olan bir 'todo' için GET /api/todos/<id> endpoint'ini test eder.
    """
    response = client.get('/api/todos/1')
    assert response.status_code == 200
    assert response.is_json
    json_data = response.get_json()
    assert json_data['id'] == 1
    assert json_data['task'] == 'Build a REST API'

def test_get_single_todo_not_found(client):
    """
    Var olmayan bir 'todo' için GET /api/todos/<id> endpoint'ini test eder.
    - 404 Not Found durum kodu dönmeli.
    """
    response = client.get('/api/todos/99')
    assert response.status_code == 404