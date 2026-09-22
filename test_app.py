from app import app

def test_health():
    r = app.test_client().get("/health")
    assert r.status_code == 200

def test_home_tiene_version():
    r = app.test_client().get("/")
    assert "version" in r.get_json()