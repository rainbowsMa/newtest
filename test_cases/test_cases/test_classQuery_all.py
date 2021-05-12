#导包
import unittest
import requests
#用例类
class TeseClassQueryAll(unittest.TestCase):
    #测试1  基本冒烟测试
    def test_classQuery_all(self):
        url=r'http://127.0.0.1:8000/api/departments/T01/classes/'
        res=requests.get(url)
        self.assertEqual(200,res.status_code) #断言状态码
    #测试2   路径错误测试
    def test_classQuery_all_wrongPath(self):
        url=r'http://127.0.0.1:8000/api/departments/sdfsdf/classes/'
        res=requests.get(url)
        self.assertEqual(404,res.status_code)
#类的内部校验
if __name__ =='__main__':
    unittest.main()
