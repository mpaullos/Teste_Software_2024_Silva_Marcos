import unittest
import localweather
from ourtcfw import OurTcFw

class MyCase(OurTcFw):
    def testItIsSunny(self):
        self.assertTrue(localweather.sunny)

    def testItIsHot(self):
        self.assertTrue(localweather.temperature > 20)
        
        

if __name__ == "__main__":
    unittest.main()