import unittest
from singleton_class import Singleton

class TestSingletonClass(unittest.TestCase):
    def test_single_instance_creation(self):
        instance1 = Singleton()
        instance2 = Singleton()
        self.assertIs(instance1, instance2)
        
if __name__=='__main__':
    unittest.main()
    