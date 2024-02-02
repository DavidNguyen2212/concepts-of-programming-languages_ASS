# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01c4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3$\3")
        buf.write("$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3*")
        buf.write("\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\7/\u014d\n/\f/\16/\u0150")
        buf.write("\13/\3\60\3\60\5\60\u0154\n\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\5\63\u0163\n")
        buf.write("\63\3\63\5\63\u0166\n\63\3\64\6\64\u0169\n\64\r\64\16")
        buf.write("\64\u016a\3\65\3\65\7\65\u016f\n\65\f\65\16\65\u0172\13")
        buf.write("\65\3\66\3\66\5\66\u0176\n\66\3\66\6\66\u0179\n\66\r\66")
        buf.write("\16\66\u017a\3\67\3\67\3\67\3\67\3\67\3\67\7\67\u0183")
        buf.write("\n\67\f\67\16\67\u0186\13\67\3\67\3\67\3\67\38\38\38\5")
        buf.write("8\u018e\n8\39\39\39\39\79\u0194\n9\f9\169\u0197\139\3")
        buf.write("9\39\3:\6:\u019c\n:\r:\16:\u019d\3:\3:\3;\3;\3;\3;\3;")
        buf.write("\3;\7;\u01a8\n;\f;\16;\u01ab\13;\3;\3;\3;\5;\u01b0\n;")
        buf.write("\3;\3;\3<\3<\3<\3<\3<\3<\7<\u01ba\n<\f<\16<\u01bd\13<")
        buf.write("\3<\3<\3<\3=\3=\3=\2\2>\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\2i\2k\2m\65o\2q\66s\67u8w9y:\3\2\17\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\62;\3\2\60\60\4\2GGgg\4\2--//\3\2$$")
        buf.write("\6\2\f\f\16\17$$^^\t\2))^^ddhhppttvv\3\2\16\17\4\2\f\f")
        buf.write("\16\17\5\2\n\13\16\16\"\"\3\3\f\f\2\u01d4\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2m\3\2\2\2\2q\3")
        buf.write("\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\3{")
        buf.write("\3\2\2\2\5\u0086\3\2\2\2\7\u0092\3\2\2\2\t\u009b\3\2\2")
        buf.write("\2\13\u00a6\3\2\2\2\r\u00b2\3\2\2\2\17\u00b9\3\2\2\2\21")
        buf.write("\u00be\3\2\2\2\23\u00c5\3\2\2\2\25\u00cc\3\2\2\2\27\u00d0")
        buf.write("\3\2\2\2\31\u00d8\3\2\2\2\33\u00dd\3\2\2\2\35\u00e1\3")
        buf.write("\2\2\2\37\u00e7\3\2\2\2!\u00ea\3\2\2\2#\u00f0\3\2\2\2")
        buf.write("%\u00f9\3\2\2\2\'\u00fc\3\2\2\2)\u0101\3\2\2\2+\u0106")
        buf.write("\3\2\2\2-\u010c\3\2\2\2/\u0110\3\2\2\2\61\u0114\3\2\2")
        buf.write("\2\63\u0118\3\2\2\2\65\u011b\3\2\2\2\67\u011d\3\2\2\2")
        buf.write("9\u011f\3\2\2\2;\u0121\3\2\2\2=\u0123\3\2\2\2?\u0125\3")
        buf.write("\2\2\2A\u0127\3\2\2\2C\u012a\3\2\2\2E\u012d\3\2\2\2G\u012f")
        buf.write("\3\2\2\2I\u0132\3\2\2\2K\u0134\3\2\2\2M\u0137\3\2\2\2")
        buf.write("O\u013b\3\2\2\2Q\u013e\3\2\2\2S\u0140\3\2\2\2U\u0142\3")
        buf.write("\2\2\2W\u0144\3\2\2\2Y\u0146\3\2\2\2[\u0148\3\2\2\2]\u014a")
        buf.write("\3\2\2\2_\u0153\3\2\2\2a\u0155\3\2\2\2c\u015a\3\2\2\2")
        buf.write("e\u0160\3\2\2\2g\u0168\3\2\2\2i\u016c\3\2\2\2k\u0173\3")
        buf.write("\2\2\2m\u017c\3\2\2\2o\u018d\3\2\2\2q\u018f\3\2\2\2s\u019b")
        buf.write("\3\2\2\2u\u01a1\3\2\2\2w\u01b3\3\2\2\2y\u01c1\3\2\2\2")
        buf.write("{|\7t\2\2|}\7g\2\2}~\7c\2\2~\177\7f\2\2\177\u0080\7P\2")
        buf.write("\2\u0080\u0081\7w\2\2\u0081\u0082\7o\2\2\u0082\u0083\7")
        buf.write("d\2\2\u0083\u0084\7g\2\2\u0084\u0085\7t\2\2\u0085\4\3")
        buf.write("\2\2\2\u0086\u0087\7y\2\2\u0087\u0088\7t\2\2\u0088\u0089")
        buf.write("\7k\2\2\u0089\u008a\7v\2\2\u008a\u008b\7g\2\2\u008b\u008c")
        buf.write("\7P\2\2\u008c\u008d\7w\2\2\u008d\u008e\7o\2\2\u008e\u008f")
        buf.write("\7d\2\2\u008f\u0090\7g\2\2\u0090\u0091\7t\2\2\u0091\6")
        buf.write("\3\2\2\2\u0092\u0093\7t\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7c\2\2\u0095\u0096\7f\2\2\u0096\u0097\7D\2\2\u0097\u0098")
        buf.write("\7q\2\2\u0098\u0099\7q\2\2\u0099\u009a\7n\2\2\u009a\b")
        buf.write("\3\2\2\2\u009b\u009c\7t\2\2\u009c\u009d\7g\2\2\u009d\u009e")
        buf.write("\7c\2\2\u009e\u009f\7f\2\2\u009f\u00a0\7U\2\2\u00a0\u00a1")
        buf.write("\7v\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7k\2\2\u00a3\u00a4")
        buf.write("\7p\2\2\u00a4\u00a5\7i\2\2\u00a5\n\3\2\2\2\u00a6\u00a7")
        buf.write("\7y\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write("\7v\2\2\u00aa\u00ab\7g\2\2\u00ab\u00ac\7U\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00b1\7i\2\2\u00b1\f\3\2\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7o\2\2\u00b5\u00b6")
        buf.write("\7d\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7t\2\2\u00b8\16")
        buf.write("\3\2\2\2\u00b9\u00ba\7d\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7n\2\2\u00bd\20\3\2\2\2\u00be\u00bf")
        buf.write("\7u\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7t\2\2\u00c1\u00c2")
        buf.write("\7k\2\2\u00c2\u00c3\7p\2\2\u00c3\u00c4\7i\2\2\u00c4\22")
        buf.write("\3\2\2\2\u00c5\u00c6\7t\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\u00c9\7w\2\2\u00c9\u00ca\7t\2\2\u00ca\u00cb")
        buf.write("\7p\2\2\u00cb\24\3\2\2\2\u00cc\u00cd\7x\2\2\u00cd\u00ce")
        buf.write("\7c\2\2\u00ce\u00cf\7t\2\2\u00cf\26\3\2\2\2\u00d0\u00d1")
        buf.write("\7f\2\2\u00d1\u00d2\7{\2\2\u00d2\u00d3\7p\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7o\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7")
        buf.write("\7e\2\2\u00d7\30\3\2\2\2\u00d8\u00d9\7h\2\2\u00d9\u00da")
        buf.write("\7w\2\2\u00da\u00db\7p\2\2\u00db\u00dc\7e\2\2\u00dc\32")
        buf.write("\3\2\2\2\u00dd\u00de\7h\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7t\2\2\u00e0\34\3\2\2\2\u00e1\u00e2\7w\2\2\u00e2\u00e3")
        buf.write("\7p\2\2\u00e3\u00e4\7v\2\2\u00e4\u00e5\7k\2\2\u00e5\u00e6")
        buf.write("\7n\2\2\u00e6\36\3\2\2\2\u00e7\u00e8\7d\2\2\u00e8\u00e9")
        buf.write("\7{\2\2\u00e9 \3\2\2\2\u00ea\u00eb\7d\2\2\u00eb\u00ec")
        buf.write("\7t\2\2\u00ec\u00ed\7g\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef")
        buf.write("\7m\2\2\u00ef\"\3\2\2\2\u00f0\u00f1\7e\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8")
        buf.write("\7g\2\2\u00f8$\3\2\2\2\u00f9\u00fa\7k\2\2\u00fa\u00fb")
        buf.write("\7h\2\2\u00fb&\3\2\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe")
        buf.write("\7n\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100\7g\2\2\u0100(\3")
        buf.write("\2\2\2\u0101\u0102\7g\2\2\u0102\u0103\7n\2\2\u0103\u0104")
        buf.write("\7k\2\2\u0104\u0105\7h\2\2\u0105*\3\2\2\2\u0106\u0107")
        buf.write("\7d\2\2\u0107\u0108\7g\2\2\u0108\u0109\7i\2\2\u0109\u010a")
        buf.write("\7k\2\2\u010a\u010b\7p\2\2\u010b,\3\2\2\2\u010c\u010d")
        buf.write("\7g\2\2\u010d\u010e\7p\2\2\u010e\u010f\7f\2\2\u010f.\3")
        buf.write("\2\2\2\u0110\u0111\7p\2\2\u0111\u0112\7q\2\2\u0112\u0113")
        buf.write("\7v\2\2\u0113\60\3\2\2\2\u0114\u0115\7c\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116\u0117\7f\2\2\u0117\62\3\2\2\2\u0118\u0119")
        buf.write("\7q\2\2\u0119\u011a\7t\2\2\u011a\64\3\2\2\2\u011b\u011c")
        buf.write("\7-\2\2\u011c\66\3\2\2\2\u011d\u011e\7/\2\2\u011e8\3\2")
        buf.write("\2\2\u011f\u0120\7,\2\2\u0120:\3\2\2\2\u0121\u0122\7\61")
        buf.write("\2\2\u0122<\3\2\2\2\u0123\u0124\7\'\2\2\u0124>\3\2\2\2")
        buf.write("\u0125\u0126\7?\2\2\u0126@\3\2\2\2\u0127\u0128\7>\2\2")
        buf.write("\u0128\u0129\7/\2\2\u0129B\3\2\2\2\u012a\u012b\7#\2\2")
        buf.write("\u012b\u012c\7?\2\2\u012cD\3\2\2\2\u012d\u012e\7>\2\2")
        buf.write("\u012eF\3\2\2\2\u012f\u0130\7>\2\2\u0130\u0131\7?\2\2")
        buf.write("\u0131H\3\2\2\2\u0132\u0133\7@\2\2\u0133J\3\2\2\2\u0134")
        buf.write("\u0135\7@\2\2\u0135\u0136\7?\2\2\u0136L\3\2\2\2\u0137")
        buf.write("\u0138\7\60\2\2\u0138\u0139\7\60\2\2\u0139\u013a\7\60")
        buf.write("\2\2\u013aN\3\2\2\2\u013b\u013c\7?\2\2\u013c\u013d\7?")
        buf.write("\2\2\u013dP\3\2\2\2\u013e\u013f\7*\2\2\u013fR\3\2\2\2")
        buf.write("\u0140\u0141\7+\2\2\u0141T\3\2\2\2\u0142\u0143\7]\2\2")
        buf.write("\u0143V\3\2\2\2\u0144\u0145\7_\2\2\u0145X\3\2\2\2\u0146")
        buf.write("\u0147\7.\2\2\u0147Z\3\2\2\2\u0148\u0149\7\f\2\2\u0149")
        buf.write("\\\3\2\2\2\u014a\u014e\t\2\2\2\u014b\u014d\t\3\2\2\u014c")
        buf.write("\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f^\3\2\2\2\u0150\u014e\3\2\2")
        buf.write("\2\u0151\u0154\5a\61\2\u0152\u0154\5c\62\2\u0153\u0151")
        buf.write("\3\2\2\2\u0153\u0152\3\2\2\2\u0154`\3\2\2\2\u0155\u0156")
        buf.write("\7v\2\2\u0156\u0157\7t\2\2\u0157\u0158\7w\2\2\u0158\u0159")
        buf.write("\7g\2\2\u0159b\3\2\2\2\u015a\u015b\7h\2\2\u015b\u015c")
        buf.write("\7c\2\2\u015c\u015d\7n\2\2\u015d\u015e\7u\2\2\u015e\u015f")
        buf.write("\7g\2\2\u015fd\3\2\2\2\u0160\u0162\5g\64\2\u0161\u0163")
        buf.write("\5i\65\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2\u0163")
        buf.write("\u0165\3\2\2\2\u0164\u0166\5k\66\2\u0165\u0164\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166f\3\2\2\2\u0167\u0169\t\4\2")
        buf.write("\2\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016bh\3\2\2\2\u016c\u0170")
        buf.write("\t\5\2\2\u016d\u016f\t\4\2\2\u016e\u016d\3\2\2\2\u016f")
        buf.write("\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171j\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0175\t\6\2")
        buf.write("\2\u0174\u0176\t\7\2\2\u0175\u0174\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0178\3\2\2\2\u0177\u0179\t\4\2\2\u0178")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017bl\3\2\2\2\u017c\u0184\t\b\2")
        buf.write("\2\u017d\u0183\n\t\2\2\u017e\u017f\7^\2\2\u017f\u0183")
        buf.write("\t\n\2\2\u0180\u0181\7)\2\2\u0181\u0183\7$\2\2\u0182\u017d")
        buf.write("\3\2\2\2\u0182\u017e\3\2\2\2\u0182\u0180\3\2\2\2\u0183")
        buf.write("\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2")
        buf.write("\u0185\u0187\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u0188\t")
        buf.write("\b\2\2\u0188\u0189\b\67\2\2\u0189n\3\2\2\2\u018a\u018e")
        buf.write("\t\13\2\2\u018b\u018c\7^\2\2\u018c\u018e\n\n\2\2\u018d")
        buf.write("\u018a\3\2\2\2\u018d\u018b\3\2\2\2\u018ep\3\2\2\2\u018f")
        buf.write("\u0190\7%\2\2\u0190\u0191\7%\2\2\u0191\u0195\3\2\2\2\u0192")
        buf.write("\u0194\n\f\2\2\u0193\u0192\3\2\2\2\u0194\u0197\3\2\2\2")
        buf.write("\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0198\3")
        buf.write("\2\2\2\u0197\u0195\3\2\2\2\u0198\u0199\b9\3\2\u0199r\3")
        buf.write("\2\2\2\u019a\u019c\t\r\2\2\u019b\u019a\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a0\b:\3\2\u01a0t\3\2\2\2\u01a1")
        buf.write("\u01a9\t\b\2\2\u01a2\u01a8\n\t\2\2\u01a3\u01a4\7^\2\2")
        buf.write("\u01a4\u01a8\t\n\2\2\u01a5\u01a6\7)\2\2\u01a6\u01a8\7")
        buf.write("$\2\2\u01a7\u01a2\3\2\2\2\u01a7\u01a3\3\2\2\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01af\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ac\u01ad\7\17\2\2\u01ad\u01b0\7\f\2\2\u01ae\u01b0")
        buf.write("\t\16\2\2\u01af\u01ac\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01b2\b;\4\2\u01b2v\3\2\2\2\u01b3")
        buf.write("\u01bb\t\b\2\2\u01b4\u01ba\n\t\2\2\u01b5\u01b6\7^\2\2")
        buf.write("\u01b6\u01ba\t\n\2\2\u01b7\u01b8\7)\2\2\u01b8\u01ba\7")
        buf.write("$\2\2\u01b9\u01b4\3\2\2\2\u01b9\u01b5\3\2\2\2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb")
        buf.write("\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2")
        buf.write("\u01be\u01bf\5o8\2\u01bf\u01c0\b<\5\2\u01c0x\3\2\2\2\u01c1")
        buf.write("\u01c2\13\2\2\2\u01c2\u01c3\b=\6\2\u01c3z\3\2\2\2\25\2")
        buf.write("\u014e\u0153\u0162\u0165\u016a\u0170\u0175\u017a\u0182")
        buf.write("\u0184\u018d\u0195\u019d\u01a7\u01a9\u01af\u01b9\u01bb")
        buf.write("\7\3\67\2\b\2\2\3;\3\3<\4\3=\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    NUMBER = 6
    BOOL = 7
    STRING = 8
    RETURN = 9
    VAR = 10
    DYNAMIC = 11
    FUNC = 12
    FOR = 13
    UNTIL = 14
    BY = 15
    BREAK = 16
    CONTINUE = 17
    IF = 18
    ELSE = 19
    ELIF = 20
    BEGIN = 21
    END = 22
    NOT = 23
    AND = 24
    OR = 25
    PLUS = 26
    MINUS = 27
    MUL = 28
    DIV = 29
    MOD = 30
    EQ_STR = 31
    ASSIGN = 32
    DIFFER = 33
    LT = 34
    LE = 35
    GT = 36
    GE = 37
    CONCAT = 38
    EQ_NUM = 39
    LP = 40
    RP = 41
    LS = 42
    RS = 43
    COMMA = 44
    NEWLINE = 45
    ID = 46
    BOO_LIT = 47
    TRUE = 48
    FALSE = 49
    NUM_LIT = 50
    STR_LIT = 51
    COMMENT = 52
    WS = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55
    ERROR_CHAR = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readNumber'", "'writeNumber'", "'readBool'", "'readString'", 
            "'writeString'", "'number'", "'bool'", "'string'", "'return'", 
            "'var'", "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
            "'break'", "'continue'", "'if'", "'else'", "'elif'", "'begin'", 
            "'end'", "'not'", "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "'\n'", 
            "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
            "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
            "BEGIN", "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "EQ_STR", "ASSIGN", "DIFFER", "LT", "LE", "GT", 
            "GE", "CONCAT", "EQ_NUM", "LP", "RP", "LS", "RS", "COMMA", "NEWLINE", 
            "ID", "BOO_LIT", "TRUE", "FALSE", "NUM_LIT", "STR_LIT", "COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUMBER", "BOOL", 
                  "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                  "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                  "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", "DIV", 
                  "MOD", "EQ_STR", "ASSIGN", "DIFFER", "LT", "LE", "GT", 
                  "GE", "CONCAT", "EQ_NUM", "LP", "RP", "LS", "RS", "COMMA", 
                  "NEWLINE", "ID", "BOO_LIT", "TRUE", "FALSE", "NUM_LIT", 
                  "INT_PART", "DEC_PART", "EXP_PART", "STR_LIT", "ILL_ESC_CHAR", 
                  "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[53] = self.STR_LIT_action 
            actions[57] = self.UNCLOSE_STRING_action 
            actions[58] = self.ILLEGAL_ESCAPE_action 
            actions[59] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
            		raise UncloseString(self.text[1:-2])
            	elif (self.text[-1] == '\n'):
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


