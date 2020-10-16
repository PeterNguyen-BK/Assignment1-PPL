import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",100))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",101))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",102))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",103))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",104))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,105))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",106))

    def test_1(self):
        self.assertTrue(TestLexer.checkLexeme("123.123.123.123", "123.123,.,123.123,<EOF>", 107))

    def test_2(self):
        self.assertTrue(TestLexer.checkLexeme("abc\\n","abc,\,n,<EOF>",108))

    def test_3(self):
        self.assertTrue(TestLexer.checkLexeme("Varr x;","Var,r,x,;,<EOF>",109))

    def test_4(self):
        self.assertTrue(TestLexer.checkLexeme("Var x[2] = {1,2}","Var,x,[,2,],=,{1,2},<EOF>",110))

    def test_5(self):
        self.assertTrue(TestLexer.checkLexeme("Var x = 4","Var,x,=,4,<EOF>",111))

    def test_6(self):
        self.assertTrue(TestLexer.checkLexeme("Var x = 12.e-4","Var,x,=,12.e-4,<EOF>",112))

    def test_7(self):
        self.assertTrue(TestLexer.checkLexeme("""Var x = "abc" ""","Var,x,=,abc,<EOF>",113))

    def test_8(self):
        self.assertTrue(TestLexer.checkLexeme("Var x = True","Var,x,=,True,<EOF>",114))

    def test_9(self):
        self.assertTrue(TestLexer.checkLexeme("12 12e5 12.0 12.2e-3","12,12e5,12.0,12.2e-3,<EOF>",115))

    def test_10(self):
        self.assertTrue(TestLexer.checkLexeme("{1,2,3} {{1,2},{2,3}} {{},{}}","{1,2,3},{{1,2},{2,3}},{{},{}},<EOF>",116))

    def test_11(self):
        self.assertTrue(TestLexer.checkLexeme("0 12 234 12 3423423","0,12,234,12,3423423,<EOF>",117))

    def test_12(self):
        self.assertTrue(TestLexer.checkLexeme("a abc abc123 asd_123 abc_asd_156","a,abc,abc123,asd_123,abc_asd_156,<EOF>",118))

    def test_13(self):
        self.assertTrue(TestLexer.checkLexeme("""** abc ** ""","<EOF>",119))

    def test_14(self):
        self.assertTrue(TestLexer.checkLexeme("""** This is a
                                                  * multiline         
                                                  * comment 
                                                    **""","<EOF>",120))

    def test_15(self):
        self.assertTrue(TestLexer.checkLexeme("123abc cde 123_abc","123,abc,cde,123,Error Token _",121))

    def test_16(self):
        self.assertTrue(TestLexer.checkLexeme("12e 12.5e .e02 e-3","12,e,12.5,e,.,e02,e,-,3,<EOF>",122))
    
    def test_17(self):
        self.assertTrue(TestLexer.checkLexeme("000123 1230001","0,0,0,123,1230001,<EOF>",123))

    def test_18(self):
        self.assertTrue(TestLexer.checkLexeme("a = 4 + b","a,=,4,+,b,<EOF>",124))

    def test_19(self):
        self.assertTrue(TestLexer.checkLexeme("_function","Error Token _",125))

    def test_20(self):
        self.assertTrue(TestLexer.checkLexeme(""" "test\\abc" ""","Illegal Escape In String: test\\a",126))

    def test_21(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc"xyz ""","abc,xyz,<EOF>",127))

    def test_22(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"xyz ""","""Unclosed String: abc'"xyz """,128))

    def test_23(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\'xyz" ""","""abc\\'xyz,<EOF>""",129))

    def test_24(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc"xyz" ""","""abc,xyz,Unclosed String:  """,130))

    def test_25(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\'xyz" ""","""abc\\'xyz,<EOF>""",131))

    def test_26(self):
        self.assertTrue(TestLexer.checkLexeme("""Break Continue For While Do Body EndBody If ElseIf EndIf""","""Break,Continue,For,While,Do,Body,EndBody,If,ElseIf,EndIf,<EOF>""",132))

    def test_27(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" "abcd" "12345" """,""",abcd,12345,<EOF>""",133))

    def test_28(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc
                                                         ""","""Unclosed String: abc
""",134))

    def test_29(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc ""","""Unclosed String: abc """,135))

    def test_30(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\r" ""","""abc \\r,<EOF>""",136))

    def test_31(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\n" ""","""abc \\n,<EOF>""",137))

    def test_32(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\f" ""","""abc \\f,<EOF>""",138))

    def test_33(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\b" ""","""abc \\b,<EOF>""",139))

    def test_34(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\t" ""","""abc \\t,<EOF>""",140))

    def test_35(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ "abc 
        cde
        " """,
        """Unclosed String: abc 
""",141))

    def test_36(self):
        self.assertTrue(TestLexer.checkLexeme(""" illegal: "\\h" ""","""illegal,:,Illegal Escape In String: \\h""",142))

    def test_37(self):
        self.assertTrue(TestLexer.checkLexeme(""" abc \\n\\f\\b ""","""abc,\,n,\,f,\,b,<EOF>""",143))

    def test_38(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\' cde" ""","""abc \\' cde,<EOF>""",144))

    def test_39(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\' cde" "xyz" ""","""abc \\' cde,xyz,<EOF>""",145))

    def test_40(self):
        self.assertTrue(TestLexer.checkLexeme("""If a != b""","""If,a,!=,b,<EOF>""",146))

    def test_41(self):
        self.assertTrue(TestLexer.checkLexeme("""If a>b""","""If,a,>,b,<EOF>""",147))

    def test_42(self):
        self.assertTrue(TestLexer.checkLexeme("""If a>b Then a + b""","""If,a,>,b,Then,a,+,b,<EOF>""",148))

    def test_43(self):
        self.assertTrue(TestLexer.checkLexeme(
        """If a>b Then a + b
        else a*b""",
        """If,a,>,b,Then,a,+,b,else,a,*,b,<EOF>""",149))

    def test_44(self):
        self.assertTrue(TestLexer.checkLexeme(
        """If a>b Then a + b
        ElseIf a < b Then b - a""",
        """If,a,>,b,Then,a,+,b,ElseIf,a,<,b,Then,b,-,a,<EOF>""",150))

    def test_45(self):
        self.assertTrue(TestLexer.checkLexeme("""For (i = 0, i < 10, 2)""","""For,(,i,=,0,,,i,<,10,,,2,),<EOF>""",151))

    def test_46(self):
        self.assertTrue(TestLexer.checkLexeme(
        """For (i = 0, i < 10, 2) Do
        writeln(i);
        EndFor.""",
        """For,(,i,=,0,,,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>""",152))

    def test_47(self):
        self.assertTrue(TestLexer.checkLexeme(
        """While a > b Do
        a = a -1;
        EndWhile.""",
        """While,a,>,b,Do,a,=,a,-,1,;,EndWhile,.,<EOF>""",153))

    def test_48(self):
        self.assertTrue(TestLexer.checkLexeme(
        """Break;""",
        """Break,;,<EOF>""",154))

    def test_49(self):
        self.assertTrue(TestLexer.checkLexeme(
        """Continue;""",
        """Continue,;,<EOF>""",155))

    def test_50(self):
        self.assertTrue(TestLexer.checkLexeme(
        """a = a & 1""",
        """a,=,a,Error Token &""",156))

    def test_51(self):
        self.assertTrue(TestLexer.checkLexeme(
        """xyz
        $a = 5""",
        """xyz,Error Token $""",157))

    def test_52(self):
        self.assertTrue(TestLexer.checkLexeme(
        """1234 0000001234 0000043123""",
        """1234,0,0,0,0,0,0,1234,0,0,0,0,0,43123,<EOF>""",158))

    def test_53(self):
        self.assertTrue(TestLexer.checkLexeme(
        """00001.1111000000
        0e-4
        000000001e-40000""",
        """0,0,0,0,1.1111000000,0,e,-,4,0,0,0,0,0,0,0,0,1e-40000,<EOF>""",159))

    def test_54(self):
        self.assertTrue(TestLexer.checkLexeme(
        """0xFF 0XABCC""",
        """0xFF,0XABCC,<EOF>""",160))
        
    def test_56(self):
        self.assertTrue(TestLexer.checkLexeme(
        """0o567 0O77""",
        """0o567,0O77,<EOF>""",161))

    def test_57(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ "abc \ xyz" """,
        """Illegal Escape In String: abc \ """,162))

    def test_58(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ "abc - xyz" """,
        """abc - xyz,<EOF>""",163))

    def test_59(self):
        self.assertTrue(TestLexer.checkLexeme(
        """abc \\ xyz""",
        """abc,\,xyz,<EOF>""",164))

    def test_60(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ "abc'"x'"yz" """,
        """abc'"x'"yz,<EOF>""",165))

    def test_61(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ "\\'" """,
        """\\',<EOF>""",166))

    def test_62(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ "\\\\" """,
        """\\\\,<EOF>""",167))

    def test_63(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ s = "string           
        "a = 4
        g = 9 """,
        """s,=,Unclosed String: string           
""",168))

    def test_64(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ Var: x = 2;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10]; """,
        """Var,:,x,=,2,;,Var,:,a,=,5,;,Var,:,b,[,2,],[,3,],=,{{2,3,4},{4,5,6}},;,Var,:,c,,,d,=,6,,,e,,,f,;,Var,:,m,,,n,[,10,],;,<EOF>""",169))

    def test_65(self):
        self.assertTrue(TestLexer.checkLexeme(
        """Var: x;
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody.
        """,
        """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,<EOF>""",170))

    def test_66(self):
        self.assertTrue(TestLexer.checkLexeme(
        """Var: x;
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
            Body:
                x = 10;
                fact (x);
            EndBody.
        """,
        """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""",171))

    def test_67(self):
        self.assertTrue(TestLexer.checkLexeme(
        """ Var: x = "hello";
        Var: a = "world";
        Var: b = True;
        Var: c, d = False; """,
        """Var,:,x,=,hello,;,Var,:,a,=,world,;,Var,:,b,=,True,;,Var,:,c,,,d,=,False,;,<EOF>""",172))

    def test_68(self):
        self.assertTrue(TestLexer.checkLexeme(
        """Var: x;
        Function: gcd
            Parameter: a,b
            Body:
                If (b == 0) Return a;
                Else Return gcd(b,a%b);
                EndIf.
            EndBody.""",
        """Var,:,x,;,Function,:,gcd,Parameter,:,a,,,b,Body,:,If,(,b,==,0,),Return,a,;,Else,Return,gcd,(,b,,,a,%,b,),;,EndIf,.,EndBody,.,<EOF>""",173))

    def test_69(self):
        self.assertTrue(TestLexer.checkLexeme(
        """** Hello """,
        """Unterminated Comment""",174))

    def test_70(self):
        self.assertTrue(TestLexer.checkLexeme(
        """** Hello
        World!!! """,
        """Unterminated Comment""",175))

    def test_71(self):
        self.assertTrue(TestLexer.checkLexeme(
        """** Hello
        World!!! ****""",
        """<EOF>""",176))

    def test_72(self):
        self.assertTrue(TestLexer.checkLexeme(
        """@2""",
        """Error Token @""",177))

    

