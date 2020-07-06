import unittest
import requests
import json

class UserTest(unittest.TestCase):
    API_URL = 'http://127.0.0.1:5000'
    USER_URL = f'{API_URL}/user'
    NEW_USER_ID = 6
    OAUTH_PROVIDER = 'google'
    OAUTH_TOKEN = '123456789'
    NEW_USER = {
    "name": "your name",
    "email": "abc@gmail.com",
    "password": "Pass",
    }
    UPDATE_USER = {
    "name": "your name",
    "email": "abc@gmail.com",
    "password": "Pass",
    }
  

    #Get request to /user returns all the users
    def test_1_get_all_users(self):
        r = requests.get(UserTest.USER_URL)
        self.assertEqual(r.status_code, 200)

    #post request to /user to add new user
    def test_2_add_new_user(self):
        r = requests.post(UserTest.USER_URL, json = UserTest.NEW_USER)
        self.assertEqual(r.status_code, 200)
        UserTest.NEW_USER_ID = json.loads(r.text)['user_id']
        print(UserTest.NEW_USER_ID)

    #put request to user/id to update user
    def test_3_update_existing_user(self):
        r = requests.put(f'{UserTest.USER_URL}/{UserTest.NEW_USER_ID}', json = UserTest.UPDATE_USER)
        self.assertEqual(r.status_code, 200)


    #Delete request to /user/id delete the user
    def test_4_delete_user(self):
        r = requests.delete(f'{UserTest.USER_URL}/{UserTest.NEW_USER_ID}')
        self.assertEqual(r.status_code, 200)

    

if __name__ == "__main__":
    unittest.main()