# Generated from d:\Studying\Year_3\PPL\assignment1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0280\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\7")
        buf.write("\2\u0098\n\2\f\2\16\2\u009b\13\2\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3%\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38")
        buf.write("\38\38\78\u016d\n8\f8\168\u0170\138\39\39\39\79\u0175")
        buf.write("\n9\f9\169\u0178\139\3:\3:\7:\u017c\n:\f:\16:\u017f\13")
        buf.write(":\3:\3:\3:\3:\3:\5:\u0186\n:\3;\3;\5;\u018a\n;\3;\6;\u018d")
        buf.write("\n;\r;\16;\u018e\3<\3<\3=\3=\7=\u0195\n=\f=\16=\u0198")
        buf.write("\13=\6=\u019a\n=\r=\16=\u019b\3=\5=\u019f\n=\3=\3=\7=")
        buf.write("\u01a3\n=\f=\16=\u01a6\13=\3=\3=\3=\3=\7=\u01ac\n=\f=")
        buf.write("\16=\u01af\13=\6=\u01b1\n=\r=\16=\u01b2\3=\5=\u01b6\n")
        buf.write("=\3=\3=\7=\u01ba\n=\f=\16=\u01bd\13=\3=\3=\7=\u01c1\n")
        buf.write("=\f=\16=\u01c4\13=\6=\u01c6\n=\r=\16=\u01c7\3=\3=\3=\7")
        buf.write("=\u01cd\n=\f=\16=\u01d0\13=\3=\5=\u01d3\n=\3=\5=\u01d6")
        buf.write("\n=\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u01e1\n>\3?\3?\5?\u01e5")
        buf.write("\n?\3@\3@\3@\3@\5@\u01eb\n@\3A\3A\3A\3B\3B\7B\u01f2\n")
        buf.write("B\fB\16B\u01f5\13B\3B\3B\3B\3C\3C\3C\3C\3C\7C\u01ff\n")
        buf.write("C\fC\16C\u0202\13C\3C\3C\3C\5C\u0207\nC\3D\3D\3D\3D\3")
        buf.write("D\7D\u020e\nD\fD\16D\u0211\13D\7D\u0213\nD\fD\16D\u0216")
        buf.write("\13D\3D\3D\3D\3D\3D\3D\3D\7D\u021f\nD\fD\16D\u0222\13")
        buf.write("D\7D\u0224\nD\fD\16D\u0227\13D\3D\3D\3D\3D\3D\3D\3D\7")
        buf.write("D\u0230\nD\fD\16D\u0233\13D\7D\u0235\nD\fD\16D\u0238\13")
        buf.write("D\3D\3D\3D\3D\3D\3D\3D\7D\u0241\nD\fD\16D\u0244\13D\7")
        buf.write("D\u0246\nD\fD\16D\u0249\13D\3D\3D\5D\u024d\nD\3E\3E\3")
        buf.write("E\3E\7E\u0253\nE\fE\16E\u0256\13E\3E\3E\3E\3E\3E\3F\6")
        buf.write("F\u025e\nF\rF\16F\u025f\3F\3F\3G\3G\3H\3H\7H\u0268\nH")
        buf.write("\fH\16H\u026b\13H\3H\3H\3I\3I\7I\u0271\nI\fI\16I\u0274")
        buf.write("\13I\3I\3I\3J\3J\3J\3J\7J\u027c\nJ\fJ\16J\u027f\13J\3")
        buf.write("\u027d\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o\2q\2s9u\2w\2y:{;}\2\177\2\u0081\2\u0083<\u0085")
        buf.write("=\u0087>\u0089?\u008b@\u008dA\u008fB\u0091C\u0093D\3\2")
        buf.write("\23\3\2c|\6\2\62;C\\aac|\4\2ZZzz\4\2\63;CH\4\2\62;CH\4")
        buf.write("\2QQqq\3\2\639\3\2\629\3\2\63;\3\2\62;\3\2\62\62\4\2G")
        buf.write("Ggg\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2))\5\2\13")
        buf.write("\f\17\17\"\"\3\2$$\2\u02a6\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2s\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u0083\3")
        buf.write("\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2")
        buf.write("\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\3\u0095\3\2\2\2\5\u009c\3\2\2")
        buf.write("\2\7\u00a0\3\2\2\2\t\u00a5\3\2\2\2\13\u00ab\3\2\2\2\r")
        buf.write("\u00b4\3\2\2\2\17\u00b7\3\2\2\2\21\u00bc\3\2\2\2\23\u00c3")
        buf.write("\3\2\2\2\25\u00cb\3\2\2\2\27\u00d1\3\2\2\2\31\u00d8\3")
        buf.write("\2\2\2\33\u00e1\3\2\2\2\35\u00e5\3\2\2\2\37\u00ee\3\2")
        buf.write("\2\2!\u00f1\3\2\2\2#\u00fb\3\2\2\2%\u0102\3\2\2\2\'\u0107")
        buf.write("\3\2\2\2)\u010d\3\2\2\2+\u0113\3\2\2\2-\u0115\3\2\2\2")
        buf.write("/\u0117\3\2\2\2\61\u0119\3\2\2\2\63\u011b\3\2\2\2\65\u011d")
        buf.write("\3\2\2\2\67\u011f\3\2\2\29\u0121\3\2\2\2;\u0123\3\2\2")
        buf.write("\2=\u0125\3\2\2\2?\u0127\3\2\2\2A\u0129\3\2\2\2C\u012b")
        buf.write("\3\2\2\2E\u012d\3\2\2\2G\u012f\3\2\2\2I\u0131\3\2\2\2")
        buf.write("K\u0134\3\2\2\2M\u0137\3\2\2\2O\u013a\3\2\2\2Q\u013d\3")
        buf.write("\2\2\2S\u013f\3\2\2\2U\u0142\3\2\2\2W\u0145\3\2\2\2Y\u0147")
        buf.write("\3\2\2\2[\u014a\3\2\2\2]\u014d\3\2\2\2_\u014f\3\2\2\2")
        buf.write("a\u0151\3\2\2\2c\u0154\3\2\2\2e\u0157\3\2\2\2g\u015b\3")
        buf.write("\2\2\2i\u015e\3\2\2\2k\u0161\3\2\2\2m\u0165\3\2\2\2o\u0169")
        buf.write("\3\2\2\2q\u0171\3\2\2\2s\u0185\3\2\2\2u\u0187\3\2\2\2")
        buf.write("w\u0190\3\2\2\2y\u01d5\3\2\2\2{\u01e0\3\2\2\2}\u01e4\3")
        buf.write("\2\2\2\177\u01ea\3\2\2\2\u0081\u01ec\3\2\2\2\u0083\u01ef")
        buf.write("\3\2\2\2\u0085\u0206\3\2\2\2\u0087\u024c\3\2\2\2\u0089")
        buf.write("\u024e\3\2\2\2\u008b\u025d\3\2\2\2\u008d\u0263\3\2\2\2")
        buf.write("\u008f\u0265\3\2\2\2\u0091\u026e\3\2\2\2\u0093\u0277\3")
        buf.write("\2\2\2\u0095\u0099\t\2\2\2\u0096\u0098\t\3\2\2\u0097\u0096")
        buf.write("\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u009a\3\2\2\2\u009a\4\3\2\2\2\u009b\u0099\3\2\2\2\u009c")
        buf.write("\u009d\7X\2\2\u009d\u009e\7c\2\2\u009e\u009f\7t\2\2\u009f")
        buf.write("\6\3\2\2\2\u00a0\u00a1\7D\2\2\u00a1\u00a2\7q\2\2\u00a2")
        buf.write("\u00a3\7f\2\2\u00a3\u00a4\7{\2\2\u00a4\b\3\2\2\2\u00a5")
        buf.write("\u00a6\7D\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g\2\2\u00a8")
        buf.write("\u00a9\7c\2\2\u00a9\u00aa\7m\2\2\u00aa\n\3\2\2\2\u00ab")
        buf.write("\u00ac\7E\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae")
        buf.write("\u00af\7v\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1\7p\2\2\u00b1")
        buf.write("\u00b2\7w\2\2\u00b2\u00b3\7g\2\2\u00b3\f\3\2\2\2\u00b4")
        buf.write("\u00b5\7F\2\2\u00b5\u00b6\7q\2\2\u00b6\16\3\2\2\2\u00b7")
        buf.write("\u00b8\7G\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba\7u\2\2\u00ba")
        buf.write("\u00bb\7g\2\2\u00bb\20\3\2\2\2\u00bc\u00bd\7G\2\2\u00bd")
        buf.write("\u00be\7n\2\2\u00be\u00bf\7u\2\2\u00bf\u00c0\7g\2\2\u00c0")
        buf.write("\u00c1\7K\2\2\u00c1\u00c2\7h\2\2\u00c2\22\3\2\2\2\u00c3")
        buf.write("\u00c4\7G\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7f\2\2\u00c6")
        buf.write("\u00c7\7D\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9\7f\2\2\u00c9")
        buf.write("\u00ca\7{\2\2\u00ca\24\3\2\2\2\u00cb\u00cc\7G\2\2\u00cc")
        buf.write("\u00cd\7p\2\2\u00cd\u00ce\7f\2\2\u00ce\u00cf\7K\2\2\u00cf")
        buf.write("\u00d0\7h\2\2\u00d0\26\3\2\2\2\u00d1\u00d2\7G\2\2\u00d2")
        buf.write("\u00d3\7p\2\2\u00d3\u00d4\7f\2\2\u00d4\u00d5\7H\2\2\u00d5")
        buf.write("\u00d6\7q\2\2\u00d6\u00d7\7t\2\2\u00d7\30\3\2\2\2\u00d8")
        buf.write("\u00d9\7G\2\2\u00d9\u00da\7p\2\2\u00da\u00db\7f\2\2\u00db")
        buf.write("\u00dc\7Y\2\2\u00dc\u00dd\7j\2\2\u00dd\u00de\7k\2\2\u00de")
        buf.write("\u00df\7n\2\2\u00df\u00e0\7g\2\2\u00e0\32\3\2\2\2\u00e1")
        buf.write("\u00e2\7H\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7t\2\2\u00e4")
        buf.write("\34\3\2\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7\7w\2\2\u00e7")
        buf.write("\u00e8\7p\2\2\u00e8\u00e9\7e\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\u00eb\7k\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7p\2\2\u00ed")
        buf.write("\36\3\2\2\2\u00ee\u00ef\7K\2\2\u00ef\u00f0\7h\2\2\u00f0")
        buf.write(" \3\2\2\2\u00f1\u00f2\7R\2\2\u00f2\u00f3\7c\2\2\u00f3")
        buf.write("\u00f4\7t\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7o\2\2\u00f6")
        buf.write("\u00f7\7g\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7g\2\2\u00f9")
        buf.write("\u00fa\7t\2\2\u00fa\"\3\2\2\2\u00fb\u00fc\7T\2\2\u00fc")
        buf.write("\u00fd\7g\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7w\2\2\u00ff")
        buf.write("\u0100\7t\2\2\u0100\u0101\7p\2\2\u0101$\3\2\2\2\u0102")
        buf.write("\u0103\7V\2\2\u0103\u0104\7j\2\2\u0104\u0105\7g\2\2\u0105")
        buf.write("\u0106\7p\2\2\u0106&\3\2\2\2\u0107\u0108\7Y\2\2\u0108")
        buf.write("\u0109\7j\2\2\u0109\u010a\7k\2\2\u010a\u010b\7n\2\2\u010b")
        buf.write("\u010c\7g\2\2\u010c(\3\2\2\2\u010d\u010e\7G\2\2\u010e")
        buf.write("\u010f\7p\2\2\u010f\u0110\7f\2\2\u0110\u0111\7F\2\2\u0111")
        buf.write("\u0112\7q\2\2\u0112*\3\2\2\2\u0113\u0114\7}\2\2\u0114")
        buf.write(",\3\2\2\2\u0115\u0116\7\177\2\2\u0116.\3\2\2\2\u0117\u0118")
        buf.write("\7*\2\2\u0118\60\3\2\2\2\u0119\u011a\7+\2\2\u011a\62\3")
        buf.write("\2\2\2\u011b\u011c\7]\2\2\u011c\64\3\2\2\2\u011d\u011e")
        buf.write("\7_\2\2\u011e\66\3\2\2\2\u011f\u0120\7=\2\2\u01208\3\2")
        buf.write("\2\2\u0121\u0122\7<\2\2\u0122:\3\2\2\2\u0123\u0124\7.")
        buf.write("\2\2\u0124<\3\2\2\2\u0125\u0126\7\60\2\2\u0126>\3\2\2")
        buf.write("\2\u0127\u0128\7-\2\2\u0128@\3\2\2\2\u0129\u012a\7/\2")
        buf.write("\2\u012aB\3\2\2\2\u012b\u012c\7,\2\2\u012cD\3\2\2\2\u012d")
        buf.write("\u012e\7^\2\2\u012eF\3\2\2\2\u012f\u0130\7\'\2\2\u0130")
        buf.write("H\3\2\2\2\u0131\u0132\7-\2\2\u0132\u0133\7\60\2\2\u0133")
        buf.write("J\3\2\2\2\u0134\u0135\7/\2\2\u0135\u0136\7\60\2\2\u0136")
        buf.write("L\3\2\2\2\u0137\u0138\7,\2\2\u0138\u0139\7\60\2\2\u0139")
        buf.write("N\3\2\2\2\u013a\u013b\7^\2\2\u013b\u013c\7\60\2\2\u013c")
        buf.write("P\3\2\2\2\u013d\u013e\7#\2\2\u013eR\3\2\2\2\u013f\u0140")
        buf.write("\7(\2\2\u0140\u0141\7(\2\2\u0141T\3\2\2\2\u0142\u0143")
        buf.write("\7~\2\2\u0143\u0144\7~\2\2\u0144V\3\2\2\2\u0145\u0146")
        buf.write("\7?\2\2\u0146X\3\2\2\2\u0147\u0148\7?\2\2\u0148\u0149")
        buf.write("\7?\2\2\u0149Z\3\2\2\2\u014a\u014b\7#\2\2\u014b\u014c")
        buf.write("\7?\2\2\u014c\\\3\2\2\2\u014d\u014e\7@\2\2\u014e^\3\2")
        buf.write("\2\2\u014f\u0150\7>\2\2\u0150`\3\2\2\2\u0151\u0152\7@")
        buf.write("\2\2\u0152\u0153\7?\2\2\u0153b\3\2\2\2\u0154\u0155\7>")
        buf.write("\2\2\u0155\u0156\7?\2\2\u0156d\3\2\2\2\u0157\u0158\7?")
        buf.write("\2\2\u0158\u0159\7\61\2\2\u0159\u015a\7?\2\2\u015af\3")
        buf.write("\2\2\2\u015b\u015c\7@\2\2\u015c\u015d\7\60\2\2\u015dh")
        buf.write("\3\2\2\2\u015e\u015f\7>\2\2\u015f\u0160\7\60\2\2\u0160")
        buf.write("j\3\2\2\2\u0161\u0162\7@\2\2\u0162\u0163\7?\2\2\u0163")
        buf.write("\u0164\7\60\2\2\u0164l\3\2\2\2\u0165\u0166\7>\2\2\u0166")
        buf.write("\u0167\7?\2\2\u0167\u0168\7\60\2\2\u0168n\3\2\2\2\u0169")
        buf.write("\u016a\t\4\2\2\u016a\u016e\t\5\2\2\u016b\u016d\t\6\2\2")
        buf.write("\u016c\u016b\3\2\2\2\u016d\u0170\3\2\2\2\u016e\u016c\3")
        buf.write("\2\2\2\u016e\u016f\3\2\2\2\u016fp\3\2\2\2\u0170\u016e")
        buf.write("\3\2\2\2\u0171\u0172\t\7\2\2\u0172\u0176\t\b\2\2\u0173")
        buf.write("\u0175\t\t\2\2\u0174\u0173\3\2\2\2\u0175\u0178\3\2\2\2")
        buf.write("\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177r\3\2\2")
        buf.write("\2\u0178\u0176\3\2\2\2\u0179\u017d\t\n\2\2\u017a\u017c")
        buf.write("\t\13\2\2\u017b\u017a\3\2\2\2\u017c\u017f\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u0186\3\2\2\2")
        buf.write("\u017f\u017d\3\2\2\2\u0180\u0181\t\f\2\2\u0181\u0186\5")
        buf.write("o8\2\u0182\u0183\t\f\2\2\u0183\u0186\5q9\2\u0184\u0186")
        buf.write("\t\f\2\2\u0185\u0179\3\2\2\2\u0185\u0180\3\2\2\2\u0185")
        buf.write("\u0182\3\2\2\2\u0185\u0184\3\2\2\2\u0186t\3\2\2\2\u0187")
        buf.write("\u0189\t\r\2\2\u0188\u018a\5A!\2\u0189\u0188\3\2\2\2\u0189")
        buf.write("\u018a\3\2\2\2\u018a\u018c\3\2\2\2\u018b\u018d\t\13\2")
        buf.write("\2\u018c\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018fv\3\2\2\2\u0190\u0191")
        buf.write("\t\13\2\2\u0191x\3\2\2\2\u0192\u0196\t\n\2\2\u0193\u0195")
        buf.write("\t\13\2\2\u0194\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196")
        buf.write("\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u019a\3\2\2\2")
        buf.write("\u0198\u0196\3\2\2\2\u0199\u0192\3\2\2\2\u019a\u019b\3")
        buf.write("\2\2\2\u019b\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019f")
        buf.write("\3\2\2\2\u019d\u019f\t\f\2\2\u019e\u0199\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a4\5=\37\2")
        buf.write("\u01a1\u01a3\5w<\2\u01a2\u01a1\3\2\2\2\u01a3\u01a6\3\2")
        buf.write("\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a7")
        buf.write("\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7\u01a8\5u;\2\u01a8\u01d6")
        buf.write("\3\2\2\2\u01a9\u01ad\t\n\2\2\u01aa\u01ac\t\13\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3")
        buf.write("\2\2\2\u01b0\u01a9\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4")
        buf.write("\u01b6\t\f\2\2\u01b5\u01b0\3\2\2\2\u01b5\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u01bb\5=\37\2\u01b8\u01ba\5")
        buf.write("w<\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01d6\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01be\u01c2\t\n\2\2\u01bf\u01c1\t\13\2")
        buf.write("\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4\3\2\2\2\u01c2\u01c0")
        buf.write("\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c5\u01be\3\2\2\2\u01c6\u01c7\3\2\2\2")
        buf.write("\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\3")
        buf.write("\2\2\2\u01c9\u01d6\5u;\2\u01ca\u01ce\t\n\2\2\u01cb\u01cd")
        buf.write("\t\13\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d3\3\2\2\2")
        buf.write("\u01d0\u01ce\3\2\2\2\u01d1\u01d3\t\f\2\2\u01d2\u01ca\3")
        buf.write("\2\2\2\u01d2\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01d6")
        buf.write("\5=\37\2\u01d5\u019e\3\2\2\2\u01d5\u01b5\3\2\2\2\u01d5")
        buf.write("\u01c5\3\2\2\2\u01d5\u01d2\3\2\2\2\u01d6z\3\2\2\2\u01d7")
        buf.write("\u01d8\7V\2\2\u01d8\u01d9\7t\2\2\u01d9\u01da\7w\2\2\u01da")
        buf.write("\u01e1\7g\2\2\u01db\u01dc\7H\2\2\u01dc\u01dd\7c\2\2\u01dd")
        buf.write("\u01de\7n\2\2\u01de\u01df\7u\2\2\u01df\u01e1\7g\2\2\u01e0")
        buf.write("\u01d7\3\2\2\2\u01e0\u01db\3\2\2\2\u01e1|\3\2\2\2\u01e2")
        buf.write("\u01e5\n\16\2\2\u01e3\u01e5\5\177@\2\u01e4\u01e2\3\2\2")
        buf.write("\2\u01e4\u01e3\3\2\2\2\u01e5~\3\2\2\2\u01e6\u01e7\7^\2")
        buf.write("\2\u01e7\u01eb\t\17\2\2\u01e8\u01e9\t\20\2\2\u01e9\u01eb")
        buf.write("\7$\2\2\u01ea\u01e6\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb")
        buf.write("\u0080\3\2\2\2\u01ec\u01ed\7^\2\2\u01ed\u01ee\n\17\2\2")
        buf.write("\u01ee\u0082\3\2\2\2\u01ef\u01f3\7$\2\2\u01f0\u01f2\5")
        buf.write("}?\2\u01f1\u01f0\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1")
        buf.write("\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6\3\2\2\2\u01f5")
        buf.write("\u01f3\3\2\2\2\u01f6\u01f7\7$\2\2\u01f7\u01f8\bB\2\2\u01f8")
        buf.write("\u0084\3\2\2\2\u01f9\u01fa\5+\26\2\u01fa\u0200\5\u0087")
        buf.write("D\2\u01fb\u01fc\5;\36\2\u01fc\u01fd\5\u0087D\2\u01fd\u01ff")
        buf.write("\3\2\2\2\u01fe\u01fb\3\2\2\2\u01ff\u0202\3\2\2\2\u0200")
        buf.write("\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0203\3\2\2\2")
        buf.write("\u0202\u0200\3\2\2\2\u0203\u0204\5-\27\2\u0204\u0207\3")
        buf.write("\2\2\2\u0205\u0207\5\u0087D\2\u0206\u01f9\3\2\2\2\u0206")
        buf.write("\u0205\3\2\2\2\u0207\u0086\3\2\2\2\u0208\u0214\5+\26\2")
        buf.write("\u0209\u020f\5s:\2\u020a\u020b\5;\36\2\u020b\u020c\5s")
        buf.write(":\2\u020c\u020e\3\2\2\2\u020d\u020a\3\2\2\2\u020e\u0211")
        buf.write("\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3\2\2\2\u0210")
        buf.write("\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0212\u0209\3\2\2\2")
        buf.write("\u0213\u0216\3\2\2\2\u0214\u0212\3\2\2\2\u0214\u0215\3")
        buf.write("\2\2\2\u0215\u0217\3\2\2\2\u0216\u0214\3\2\2\2\u0217\u0218")
        buf.write("\5-\27\2\u0218\u024d\3\2\2\2\u0219\u0225\5+\26\2\u021a")
        buf.write("\u0220\5y=\2\u021b\u021c\5;\36\2\u021c\u021d\5y=\2\u021d")
        buf.write("\u021f\3\2\2\2\u021e\u021b\3\2\2\2\u021f\u0222\3\2\2\2")
        buf.write("\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2\u0221\u0224\3")
        buf.write("\2\2\2\u0222\u0220\3\2\2\2\u0223\u021a\3\2\2\2\u0224\u0227")
        buf.write("\3\2\2\2\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226")
        buf.write("\u0228\3\2\2\2\u0227\u0225\3\2\2\2\u0228\u0229\5-\27\2")
        buf.write("\u0229\u024d\3\2\2\2\u022a\u0236\5+\26\2\u022b\u0231\5")
        buf.write("\u0083B\2\u022c\u022d\5;\36\2\u022d\u022e\5\u0083B\2\u022e")
        buf.write("\u0230\3\2\2\2\u022f\u022c\3\2\2\2\u0230\u0233\3\2\2\2")
        buf.write("\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u0235\3")
        buf.write("\2\2\2\u0233\u0231\3\2\2\2\u0234\u022b\3\2\2\2\u0235\u0238")
        buf.write("\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237\3\2\2\2\u0237")
        buf.write("\u0239\3\2\2\2\u0238\u0236\3\2\2\2\u0239\u023a\5-\27\2")
        buf.write("\u023a\u024d\3\2\2\2\u023b\u0247\5+\26\2\u023c\u0242\5")
        buf.write("{>\2\u023d\u023e\5;\36\2\u023e\u023f\5{>\2\u023f\u0241")
        buf.write("\3\2\2\2\u0240\u023d\3\2\2\2\u0241\u0244\3\2\2\2\u0242")
        buf.write("\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0246\3\2\2\2")
        buf.write("\u0244\u0242\3\2\2\2\u0245\u023c\3\2\2\2\u0246\u0249\3")
        buf.write("\2\2\2\u0247\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u024a")
        buf.write("\3\2\2\2\u0249\u0247\3\2\2\2\u024a\u024b\5-\27\2\u024b")
        buf.write("\u024d\3\2\2\2\u024c\u0208\3\2\2\2\u024c\u0219\3\2\2\2")
        buf.write("\u024c\u022a\3\2\2\2\u024c\u023b\3\2\2\2\u024d\u0088\3")
        buf.write("\2\2\2\u024e\u024f\7,\2\2\u024f\u0250\7,\2\2\u0250\u0254")
        buf.write("\3\2\2\2\u0251\u0253\13\2\2\2\u0252\u0251\3\2\2\2\u0253")
        buf.write("\u0256\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2")
        buf.write("\u0255\u0257\3\2\2\2\u0256\u0254\3\2\2\2\u0257\u0258\7")
        buf.write(",\2\2\u0258\u0259\7,\2\2\u0259\u025a\3\2\2\2\u025a\u025b")
        buf.write("\bE\3\2\u025b\u008a\3\2\2\2\u025c\u025e\t\21\2\2\u025d")
        buf.write("\u025c\3\2\2\2\u025e\u025f\3\2\2\2\u025f\u025d\3\2\2\2")
        buf.write("\u025f\u0260\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u0262\b")
        buf.write("F\3\2\u0262\u008c\3\2\2\2\u0263\u0264\13\2\2\2\u0264\u008e")
        buf.write("\3\2\2\2\u0265\u0269\7$\2\2\u0266\u0268\5}?\2\u0267\u0266")
        buf.write("\3\2\2\2\u0268\u026b\3\2\2\2\u0269\u0267\3\2\2\2\u0269")
        buf.write("\u026a\3\2\2\2\u026a\u026c\3\2\2\2\u026b\u0269\3\2\2\2")
        buf.write("\u026c\u026d\n\22\2\2\u026d\u0090\3\2\2\2\u026e\u0272")
        buf.write("\7$\2\2\u026f\u0271\5}?\2\u0270\u026f\3\2\2\2\u0271\u0274")
        buf.write("\3\2\2\2\u0272\u0270\3\2\2\2\u0272\u0273\3\2\2\2\u0273")
        buf.write("\u0275\3\2\2\2\u0274\u0272\3\2\2\2\u0275\u0276\5\u0081")
        buf.write("A\2\u0276\u0092\3\2\2\2\u0277\u0278\7,\2\2\u0278\u0279")
        buf.write("\7,\2\2\u0279\u027d\3\2\2\2\u027a\u027c\13\2\2\2\u027b")
        buf.write("\u027a\3\2\2\2\u027c\u027f\3\2\2\2\u027d\u027e\3\2\2\2")
        buf.write("\u027d\u027b\3\2\2\2\u027e\u0094\3\2\2\2\u027f\u027d\3")
        buf.write("\2\2\2+\2\u0099\u016e\u0176\u017d\u0185\u0189\u018e\u0196")
        buf.write("\u019b\u019e\u01a4\u01ad\u01b2\u01b5\u01bb\u01c2\u01c7")
        buf.write("\u01ce\u01d2\u01d5\u01e0\u01e4\u01ea\u01f3\u0200\u0206")
        buf.write("\u020f\u0214\u0220\u0225\u0231\u0236\u0242\u0247\u024c")
        buf.write("\u0254\u025f\u0269\u0272\u027d\4\3B\2\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    VAR = 2
    BODY = 3
    BREAK = 4
    CONTINUE = 5
    DO = 6
    ELSE = 7
    ELSEIF = 8
    ENDBODY = 9
    ENDIF = 10
    ENDFOR = 11
    ENDWHILE = 12
    FOR = 13
    FUNCTION = 14
    IF = 15
    PARAMETER = 16
    RETURN = 17
    THEN = 18
    WHILE = 19
    ENDDO = 20
    LB = 21
    RB = 22
    LP = 23
    RP = 24
    LS = 25
    RS = 26
    SEMI = 27
    COLON = 28
    COMMA = 29
    DOT = 30
    ADDINT = 31
    SUBINT = 32
    MULINT = 33
    DIVINT = 34
    MOD = 35
    ADDFLOAT = 36
    SUBFLOAT = 37
    MULFLOAT = 38
    DIVFLOAT = 39
    EP = 40
    AND = 41
    OR = 42
    ASSIGNMENT = 43
    EQ = 44
    NEQ = 45
    GT = 46
    LT = 47
    GTE = 48
    LTE = 49
    NEQFLOAT = 50
    GTFLOAT = 51
    LTFLOAT = 52
    GTEFLOAT = 53
    LTEFLOAT = 54
    INTLIT = 55
    FLOATLIT = 56
    BOOLLIT = 57
    STRINGLIT = 58
    ARRAYLIT = 59
    ARRAY = 60
    BLOCK_COMMENT = 61
    WS = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    UNTERMINATED_COMMENT = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Var'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'While'", "'EndDo'", "'{'", "'}'", "'('", "')'", "'['", "']'", 
            "';'", "':'", "','", "'.'", "'+'", "'-'", "'*'", "'\\'", "'%'", 
            "'+.'", "'-.'", "'*.'", "'\\.'", "'!'", "'&&'", "'||'", "'='", 
            "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'=/='", "'>.'", 
            "'<.'", "'>=.'", "'<=.'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "VAR", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "WHILE", "ENDDO", "LB", 
            "RB", "LP", "RP", "LS", "RS", "SEMI", "COLON", "COMMA", "DOT", 
            "ADDINT", "SUBINT", "MULINT", "DIVINT", "MOD", "ADDFLOAT", "SUBFLOAT", 
            "MULFLOAT", "DIVFLOAT", "EP", "AND", "OR", "ASSIGNMENT", "EQ", 
            "NEQ", "GT", "LT", "GTE", "LTE", "NEQFLOAT", "GTFLOAT", "LTFLOAT", 
            "GTEFLOAT", "LTEFLOAT", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
            "ARRAYLIT", "ARRAY", "BLOCK_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "VAR", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", 
                  "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "WHILE", 
                  "ENDDO", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", "COLON", 
                  "COMMA", "DOT", "ADDINT", "SUBINT", "MULINT", "DIVINT", 
                  "MOD", "ADDFLOAT", "SUBFLOAT", "MULFLOAT", "DIVFLOAT", 
                  "EP", "AND", "OR", "ASSIGNMENT", "EQ", "NEQ", "GT", "LT", 
                  "GTE", "LTE", "NEQFLOAT", "GTFLOAT", "LTFLOAT", "GTEFLOAT", 
                  "LTEFLOAT", "Hex", "Oct", "INTLIT", "Exponent", "Digit", 
                  "FLOATLIT", "BOOLLIT", "Characters", "Esc_Seq", "Illegal_esc", 
                  "STRINGLIT", "ARRAYLIT", "ARRAY", "BLOCK_COMMENT", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:
    	    str = result.text
    	    escSeq = ['\b', '\t', '\n', '\f', '\r', "'", '\\']
    	    if str in escSeq:        
                raise UncloseString(str[1:-1])
    	    else:
    	        raise UncloseString(str[1:])
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape((result.text)[1:])
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[64] = self.STRINGLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		text = str(self.text)
            		self.text = text[1:-1]
            	
     


