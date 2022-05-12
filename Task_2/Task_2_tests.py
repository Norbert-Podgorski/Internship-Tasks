import unittest
import requests


class MyTestCase(unittest.TestCase):
    def test_invalid_login(self):
        url = 'https://restful-booker.herokuapp.com/auth'
        data = {'username': 'admin', 'password': 'password123'}
        self.assertEqual(404, requests.put(url, data=data).status_code)

    def test_get_booking_valid(self):
        url = 'https://restful-booker.herokuapp.com/booking/1322'
        self.assertEqual(200, requests.get(url).status_code)

    def test_get_booking_invalid(self):
        url = 'https://restful-booker.herokuapp.com/booking/1'
        self.assertEqual(404, requests.get(url).status_code)

    def test_get_bookings(self):
        url = 'https://restful-booker.herokuapp.com/booking'
        self.assertEqual(200, requests.get(url).status_code)

    def test_generate_new_booking(self):
        url = "https://restful-booker.herokuapp.com/booking"
        data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        self.assertEqual(200, requests.post(url, json=data).status_code)

    def test_delete_booking(self):
        url = 'https://restful-booker.herokuapp.com/booking/1322'
        self.assertEqual(403, requests.delete(url).status_code)

    def test_health_check(self):
        url = "https://restful-booker.herokuapp.com/ping"
        self.assertEqual(201, requests.get(url).status_code)


if __name__ == '__main__':
    unittest.main()
