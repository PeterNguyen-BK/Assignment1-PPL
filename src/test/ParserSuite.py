import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x[3][2] = {{1,2,3},{1,2}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_1(self):
        """Miss variable"""
        input = """Function: fact
                        Parameter: n, x, y
                        Body:
                            Var: r = 2;
                            Var: v[3] = {1,2,3};
                            Var: a[2] = {1,2};
                            a[2] = 19;
                        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))