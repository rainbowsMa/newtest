#导包
import unittest
import requests

#设置测试类
class TestDepQueryByName(unittest.TestCase):
    def test_depQuery_byName(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        params={"dep_name":"Test学院"}
        res = requests.get(url,params)
        self.assertEqual(200,res.status_code)

    def test_depQuery_byName_notExistsName(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        params = {"dep_name": "dadfadf"}
        res = requests.get(url, params)
        self.assertEqual(200, res.status_code)

    if __name__ =='__main__':
        unittest.main()


