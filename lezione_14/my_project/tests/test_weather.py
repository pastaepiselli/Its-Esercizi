from my_project.weather import check_weather

def test_check_weather():
    assert check_weather(21.00) == 'hot', 'temperature greater than 20 degree \
        must be consider as hot'
        