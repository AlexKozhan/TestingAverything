import random
import unittest
import requests
from datetime import datetime
from services.config import BaseResponseModel, UserModel, Urls


class TestUserEndpoint(unittest.TestCase):

    def test_get_login(self):
        response = requests.get(Urls.URL_LOGIN, params={"login": "Username", "password": "password"})
        self.assertEqual(response.status_code, 200)
        message = BaseResponseModel.parse_raw(response.text)
        self.assertEqual(message.code, 200)
        self.assertEqual(message.type, "unknown")
        self.assertTrue(message.message.startswith('logged in user session:'))

    def test_get_logout(self):
        response = requests.get(Urls.URL_LOGOUT)
        self.assertEqual(response.status_code, 200)
        message = BaseResponseModel.parse_raw(response.text)
        self.assertEqual(message.code, 200)
        self.assertEqual(message.type, "unknown")
        self.assertEqual(message.message, "ok")

    def test_get_user_not_found(self):
        response = requests.get(f'{Urls.BASE_URL}some_name')
        self.assertEqual(response.status_code, 404)
        message = BaseResponseModel.parse_raw(response.text)
        self.assertEqual(message.code, 1)
        self.assertEqual(message.type, "error")
        self.assertEqual(message.message, 'User not found')

    def test_delete_user_not_found(self):
        response = requests.delete(f'{Urls.BASE_URL}some_name{datetime.utcnow()}')
        self.assertEqual(response.status_code, 404)

    def test_post_create_with_list(self):
        status = random.randint(1, 10000)
        body = UserModel(
            username="Username",
            firstName="Name",
            lastName="Eman",
            email="test@email.com",
            password="testpass",
            phone="129093189",
            userStatus=status
        )

        response = requests.post(Urls.CREATE_WITH_LIST_URL, json=[body.dict()])
        self.assertEqual(response.status_code, 200)
        message = BaseResponseModel.parse_raw(response.text)
        self.assertEqual(message.code, 200)
        self.assertEqual(message.type, "unknown")
        self.assertEqual(message.message, 'ok')

        response2 = requests.get(f'{Urls.BASE_URL}{body.username}')
        self.assertEqual(response2.status_code, 200)
        message2 = UserModel.parse_raw(response2.text)
        self.assertEqual(type(message2.id), int)
        self.assertEqual(message2.username, body.username)
        self.assertEqual(message2.firstName, body.firstName)
        self.assertEqual(message2.lastName, body.lastName)
        self.assertEqual(message2.email, body.email)
        self.assertEqual(message2.password, body.password)
        self.assertEqual(message2.phone, body.phone)
        self.assertEqual(message2.userStatus, body.userStatus)

    def test_post_create_with_array(self):
        time_str = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        status = random.randint(1, 10000)
        body = UserModel(
            username=f"Username{time_str}",
            firstName="Name",
            lastName="Eman",
            email="test@email.com",
            password="testpass",
            phone="129093189",
            userStatus=status
        )

        response = requests.post(Urls.CREATE_WITH_ARRAY_URL, json=[body.dict()])
        self.assertEqual(response.status_code, 200)
        message = BaseResponseModel.parse_raw(response.text)
        self.assertEqual(message.code, 200)
        self.assertEqual(message.type, "unknown")
        self.assertEqual(message.message, 'ok')

        response2 = requests.get(f'{Urls.BASE_URL}{body.username}')
        self.assertEqual(response2.status_code, 200)
        message2 = UserModel.parse_raw(response2.text)
        self.assertEqual(type(message2.id), int)
        self.assertEqual(message2.username, body.username)
        self.assertEqual(message2.firstName, body.firstName)
        self.assertEqual(message2.lastName, body.lastName)
        self.assertEqual(message2.email, body.email)
        self.assertEqual(message2.password, body.password)
        self.assertEqual(message2.phone, body.phone)
        self.assertEqual(message2.userStatus, body.userStatus)

    def test_create_delete_user(self):
        time_str = datetime.now().strftime("%H%M%S")
        status = random.randint(1, 10000)
        body = UserModel(
            username=f"new{time_str}",
            firstName="Name",
            lastName="Eman",
            email="test@email.com",
            password="testpass",
            phone="129093189",
            userStatus=status
        )

        response = requests.post(Urls.BASE_URL, json=body.dict())
        self.assertEqual(response.status_code, 200)
        message = BaseResponseModel.parse_raw(response.text)
        self.assertEqual(message.code, 200)
        self.assertEqual(message.type, "unknown")
        self.assertEqual(type(message.message), str)

        response2 = requests.get(f'{Urls.BASE_URL}{body.username}')
        self.assertEqual(response2.status_code, 200)
        message2 = UserModel.parse_raw(response2.text)
        self.assertEqual(type(message2.id), int)
        self.assertEqual(message2.username, body.username)
        self.assertEqual(message2.firstName, body.firstName)
        self.assertEqual(message2.lastName, body.lastName)
        self.assertEqual(message2.email, body.email)
        self.assertEqual(message2.password, body.password)
        self.assertEqual(message2.phone, body.phone)
        self.assertEqual(message2.userStatus, body.userStatus)

        response3 = requests.delete(f'{Urls.BASE_URL}{body.username}')
        self.assertEqual(response3.status_code, 200)
        message3 = BaseResponseModel.parse_raw(response3.text)
        self.assertEqual(message3.code, 200)
        self.assertEqual(message3.type, "unknown")
        self.assertEqual(message3.message, body.username)

        response4 = requests.get(f'{Urls.BASE_URL}{body.username}')
        self.assertEqual(response4.status_code, 404)
        message4 = BaseResponseModel.parse_raw(response4.text)
        self.assertEqual(message4.code, 1)
        self.assertEqual(message4.type, 'error')
        self.assertEqual(message4.message, "User not found")


if __name__ == '__main__':
    unittest.main()
