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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u019d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3+\3+\3+\3,\3,")
        buf.write("\5,\u011f\n,\3,\5,\u0122\n,\3-\6-\u0125\n-\r-\16-\u0126")
        buf.write("\3.\3.\7.\u012b\n.\f.\16.\u012e\13.\3/\3/\5/\u0132\n/")
        buf.write("\3/\6/\u0135\n/\r/\16/\u0136\3\60\3\60\5\60\u013b\n\60")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u0141\n\61\f\61\16\61\u0144")
        buf.write("\13\61\3\61\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u015e\n\65\3\66\3\66\3\66\3")
        buf.write("\66\5\66\u0164\n\66\3\67\3\67\7\67\u0168\n\67\f\67\16")
        buf.write("\67\u016b\13\67\38\38\38\38\78\u0171\n8\f8\168\u0174\13")
        buf.write("8\39\69\u0177\n9\r9\169\u0178\39\39\3:\3:\3:\3:\7:\u0181")
        buf.write("\n:\f:\16:\u0184\13:\3:\5:\u0187\n:\3:\3:\5:\u018b\n:")
        buf.write("\3:\3:\3;\3;\3;\3;\7;\u0193\n;\f;\16;\u0196\13;\3;\3;")
        buf.write("\3;\3<\3<\3<\2\2=\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y\2[\2]\2_.a/c\60e\2g\2i\2k\2")
        buf.write("m\61o\62q\63s\64u\65w\66\3\2\17\3\2\62;\3\2\60\60\4\2")
        buf.write("GGgg\4\2--//\7\2\f\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2")
        buf.write("))\3\2$$\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\16\17\5\2\13")
        buf.write("\13\17\17\"\"\6\2\f\f\16\17$$^^\2\u01b1\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2m\3\2\2\2")
        buf.write("\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2")
        buf.write("\2\3y\3\2\2\2\5{\3\2\2\2\7}\3\2\2\2\t\177\3\2\2\2\13\u0081")
        buf.write("\3\2\2\2\r\u0083\3\2\2\2\17\u0085\3\2\2\2\21\u0088\3\2")
        buf.write("\2\2\23\u008b\3\2\2\2\25\u008d\3\2\2\2\27\u0090\3\2\2")
        buf.write("\2\31\u0092\3\2\2\2\33\u0095\3\2\2\2\35\u0099\3\2\2\2")
        buf.write("\37\u009c\3\2\2\2!\u009e\3\2\2\2#\u00a0\3\2\2\2%\u00a2")
        buf.write("\3\2\2\2\'\u00a4\3\2\2\2)\u00a6\3\2\2\2+\u00a8\3\2\2\2")
        buf.write("-\u00ad\3\2\2\2/\u00b3\3\2\2\2\61\u00ba\3\2\2\2\63\u00bf")
        buf.write("\3\2\2\2\65\u00c6\3\2\2\2\67\u00cd\3\2\2\29\u00d1\3\2")
        buf.write("\2\2;\u00d9\3\2\2\2=\u00de\3\2\2\2?\u00e2\3\2\2\2A\u00e8")
        buf.write("\3\2\2\2C\u00eb\3\2\2\2E\u00f1\3\2\2\2G\u00fa\3\2\2\2")
        buf.write("I\u00fd\3\2\2\2K\u0102\3\2\2\2M\u0107\3\2\2\2O\u010d\3")
        buf.write("\2\2\2Q\u0111\3\2\2\2S\u0115\3\2\2\2U\u0119\3\2\2\2W\u011c")
        buf.write("\3\2\2\2Y\u0124\3\2\2\2[\u0128\3\2\2\2]\u012f\3\2\2\2")
        buf.write("_\u013a\3\2\2\2a\u013c\3\2\2\2c\u0148\3\2\2\2e\u014a\3")
        buf.write("\2\2\2g\u014c\3\2\2\2i\u015d\3\2\2\2k\u0163\3\2\2\2m\u0165")
        buf.write("\3\2\2\2o\u016c\3\2\2\2q\u0176\3\2\2\2s\u017c\3\2\2\2")
        buf.write("u\u018e\3\2\2\2w\u019a\3\2\2\2yz\7-\2\2z\4\3\2\2\2{|\7")
        buf.write("/\2\2|\6\3\2\2\2}~\7,\2\2~\b\3\2\2\2\177\u0080\7\61\2")
        buf.write("\2\u0080\n\3\2\2\2\u0081\u0082\7\'\2\2\u0082\f\3\2\2\2")
        buf.write("\u0083\u0084\7?\2\2\u0084\16\3\2\2\2\u0085\u0086\7>\2")
        buf.write("\2\u0086\u0087\7/\2\2\u0087\20\3\2\2\2\u0088\u0089\7#")
        buf.write("\2\2\u0089\u008a\7?\2\2\u008a\22\3\2\2\2\u008b\u008c\7")
        buf.write(">\2\2\u008c\24\3\2\2\2\u008d\u008e\7>\2\2\u008e\u008f")
        buf.write("\7?\2\2\u008f\26\3\2\2\2\u0090\u0091\7@\2\2\u0091\30\3")
        buf.write("\2\2\2\u0092\u0093\7@\2\2\u0093\u0094\7?\2\2\u0094\32")
        buf.write("\3\2\2\2\u0095\u0096\7\60\2\2\u0096\u0097\7\60\2\2\u0097")
        buf.write("\u0098\7\60\2\2\u0098\34\3\2\2\2\u0099\u009a\7?\2\2\u009a")
        buf.write("\u009b\7?\2\2\u009b\36\3\2\2\2\u009c\u009d\7*\2\2\u009d")
        buf.write(" \3\2\2\2\u009e\u009f\7+\2\2\u009f\"\3\2\2\2\u00a0\u00a1")
        buf.write("\7]\2\2\u00a1$\3\2\2\2\u00a2\u00a3\7_\2\2\u00a3&\3\2\2")
        buf.write("\2\u00a4\u00a5\7.\2\2\u00a5(\3\2\2\2\u00a6\u00a7\7=\2")
        buf.write("\2\u00a7*\3\2\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7t\2")
        buf.write("\2\u00aa\u00ab\7w\2\2\u00ab\u00ac\7g\2\2\u00ac,\3\2\2")
        buf.write("\2\u00ad\u00ae\7h\2\2\u00ae\u00af\7c\2\2\u00af\u00b0\7")
        buf.write("n\2\2\u00b0\u00b1\7u\2\2\u00b1\u00b2\7g\2\2\u00b2.\3\2")
        buf.write("\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5\7w\2\2\u00b5\u00b6")
        buf.write("\7o\2\2\u00b6\u00b7\7d\2\2\u00b7\u00b8\7g\2\2\u00b8\u00b9")
        buf.write("\7t\2\2\u00b9\60\3\2\2\2\u00ba\u00bb\7d\2\2\u00bb\u00bc")
        buf.write("\7q\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be\7n\2\2\u00be\62")
        buf.write("\3\2\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1\7v\2\2\u00c1\u00c2")
        buf.write("\7t\2\2\u00c2\u00c3\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5")
        buf.write("\7i\2\2\u00c5\64\3\2\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8")
        buf.write("\7g\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb")
        buf.write("\7t\2\2\u00cb\u00cc\7p\2\2\u00cc\66\3\2\2\2\u00cd\u00ce")
        buf.write("\7x\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7t\2\2\u00d08\3")
        buf.write("\2\2\2\u00d1\u00d2\7f\2\2\u00d2\u00d3\7{\2\2\u00d3\u00d4")
        buf.write("\7p\2\2\u00d4\u00d5\7c\2\2\u00d5\u00d6\7o\2\2\u00d6\u00d7")
        buf.write("\7k\2\2\u00d7\u00d8\7e\2\2\u00d8:\3\2\2\2\u00d9\u00da")
        buf.write("\7h\2\2\u00da\u00db\7w\2\2\u00db\u00dc\7p\2\2\u00dc\u00dd")
        buf.write("\7e\2\2\u00dd<\3\2\2\2\u00de\u00df\7h\2\2\u00df\u00e0")
        buf.write("\7q\2\2\u00e0\u00e1\7t\2\2\u00e1>\3\2\2\2\u00e2\u00e3")
        buf.write("\7w\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7v\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7n\2\2\u00e7@\3\2\2\2\u00e8\u00e9")
        buf.write("\7d\2\2\u00e9\u00ea\7{\2\2\u00eaB\3\2\2\2\u00eb\u00ec")
        buf.write("\7d\2\2\u00ec\u00ed\7t\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7m\2\2\u00f0D\3\2\2\2\u00f1\u00f2")
        buf.write("\7e\2\2\u00f2\u00f3\7q\2\2\u00f3\u00f4\7p\2\2\u00f4\u00f5")
        buf.write("\7v\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8")
        buf.write("\7w\2\2\u00f8\u00f9\7g\2\2\u00f9F\3\2\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7h\2\2\u00fcH\3\2\2\2\u00fd\u00fe")
        buf.write("\7g\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100\7u\2\2\u0100\u0101")
        buf.write("\7g\2\2\u0101J\3\2\2\2\u0102\u0103\7g\2\2\u0103\u0104")
        buf.write("\7n\2\2\u0104\u0105\7k\2\2\u0105\u0106\7h\2\2\u0106L\3")
        buf.write("\2\2\2\u0107\u0108\7d\2\2\u0108\u0109\7g\2\2\u0109\u010a")
        buf.write("\7i\2\2\u010a\u010b\7k\2\2\u010b\u010c\7p\2\2\u010cN\3")
        buf.write("\2\2\2\u010d\u010e\7g\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7f\2\2\u0110P\3\2\2\2\u0111\u0112\7p\2\2\u0112\u0113")
        buf.write("\7q\2\2\u0113\u0114\7v\2\2\u0114R\3\2\2\2\u0115\u0116")
        buf.write("\7c\2\2\u0116\u0117\7p\2\2\u0117\u0118\7f\2\2\u0118T\3")
        buf.write("\2\2\2\u0119\u011a\7q\2\2\u011a\u011b\7t\2\2\u011bV\3")
        buf.write("\2\2\2\u011c\u011e\5Y-\2\u011d\u011f\5[.\2\u011e\u011d")
        buf.write("\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2\u0120")
        buf.write("\u0122\5]/\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2\u0122")
        buf.write("X\3\2\2\2\u0123\u0125\t\2\2\2\u0124\u0123\3\2\2\2\u0125")
        buf.write("\u0126\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0127\3\2\2\2")
        buf.write("\u0127Z\3\2\2\2\u0128\u012c\t\3\2\2\u0129\u012b\t\2\2")
        buf.write("\2\u012a\u0129\3\2\2\2\u012b\u012e\3\2\2\2\u012c\u012a")
        buf.write("\3\2\2\2\u012c\u012d\3\2\2\2\u012d\\\3\2\2\2\u012e\u012c")
        buf.write("\3\2\2\2\u012f\u0131\t\4\2\2\u0130\u0132\t\5\2\2\u0131")
        buf.write("\u0130\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0134\3\2\2\2")
        buf.write("\u0133\u0135\t\2\2\2\u0134\u0133\3\2\2\2\u0135\u0136\3")
        buf.write("\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137^")
        buf.write("\3\2\2\2\u0138\u013b\5+\26\2\u0139\u013b\5-\27\2\u013a")
        buf.write("\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013b`\3\2\2\2\u013c")
        buf.write("\u0142\5e\63\2\u013d\u0141\n\6\2\2\u013e\u0141\5i\65\2")
        buf.write("\u013f\u0141\5g\64\2\u0140\u013d\3\2\2\2\u0140\u013e\3")
        buf.write("\2\2\2\u0140\u013f\3\2\2\2\u0141\u0144\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0145\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0145\u0146\5e\63\2\u0146\u0147\b\61\2")
        buf.write("\2\u0147b\3\2\2\2\u0148\u0149\7\f\2\2\u0149d\3\2\2\2\u014a")
        buf.write("\u014b\7$\2\2\u014bf\3\2\2\2\u014c\u014d\7)\2\2\u014d")
        buf.write("\u014e\7$\2\2\u014eh\3\2\2\2\u014f\u0150\7^\2\2\u0150")
        buf.write("\u015e\7d\2\2\u0151\u0152\7^\2\2\u0152\u015e\7h\2\2\u0153")
        buf.write("\u0154\7^\2\2\u0154\u015e\7t\2\2\u0155\u0156\7^\2\2\u0156")
        buf.write("\u015e\7p\2\2\u0157\u0158\7^\2\2\u0158\u015e\7v\2\2\u0159")
        buf.write("\u015a\7^\2\2\u015a\u015e\7^\2\2\u015b\u015c\7^\2\2\u015c")
        buf.write("\u015e\7)\2\2\u015d\u014f\3\2\2\2\u015d\u0151\3\2\2\2")
        buf.write("\u015d\u0153\3\2\2\2\u015d\u0155\3\2\2\2\u015d\u0157\3")
        buf.write("\2\2\2\u015d\u0159\3\2\2\2\u015d\u015b\3\2\2\2\u015ej")
        buf.write("\3\2\2\2\u015f\u0160\7^\2\2\u0160\u0164\n\7\2\2\u0161")
        buf.write("\u0162\t\b\2\2\u0162\u0164\n\t\2\2\u0163\u015f\3\2\2\2")
        buf.write("\u0163\u0161\3\2\2\2\u0164l\3\2\2\2\u0165\u0169\t\n\2")
        buf.write("\2\u0166\u0168\t\13\2\2\u0167\u0166\3\2\2\2\u0168\u016b")
        buf.write("\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("n\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d\7%\2\2\u016d")
        buf.write("\u016e\7%\2\2\u016e\u0172\3\2\2\2\u016f\u0171\n\f\2\2")
        buf.write("\u0170\u016f\3\2\2\2\u0171\u0174\3\2\2\2\u0172\u0170\3")
        buf.write("\2\2\2\u0172\u0173\3\2\2\2\u0173p\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0175\u0177\t\r\2\2\u0176\u0175\3\2\2\2\u0177")
        buf.write("\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2")
        buf.write("\u0179\u017a\3\2\2\2\u017a\u017b\b9\3\2\u017br\3\2\2\2")
        buf.write("\u017c\u0182\5e\63\2\u017d\u0181\n\16\2\2\u017e\u0181")
        buf.write("\5i\65\2\u017f\u0181\5g\64\2\u0180\u017d\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u018a\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0185\u0187\7\17\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0186\u0187\3\2\2\2\u0187\u0188\3\2\2\2")
        buf.write("\u0188\u018b\7\f\2\2\u0189\u018b\7\2\2\3\u018a\u0186\3")
        buf.write("\2\2\2\u018a\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018c\u018d")
        buf.write("\b:\4\2\u018dt\3\2\2\2\u018e\u0194\5e\63\2\u018f\u0193")
        buf.write("\n\16\2\2\u0190\u0193\5i\65\2\u0191\u0193\5g\64\2\u0192")
        buf.write("\u018f\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0191\3\2\2\2")
        buf.write("\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3")
        buf.write("\2\2\2\u0195\u0197\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u0198")
        buf.write("\5k\66\2\u0198\u0199\b;\5\2\u0199v\3\2\2\2\u019a\u019b")
        buf.write("\13\2\2\2\u019b\u019c\b<\6\2\u019cx\3\2\2\2\27\2\u011e")
        buf.write("\u0121\u0126\u012c\u0131\u0136\u013a\u0140\u0142\u015d")
        buf.write("\u0163\u0169\u0172\u0178\u0180\u0182\u0186\u018a\u0192")
        buf.write("\u0194\7\3\61\2\b\2\2\3:\3\3;\4\3<\5")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    MUL = 3
    DIV = 4
    MOD = 5
    EQ_STR = 6
    ASSIGN = 7
    DIFFER = 8
    LT = 9
    LE = 10
    GT = 11
    GE = 12
    CONCAT = 13
    EQ_NUM = 14
    LP = 15
    RP = 16
    LS = 17
    RS = 18
    COMMA = 19
    SEMI = 20
    TRUE = 21
    FALSE = 22
    NUMBER = 23
    BOOL = 24
    STRING = 25
    RETURN = 26
    VAR = 27
    DYNAMIC = 28
    FUNC = 29
    FOR = 30
    UNTIL = 31
    BY = 32
    BREAK = 33
    CONTINUE = 34
    IF = 35
    ELSE = 36
    ELIF = 37
    BEGIN = 38
    END = 39
    NOT = 40
    AND = 41
    OR = 42
    NUM_LIT = 43
    BOO_LIT = 44
    STR_LIT = 45
    NEWLINE = 46
    ID = 47
    COMMENT = 48
    WS = 49
    UNCLOSE_STRING = 50
    ILLEGAL_ESCAPE = 51
    ERROR_CHAR = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'...'", "'=='", "'('", "')'", "'['", 
            "']'", "','", "';'", "'true'", "'false'", "'number'", "'bool'", 
            "'string'", "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
            "'until'", "'by'", "'break'", "'continue'", "'if'", "'else'", 
            "'elif'", "'begin'", "'end'", "'not'", "'and'", "'or'", "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ_STR", "ASSIGN", "DIFFER", 
            "LT", "LE", "GT", "GE", "CONCAT", "EQ_NUM", "LP", "RP", "LS", 
            "RS", "COMMA", "SEMI", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
            "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
            "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", 
            "OR", "NUM_LIT", "BOO_LIT", "STR_LIT", "NEWLINE", "ID", "COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "PLUS", "MINUS", "MUL", "DIV", "MOD", "EQ_STR", "ASSIGN", 
                  "DIFFER", "LT", "LE", "GT", "GE", "CONCAT", "EQ_NUM", 
                  "LP", "RP", "LS", "RS", "COMMA", "SEMI", "TRUE", "FALSE", 
                  "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                  "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", 
                  "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "NUM_LIT", 
                  "INT_PART", "DEC_PART", "EXP_PART", "BOO_LIT", "STR_LIT", 
                  "NEWLINE", "DOU_Q", "DOU_Q_INTEXT", "ESCAPE", "ILL_ESC_CHAR", 
                  "ID", "COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

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
            actions[47] = self.STR_LIT_action 
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[58] = self.ERROR_CHAR_action 
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

            	err_string = self.text[1:]
            	if (err_string[-1] == '\n'):
            		raise UncloseString(self.text[1:-2])
            	else:
            		raise UncloseString(err_string)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	esc_list = ['\'', 'b', 'f', 'r', 'n', 't', '\\']
            	for i in range(1, len(self.text) - 1):
            		if (self.text[i] == esc_list[0]) or (self.text[i] == '\\' and self.text[i+1] not in esc_list): 
            			raise IllegalEscape(self.text[1:i+2])
            			break

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     


