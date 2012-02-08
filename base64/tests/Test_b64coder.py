import unittest
import sys
sys.path[0:0] = [""]
import base64
from nose.tools import *
import b64coder
from random import randint
from array import *


# random array generator for random string testing
def randarray(typecode, numElements, minValue, maxValue):
    a = array(typecode)
    for i in xrange(0, numElements):
        a.append(randint(minValue, maxValue))
    return a

randnums1 = list(randarray('i', 11, 0, 255))
randnums2 = list(randarray('i', 753, 0, 255))
randnums3 = list(randarray('i', 20000, 0, 255))

# string concatenator
def stringGen(number_list):
    teststring = ""
    for i in range(0, len(number_list)):
        tmp = chr(number_list[i])
        teststring += tmp
    return teststring

# place strings to test here
testerstring1 = stringGen(randnums1)
testerstring2 = stringGen(randnums2)
testerstring3 = stringGen(randnums3)
testerstring4 = ""
testerstring5 = "**************"
testerstring6 = "?A?df/ad/DS?fAsd/A?sdzZ/xc//221eaD//csZ?Xcv/zxCV?zDX/vAWER/bhaerbhASETB*"
testerstring7 = "?23-=2--=32-=32-=-al--23``~=-l`\|}[[{sa-=cvxzc-v=-xcv=z-cv=-321=-"
testerstring8 = "game"
testerstring9 = "imakeitrain"
testerstring10 = "sonned"


# main testing class for nose tests. assertEqual is a method from unittest
class TestEncoding(unittest.TestCase):

    def test_string1(self):
        self.assertEqual(b64coder.str_to_base64(testerstring1), base64.b64encode(testerstring1))

    def test_string2(self):
        self.assertEqual(b64coder.str_to_base64(testerstring2), base64.b64encode(testerstring2))

    def test_string3(self):
        self.assertEqual(b64coder.str_to_base64(testerstring3), base64.b64encode(testerstring3))

    def test_string4(self):
        self.assertEqual(b64coder.str_to_base64(testerstring4), base64.b64encode(testerstring4))

    def test_string5(self):
        self.assertEqual(b64coder.str_to_base64(testerstring5), base64.b64encode(testerstring5))

    def test_string6(self):
        self.assertEqual(b64coder.str_to_base64(testerstring6), base64.b64encode(testerstring6))

    def test_string7(self):
        self.assertEqual(b64coder.str_to_base64(testerstring7), base64.b64encode(testerstring7))

    def test_string8(self):
        self.assertEqual(b64coder.str_to_base64(testerstring8), base64.b64encode(testerstring8))

    def test_string9(self):
        self.assertEqual(b64coder.str_to_base64(testerstring9), base64.b64encode(testerstring9))

    def test_string10(self):
        self.assertEqual(b64coder.str_to_base64(testerstring10), base64.b64encode(testerstring10))

if __name__ == "__main__":
    unittest.main()
