from graphene.test import Client
# import sys
# sys.path.append("..")
from main import schema
# from string import Template
img = open('my.png', 'rb')


# from snapshottest import TestCase
# from unittest import TestCase
import logging
logger = logging.getLogger(__name__)










import pytest

# from app import db


# @pytest.fixture
# def admin_client(mock_admin_request):
#     return Client(schema)


# @pytest.mark.asyncio
# @pytest.fixture
# async def db_connect():
#     conn = db.connection() if db.is_connected else await db.connect()
#     yield conn
#     await db.disconnect()


# @pytest.fixture
# def mock_request(token):
#     return Request(
#         dict(
#             type="http",
#             headers=[(b"authorization", ("Bearer " + token).encode("latin-1"))],
#         )
#     )


# @pytest.fixture
# def mock_admin_request(admin_jwt):
#     return mock_request(admin_jwt)


# @pytest.fixture
# def mock_iqmodule_request(iqmodule_jwt):
#     return mock_request(iqmodule_jwt)
# @pytest.fixture
# def error_fixture():
#     assert "pk"

# logging.basicConfig(
#     filename='test.log',
#     filemode='w',
#     level=logging.ERROR,
#     format = '%(asctime)s - %(levelname)s: %(message)s',
# )
# @pytest.fixture


# Test For Authentication
def test_auth():
    client = Client(schema)
    response = client.execute(
        """mutation a {
        auth(email: "ranaamnan181@gmail.com", password:"amnan181") {
            accessToken
            message
        }
    }"""
    )
    
    assert response["data"]["auth"]
    return response["data"]["auth"]

# Test For Uploading File
def test_file_uploading():
    client = Client(schema)
    variables = {
            'file': img
        }
    response = client.execute(
        """mutation uploadFile($file: Upload!) {
  uploadFile(file: $file) {
    success
    filename
    extension
    size
  }
}""",variables
    )
    logger.critical(response)
    assert response["data"]
    return response["data"]

# def test_ok():
#     client = Client(schema)
#     response = client.execute(
#         """mutation a {
#         auth(email: "ranaamnan181@gmail.com", password:"amnan181") {
#             accessToken
#             message
#         }
#     }"""
#     )
#     print(response)
#     assert 1
#     return response["accessToken"]
#     print("ok")


# def test_fail():
#     assert 0


# def test_error(error_fixture):
#     pass


# def test_skip():
#     pytest.skip("skipping this test")


# def test_xfail():
#     pytest.xfail("xfailing this test")


# @pytest.mark.xfail(reason="always xfail")
# def test_xpass():
#     pass












# class APITestCase(TestCase):
#     def test_todos_for_login_user(self):
#         """Testing the API for /me"""
#         client = Client(schema)
#         self.assertMatchSnapshot(client.execute('''

        

#                                                 '''))

# def test_hey():
#     client = Client(schema)
    # q = Template('''mutation{ uploadFile(file:$file) {
    #     success
    #     } }
        
        
    #     ''')
#     with open('my.png', 'rb') as img:
#         query = q.substitute(file=img)
#         executed = client.execute(query)
#         print(executed)
    # assert executed == {
    #     'file': "ok"
    # }
    
# if __name__ == '__main__':
#     unittest.main()    
# test_hey()