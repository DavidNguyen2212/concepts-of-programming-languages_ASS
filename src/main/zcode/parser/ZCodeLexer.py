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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u0188\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\5)\u010d\n)\3*\3*\7*\u0111\n*\f*\16*\u0114\13*\3+\3")
        buf.write("+\5+\u0118\n+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\5")
        buf.write(".\u0127\n.\3.\5.\u012a\n.\3/\6/\u012d\n/\r/\16/\u012e")
        buf.write("\3\60\3\60\7\60\u0133\n\60\f\60\16\60\u0136\13\60\3\61")
        buf.write("\3\61\5\61\u013a\n\61\3\61\6\61\u013d\n\61\r\61\16\61")
        buf.write("\u013e\3\62\3\62\3\62\3\62\3\62\3\62\7\62\u0147\n\62\f")
        buf.write("\62\16\62\u014a\13\62\3\62\3\62\3\62\3\63\3\63\3\63\5")
        buf.write("\63\u0152\n\63\3\64\3\64\3\64\3\64\7\64\u0158\n\64\f\64")
        buf.write("\16\64\u015b\13\64\3\64\3\64\3\65\6\65\u0160\n\65\r\65")
        buf.write("\16\65\u0161\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\7")
        buf.write("\66\u016c\n\66\f\66\16\66\u016f\13\66\3\66\3\66\3\66\5")
        buf.write("\66\u0174\n\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\7\67\u017e\n\67\f\67\16\67\u0181\13\67\3\67\3\67\3\67")
        buf.write("\38\38\38\2\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\2_\2a\2c\60e\2g\61i\62k\63")
        buf.write("m\64o\65\3\2\17\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2")
        buf.write("\60\60\4\2GGgg\4\2--//\3\2$$\6\2\f\f\16\17$$^^\t\2))^")
        buf.write("^ddhhppttvv\3\2\16\17\4\2\f\f\16\17\5\2\n\13\16\16\"\"")
        buf.write("\3\3\f\f\2\u0199\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2c\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\3q\3\2\2\2\5x\3\2\2\2\7}\3\2\2")
        buf.write("\2\t\u0084\3\2\2\2\13\u008b\3\2\2\2\r\u008f\3\2\2\2\17")
        buf.write("\u0097\3\2\2\2\21\u009c\3\2\2\2\23\u00a0\3\2\2\2\25\u00a6")
        buf.write("\3\2\2\2\27\u00a9\3\2\2\2\31\u00af\3\2\2\2\33\u00b8\3")
        buf.write("\2\2\2\35\u00bb\3\2\2\2\37\u00c0\3\2\2\2!\u00c5\3\2\2")
        buf.write("\2#\u00cb\3\2\2\2%\u00cf\3\2\2\2\'\u00d3\3\2\2\2)\u00d7")
        buf.write("\3\2\2\2+\u00da\3\2\2\2-\u00dc\3\2\2\2/\u00de\3\2\2\2")
        buf.write("\61\u00e0\3\2\2\2\63\u00e2\3\2\2\2\65\u00e4\3\2\2\2\67")
        buf.write("\u00e6\3\2\2\29\u00e9\3\2\2\2;\u00ec\3\2\2\2=\u00ee\3")
        buf.write("\2\2\2?\u00f1\3\2\2\2A\u00f3\3\2\2\2C\u00f6\3\2\2\2E\u00fa")
        buf.write("\3\2\2\2G\u00fd\3\2\2\2I\u00ff\3\2\2\2K\u0101\3\2\2\2")
        buf.write("M\u0103\3\2\2\2O\u0105\3\2\2\2Q\u010c\3\2\2\2S\u010e\3")
        buf.write("\2\2\2U\u0117\3\2\2\2W\u0119\3\2\2\2Y\u011e\3\2\2\2[\u0124")
        buf.write("\3\2\2\2]\u012c\3\2\2\2_\u0130\3\2\2\2a\u0137\3\2\2\2")
        buf.write("c\u0140\3\2\2\2e\u0151\3\2\2\2g\u0153\3\2\2\2i\u015f\3")
        buf.write("\2\2\2k\u0165\3\2\2\2m\u0177\3\2\2\2o\u0185\3\2\2\2qr")
        buf.write("\7p\2\2rs\7w\2\2st\7o\2\2tu\7d\2\2uv\7g\2\2vw\7t\2\2w")
        buf.write("\4\3\2\2\2xy\7d\2\2yz\7q\2\2z{\7q\2\2{|\7n\2\2|\6\3\2")
        buf.write("\2\2}~\7u\2\2~\177\7v\2\2\177\u0080\7t\2\2\u0080\u0081")
        buf.write("\7k\2\2\u0081\u0082\7p\2\2\u0082\u0083\7i\2\2\u0083\b")
        buf.write("\3\2\2\2\u0084\u0085\7t\2\2\u0085\u0086\7g\2\2\u0086\u0087")
        buf.write("\7v\2\2\u0087\u0088\7w\2\2\u0088\u0089\7t\2\2\u0089\u008a")
        buf.write("\7p\2\2\u008a\n\3\2\2\2\u008b\u008c\7x\2\2\u008c\u008d")
        buf.write("\7c\2\2\u008d\u008e\7t\2\2\u008e\f\3\2\2\2\u008f\u0090")
        buf.write("\7f\2\2\u0090\u0091\7{\2\2\u0091\u0092\7p\2\2\u0092\u0093")
        buf.write("\7c\2\2\u0093\u0094\7o\2\2\u0094\u0095\7k\2\2\u0095\u0096")
        buf.write("\7e\2\2\u0096\16\3\2\2\2\u0097\u0098\7h\2\2\u0098\u0099")
        buf.write("\7w\2\2\u0099\u009a\7p\2\2\u009a\u009b\7e\2\2\u009b\20")
        buf.write("\3\2\2\2\u009c\u009d\7h\2\2\u009d\u009e\7q\2\2\u009e\u009f")
        buf.write("\7t\2\2\u009f\22\3\2\2\2\u00a0\u00a1\7w\2\2\u00a1\u00a2")
        buf.write("\7p\2\2\u00a2\u00a3\7v\2\2\u00a3\u00a4\7k\2\2\u00a4\u00a5")
        buf.write("\7n\2\2\u00a5\24\3\2\2\2\u00a6\u00a7\7d\2\2\u00a7\u00a8")
        buf.write("\7{\2\2\u00a8\26\3\2\2\2\u00a9\u00aa\7d\2\2\u00aa\u00ab")
        buf.write("\7t\2\2\u00ab\u00ac\7g\2\2\u00ac\u00ad\7c\2\2\u00ad\u00ae")
        buf.write("\7m\2\2\u00ae\30\3\2\2\2\u00af\u00b0\7e\2\2\u00b0\u00b1")
        buf.write("\7q\2\2\u00b1\u00b2\7p\2\2\u00b2\u00b3\7v\2\2\u00b3\u00b4")
        buf.write("\7k\2\2\u00b4\u00b5\7p\2\2\u00b5\u00b6\7w\2\2\u00b6\u00b7")
        buf.write("\7g\2\2\u00b7\32\3\2\2\2\u00b8\u00b9\7k\2\2\u00b9\u00ba")
        buf.write("\7h\2\2\u00ba\34\3\2\2\2\u00bb\u00bc\7g\2\2\u00bc\u00bd")
        buf.write("\7n\2\2\u00bd\u00be\7u\2\2\u00be\u00bf\7g\2\2\u00bf\36")
        buf.write("\3\2\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7h\2\2\u00c4 \3\2\2\2\u00c5\u00c6")
        buf.write("\7d\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7i\2\2\u00c8\u00c9")
        buf.write("\7k\2\2\u00c9\u00ca\7p\2\2\u00ca\"\3\2\2\2\u00cb\u00cc")
        buf.write("\7g\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7f\2\2\u00ce$\3")
        buf.write("\2\2\2\u00cf\u00d0\7p\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7v\2\2\u00d2&\3\2\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5")
        buf.write("\7p\2\2\u00d5\u00d6\7f\2\2\u00d6(\3\2\2\2\u00d7\u00d8")
        buf.write("\7q\2\2\u00d8\u00d9\7t\2\2\u00d9*\3\2\2\2\u00da\u00db")
        buf.write("\7-\2\2\u00db,\3\2\2\2\u00dc\u00dd\7/\2\2\u00dd.\3\2\2")
        buf.write("\2\u00de\u00df\7,\2\2\u00df\60\3\2\2\2\u00e0\u00e1\7\61")
        buf.write("\2\2\u00e1\62\3\2\2\2\u00e2\u00e3\7\'\2\2\u00e3\64\3\2")
        buf.write("\2\2\u00e4\u00e5\7?\2\2\u00e5\66\3\2\2\2\u00e6\u00e7\7")
        buf.write(">\2\2\u00e7\u00e8\7/\2\2\u00e88\3\2\2\2\u00e9\u00ea\7")
        buf.write("#\2\2\u00ea\u00eb\7?\2\2\u00eb:\3\2\2\2\u00ec\u00ed\7")
        buf.write(">\2\2\u00ed<\3\2\2\2\u00ee\u00ef\7>\2\2\u00ef\u00f0\7")
        buf.write("?\2\2\u00f0>\3\2\2\2\u00f1\u00f2\7@\2\2\u00f2@\3\2\2\2")
        buf.write("\u00f3\u00f4\7@\2\2\u00f4\u00f5\7?\2\2\u00f5B\3\2\2\2")
        buf.write("\u00f6\u00f7\7\60\2\2\u00f7\u00f8\7\60\2\2\u00f8\u00f9")
        buf.write("\7\60\2\2\u00f9D\3\2\2\2\u00fa\u00fb\7?\2\2\u00fb\u00fc")
        buf.write("\7?\2\2\u00fcF\3\2\2\2\u00fd\u00fe\7*\2\2\u00feH\3\2\2")
        buf.write("\2\u00ff\u0100\7+\2\2\u0100J\3\2\2\2\u0101\u0102\7]\2")
        buf.write("\2\u0102L\3\2\2\2\u0103\u0104\7_\2\2\u0104N\3\2\2\2\u0105")
        buf.write("\u0106\7.\2\2\u0106P\3\2\2\2\u0107\u010d\7\f\2\2\u0108")
        buf.write("\u0109\7\17\2\2\u0109\u010a\7\f\2\2\u010a\u010b\3\2\2")
        buf.write("\2\u010b\u010d\b)\2\2\u010c\u0107\3\2\2\2\u010c\u0108")
        buf.write("\3\2\2\2\u010dR\3\2\2\2\u010e\u0112\t\2\2\2\u010f\u0111")
        buf.write("\t\3\2\2\u0110\u010f\3\2\2\2\u0111\u0114\3\2\2\2\u0112")
        buf.write("\u0110\3\2\2\2\u0112\u0113\3\2\2\2\u0113T\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0115\u0118\5W,\2\u0116\u0118\5Y-\2\u0117")
        buf.write("\u0115\3\2\2\2\u0117\u0116\3\2\2\2\u0118V\3\2\2\2\u0119")
        buf.write("\u011a\7v\2\2\u011a\u011b\7t\2\2\u011b\u011c\7w\2\2\u011c")
        buf.write("\u011d\7g\2\2\u011dX\3\2\2\2\u011e\u011f\7h\2\2\u011f")
        buf.write("\u0120\7c\2\2\u0120\u0121\7n\2\2\u0121\u0122\7u\2\2\u0122")
        buf.write("\u0123\7g\2\2\u0123Z\3\2\2\2\u0124\u0126\5]/\2\u0125\u0127")
        buf.write("\5_\60\2\u0126\u0125\3\2\2\2\u0126\u0127\3\2\2\2\u0127")
        buf.write("\u0129\3\2\2\2\u0128\u012a\5a\61\2\u0129\u0128\3\2\2\2")
        buf.write("\u0129\u012a\3\2\2\2\u012a\\\3\2\2\2\u012b\u012d\t\4\2")
        buf.write("\2\u012c\u012b\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u012c")
        buf.write("\3\2\2\2\u012e\u012f\3\2\2\2\u012f^\3\2\2\2\u0130\u0134")
        buf.write("\t\5\2\2\u0131\u0133\t\4\2\2\u0132\u0131\3\2\2\2\u0133")
        buf.write("\u0136\3\2\2\2\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2")
        buf.write("\u0135`\3\2\2\2\u0136\u0134\3\2\2\2\u0137\u0139\t\6\2")
        buf.write("\2\u0138\u013a\t\7\2\2\u0139\u0138\3\2\2\2\u0139\u013a")
        buf.write("\3\2\2\2\u013a\u013c\3\2\2\2\u013b\u013d\t\4\2\2\u013c")
        buf.write("\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013c\3\2\2\2")
        buf.write("\u013e\u013f\3\2\2\2\u013fb\3\2\2\2\u0140\u0148\t\b\2")
        buf.write("\2\u0141\u0147\n\t\2\2\u0142\u0143\7^\2\2\u0143\u0147")
        buf.write("\t\n\2\2\u0144\u0145\7)\2\2\u0145\u0147\7$\2\2\u0146\u0141")
        buf.write("\3\2\2\2\u0146\u0142\3\2\2\2\u0146\u0144\3\2\2\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149\u014b\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\t")
        buf.write("\b\2\2\u014c\u014d\b\62\3\2\u014dd\3\2\2\2\u014e\u0152")
        buf.write("\t\13\2\2\u014f\u0150\7^\2\2\u0150\u0152\n\n\2\2\u0151")
        buf.write("\u014e\3\2\2\2\u0151\u014f\3\2\2\2\u0152f\3\2\2\2\u0153")
        buf.write("\u0154\7%\2\2\u0154\u0155\7%\2\2\u0155\u0159\3\2\2\2\u0156")
        buf.write("\u0158\n\f\2\2\u0157\u0156\3\2\2\2\u0158\u015b\3\2\2\2")
        buf.write("\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2\u015a\u015c\3")
        buf.write("\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\b\64\4\2\u015d")
        buf.write("h\3\2\2\2\u015e\u0160\t\r\2\2\u015f\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2")
        buf.write("\u0162\u0163\3\2\2\2\u0163\u0164\b\65\4\2\u0164j\3\2\2")
        buf.write("\2\u0165\u016d\t\b\2\2\u0166\u016c\n\t\2\2\u0167\u0168")
        buf.write("\7^\2\2\u0168\u016c\t\n\2\2\u0169\u016a\7)\2\2\u016a\u016c")
        buf.write("\7$\2\2\u016b\u0166\3\2\2\2\u016b\u0167\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016e\3\2\2\2\u016e\u0173\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u0170\u0171\7\17\2\2\u0171\u0174\7\f\2\2\u0172")
        buf.write("\u0174\t\16\2\2\u0173\u0170\3\2\2\2\u0173\u0172\3\2\2")
        buf.write("\2\u0174\u0175\3\2\2\2\u0175\u0176\b\66\5\2\u0176l\3\2")
        buf.write("\2\2\u0177\u017f\t\b\2\2\u0178\u017e\n\t\2\2\u0179\u017a")
        buf.write("\7^\2\2\u017a\u017e\t\n\2\2\u017b\u017c\7)\2\2\u017c\u017e")
        buf.write("\7$\2\2\u017d\u0178\3\2\2\2\u017d\u0179\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u017f\u0180\3\2\2\2\u0180\u0182\3\2\2\2\u0181\u017f\3")
        buf.write("\2\2\2\u0182\u0183\5e\63\2\u0183\u0184\b\67\6\2\u0184")
        buf.write("n\3\2\2\2\u0185\u0186\13\2\2\2\u0186\u0187\b8\7\2\u0187")
        buf.write("p\3\2\2\2\26\2\u010c\u0112\u0117\u0126\u0129\u012e\u0134")
        buf.write("\u0139\u013e\u0146\u0148\u0151\u0159\u0161\u016b\u016d")
        buf.write("\u0173\u017d\u017f\b\3)\2\3\62\3\b\2\2\3\66\4\3\67\5\3")
        buf.write("8\6")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    BOOL = 2
    STRING = 3
    RETURN = 4
    VAR = 5
    DYNAMIC = 6
    FUNC = 7
    FOR = 8
    UNTIL = 9
    BY = 10
    BREAK = 11
    CONTINUE = 12
    IF = 13
    ELSE = 14
    ELIF = 15
    BEGIN = 16
    END = 17
    NOT = 18
    AND = 19
    OR = 20
    PLUS = 21
    MINUS = 22
    MUL = 23
    DIV = 24
    MOD = 25
    EQ_STR = 26
    ASSIGN = 27
    DIFFER = 28
    LT = 29
    LE = 30
    GT = 31
    GE = 32
    CONCAT = 33
    EQ_NUM = 34
    LP = 35
    RP = 36
    LS = 37
    RS = 38
    COMMA = 39
    NEWLINE = 40
    ID = 41
    BOO_LIT = 42
    TRUE = 43
    FALSE = 44
    NUM_LIT = 45
    STR_LIT = 46
    COMMENT = 47
    WS = 48
    UNCLOSE_STRING = 49
    ILLEGAL_ESCAPE = 50
    ERROR_CHAR = 51

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
            "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", "')'", 
            "'['", "']'", "','", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
            "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
            "BEGIN", "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "EQ_STR", "ASSIGN", "DIFFER", "LT", "LE", "GT", 
            "GE", "CONCAT", "EQ_NUM", "LP", "RP", "LS", "RS", "COMMA", "NEWLINE", 
            "ID", "BOO_LIT", "TRUE", "FALSE", "NUM_LIT", "STR_LIT", "COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                  "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", 
                  "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
                  "MINUS", "MUL", "DIV", "MOD", "EQ_STR", "ASSIGN", "DIFFER", 
                  "LT", "LE", "GT", "GE", "CONCAT", "EQ_NUM", "LP", "RP", 
                  "LS", "RS", "COMMA", "NEWLINE", "ID", "BOO_LIT", "TRUE", 
                  "FALSE", "NUM_LIT", "INT_PART", "DEC_PART", "EXP_PART", 
                  "STR_LIT", "ILL_ESC_CHAR", "COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[39] = self.NEWLINE_action 
            actions[48] = self.STR_LIT_action 
            actions[52] = self.UNCLOSE_STRING_action 
            actions[53] = self.ILLEGAL_ESCAPE_action 
            actions[54] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = '\n'
     

    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	if (len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
            		raise UncloseString(self.text[1:-2])
            	elif (self.text[-1] == '\n'):
            		raise UncloseString(self.text[1:-1])
            	else:
            		raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     


