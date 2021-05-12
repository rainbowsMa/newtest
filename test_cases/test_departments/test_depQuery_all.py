#导包
import unittest
import requests
#设置测试类
class TestDepQueryAll(unittest.TestCase):
    #查询学院所有冒烟测试
    def test_depQuery_all(self):
        url=r'http://127.0.0.1:8000/api/departments/'
        res=requests.get(url)
        self.assertEqual(200,res.status_code)
    #查询学院所有，用错误的方法
    def test_depQuery_all_wrongMethod(self):
        url = r'http://127.0.0.1:8000/api/departments/'
        res = requests.post(url)  #用post方法（错误的方法）
        self.assertEqual(200, res.status_code)
if __name__=="__main__":
    unittest.main()