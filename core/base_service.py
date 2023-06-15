import requests


class BaseService:
    @staticmethod
    def post(self):
        pass

    @staticmethod
    def get(url, code=200):
        response = requests.request("GET", url)
        body = response.json()
        assert response.status_code == code
        return body

    @staticmethod
    def put(self):
        pass

    @staticmethod
    def delete(self):
        pass
