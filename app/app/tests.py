from django.test import SimpleTestCase
from app import calc


class SimpleTests(SimpleTestCase):
    
        def test_calc(self):
            res = calc.add(1, 2)
            self.assertEqual(res, 3)
        
        
        def test_subtract(self):
            res = calc.subtract(15, 10)
            self.assertEqual(res, 5)

        

