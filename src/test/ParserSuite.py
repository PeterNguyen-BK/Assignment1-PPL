import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,200))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_1(self):
        """Miss variable"""
        input = """Var: x"""
        expect = "Error on line 1 col 6: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_2(self):
        """Miss variable"""
        input = """Var: x = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
    
    def test_3(self):
        """Miss variable"""
        input = """Var x,y,z;"""
        expect = "Error on line 1 col 4: x"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    
    def test_4(self):
        """Miss variable"""
        input = """Var: x = 5, y;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_5(self):
        """Miss variable"""
        input = """Var: x = 5 y;"""
        expect = "Error on line 1 col 11: y"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    
    def test_6(self):
        """Miss variable"""
        input = """Var: x = 5, y, z = 7;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    
    def test_7(self):
        """Miss variable"""
        input = """Var: x = "hello", y = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    
    def test_8(self):
        """Miss variable"""
        input = """Var: x = 12.e5, y = "test, z = 2;"""
        expect = "test, z = 2;"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test_9(self):
        """Miss variable"""
        input = """var: x = 10;"""
        expect = "Error on line 1 col 0: var"
        self.assertTrue(TestParser.checkParser(input,expect,210))
    
    def test_10(self):
        """Miss variable"""
        input = """Var: x = True;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
    def test_11(self):
        """Miss variable"""
        input = """Var: x = true, y = False;"""
        expect = "Error on line 1 col 9: true"
        self.assertTrue(TestParser.checkParser(input,expect,212))
    
    def test_12(self):
        """Miss variable"""
        input = """Var: x == True;"""
        expect = "Error on line 1 col 7: =="
        self.assertTrue(TestParser.checkParser(input,expect,213))
    
    def test_13(self):
        """Miss variable"""
        input = """Var: x, y, z, d e;"""
        expect = "Error on line 1 col 16: e"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    
    def test_14(self):
        """Miss variable"""
        input = """Var: x[1] = {10};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))
    
    def test_15(self):
        """Miss variable"""
        input = """Var: x[-2] = {1,2};"""
        expect = "Error on line 1 col 7: -"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    
    def test_16(self):
        """Miss variable"""
        input = """Var: x[2][3] = {{1,2},{1,2,3}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))
    
    def test_17(self):
        """Miss variable"""
        input = """Var: x = {1,2};"""
        expect = "Error on line 1 col 9: {1,2}"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_18(self):
        """Miss variable"""
        input = """Var: x[2][3] = {{1,2},{1,2,3};"""
        expect = "Error on line 1 col 15: {"
        self.assertTrue(TestParser.checkParser(input,expect,219))
    
    def test_19(self):
        """Miss variable"""
        input = """Var: x[2] = {"Text1","Text2"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    
    def test_20(self):
        """Miss variable"""
        input = """Var: x[1] = {12e-5,12e-5};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))
    
    def test_21(self):
        """Miss variable"""
        input = """Var: x = 12e;"""
        expect = "Error on line 1 col 11: e"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    
    def test_22(self):
        """Miss variable"""
        input = """Var: x = 012123;"""
        expect = "Error on line 1 col 10: 12123"
        self.assertTrue(TestParser.checkParser(input,expect,223))
    
    def test_23(self):
        """Miss variable"""
        input = """Var: x = 0xABC;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_24(self):
        """Miss variable"""
        input = """Varr: x = 0xABC;"""
        expect = "Error on line 1 col 3: r"
        self.assertTrue(TestParser.checkParser(input,expect,225))
    
    def test_25(self):
        """Miss variable"""
        input = """Var: x156 = 0xABC;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))
    
    def test_26(self):
        """Miss variable"""
        input = """Var: 123 = 0xABC;"""
        expect = "Error on line 1 col 5: 123"
        self.assertTrue(TestParser.checkParser(input,expect,227))
    
    def test_27(self):
        """Miss variable"""
        input = """Var: x123 = 0o123;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))
    
    def test_28(self):
        """Miss variable"""
        input = """Var: x = 0.123213;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test_29(self):
        """Miss variable"""
        input = """Var: x[2] = {True,False};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))
    
    def test_30(self):
        """Miss variable"""
        input = """Var: x[2 = {1,2};"""
        expect = "Error on line 1 col 9: ="
        self.assertTrue(TestParser.checkParser(input,expect,231))
    
    def test_31(self):
        """Miss variable"""
        input = """
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n - 1;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))
    
    def test_32(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                x = 10;
                fact(x);
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    
    def test_33(self):
        """Miss variable"""
        input = """
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody."""
        expect = "Error on line 7 col 16: Else"
        self.assertTrue(TestParser.checkParser(input,expect,234))
    
    def test_34(self):
        """Miss variable"""
        input = """
        Function: fact
            Parameter: n
            Body:
                if n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody."""
        expect = "Error on line 5 col 19: n"
        self.assertTrue(TestParser.checkParser(input,expect,235))
    
    def test_35(self):
        """Miss variable"""
        input = """
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact(x);
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    
    def test_36(self):
        """Miss variable"""
        input = """
        Function: gcd
            Parameter: a,b
            Body:
                If b == 0 Then
                    Return a;
                Else
                    Return gcd(b, a%b);
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))
    
    def test_37(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n
            Body:
                If n == 0 Then
                    Return "Hihi";
                ElseIf n == 1 Then
                    Return "Huhu";
                Else 
                    Return "Haha";
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    
    def test_38(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n
            Body:
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))
    
    def test_39(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: x = 1, y, z = 12.e5;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    
    def test_40(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: x = 1, y, z = 12.e5;
                Return x + y + z;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))
    
    def test_41(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))
    
    def test_42(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                EndFor.
            EndBody"""
        expect = "Error on line 7 col 19: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,243))
    
    def test_43(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                EndFor
            EndBody."""
        expect = "Error on line 7 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    
    def test_44(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: i = 0;
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                EndFor
            EndBody."""
        expect = "Error on line 8 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,245))
    
    def test_45(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: i = 0;
                While (i < 5) Do
                    a[i + foo(3)] = b +. 1.0;
                    i = i + 1;
                EndWhile.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))
    
    def test_46(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: i = 0;
                Do x = x + 2; 
                While x < 9
                EndDo.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))
    
    def test_47(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: r = 10., v;
                v = (4. \. 3.) *. 3.14 *. r *. r *. r;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_48(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: i = 0;
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                    If i == 5 Then 
                        Break;
                    EndIf.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))
    
    def test_49(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: i = 0;
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                    If i == 5 Then 
                        break;
                    EndIf.
                EndFor.
            EndBody."""
        expect = "Error on line 8 col 29: ;"
        self.assertTrue(TestParser.checkParser(input,expect,250))
    
    def test_50(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: i = 0;
                For (i = 0, i < 10, 2) Do
                    writeln(i);
                    Continue;
                    If i == 5 Then 
                        Break;
                    EndIf.
                EndFor.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    
    def test_51(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: x;
                x = -5 - 6 + ! 5 - 9 - ! -(3 + ! -5);
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))
    
    def test_52(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: x;
                x = "Hello" + "World";
            EndBody."""
        expect = "Error on line 5 col 20: Hello"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    
    def test_53(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: x, y;
                x = (2 == 3);
                y = (2 != 3);
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    
    def test_54(self):
        """Miss variable"""
        input = """
        Function: main
            Body:
                Var: x, y;
                x = (2 + 3) * 4 - 5 \ 10 +. 12.2;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))
    
    def test_55(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: a,b
            Body:
                Var: x[2] = {1,2}, y[3] = {4,5,6};
                a = (2 + 3) * 4 - 5 \ 10 +. 12.2;
                b = x[1] + y[2] + a;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))
    
    def test_56(self):
        """Miss variable"""
        input = """
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody.
        Function: main
            Parameter: a,b
            Body:
                a = fact(5);
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    
    def test_57(self):
        """Miss variable"""
        input = """
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody.
        Function: main
            Parameter: a,b
            Body:
                a = fact(5) + 2 \ 4 * (2 + 4) -. 3.45e-5;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    
    def test_58(self):
        """Miss variable"""
        input = """
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody.
        Function: main
            Parameter: a,b
            Body:
                a = fact(2 \ 4 * (2 + 4) -. 3.45e-5) + 1;
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    
    def test_59(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n,m
            Body:
                If (n == 0) || (m == 0) Then
                    Return n + m;
                Else
                    Return n - m;
                EndIf.
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    
    def test_60(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n,m
            Body:
                Return n + m;
            """
        expect = "Error on line 6 col 12: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,261))
    
    def test_61(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n,m
            Body:
                Return n || m;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    
    def test_62(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n,m
            Body:
                Return n && m;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    
    def test_63(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n,m
            Body:
                Var: a = True;
                Return !a;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    
    def test_64(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n,m
            Body:
                Var: a = 15.6e3, b = 0.1234;
                If a =/= b Then
                    If a >. b Then 
                        Return a -. b;
                    Else
                        Return b -. a;
                    EndIf.
                Else 
                    Return "Equal";  
                EndIf.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    
    def test_65(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n,m
            Body:
                Var: a = 15.6e3, b = 0.1234;
                If a =/= b Then
                    If a >. b Then
                        Var: i = 0;
                        Return a[i - 1];
                    Else
                        Return b -. a;
                    EndIf.
                Else 
                    Return "Equal";  
                EndIf.
            EndBody.
            """
        expect = "Error on line 8 col 24: Var"
        self.assertTrue(TestParser.checkParser(input,expect,266))
    
    def test_66(self):
        """Miss variable"""
        input = """
        Function: main
            Parameter: n,m
            Body:
                Var: a = 15.6e3, b = 0.1234, x[2] = {1.2,2.3e-5};
                If (a =/= b) || (n == True) || (m == False) Then
                    x[2] = a +. b -. x[1];
                Else 
                    Return x[1 + 1];  
                EndIf.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    
    def test_67(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Return t;
            EndBody.
        Function: main
            Parameter: n,m
            Body:
                Var: x[5] = {1,2,3,4,5};
                x[3 + foo(3)] = 2 + foo(4);
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))
    
    def test_68(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Return t;
            EndBody.
        Function: main
            Parameter: n,m
            Body:
                Var: x[5][3] = {{1,2,3,4,5},{1,2,3}};
                x[3 + foo(3)][3] = 2 + foo(4);
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))
    
    def test_69(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Return t;
            EndBody.
        Function: main
            Parameter: n,m
            Body:
                Var: x[5][3][2] = {{1,2,3,4,5},{1,2,3},{5,6}};
                x[3 + foo(3)][3][m + 3] = 2 + foo(4);
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    
    def test_70(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Return t;
            EndBody.
        Function: main
            Parameter: n,m
            Body:
                Var: x[5][3][2] = {{1,2,3,4,5},{1,2,3},{5,6}};
                x[3 + foo(3)][3][m + 3] = 2 + foo(4);
                If x[2] == 5 Then
                    Var: y;
                EndIf.
            EndBody.
            """
        expect = "Error on line 13 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,271))
    
    def test_71(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Return t;
            EndBody.
        Function: main
            Parameter: n,m
            Body:
                Var: x[5][3][2] = {{1,2,3,4,5},{1,2,3},{5,6}};
                x[3 + foo(3)][3][m + 3] = 2 + foo(4);
                If x[2] == 5 Then
                    Var: y;
                EndIf.
            EndBody.
            """
        expect = "Error on line 13 col 20: Var"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    
    def test_72(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Return ;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    
    def test_73(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Var: x = y;
                Return x;
            EndBody.
            """
        expect = "Error on line 5 col 25: y"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    
    def test_74(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t; x = 12, y = 12.
            Body:
                Var: z = 2;
                Return x;
            EndBody.
            """
        expect = "Error on line 3 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    
    def test_75(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Var: z[2] = {1,2};
                z[True] = 2;
            EndBody.
            """
        expect = "Error on line 6 col 18: True"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    
    def test_76(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Var: z[2] = {1,2};
                z[2.] = 2;
            EndBody.
            """
        expect = "Error on line 6 col 18: 2."
        self.assertTrue(TestParser.checkParser(input,expect,277))
    
    def test_77(self):
        """Miss variable"""
        input = """
        Function : foo
            Parameter: t
            Body:
                Var: z[2] = {1,2};
                z["Two"] = 2;
            EndBody.
            """
        expect = "Error on line 6 col 18: Two"
        self.assertTrue(TestParser.checkParser(input,expect,278))
    
    def test_78(self):
        """Miss variable"""
        input = """
        Function : main
            Parameter: t
            Body:
                Var: a[5] = {1,2,3,4,5}, b[3][5] = {{1,2,3},{4,5,6,7,8}};
                a[3 + foo(2)] = a[b[2][3]] + 4;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))
    
    def test_79(self):
        """Miss variable"""
        input = """
        Function : main
            Parameter: t
            Body:
                Var: a[5] = {1,2,3,4,5}, b[3][5] = {{1,2,3},{4,5,6,7,8}};
                a[[3] + foo(2)] = a[b[2][3]] + 4;
            EndBody.
            """
        expect = "Error on line 6 col 18: ["
        self.assertTrue(TestParser.checkParser(input,expect,280))
    
    def test_80(self):
        """Miss variable"""
        input = """
        Function : main
            Parameter: t
            Body:
                Body:
                EndBody.
            EndBody.
            """
        expect = "Error on line 5 col 16: Body"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test_81(self):
        """Miss variable"""
        input = """
        Function : main
            Parameter: t
            Body:
                foo()[2] = 5;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    
    def test_82(self):
        """Miss variable"""
        input = """
        Function : main
            paraMeter: t
            Body:
                foo()[2] = 5;
            EndBody.
            """
        expect = "Error on line 3 col 12: paraMeter"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    
    def test_83(self):
        """Miss variable"""
        input = """
        Function : main
            Parameter: t
            Body:
                foo()[2] = 5 + 2 !2 -. 12. && 3;
            EndBody.
            """
        expect = "Error on line 5 col 33: !"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    
    def test_84(self):
        """Miss variable"""
        input = """
        Function : main
            Parameter: t
            Body:
                test = !x && y || t;
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
    
    def test_85(self):
        """Miss variable"""
        input = """
        Function : main
            Parameter: t
            Body:
                While True 
                    Return t - 2;
                EndWhile.
            EndBody.
            """
        expect = "Error on line 6 col 20: Return"
        self.assertTrue(TestParser.checkParser(input,expect,286))
    
    def test_86(self):
        """Miss variable"""
        input = """
        Function : main
            Parameter: t
            Body:
                Var: a;
                a = "Hello" + 2;
            EndBody.
            """
        expect = "Error on line 6 col 20: Hello"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    
    def test_87(self):
        """Miss variable"""
        input = """
        Function: swap
            Parameter: a,b
            Body:
                Var: temp;
                temp = a;
                a = b;
                b = temp;
            EndBody.
        Function : main
            Body:
                Var: x = 2, y = 3;
                swap(x,y);
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    
    def test_88(self):
        """Miss variable"""
        input = """
        Function swap
            Parameter: a,b
            Body:
                Var: temp;
                temp = a;
                a = b;
                b = temp;
            EndBody.
        Function : main
            Body:
                Var: x = 2, y = 3;
                swap(x,y);
            EndBody.
            """
        expect = "Error on line 2 col 17: swap"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    
    def test_89(self):
        """Miss variable"""
        input = """
        Function: swap
            Parameter: a,b
            Body:
                Var: temp;
                temp = a;
                a = b;
                b = temp;
        Function : main
            Body:
                Var: x = 2, y = 3;
                swap(x,y);
            EndBody.
            EndBody.
            """
        expect = "Error on line 9 col 8: Function"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    
    def test_90(self):
        """Miss variable"""
        input = """
        Function: swap;
            Parameter: a,b
            Body:
                Var: temp;
                temp = a;
                a = b;
                b = temp;
        Function : main
            Body:
                Var: x = 2, y = 3;
                swap(x,y);
            EndBody.
            EndBody.
            """
        expect = "Error on line 2 col 22: ;"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    
    def test_91(self):
        """Miss variable"""
        input = """
        Function : main
            Body:
                Var: x = 2, y = 3;
                If x == 2 Then
                    While y == 3 Do
                        y = y + 1;
                    EndWhile.
                    If y != 3 Then 
                        Break;
                    EndIf.
                EndIf.
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    
    def test_92(self):
        """Miss variable"""
        input = """
        Function : main
            Body:
                Return foo();
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    
    def test_93(self):
        """Miss variable"""
        input = """
        Function : main
            Body:
                Var: x; ** Declare variable **
                x = 2 + 3; ** Assign value to x **
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    
    def test_94(self):
        """Miss variable"""
        input = """
        Function : main
            Body:
                Var: x = 2; 
                ** Declare variable 
                   and assign value to x **
            EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_95(self):
        """Miss variable"""
        input = """
        Function : main
            Body:
                Var: x = 2...2; 
            EndBody.
            """
        expect = "Error on line 4 col 27: ."
        self.assertTrue(TestParser.checkParser(input,expect,296))
    
    def test_96(self):
        """Miss variable"""
        input = """
        Function : main
            Body:
                Var: x = 0oABC; 
            EndBody.
            """
        expect = "Error on line 4 col 26: oABC"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    
    def test_97(self):
        """Miss variable"""
        input = """
        Function : main
            Body:
                Var: x = 0xMNH; 
            EndBody.
            """
        expect = "Error on line 4 col 26: xMNH"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    
    def test_98(self):
        """Miss variable"""
        input = """
        Function : main
            Body:
                Var: x = 2 + 3; 
            EndBody.
            """
        expect = "Error on line 4 col 27: +"
        self.assertTrue(TestParser.checkParser(input,expect,299))