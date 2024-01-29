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
        buf.write("\u01d9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'")
        buf.write("\3(\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\7.\u0151")
        buf.write("\n.\f.\16.\u0154\13.\3/\3/\5/\u0158\n/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\5\62")
        buf.write("\u0167\n\62\3\62\5\62\u016a\n\62\3\63\6\63\u016d\n\63")
        buf.write("\r\63\16\63\u016e\3\64\3\64\7\64\u0173\n\64\f\64\16\64")
        buf.write("\u0176\13\64\3\65\3\65\5\65\u017a\n\65\3\65\6\65\u017d")
        buf.write("\n\65\r\65\16\65\u017e\3\66\3\66\3\66\3\66\7\66\u0185")
        buf.write("\n\66\f\66\16\66\u0188\13\66\3\66\3\66\3\66\3\67\3\67")
        buf.write("\38\38\38\39\39\39\39\39\39\39\39\39\39\39\39\39\39\5")
        buf.write("9\u01a0\n9\3:\3:\3:\3:\3:\5:\u01a7\n:\3;\3;\3<\3<\3<\3")
        buf.write("<\7<\u01af\n<\f<\16<\u01b2\13<\3=\6=\u01b5\n=\r=\16=\u01b6")
        buf.write("\3=\3=\3>\3>\3>\3>\7>\u01bf\n>\f>\16>\u01c2\13>\3>\3>")
        buf.write("\3>\5>\u01c7\n>\3>\3>\3?\3?\3?\3?\7?\u01cf\n?\f?\16?\u01d2")
        buf.write("\13?\3?\3?\3?\3@\3@\3@\2\2A\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\2g\2i\2k\64m\2o\2q\2s\2u\65w\66y\67{8}9\177:\3\2\20")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\60\60\4\2GGgg\4")
        buf.write("\2--//\7\2\f\f\16\17$$))^^\4\2\16\17^^\b\2^^ddhhppttv")
        buf.write("v\3\2))\3\2$$\4\2\f\f\16\17\5\2\13\13\17\17\"\"\3\3\f")
        buf.write("\f\2\u01ed\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2k")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\3\u0081\3\2\2\2\5\u008c\3\2\2")
        buf.write("\2\7\u0098\3\2\2\2\t\u00a1\3\2\2\2\13\u00ac\3\2\2\2\r")
        buf.write("\u00b8\3\2\2\2\17\u00bf\3\2\2\2\21\u00c4\3\2\2\2\23\u00cb")
        buf.write("\3\2\2\2\25\u00d2\3\2\2\2\27\u00d6\3\2\2\2\31\u00de\3")
        buf.write("\2\2\2\33\u00e3\3\2\2\2\35\u00e7\3\2\2\2\37\u00ed\3\2")
        buf.write("\2\2!\u00f0\3\2\2\2#\u00f6\3\2\2\2%\u00ff\3\2\2\2\'\u0102")
        buf.write("\3\2\2\2)\u0107\3\2\2\2+\u010c\3\2\2\2-\u0112\3\2\2\2")
        buf.write("/\u0116\3\2\2\2\61\u011a\3\2\2\2\63\u011e\3\2\2\2\65\u0121")
        buf.write("\3\2\2\2\67\u0123\3\2\2\29\u0125\3\2\2\2;\u0127\3\2\2")
        buf.write("\2=\u0129\3\2\2\2?\u012b\3\2\2\2A\u012d\3\2\2\2C\u0130")
        buf.write("\3\2\2\2E\u0133\3\2\2\2G\u0135\3\2\2\2I\u0138\3\2\2\2")
        buf.write("K\u013a\3\2\2\2M\u013d\3\2\2\2O\u0141\3\2\2\2Q\u0144\3")
        buf.write("\2\2\2S\u0146\3\2\2\2U\u0148\3\2\2\2W\u014a\3\2\2\2Y\u014c")
        buf.write("\3\2\2\2[\u014e\3\2\2\2]\u0157\3\2\2\2_\u0159\3\2\2\2")
        buf.write("a\u015e\3\2\2\2c\u0164\3\2\2\2e\u016c\3\2\2\2g\u0170\3")
        buf.write("\2\2\2i\u0177\3\2\2\2k\u0180\3\2\2\2m\u018c\3\2\2\2o\u018e")
        buf.write("\3\2\2\2q\u019f\3\2\2\2s\u01a6\3\2\2\2u\u01a8\3\2\2\2")
        buf.write("w\u01aa\3\2\2\2y\u01b4\3\2\2\2{\u01ba\3\2\2\2}\u01ca\3")
        buf.write("\2\2\2\177\u01d6\3\2\2\2\u0081\u0082\7t\2\2\u0082\u0083")
        buf.write("\7g\2\2\u0083\u0084\7c\2\2\u0084\u0085\7f\2\2\u0085\u0086")
        buf.write("\7P\2\2\u0086\u0087\7w\2\2\u0087\u0088\7o\2\2\u0088\u0089")
        buf.write("\7d\2\2\u0089\u008a\7g\2\2\u008a\u008b\7t\2\2\u008b\4")
        buf.write("\3\2\2\2\u008c\u008d\7y\2\2\u008d\u008e\7t\2\2\u008e\u008f")
        buf.write("\7k\2\2\u008f\u0090\7v\2\2\u0090\u0091\7g\2\2\u0091\u0092")
        buf.write("\7P\2\2\u0092\u0093\7w\2\2\u0093\u0094\7o\2\2\u0094\u0095")
        buf.write("\7d\2\2\u0095\u0096\7g\2\2\u0096\u0097\7t\2\2\u0097\6")
        buf.write("\3\2\2\2\u0098\u0099\7t\2\2\u0099\u009a\7g\2\2\u009a\u009b")
        buf.write("\7c\2\2\u009b\u009c\7f\2\2\u009c\u009d\7D\2\2\u009d\u009e")
        buf.write("\7q\2\2\u009e\u009f\7q\2\2\u009f\u00a0\7n\2\2\u00a0\b")
        buf.write("\3\2\2\2\u00a1\u00a2\7t\2\2\u00a2\u00a3\7g\2\2\u00a3\u00a4")
        buf.write("\7c\2\2\u00a4\u00a5\7f\2\2\u00a5\u00a6\7U\2\2\u00a6\u00a7")
        buf.write("\7v\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7k\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\u00ab\7i\2\2\u00ab\n\3\2\2\2\u00ac\u00ad")
        buf.write("\7y\2\2\u00ad\u00ae\7t\2\2\u00ae\u00af\7k\2\2\u00af\u00b0")
        buf.write("\7v\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7U\2\2\u00b2\u00b3")
        buf.write("\7v\2\2\u00b3\u00b4\7t\2\2\u00b4\u00b5\7k\2\2\u00b5\u00b6")
        buf.write("\7p\2\2\u00b6\u00b7\7i\2\2\u00b7\f\3\2\2\2\u00b8\u00b9")
        buf.write("\7p\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb\7o\2\2\u00bb\u00bc")
        buf.write("\7d\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7t\2\2\u00be\16")
        buf.write("\3\2\2\2\u00bf\u00c0\7d\2\2\u00c0\u00c1\7q\2\2\u00c1\u00c2")
        buf.write("\7q\2\2\u00c2\u00c3\7n\2\2\u00c3\20\3\2\2\2\u00c4\u00c5")
        buf.write("\7u\2\2\u00c5\u00c6\7v\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7k\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7i\2\2\u00ca\22")
        buf.write("\3\2\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7g\2\2\u00cd\u00ce")
        buf.write("\7v\2\2\u00ce\u00cf\7w\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1")
        buf.write("\7p\2\2\u00d1\24\3\2\2\2\u00d2\u00d3\7x\2\2\u00d3\u00d4")
        buf.write("\7c\2\2\u00d4\u00d5\7t\2\2\u00d5\26\3\2\2\2\u00d6\u00d7")
        buf.write("\7f\2\2\u00d7\u00d8\7{\2\2\u00d8\u00d9\7p\2\2\u00d9\u00da")
        buf.write("\7c\2\2\u00da\u00db\7o\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd")
        buf.write("\7e\2\2\u00dd\30\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0")
        buf.write("\7w\2\2\u00e0\u00e1\7p\2\2\u00e1\u00e2\7e\2\2\u00e2\32")
        buf.write("\3\2\2\2\u00e3\u00e4\7h\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\34\3\2\2\2\u00e7\u00e8\7w\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7n\2\2\u00ec\36\3\2\2\2\u00ed\u00ee\7d\2\2\u00ee\u00ef")
        buf.write("\7{\2\2\u00ef \3\2\2\2\u00f0\u00f1\7d\2\2\u00f1\u00f2")
        buf.write("\7t\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5")
        buf.write("\7m\2\2\u00f5\"\3\2\2\2\u00f6\u00f7\7e\2\2\u00f7\u00f8")
        buf.write("\7q\2\2\u00f8\u00f9\7p\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe$\3\2\2\2\u00ff\u0100\7k\2\2\u0100\u0101")
        buf.write("\7h\2\2\u0101&\3\2\2\2\u0102\u0103\7g\2\2\u0103\u0104")
        buf.write("\7n\2\2\u0104\u0105\7u\2\2\u0105\u0106\7g\2\2\u0106(\3")
        buf.write("\2\2\2\u0107\u0108\7g\2\2\u0108\u0109\7n\2\2\u0109\u010a")
        buf.write("\7k\2\2\u010a\u010b\7h\2\2\u010b*\3\2\2\2\u010c\u010d")
        buf.write("\7d\2\2\u010d\u010e\7g\2\2\u010e\u010f\7i\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7p\2\2\u0111,\3\2\2\2\u0112\u0113")
        buf.write("\7g\2\2\u0113\u0114\7p\2\2\u0114\u0115\7f\2\2\u0115.\3")
        buf.write("\2\2\2\u0116\u0117\7p\2\2\u0117\u0118\7q\2\2\u0118\u0119")
        buf.write("\7v\2\2\u0119\60\3\2\2\2\u011a\u011b\7c\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c\u011d\7f\2\2\u011d\62\3\2\2\2\u011e\u011f")
        buf.write("\7q\2\2\u011f\u0120\7t\2\2\u0120\64\3\2\2\2\u0121\u0122")
        buf.write("\7-\2\2\u0122\66\3\2\2\2\u0123\u0124\7/\2\2\u01248\3\2")
        buf.write("\2\2\u0125\u0126\7,\2\2\u0126:\3\2\2\2\u0127\u0128\7\61")
        buf.write("\2\2\u0128<\3\2\2\2\u0129\u012a\7\'\2\2\u012a>\3\2\2\2")
        buf.write("\u012b\u012c\7?\2\2\u012c@\3\2\2\2\u012d\u012e\7>\2\2")
        buf.write("\u012e\u012f\7/\2\2\u012fB\3\2\2\2\u0130\u0131\7#\2\2")
        buf.write("\u0131\u0132\7?\2\2\u0132D\3\2\2\2\u0133\u0134\7>\2\2")
        buf.write("\u0134F\3\2\2\2\u0135\u0136\7>\2\2\u0136\u0137\7?\2\2")
        buf.write("\u0137H\3\2\2\2\u0138\u0139\7@\2\2\u0139J\3\2\2\2\u013a")
        buf.write("\u013b\7@\2\2\u013b\u013c\7?\2\2\u013cL\3\2\2\2\u013d")
        buf.write("\u013e\7\60\2\2\u013e\u013f\7\60\2\2\u013f\u0140\7\60")
        buf.write("\2\2\u0140N\3\2\2\2\u0141\u0142\7?\2\2\u0142\u0143\7?")
        buf.write("\2\2\u0143P\3\2\2\2\u0144\u0145\7*\2\2\u0145R\3\2\2\2")
        buf.write("\u0146\u0147\7+\2\2\u0147T\3\2\2\2\u0148\u0149\7]\2\2")
        buf.write("\u0149V\3\2\2\2\u014a\u014b\7_\2\2\u014bX\3\2\2\2\u014c")
        buf.write("\u014d\7.\2\2\u014dZ\3\2\2\2\u014e\u0152\t\2\2\2\u014f")
        buf.write("\u0151\t\3\2\2\u0150\u014f\3\2\2\2\u0151\u0154\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\\\3\2\2")
        buf.write("\2\u0154\u0152\3\2\2\2\u0155\u0158\5_\60\2\u0156\u0158")
        buf.write("\5a\61\2\u0157\u0155\3\2\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("^\3\2\2\2\u0159\u015a\7v\2\2\u015a\u015b\7t\2\2\u015b")
        buf.write("\u015c\7w\2\2\u015c\u015d\7g\2\2\u015d`\3\2\2\2\u015e")
        buf.write("\u015f\7h\2\2\u015f\u0160\7c\2\2\u0160\u0161\7n\2\2\u0161")
        buf.write("\u0162\7u\2\2\u0162\u0163\7g\2\2\u0163b\3\2\2\2\u0164")
        buf.write("\u0166\5e\63\2\u0165\u0167\5g\64\2\u0166\u0165\3\2\2\2")
        buf.write("\u0166\u0167\3\2\2\2\u0167\u0169\3\2\2\2\u0168\u016a\5")
        buf.write("i\65\2\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016ad")
        buf.write("\3\2\2\2\u016b\u016d\t\4\2\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("\u016e\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016ff\3\2\2\2\u0170\u0174\t\5\2\2\u0171\u0173\t\4\2")
        buf.write("\2\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0175\3\2\2\2\u0175h\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0177\u0179\t\6\2\2\u0178\u017a\t\7\2\2\u0179")
        buf.write("\u0178\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017c\3\2\2\2")
        buf.write("\u017b\u017d\t\4\2\2\u017c\u017b\3\2\2\2\u017d\u017e\3")
        buf.write("\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fj")
        buf.write("\3\2\2\2\u0180\u0186\5m\67\2\u0181\u0185\n\b\2\2\u0182")
        buf.write("\u0185\5q9\2\u0183\u0185\5o8\2\u0184\u0181\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0183\3\2\2\2\u0185\u0188\3\2\2\2")
        buf.write("\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0189\3")
        buf.write("\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a\5m\67\2\u018a\u018b")
        buf.write("\b\66\2\2\u018bl\3\2\2\2\u018c\u018d\7$\2\2\u018dn\3\2")
        buf.write("\2\2\u018e\u018f\7)\2\2\u018f\u0190\7$\2\2\u0190p\3\2")
        buf.write("\2\2\u0191\u0192\7^\2\2\u0192\u01a0\7d\2\2\u0193\u0194")
        buf.write("\7^\2\2\u0194\u01a0\7h\2\2\u0195\u0196\7^\2\2\u0196\u01a0")
        buf.write("\7t\2\2\u0197\u0198\7^\2\2\u0198\u01a0\7p\2\2\u0199\u019a")
        buf.write("\7^\2\2\u019a\u01a0\7v\2\2\u019b\u019c\7^\2\2\u019c\u01a0")
        buf.write("\7^\2\2\u019d\u019e\7^\2\2\u019e\u01a0\7)\2\2\u019f\u0191")
        buf.write("\3\2\2\2\u019f\u0193\3\2\2\2\u019f\u0195\3\2\2\2\u019f")
        buf.write("\u0197\3\2\2\2\u019f\u0199\3\2\2\2\u019f\u019b\3\2\2\2")
        buf.write("\u019f\u019d\3\2\2\2\u01a0r\3\2\2\2\u01a1\u01a7\t\t\2")
        buf.write("\2\u01a2\u01a3\7^\2\2\u01a3\u01a7\n\n\2\2\u01a4\u01a5")
        buf.write("\t\13\2\2\u01a5\u01a7\n\f\2\2\u01a6\u01a1\3\2\2\2\u01a6")
        buf.write("\u01a2\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a7t\3\2\2\2\u01a8")
        buf.write("\u01a9\7\f\2\2\u01a9v\3\2\2\2\u01aa\u01ab\7%\2\2\u01ab")
        buf.write("\u01ac\7%\2\2\u01ac\u01b0\3\2\2\2\u01ad\u01af\n\r\2\2")
        buf.write("\u01ae\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3")
        buf.write("\2\2\2\u01b0\u01b1\3\2\2\2\u01b1x\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b3\u01b5\t\16\2\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01b9\b=\3\2\u01b9z\3\2\2\2")
        buf.write("\u01ba\u01c0\5m\67\2\u01bb\u01bf\n\b\2\2\u01bc\u01bf\5")
        buf.write("q9\2\u01bd\u01bf\5o8\2\u01be\u01bb\3\2\2\2\u01be\u01bc")
        buf.write("\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c6\3\2\2\2")
        buf.write("\u01c2\u01c0\3\2\2\2\u01c3\u01c4\7\17\2\2\u01c4\u01c7")
        buf.write("\7\f\2\2\u01c5\u01c7\t\17\2\2\u01c6\u01c3\3\2\2\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\b>\4\2")
        buf.write("\u01c9|\3\2\2\2\u01ca\u01d0\5m\67\2\u01cb\u01cf\n\b\2")
        buf.write("\2\u01cc\u01cf\5q9\2\u01cd\u01cf\5o8\2\u01ce\u01cb\3\2")
        buf.write("\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf\u01d2")
        buf.write("\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d3\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3\u01d4\5s:\2\u01d4")
        buf.write("\u01d5\b?\5\2\u01d5~\3\2\2\2\u01d6\u01d7\13\2\2\2\u01d7")
        buf.write("\u01d8\b@\6\2\u01d8\u0080\3\2\2\2\26\2\u0152\u0157\u0166")
        buf.write("\u0169\u016e\u0174\u0179\u017e\u0184\u0186\u019f\u01a6")
        buf.write("\u01b0\u01b6\u01be\u01c0\u01c6\u01ce\u01d0\7\3\66\2\b")
        buf.write("\2\2\3>\3\3?\4\3@\5")
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
    ID = 45
    BOO_LIT = 46
    TRUE = 47
    FALSE = 48
    NUM_LIT = 49
    STR_LIT = 50
    NEWLINE = 51
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
            "'...'", "'=='", "'('", "')'", "'['", "']'", "','", "'true'", 
            "'false'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
            "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
            "BEGIN", "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "EQ_STR", "ASSIGN", "DIFFER", "LT", "LE", "GT", 
            "GE", "CONCAT", "EQ_NUM", "LP", "RP", "LS", "RS", "COMMA", "ID", 
            "BOO_LIT", "TRUE", "FALSE", "NUM_LIT", "STR_LIT", "NEWLINE", 
            "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "NUMBER", "BOOL", 
                  "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                  "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                  "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", "DIV", 
                  "MOD", "EQ_STR", "ASSIGN", "DIFFER", "LT", "LE", "GT", 
                  "GE", "CONCAT", "EQ_NUM", "LP", "RP", "LS", "RS", "COMMA", 
                  "ID", "BOO_LIT", "TRUE", "FALSE", "NUM_LIT", "INT_PART", 
                  "DEC_PART", "EXP_PART", "STR_LIT", "DOU_Q", "DOU_Q_INTEXT", 
                  "ESCAPE", "ILL_ESC_CHAR", "NEWLINE", "COMMENT", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[52] = self.STR_LIT_action 
            actions[60] = self.UNCLOSE_STRING_action 
            actions[61] = self.ILLEGAL_ESCAPE_action 
            actions[62] = self.ERROR_CHAR_action 
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
     


