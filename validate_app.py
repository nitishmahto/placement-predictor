from app import app


def main():
    client = app.test_client()

    home = client.get('/')
    assert home.status_code == 200, home.status_code
    assert 'AI Placement Predictor' in home.get_data(as_text=True), home.get_data(as_text=True)[:200]

    prediction = client.post('/predict', data={
        'cgpa': '8.5',
        'skills': '5',
        'projects': '2',
        'internships': '1',
    })
    assert prediction.status_code == 200, prediction.status_code
    assert 'Placement probability' in prediction.get_data(as_text=True), prediction.get_data(as_text=True)[:200]

    health = client.get('/health')
    assert health.status_code == 200, health.status_code
    assert 'status' in health.get_json(), health.get_json()

    print('Validation passed: home, health, and prediction routes work.')


if __name__ == '__main__':
    main()
