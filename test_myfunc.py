import unittest
from operation import arithmetic

class TestMyFunc(unittest.TestCase):

    def setUp(self):
        print("每个用例执行前会调用setUp准备环境")

    def tearDown(self):
        print("每个用例执行后会调用tearDown方法进行环境清理")
    
    def test_add(self):
        print('add')
        self.assertEqual(3,arithmetic(1,2,"add"))
        self.assertNotEqual(3,arithmetic(2,2,"add"))

    def test_subtract(self):
        print('subtract')
        self.assertEqual(1,arithmetic(2,1,"subtract"))
        self.assertNotEqual(3,arithmetic(2,2,"subtract"))

    def test_multiply(self):
        print("multiply")
        self.assertEqual(6,arithmetic(2,3,"multiply"))
        self.assertNotEqual(3,arithmetic(12,3,"multiply"))
    
    def test_divide(self):
        print("divide")
        self.assertEqual(2,arithmetic(6,3,"divide"))
        self.assertNotEqual(3,arithmetic(12,3,"divide"))

if __name__ == '__main__':
    unittest.main()
