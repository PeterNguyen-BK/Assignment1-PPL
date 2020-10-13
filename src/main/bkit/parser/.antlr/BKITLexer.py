# Generated from d:\Studying\Year_3\PPL\assignment1\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0223\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\7\2\u009c\n\2\f\2\16\2\u009f\13\2\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-")
        buf.write("\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3")
        buf.write("\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\38\38\38\38\39\39\39\3")
        buf.write("9\3:\3:\3:\5:\u017c\n:\3;\3;\7;\u0180\n;\f;\16;\u0183")
        buf.write("\13;\3;\5;\u0186\n;\3<\3<\3<\3<\7<\u018c\n<\f<\16<\u018f")
        buf.write("\13<\7<\u0191\n<\f<\16<\u0194\13<\3=\3=\3=\3=\7=\u019a")
        buf.write("\n=\f=\16=\u019d\13=\7=\u019f\n=\f=\16=\u01a2\13=\3>\3")
        buf.write(">\5>\u01a6\n>\3>\6>\u01a9\n>\r>\16>\u01aa\3?\3?\3@\6@")
        buf.write("\u01b0\n@\r@\16@\u01b1\3@\3@\7@\u01b6\n@\f@\16@\u01b9")
        buf.write("\13@\3@\3@\3@\6@\u01be\n@\r@\16@\u01bf\3@\3@\7@\u01c4")
        buf.write("\n@\f@\16@\u01c7\13@\3@\5@\u01ca\n@\3@\3@\3@\5@\u01cf")
        buf.write("\n@\3A\3A\5A\u01d3\nA\3B\3B\5B\u01d7\nB\3C\3C\3C\3C\5")
        buf.write("C\u01dd\nC\3D\3D\3D\3E\3E\7E\u01e4\nE\fE\16E\u01e7\13")
        buf.write("E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3F\5F\u01f3\nF\3G\3G\3G\3")
        buf.write("G\5G\u01f9\nG\3G\3G\3G\3G\3G\7G\u0200\nG\fG\16G\u0203")
        buf.write("\13G\3G\3G\3H\6H\u0208\nH\rH\16H\u0209\3H\3H\3I\3I\3J")
        buf.write("\3J\7J\u0212\nJ\fJ\16J\u0215\13J\3J\3J\3K\3K\7K\u021b")
        buf.write("\nK\fK\16K\u021e\13K\3K\3K\3L\3L\2\2M\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u\2w\2y\2{\2}\2\177")
        buf.write("<\u0081=\u0083\2\u0085\2\u0087\2\u0089>\u008b?\u008d@")
        buf.write("\u008fA\u0091B\u0093C\u0095D\u0097E\3\2\22\3\2c|\6\2\62")
        buf.write(";C\\aac|\3\2\63;\3\2\62;\3\2\62\62\4\2ZZzz\4\2\62;CH\4")
        buf.write("\2QQqq\3\2\639\3\2\629\4\2GGgg\7\2\n\f\16\17$$))^^\t\2")
        buf.write("))^^ddhhppttvv\3\2))\5\2\13\f\17\17\"\"\3\2$$\2\u0239")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\3\u0099\3\2\2\2\5\u00a0\3\2\2\2\7\u00a4\3\2\2")
        buf.write("\2\t\u00a9\3\2\2\2\13\u00af\3\2\2\2\r\u00b8\3\2\2\2\17")
        buf.write("\u00bb\3\2\2\2\21\u00c0\3\2\2\2\23\u00c7\3\2\2\2\25\u00cf")
        buf.write("\3\2\2\2\27\u00d5\3\2\2\2\31\u00dc\3\2\2\2\33\u00e5\3")
        buf.write("\2\2\2\35\u00e9\3\2\2\2\37\u00f2\3\2\2\2!\u00f5\3\2\2")
        buf.write("\2#\u00ff\3\2\2\2%\u0106\3\2\2\2\'\u010b\3\2\2\2)\u0111")
        buf.write("\3\2\2\2+\u0116\3\2\2\2-\u011c\3\2\2\2/\u0122\3\2\2\2")
        buf.write("\61\u0124\3\2\2\2\63\u0126\3\2\2\2\65\u0128\3\2\2\2\67")
        buf.write("\u012a\3\2\2\29\u012c\3\2\2\2;\u012e\3\2\2\2=\u0130\3")
        buf.write("\2\2\2?\u0132\3\2\2\2A\u0134\3\2\2\2C\u0136\3\2\2\2E\u0138")
        buf.write("\3\2\2\2G\u013a\3\2\2\2I\u013c\3\2\2\2K\u013e\3\2\2\2")
        buf.write("M\u0140\3\2\2\2O\u0143\3\2\2\2Q\u0146\3\2\2\2S\u0149\3")
        buf.write("\2\2\2U\u014c\3\2\2\2W\u014e\3\2\2\2Y\u0151\3\2\2\2[\u0154")
        buf.write("\3\2\2\2]\u0156\3\2\2\2_\u0159\3\2\2\2a\u015c\3\2\2\2")
        buf.write("c\u015e\3\2\2\2e\u0160\3\2\2\2g\u0163\3\2\2\2i\u0166\3")
        buf.write("\2\2\2k\u016a\3\2\2\2m\u016d\3\2\2\2o\u0170\3\2\2\2q\u0174")
        buf.write("\3\2\2\2s\u017b\3\2\2\2u\u0185\3\2\2\2w\u0187\3\2\2\2")
        buf.write("y\u0195\3\2\2\2{\u01a3\3\2\2\2}\u01ac\3\2\2\2\177\u01ce")
        buf.write("\3\2\2\2\u0081\u01d2\3\2\2\2\u0083\u01d6\3\2\2\2\u0085")
        buf.write("\u01dc\3\2\2\2\u0087\u01de\3\2\2\2\u0089\u01e1\3\2\2\2")
        buf.write("\u008b\u01f2\3\2\2\2\u008d\u01f4\3\2\2\2\u008f\u0207\3")
        buf.write("\2\2\2\u0091\u020d\3\2\2\2\u0093\u020f\3\2\2\2\u0095\u0218")
        buf.write("\3\2\2\2\u0097\u0221\3\2\2\2\u0099\u009d\t\2\2\2\u009a")
        buf.write("\u009c\t\3\2\2\u009b\u009a\3\2\2\2\u009c\u009f\3\2\2\2")
        buf.write("\u009d\u009b\3\2\2\2\u009d\u009e\3\2\2\2\u009e\4\3\2\2")
        buf.write("\2\u009f\u009d\3\2\2\2\u00a0\u00a1\7X\2\2\u00a1\u00a2")
        buf.write("\7c\2\2\u00a2\u00a3\7t\2\2\u00a3\6\3\2\2\2\u00a4\u00a5")
        buf.write("\7D\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7f\2\2\u00a7\u00a8")
        buf.write("\7{\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7D\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7m\2\2\u00ae\n\3\2\2\2\u00af\u00b0\7E\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\f\3\2\2\2\u00b8\u00b9\7F\2\2\u00b9\u00ba")
        buf.write("\7q\2\2\u00ba\16\3\2\2\2\u00bb\u00bc\7G\2\2\u00bc\u00bd")
        buf.write("\7n\2\2\u00bd\u00be\7u\2\2\u00be\u00bf\7g\2\2\u00bf\20")
        buf.write("\3\2\2\2\u00c0\u00c1\7G\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3")
        buf.write("\7u\2\2\u00c3\u00c4\7g\2\2\u00c4\u00c5\7K\2\2\u00c5\u00c6")
        buf.write("\7h\2\2\u00c6\22\3\2\2\2\u00c7\u00c8\7G\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\u00ca\7f\2\2\u00ca\u00cb\7D\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7f\2\2\u00cd\u00ce\7{\2\2\u00ce\24")
        buf.write("\3\2\2\2\u00cf\u00d0\7G\2\2\u00d0\u00d1\7p\2\2\u00d1\u00d2")
        buf.write("\7f\2\2\u00d2\u00d3\7K\2\2\u00d3\u00d4\7h\2\2\u00d4\26")
        buf.write("\3\2\2\2\u00d5\u00d6\7G\2\2\u00d6\u00d7\7p\2\2\u00d7\u00d8")
        buf.write("\7f\2\2\u00d8\u00d9\7H\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7t\2\2\u00db\30\3\2\2\2\u00dc\u00dd\7G\2\2\u00dd\u00de")
        buf.write("\7p\2\2\u00de\u00df\7f\2\2\u00df\u00e0\7Y\2\2\u00e0\u00e1")
        buf.write("\7j\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4")
        buf.write("\7g\2\2\u00e4\32\3\2\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7")
        buf.write("\7q\2\2\u00e7\u00e8\7t\2\2\u00e8\34\3\2\2\2\u00e9\u00ea")
        buf.write("\7H\2\2\u00ea\u00eb\7w\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed")
        buf.write("\7e\2\2\u00ed\u00ee\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7q\2\2\u00f0\u00f1\7p\2\2\u00f1\36\3\2\2\2\u00f2\u00f3")
        buf.write("\7K\2\2\u00f3\u00f4\7h\2\2\u00f4 \3\2\2\2\u00f5\u00f6")
        buf.write("\7R\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8\7t\2\2\u00f8\u00f9")
        buf.write("\7c\2\2\u00f9\u00fa\7o\2\2\u00fa\u00fb\7g\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7t\2\2\u00fe\"")
        buf.write("\3\2\2\2\u00ff\u0100\7T\2\2\u0100\u0101\7g\2\2\u0101\u0102")
        buf.write("\7v\2\2\u0102\u0103\7w\2\2\u0103\u0104\7t\2\2\u0104\u0105")
        buf.write("\7p\2\2\u0105$\3\2\2\2\u0106\u0107\7V\2\2\u0107\u0108")
        buf.write("\7j\2\2\u0108\u0109\7g\2\2\u0109\u010a\7p\2\2\u010a&\3")
        buf.write("\2\2\2\u010b\u010c\7Y\2\2\u010c\u010d\7j\2\2\u010d\u010e")
        buf.write("\7k\2\2\u010e\u010f\7n\2\2\u010f\u0110\7g\2\2\u0110(\3")
        buf.write("\2\2\2\u0111\u0112\7V\2\2\u0112\u0113\7t\2\2\u0113\u0114")
        buf.write("\7w\2\2\u0114\u0115\7g\2\2\u0115*\3\2\2\2\u0116\u0117")
        buf.write("\7H\2\2\u0117\u0118\7c\2\2\u0118\u0119\7n\2\2\u0119\u011a")
        buf.write("\7u\2\2\u011a\u011b\7g\2\2\u011b,\3\2\2\2\u011c\u011d")
        buf.write("\7G\2\2\u011d\u011e\7p\2\2\u011e\u011f\7f\2\2\u011f\u0120")
        buf.write("\7F\2\2\u0120\u0121\7q\2\2\u0121.\3\2\2\2\u0122\u0123")
        buf.write("\7}\2\2\u0123\60\3\2\2\2\u0124\u0125\7\177\2\2\u0125\62")
        buf.write("\3\2\2\2\u0126\u0127\7*\2\2\u0127\64\3\2\2\2\u0128\u0129")
        buf.write("\7+\2\2\u0129\66\3\2\2\2\u012a\u012b\7]\2\2\u012b8\3\2")
        buf.write("\2\2\u012c\u012d\7_\2\2\u012d:\3\2\2\2\u012e\u012f\7=")
        buf.write("\2\2\u012f<\3\2\2\2\u0130\u0131\7<\2\2\u0131>\3\2\2\2")
        buf.write("\u0132\u0133\7.\2\2\u0133@\3\2\2\2\u0134\u0135\7\60\2")
        buf.write("\2\u0135B\3\2\2\2\u0136\u0137\7-\2\2\u0137D\3\2\2\2\u0138")
        buf.write("\u0139\7/\2\2\u0139F\3\2\2\2\u013a\u013b\7,\2\2\u013b")
        buf.write("H\3\2\2\2\u013c\u013d\7^\2\2\u013dJ\3\2\2\2\u013e\u013f")
        buf.write("\7\'\2\2\u013fL\3\2\2\2\u0140\u0141\7-\2\2\u0141\u0142")
        buf.write("\7\60\2\2\u0142N\3\2\2\2\u0143\u0144\7/\2\2\u0144\u0145")
        buf.write("\7\60\2\2\u0145P\3\2\2\2\u0146\u0147\7,\2\2\u0147\u0148")
        buf.write("\7\60\2\2\u0148R\3\2\2\2\u0149\u014a\7^\2\2\u014a\u014b")
        buf.write("\7\60\2\2\u014bT\3\2\2\2\u014c\u014d\7#\2\2\u014dV\3\2")
        buf.write("\2\2\u014e\u014f\7(\2\2\u014f\u0150\7(\2\2\u0150X\3\2")
        buf.write("\2\2\u0151\u0152\7~\2\2\u0152\u0153\7~\2\2\u0153Z\3\2")
        buf.write("\2\2\u0154\u0155\7?\2\2\u0155\\\3\2\2\2\u0156\u0157\7")
        buf.write("?\2\2\u0157\u0158\7?\2\2\u0158^\3\2\2\2\u0159\u015a\7")
        buf.write("#\2\2\u015a\u015b\7?\2\2\u015b`\3\2\2\2\u015c\u015d\7")
        buf.write("@\2\2\u015db\3\2\2\2\u015e\u015f\7>\2\2\u015fd\3\2\2\2")
        buf.write("\u0160\u0161\7@\2\2\u0161\u0162\7?\2\2\u0162f\3\2\2\2")
        buf.write("\u0163\u0164\7>\2\2\u0164\u0165\7?\2\2\u0165h\3\2\2\2")
        buf.write("\u0166\u0167\7?\2\2\u0167\u0168\7\61\2\2\u0168\u0169\7")
        buf.write("?\2\2\u0169j\3\2\2\2\u016a\u016b\7@\2\2\u016b\u016c\7")
        buf.write("\60\2\2\u016cl\3\2\2\2\u016d\u016e\7>\2\2\u016e\u016f")
        buf.write("\7\60\2\2\u016fn\3\2\2\2\u0170\u0171\7@\2\2\u0171\u0172")
        buf.write("\7?\2\2\u0172\u0173\7\60\2\2\u0173p\3\2\2\2\u0174\u0175")
        buf.write("\7>\2\2\u0175\u0176\7?\2\2\u0176\u0177\7\60\2\2\u0177")
        buf.write("r\3\2\2\2\u0178\u017c\5u;\2\u0179\u017c\5w<\2\u017a\u017c")
        buf.write("\5y=\2\u017b\u0178\3\2\2\2\u017b\u0179\3\2\2\2\u017b\u017a")
        buf.write("\3\2\2\2\u017ct\3\2\2\2\u017d\u0181\t\4\2\2\u017e\u0180")
        buf.write("\t\5\2\2\u017f\u017e\3\2\2\2\u0180\u0183\3\2\2\2\u0181")
        buf.write("\u017f\3\2\2\2\u0181\u0182\3\2\2\2\u0182\u0186\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0184\u0186\t\6\2\2\u0185\u017d\3")
        buf.write("\2\2\2\u0185\u0184\3\2\2\2\u0186v\3\2\2\2\u0187\u0192")
        buf.write("\t\6\2\2\u0188\u0189\t\7\2\2\u0189\u018d\t\4\2\2\u018a")
        buf.write("\u018c\t\b\2\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2")
        buf.write("\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u0191\3")
        buf.write("\2\2\2\u018f\u018d\3\2\2\2\u0190\u0188\3\2\2\2\u0191\u0194")
        buf.write("\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("x\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u01a0\t\6\2\2\u0196")
        buf.write("\u0197\t\t\2\2\u0197\u019b\t\n\2\2\u0198\u019a\t\13\2")
        buf.write("\2\u0199\u0198\3\2\2\2\u019a\u019d\3\2\2\2\u019b\u0199")
        buf.write("\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019f\3\2\2\2\u019d")
        buf.write("\u019b\3\2\2\2\u019e\u0196\3\2\2\2\u019f\u01a2\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1z\3\2\2")
        buf.write("\2\u01a2\u01a0\3\2\2\2\u01a3\u01a5\t\f\2\2\u01a4\u01a6")
        buf.write("\5E#\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a8")
        buf.write("\3\2\2\2\u01a7\u01a9\t\5\2\2\u01a8\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2")
        buf.write("\u01ab|\3\2\2\2\u01ac\u01ad\t\5\2\2\u01ad~\3\2\2\2\u01ae")
        buf.write("\u01b0\5}?\2\u01af\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01b7\5A!\2\u01b4\u01b6\5}?\2\u01b5\u01b4\3\2\2")
        buf.write("\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba")
        buf.write("\u01bb\5{>\2\u01bb\u01cf\3\2\2\2\u01bc\u01be\5}?\2\u01bd")
        buf.write("\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01bd\3\2\2\2")
        buf.write("\u01bf\u01c0\3\2\2\2\u01c0\u01c9\3\2\2\2\u01c1\u01c5\5")
        buf.write("A!\2\u01c2\u01c4\5}?\2\u01c3\u01c2\3\2\2\2\u01c4\u01c7")
        buf.write("\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01ca\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01ca\5{>\2\u01c9")
        buf.write("\u01c1\3\2\2\2\u01c9\u01c8\3\2\2\2\u01ca\u01cf\3\2\2\2")
        buf.write("\u01cb\u01cc\5}?\2\u01cc\u01cd\5A!\2\u01cd\u01cf\3\2\2")
        buf.write("\2\u01ce\u01af\3\2\2\2\u01ce\u01bd\3\2\2\2\u01ce\u01cb")
        buf.write("\3\2\2\2\u01cf\u0080\3\2\2\2\u01d0\u01d3\5)\25\2\u01d1")
        buf.write("\u01d3\5+\26\2\u01d2\u01d0\3\2\2\2\u01d2\u01d1\3\2\2\2")
        buf.write("\u01d3\u0082\3\2\2\2\u01d4\u01d7\n\r\2\2\u01d5\u01d7\5")
        buf.write("\u0085C\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7")
        buf.write("\u0084\3\2\2\2\u01d8\u01d9\7^\2\2\u01d9\u01dd\t\16\2\2")
        buf.write("\u01da\u01db\t\17\2\2\u01db\u01dd\7$\2\2\u01dc\u01d8\3")
        buf.write("\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u0086\3\2\2\2\u01de\u01df")
        buf.write("\7^\2\2\u01df\u01e0\n\16\2\2\u01e0\u0088\3\2\2\2\u01e1")
        buf.write("\u01e5\7$\2\2\u01e2\u01e4\5\u0083B\2\u01e3\u01e2\3\2\2")
        buf.write("\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e6")
        buf.write("\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8")
        buf.write("\u01e9\7$\2\2\u01e9\u01ea\bE\2\2\u01ea\u008a\3\2\2\2\u01eb")
        buf.write("\u01ec\5/\30\2\u01ec\u01ed\5\u008dG\2\u01ed\u01ee\5? ")
        buf.write("\2\u01ee\u01ef\5\u008bF\2\u01ef\u01f0\5\61\31\2\u01f0")
        buf.write("\u01f3\3\2\2\2\u01f1\u01f3\5\u008dG\2\u01f2\u01eb\3\2")
        buf.write("\2\2\u01f2\u01f1\3\2\2\2\u01f3\u008c\3\2\2\2\u01f4\u01f8")
        buf.write("\5/\30\2\u01f5\u01f9\5s:\2\u01f6\u01f9\5\177@\2\u01f7")
        buf.write("\u01f9\5\u0089E\2\u01f8\u01f5\3\2\2\2\u01f8\u01f6\3\2")
        buf.write("\2\2\u01f8\u01f7\3\2\2\2\u01f9\u0201\3\2\2\2\u01fa\u01fb")
        buf.write("\5? \2\u01fb\u01fc\5s:\2\u01fc\u0200\3\2\2\2\u01fd\u0200")
        buf.write("\5\177@\2\u01fe\u0200\5\u0089E\2\u01ff\u01fa\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200\u0203\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0204\3")
        buf.write("\2\2\2\u0203\u0201\3\2\2\2\u0204\u0205\5\61\31\2\u0205")
        buf.write("\u008e\3\2\2\2\u0206\u0208\t\20\2\2\u0207\u0206\3\2\2")
        buf.write("\2\u0208\u0209\3\2\2\2\u0209\u0207\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020c\bH\3\2\u020c")
        buf.write("\u0090\3\2\2\2\u020d\u020e\13\2\2\2\u020e\u0092\3\2\2")
        buf.write("\2\u020f\u0213\7$\2\2\u0210\u0212\5\u0083B\2\u0211\u0210")
        buf.write("\3\2\2\2\u0212\u0215\3\2\2\2\u0213\u0211\3\2\2\2\u0213")
        buf.write("\u0214\3\2\2\2\u0214\u0216\3\2\2\2\u0215\u0213\3\2\2\2")
        buf.write("\u0216\u0217\n\21\2\2\u0217\u0094\3\2\2\2\u0218\u021c")
        buf.write("\7$\2\2\u0219\u021b\5\u0083B\2\u021a\u0219\3\2\2\2\u021b")
        buf.write("\u021e\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2")
        buf.write("\u021d\u021f\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0220\5")
        buf.write("\u0087D\2\u0220\u0096\3\2\2\2\u0221\u0222\13\2\2\2\u0222")
        buf.write("\u0098\3\2\2\2\36\2\u009d\u017b\u0181\u0185\u018d\u0192")
        buf.write("\u019b\u01a0\u01a5\u01aa\u01b1\u01b7\u01bf\u01c5\u01c9")
        buf.write("\u01ce\u01d2\u01d6\u01dc\u01e5\u01f2\u01f8\u01ff\u0201")
        buf.write("\u0209\u0213\u021c\4\3E\2\b\2\2")
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
    TRUE = 20
    FALSE = 21
    ENDDO = 22
    LB = 23
    RB = 24
    LP = 25
    RP = 26
    LS = 27
    RS = 28
    SEMI = 29
    COLON = 30
    COMMA = 31
    DOT = 32
    ADDINT = 33
    SUBINT = 34
    MULINT = 35
    DIVINT = 36
    MOD = 37
    ADDFLOAT = 38
    SUBFLOAT = 39
    MULFLOAT = 40
    DIVFLOAT = 41
    EP = 42
    AND = 43
    OR = 44
    ASSIGNMENT = 45
    EQ = 46
    NEQ = 47
    GT = 48
    LT = 49
    GTE = 50
    LTE = 51
    NEQFLOAT = 52
    GTFLOAT = 53
    LTFLOAT = 54
    GTEFLOAT = 55
    LTEFLOAT = 56
    INTLIT = 57
    FLOATLIT = 58
    BOOLLIT = 59
    STRINGLIT = 60
    ARRAYLIT = 61
    ARRAY = 62
    WS = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66
    UNTERMINATED_COMMENT = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Var'", "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", 
            "'ElseIf'", "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", 
            "'For'", "'Function'", "'If'", "'Parameter'", "'Return'", "'Then'", 
            "'While'", "'True'", "'False'", "'EndDo'", "'{'", "'}'", "'('", 
            "')'", "'['", "']'", "';'", "':'", "','", "'.'", "'+'", "'-'", 
            "'*'", "'\\'", "'%'", "'+.'", "'-.'", "'*.'", "'\\.'", "'!'", 
            "'&&'", "'||'", "'='", "'=='", "'!='", "'>'", "'<'", "'>='", 
            "'<='", "'=/='", "'>.'", "'<.'", "'>=.'", "'<=.'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "VAR", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "WHILE", "TRUE", "FALSE", 
            "ENDDO", "LB", "RB", "LP", "RP", "LS", "RS", "SEMI", "COLON", 
            "COMMA", "DOT", "ADDINT", "SUBINT", "MULINT", "DIVINT", "MOD", 
            "ADDFLOAT", "SUBFLOAT", "MULFLOAT", "DIVFLOAT", "EP", "AND", 
            "OR", "ASSIGNMENT", "EQ", "NEQ", "GT", "LT", "GTE", "LTE", "NEQFLOAT", 
            "GTFLOAT", "LTFLOAT", "GTEFLOAT", "LTEFLOAT", "INTLIT", "FLOATLIT", 
            "BOOLLIT", "STRINGLIT", "ARRAYLIT", "ARRAY", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "VAR", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", 
                  "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", 
                  "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "WHILE", 
                  "TRUE", "FALSE", "ENDDO", "LB", "RB", "LP", "RP", "LS", 
                  "RS", "SEMI", "COLON", "COMMA", "DOT", "ADDINT", "SUBINT", 
                  "MULINT", "DIVINT", "MOD", "ADDFLOAT", "SUBFLOAT", "MULFLOAT", 
                  "DIVFLOAT", "EP", "AND", "OR", "ASSIGNMENT", "EQ", "NEQ", 
                  "GT", "LT", "GTE", "LTE", "NEQFLOAT", "GTFLOAT", "LTFLOAT", 
                  "GTEFLOAT", "LTEFLOAT", "INTLIT", "DECINT", "HEXINT", 
                  "OCTINT", "Exponent", "Digit", "FLOATLIT", "BOOLLIT", 
                  "Characters", "Esc_Seq", "Illegal_esc", "STRINGLIT", "ARRAYLIT", 
                  "ARRAY", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

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
            actions[67] = self.STRINGLIT_action 
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
            	
     


