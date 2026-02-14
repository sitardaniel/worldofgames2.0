import pytest
from MainScores import app


@pytest.fixture
def client():
    """Create test client for Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint(client):
    """Test /health endpoint returns 200"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'


def test_ready_endpoint(client):
    """Test /ready endpoint returns 200"""
    response = client.get('/ready')
    assert response.status_code == 200
    assert response.json['status'] == 'ready'


def test_metrics_endpoint(client):
    """Test /metrics endpoint returns Prometheus metrics"""
    response = client.get('/metrics')
    assert response.status_code == 200
    assert b'http_requests_total' in response.data


def test_score_page_returns_html(client):
    """Test main page returns HTML"""
    response = client.get('/')
    assert response.status_code in [200, 500]  # 500 if no Scores.txt
    assert b'<html>' in response.data
