import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_2(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_3(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_4(self):
        """test integer"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_5(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_6(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def ""","""Unclosed String: abc def """,106))

    def test_7(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_8(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("123.123.123.123", "123.123,.,123.123,<EOF>", 108))

    def test_9(self):
        """test sequence escape"""
        self.assertTrue(TestLexer.checkLexeme("abc\\n","abc,\,n,<EOF>",109))

    def test_10(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("Varr x;","Var,r,x,;,<EOF>",110))

    def test_11(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("Var x[2] = {1,2}","Var,x,[,2,],=,{1,2},<EOF>",111))

    def test_12(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("Var x = 4","Var,x,=,4,<EOF>",112))

    def test_13(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("Var x = 12.e-4","Var,x,=,12.e-4,<EOF>",113))

    def test_14(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("""Var x = "abc" ""","Var,x,=,abc,<EOF>",114))

    def test_15(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("Var x = True","Var,x,=,True,<EOF>",115))

    def test_16(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("12 12e5 12.0 12.2e-3","12,12e5,12.0,12.2e-3,<EOF>",116))

    def test_17(self):
        self.assertTrue(TestLexer.checkLexeme("{1,2,3} {{1,2},{2,3}} {{},{}}","{1,2,3},{{1,2},{2,3}},{{},{}},<EOF>",117))

    def test_18(self):
        """Test literal"""
        self.assertTrue(TestLexer.checkLexeme("0 12 234 12 3423423","0,12,234,12,3423423,<EOF>",118))

    def test_19(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("a abc abc123 asd_123 abc_asd_156","a,abc,abc123,asd_123,abc_asd_156,<EOF>",119))

    def test_20(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme("""** abc ** ""","<EOF>",120))

    def test_21(self):
        """test block comment"""
        self.assertTrue(TestLexer.checkLexeme("""** This is a
                                                  * multiline         
                                                  * comment 
                                                    **""","<EOF>",121))

    def test_22(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme("123abc cde 123_abc","123,abc,cde,123,Error Token _",122))

    def test_23(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("12e 12.5e .e02 e-3","12,e,12.5,e,.,e02,e,-,3,<EOF>",123))
    
    def test_24(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme("000123 1230001","0,0,0,123,1230001,<EOF>",124))

    def test_25(self):
        """test assign statement"""
        self.assertTrue(TestLexer.checkLexeme("a = 4 + b","a,=,4,+,b,<EOF>",125))

    def test_26(self):
        """test error identifier"""
        self.assertTrue(TestLexer.checkLexeme("_function","Error Token _",126))

    def test_27(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "test\\abc" ""","Illegal Escape In String: test\\a",127))

    def test_28(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc"xyz ""","abc,xyz,<EOF>",128))

    def test_29(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"xyz ""","""Unclosed String: abc'"xyz """,129))

    def test_30(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\'xyz" ""","""abc\\'xyz,<EOF>""",130))

    def test_31(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc"xyz" ""","""abc,xyz,Unclosed String:  """,131))

    def test_32(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\bxyz" ""","""abc\\bxyz,<EOF>""",132))

    def test_33(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("""Break Continue For While Do Body EndBody If ElseIf EndIf""","""Break,Continue,For,While,Do,Body,EndBody,If,ElseIf,EndIf,<EOF>""",133))

    def test_34(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "" "abcd" "12345" """,""",abcd,12345,<EOF>""",134))

    def test_35(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc
                                                         ""","""Unclosed String: abc
""",135))

    def test_36(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc ""","""Unclosed String: abc """,136))

    def test_37(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\r" ""","""abc \\r,<EOF>""",137))

    def test_38(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\n" ""","""abc \\n,<EOF>""",138))

    def test_39(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\f" ""","""abc \\f,<EOF>""",139))

    def test_40(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\b" ""","""abc \\b,<EOF>""",140))

    def test_41(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\t" ""","""abc \\t,<EOF>""",141))

    def test_42(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
        """ "abc 
        cde
        " """,
        """Unclosed String: abc 
""",142))

    def test_43(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" illegal: "\\h" ""","""illegal,:,Illegal Escape In String: \\h""",143))

    def test_44(self):
        """test sequence escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\n\\f\\b" ""","""abc \\n\\f\\b,<EOF>""",144))

    def test_45(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\' cde" ""","""abc \\' cde,<EOF>""",145))

    def test_46(self):
        """test string literal"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc \\' cde "xyz"" ""","""abc \\' cde ,xyz,,<EOF>""",146))

    def test_47(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme("""If a != b""","""If,a,!=,b,<EOF>""",147))

    def test_48(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme("""If a>b""","""If,a,>,b,<EOF>""",148))

    def test_49(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme("""If a>b Then a + b""","""If,a,>,b,Then,a,+,b,<EOF>""",149))

    def test_50(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme(
        """If a>b Then a + b
        else a*b""",
        """If,a,>,b,Then,a,+,b,else,a,*,b,<EOF>""",150))

    def test_51(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme(
        """If a>b Then a + b
        ElseIf a < b Then b - a""",
        """If,a,>,b,Then,a,+,b,ElseIf,a,<,b,Then,b,-,a,<EOF>""",151))

    def test_52(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme("""For (i = 0, i < 10, 2)""","""For,(,i,=,0,,,i,<,10,,,2,),<EOF>""",152))

    def test_53(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme(
        """For (i = 0, i < 10, 2) Do
        writeln(i);
        EndFor.""",
        """For,(,i,=,0,,,i,<,10,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>""",153))

    def test_54(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme(
        """While a > b Do
        a = a -1;
        EndWhile.""",
        """While,a,>,b,Do,a,=,a,-,1,;,EndWhile,.,<EOF>""",154))

    def test_55(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme(
        """Break;""",
        """Break,;,<EOF>""",155))

    def test_56(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme(
        """Continue;""",
        """Continue,;,<EOF>""",156))

    def test_57(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme(
        """a = a & 1""",
        """a,=,a,Error Token &""",157))

    def test_58(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme(
        """xyz
        $a = 5""",
        """xyz,Error Token $""",158))

    def test_59(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme(
        """1234 0000001234 0000043123000000000000000""",
        """1234,0,0,0,0,0,0,1234,0,0,0,0,0,43123000000000000000,<EOF>""",159))

    def test_60(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme(
        """00001.1111000000
        0e-4
        000000001e-40000""",
        """0,0,0,0,1.1111000000,0,e,-,4,0,0,0,0,0,0,0,0,1e-40000,<EOF>""",160))

    def test_61(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme(
        """0xFF 0XABCC""",
        """0xFF,0XABCC,<EOF>""",161))
        
    def test_62(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme(
        """0o567 0O77""",
        """0o567,0O77,<EOF>""",162))

    def test_63(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
        """ "abc \ xyz" """,
        """Illegal Escape In String: abc \ """,163))

    def test_64(self):
        """test string"""
        self.assertTrue(TestLexer.checkLexeme(
        """ "abc - xyz" """,
        """abc - xyz,<EOF>""",164))

    def test_65(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(
        """abc \\ xyz""",
        """abc,\,xyz,<EOF>""",165))

    def test_66(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(
        """ "abc'"x'"yz" """,
        """abc'"x'"yz,<EOF>""",166))

    def test_67(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(
        """ "\\'" """,
        """\\',<EOF>""",167))

    def test_68(self):
        """test escape"""
        self.assertTrue(TestLexer.checkLexeme(
        """ "\\\\" """,
        """\\\\,<EOF>""",168))

    def test_69(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
        """ s = "string           
        "a = 4
        g = 9 """,
        """s,=,Unclosed String: string           
""",169))

    def test_70(self):
        """test declaration"""
        self.assertTrue(TestLexer.checkLexeme(
        """ Var: x = 2;
        Var: a = 5;
        Var: b[2][3] = {{2,3,4},{4,5,6}};
        Var: c, d = 6, e, f;
        Var: m, n[10]; """,
        """Var,:,x,=,2,;,Var,:,a,=,5,;,Var,:,b,[,2,],[,3,],=,{{2,3,4},{4,5,6}},;,Var,:,c,,,d,=,6,,,e,,,f,;,Var,:,m,,,n,[,10,],;,<EOF>""",170))

    def test_71(self):
        """test function"""
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
        """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,<EOF>""",171))

    def test_72(self):
        """test function"""
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
        """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""",172))

    def test_73(self):
        """test declaration"""
        self.assertTrue(TestLexer.checkLexeme(
        """ Var: x = "hello";
        Var: a = "world";
        Var: b = True;
        Var: c, d = False; """,
        """Var,:,x,=,hello,;,Var,:,a,=,world,;,Var,:,b,=,True,;,Var,:,c,,,d,=,False,;,<EOF>""",173))

    def test_74(self):
        """test function"""
        self.assertTrue(TestLexer.checkLexeme(
        """Var: x;
        Function: gcd
            Parameter: a,b
            Body:
                If (b == 0) Return a;
                Else Return gcd(b,a%b);
                EndIf.
            EndBody.""",
        """Var,:,x,;,Function,:,gcd,Parameter,:,a,,,b,Body,:,If,(,b,==,0,),Return,a,;,Else,Return,gcd,(,b,,,a,%,b,),;,EndIf,.,EndBody,.,<EOF>""",174))

    def test_75(self):
        """test unterminated comment"""
        self.assertTrue(TestLexer.checkLexeme(
        """** Hello """,
        """Unterminated Comment""",175))

    def test_76(self):
        """test unterminated comment"""
        self.assertTrue(TestLexer.checkLexeme(
        """** Hello
        World!!! """,
        """Unterminated Comment""",176))

    def test_77(self):
        """test block comment"""
        self.assertTrue(TestLexer.checkLexeme(
        """** Hello
        World!!! **""",
        """<EOF>""",177))

    def test_78(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme(
        """@2""",
        """Error Token @""",178))

    def test_79(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme(
        """Do x = x + 2; 
        While x < 9
        EndDo.""",
        """Do,x,=,x,+,2,;,While,x,<,9,EndDo,.,<EOF>""",179))

    def test_80(self):
        """test function call"""
        self.assertTrue(TestLexer.checkLexeme(
        """foo(2 + x, 4. \. y);""",
        """foo,(,2,+,x,,,4.,\.,y,),;,<EOF>""",180))

    def test_81(self):
        """test fucntion call"""
        self.assertTrue(TestLexer.checkLexeme(
        """goo();""",
        """goo,(,),;,<EOF>""",181))

    def test_82(self):
        """test statement"""
        self.assertTrue(TestLexer.checkLexeme(
        """return a + b;""",
        """return,a,+,b,;,<EOF>""",182))

    def test_83(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
        """ "This is test for" unclosed string" """,
        """This is test for,unclosed,string,Unclosed String:  """,183))

    def test_84(self):
        """test with auto generate code"""
        self.assertTrue(TestLexer.checkLexeme(
        """then,return,< e0352 : ,,of,>=
return > array Qbfb5 , function var M274c if <= ; function or <= to = x4045 procedure to <> ] ( else *
(* false of Bcdfa,<=,J490b begin J6626,<=,break*)""",
        """then,,,return,,,<,e0352,:,,,,,of,,,>=,return,>,array,Error Token Q""",184))

    def test_85(self):
        """test with auto generate code"""
        self.assertTrue(TestLexer.checkLexeme(
        """],],* ae0bc not mod,return,,
function < + qefbe and ; of o366c false array else < > and downto for J4981 : <> return = for then ..
(* of break h80bb,or,bfa18 ) W6bd3,real,<*)""",
        """],,,],,,*,ae0bc,not,mod,,,return,,,,,function,<,+,qefbe,and,;,of,o366c,false,array,else,<,>,and,downto,for,Error Token J""",185))

    def test_86(self):
        """test with auto generate code"""
        self.assertTrue(TestLexer.checkLexeme(
        """(,while,: h050f end return,+,[
,  or m3ff3 while  for y848d while downto - + , ] ) >= hdcb8 false  for > not and (
(* ( [ bc9ca,],b1ebd ; w28cd,procedure,if*)""",
        """(,,,while,,,:,h050f,end,return,,,+,,,[,,,or,m3ff3,while,for,y848d,while,downto,-,+,,,],),>=,hdcb8,false,for,>,not,and,(,(,*,(,[,bc9ca,,,],,,b1ebd,;,w28cd,,,procedure,,,if,*,),<EOF>""",186))

    def test_87(self):
        """test with auto generate code"""
        self.assertTrue(TestLexer.checkLexeme(
        """rdad 40oBhenK292aWfTSFLt6""",
        """rdad,40,oBhenK292aWfTSFLt6,<EOF>""",187))

    def test_88(self):
        """test operator"""
        self.assertTrue(TestLexer.checkLexeme(
        """=||<=<><>=-<=>""",
        """=,||,<=,<,>,<,>=,-,<=,>,<EOF>""",188))
    
    def test_89(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme(
        """1.2 1. .1 1e2 1.2E-2 1.2e-2 .1E2 9.0 12e8 0.33E-3 128e-42""",
        """1.2,1.,.,1,1e2,1.2E-2,1.2e-2,.,1E2,9.0,12e8,0.33E-3,128e-42,<EOF>""",189))
    
    def test_90(self):
        """test literal"""
        self.assertTrue(TestLexer.checkLexeme(
        """e--12 e12 2E-15 99e 1 1. 1""",
        """e,-,-,12,e12,2E-15,99,e,1,1.,1,<EOF>""",190))
    
    def test_91(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
        """abc** Comment**""",
        """abc,<EOF>""",191))
    
    def test_92(self):
        """test comment"""
        self.assertTrue(TestLexer.checkLexeme(
        """abc*qwe**Test**""",
        """abc,*,qwe,<EOF>""",192))
    
    def test_93(self):
        """test erro char"""
        self.assertTrue(TestLexer.checkLexeme(
        """abc**qwe**Test**""",
        """abc,Error Token T""",193))
    
    def test_94(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme(
        """(*-101*) 11.+12*#$""",
        """(,*,-,101,*,),11.,+,12,*,Error Token #""",194))
    
    def test_95(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme(
        """;j~%IbnQL!x-OBd""",
        """;,j,Error Token ~""",195))
    
    def test_96(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
        """ "abcd \\b 
        efg""",
        """Unclosed String: abcd \\b 
""",196))
    
    def test_97(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
        """ "\\dado\\mado\\a """,
        """Illegal Escape In String: \\d""",197))
    
    def test_98(self):
        """test error char"""
        self.assertTrue(TestLexer.checkLexeme(
        """kz-70S9+0s)f<)?0gg""",
        """kz,-,70,Error Token S""",198))
    
    def test_99(self):
        """test valid keyword"""
        self.assertTrue(TestLexer.checkLexeme(
        """if then else elif fOr dO WhIle breAk""",
        """if,then,else,elif,fOr,dO,Error Token W""",199))
    
    def test_100(self):
        """test valid literal"""
        self.assertTrue(TestLexer.checkLexeme(
        """12.e0 -101 11.E 11.1e2""",
        """12.e0,-,101,11.,Error Token E""",200))

    

    

