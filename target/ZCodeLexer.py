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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\64")
        buf.write("\u017d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3$")
        buf.write("\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3*\3*\3+")
        buf.write("\3+\3+\3+\3+\3+\3,\3,\5,\u0115\n,\3,\5,\u0118\n,\3-\6")
        buf.write("-\u011b\n-\r-\16-\u011c\3.\3.\7.\u0121\n.\f.\16.\u0124")
        buf.write("\13.\3/\3/\5/\u0128\n/\3/\6/\u012b\n/\r/\16/\u012c\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\7\60\u0135\n\60\f\60\16\60\u0138")
        buf.write("\13\60\3\60\3\60\3\60\3\61\3\61\3\61\5\61\u0140\n\61\3")
        buf.write("\62\3\62\7\62\u0144\n\62\f\62\16\62\u0147\13\62\3\63\3")
        buf.write("\63\3\63\3\63\7\63\u014d\n\63\f\63\16\63\u0150\13\63\3")
        buf.write("\63\3\63\3\64\6\64\u0155\n\64\r\64\16\64\u0156\3\64\3")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u0161\n\65\f\65")
        buf.write("\16\65\u0164\13\65\3\65\3\65\3\65\5\65\u0169\n\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\66\3\66\3\66\7\66\u0173\n\66\f")
        buf.write("\66\16\66\u0176\13\66\3\66\3\66\3\66\3\67\3\67\3\67\2")
        buf.write("\28\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y\2[\2]\2_.a\2c/e\60g\61i\62k\63m\64\3\2\17")
        buf.write("\3\2\62;\3\2\60\60\4\2GGgg\4\2--//\3\2$$\6\2\f\f\16\17")
        buf.write("$$^^\t\2))^^ddhhppttvv\3\2\16\17\5\2C\\aac|\6\2\62;C\\")
        buf.write("aac|\4\2\f\f\16\17\5\2\n\13\16\17\"\"\3\3\f\f\2\u018c")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2_\3\2\2\2\2c\3\2\2\2\2e\3\2")
        buf.write("\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\3o\3")
        buf.write("\2\2\2\5v\3\2\2\2\7{\3\2\2\2\t\u0082\3\2\2\2\13\u0089")
        buf.write("\3\2\2\2\r\u008d\3\2\2\2\17\u0095\3\2\2\2\21\u009a\3\2")
        buf.write("\2\2\23\u009e\3\2\2\2\25\u00a4\3\2\2\2\27\u00a7\3\2\2")
        buf.write("\2\31\u00ad\3\2\2\2\33\u00b6\3\2\2\2\35\u00b9\3\2\2\2")
        buf.write("\37\u00be\3\2\2\2!\u00c3\3\2\2\2#\u00c9\3\2\2\2%\u00cd")
        buf.write("\3\2\2\2\'\u00d1\3\2\2\2)\u00d5\3\2\2\2+\u00d8\3\2\2\2")
        buf.write("-\u00da\3\2\2\2/\u00dc\3\2\2\2\61\u00de\3\2\2\2\63\u00e0")
        buf.write("\3\2\2\2\65\u00e2\3\2\2\2\67\u00e4\3\2\2\29\u00e7\3\2")
        buf.write("\2\2;\u00ea\3\2\2\2=\u00ec\3\2\2\2?\u00ef\3\2\2\2A\u00f1")
        buf.write("\3\2\2\2C\u00f4\3\2\2\2E\u00f8\3\2\2\2G\u00fb\3\2\2\2")
        buf.write("I\u00fd\3\2\2\2K\u00ff\3\2\2\2M\u0101\3\2\2\2O\u0103\3")
        buf.write("\2\2\2Q\u0105\3\2\2\2S\u0107\3\2\2\2U\u010c\3\2\2\2W\u0112")
        buf.write("\3\2\2\2Y\u011a\3\2\2\2[\u011e\3\2\2\2]\u0125\3\2\2\2")
        buf.write("_\u012e\3\2\2\2a\u013f\3\2\2\2c\u0141\3\2\2\2e\u0148\3")
        buf.write("\2\2\2g\u0154\3\2\2\2i\u015a\3\2\2\2k\u016c\3\2\2\2m\u017a")
        buf.write("\3\2\2\2op\7p\2\2pq\7w\2\2qr\7o\2\2rs\7d\2\2st\7g\2\2")
        buf.write("tu\7t\2\2u\4\3\2\2\2vw\7d\2\2wx\7q\2\2xy\7q\2\2yz\7n\2")
        buf.write("\2z\6\3\2\2\2{|\7u\2\2|}\7v\2\2}~\7t\2\2~\177\7k\2\2\177")
        buf.write("\u0080\7p\2\2\u0080\u0081\7i\2\2\u0081\b\3\2\2\2\u0082")
        buf.write("\u0083\7t\2\2\u0083\u0084\7g\2\2\u0084\u0085\7v\2\2\u0085")
        buf.write("\u0086\7w\2\2\u0086\u0087\7t\2\2\u0087\u0088\7p\2\2\u0088")
        buf.write("\n\3\2\2\2\u0089\u008a\7x\2\2\u008a\u008b\7c\2\2\u008b")
        buf.write("\u008c\7t\2\2\u008c\f\3\2\2\2\u008d\u008e\7f\2\2\u008e")
        buf.write("\u008f\7{\2\2\u008f\u0090\7p\2\2\u0090\u0091\7c\2\2\u0091")
        buf.write("\u0092\7o\2\2\u0092\u0093\7k\2\2\u0093\u0094\7e\2\2\u0094")
        buf.write("\16\3\2\2\2\u0095\u0096\7h\2\2\u0096\u0097\7w\2\2\u0097")
        buf.write("\u0098\7p\2\2\u0098\u0099\7e\2\2\u0099\20\3\2\2\2\u009a")
        buf.write("\u009b\7h\2\2\u009b\u009c\7q\2\2\u009c\u009d\7t\2\2\u009d")
        buf.write("\22\3\2\2\2\u009e\u009f\7w\2\2\u009f\u00a0\7p\2\2\u00a0")
        buf.write("\u00a1\7v\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7n\2\2\u00a3")
        buf.write("\24\3\2\2\2\u00a4\u00a5\7d\2\2\u00a5\u00a6\7{\2\2\u00a6")
        buf.write("\26\3\2\2\2\u00a7\u00a8\7d\2\2\u00a8\u00a9\7t\2\2\u00a9")
        buf.write("\u00aa\7g\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7m\2\2\u00ac")
        buf.write("\30\3\2\2\2\u00ad\u00ae\7e\2\2\u00ae\u00af\7q\2\2\u00af")
        buf.write("\u00b0\7p\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7k\2\2\u00b2")
        buf.write("\u00b3\7p\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7g\2\2\u00b5")
        buf.write("\32\3\2\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7h\2\2\u00b8")
        buf.write("\34\3\2\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7n\2\2\u00bb")
        buf.write("\u00bc\7u\2\2\u00bc\u00bd\7g\2\2\u00bd\36\3\2\2\2\u00be")
        buf.write("\u00bf\7g\2\2\u00bf\u00c0\7n\2\2\u00c0\u00c1\7k\2\2\u00c1")
        buf.write("\u00c2\7h\2\2\u00c2 \3\2\2\2\u00c3\u00c4\7d\2\2\u00c4")
        buf.write("\u00c5\7g\2\2\u00c5\u00c6\7i\2\2\u00c6\u00c7\7k\2\2\u00c7")
        buf.write("\u00c8\7p\2\2\u00c8\"\3\2\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\u00cb\7p\2\2\u00cb\u00cc\7f\2\2\u00cc$\3\2\2\2\u00cd")
        buf.write("\u00ce\7p\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0\7v\2\2\u00d0")
        buf.write("&\3\2\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7p\2\2\u00d3")
        buf.write("\u00d4\7f\2\2\u00d4(\3\2\2\2\u00d5\u00d6\7q\2\2\u00d6")
        buf.write("\u00d7\7t\2\2\u00d7*\3\2\2\2\u00d8\u00d9\7-\2\2\u00d9")
        buf.write(",\3\2\2\2\u00da\u00db\7/\2\2\u00db.\3\2\2\2\u00dc\u00dd")
        buf.write("\7,\2\2\u00dd\60\3\2\2\2\u00de\u00df\7\61\2\2\u00df\62")
        buf.write("\3\2\2\2\u00e0\u00e1\7\'\2\2\u00e1\64\3\2\2\2\u00e2\u00e3")
        buf.write("\7?\2\2\u00e3\66\3\2\2\2\u00e4\u00e5\7>\2\2\u00e5\u00e6")
        buf.write("\7/\2\2\u00e68\3\2\2\2\u00e7\u00e8\7#\2\2\u00e8\u00e9")
        buf.write("\7?\2\2\u00e9:\3\2\2\2\u00ea\u00eb\7>\2\2\u00eb<\3\2\2")
        buf.write("\2\u00ec\u00ed\7>\2\2\u00ed\u00ee\7?\2\2\u00ee>\3\2\2")
        buf.write("\2\u00ef\u00f0\7@\2\2\u00f0@\3\2\2\2\u00f1\u00f2\7@\2")
        buf.write("\2\u00f2\u00f3\7?\2\2\u00f3B\3\2\2\2\u00f4\u00f5\7\60")
        buf.write("\2\2\u00f5\u00f6\7\60\2\2\u00f6\u00f7\7\60\2\2\u00f7D")
        buf.write("\3\2\2\2\u00f8\u00f9\7?\2\2\u00f9\u00fa\7?\2\2\u00faF")
        buf.write("\3\2\2\2\u00fb\u00fc\7*\2\2\u00fcH\3\2\2\2\u00fd\u00fe")
        buf.write("\7+\2\2\u00feJ\3\2\2\2\u00ff\u0100\7]\2\2\u0100L\3\2\2")
        buf.write("\2\u0101\u0102\7_\2\2\u0102N\3\2\2\2\u0103\u0104\7.\2")
        buf.write("\2\u0104P\3\2\2\2\u0105\u0106\7\f\2\2\u0106R\3\2\2\2\u0107")
        buf.write("\u0108\7v\2\2\u0108\u0109\7t\2\2\u0109\u010a\7w\2\2\u010a")
        buf.write("\u010b\7g\2\2\u010bT\3\2\2\2\u010c\u010d\7h\2\2\u010d")
        buf.write("\u010e\7c\2\2\u010e\u010f\7n\2\2\u010f\u0110\7u\2\2\u0110")
        buf.write("\u0111\7g\2\2\u0111V\3\2\2\2\u0112\u0114\5Y-\2\u0113\u0115")
        buf.write("\5[.\2\u0114\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117")
        buf.write("\3\2\2\2\u0116\u0118\5]/\2\u0117\u0116\3\2\2\2\u0117\u0118")
        buf.write("\3\2\2\2\u0118X\3\2\2\2\u0119\u011b\t\2\2\2\u011a\u0119")
        buf.write("\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011a\3\2\2\2\u011c")
        buf.write("\u011d\3\2\2\2\u011dZ\3\2\2\2\u011e\u0122\t\3\2\2\u011f")
        buf.write("\u0121\t\2\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2")
        buf.write("\u0122\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\\\3\2\2")
        buf.write("\2\u0124\u0122\3\2\2\2\u0125\u0127\t\4\2\2\u0126\u0128")
        buf.write("\t\5\2\2\u0127\u0126\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u012a\3\2\2\2\u0129\u012b\t\2\2\2\u012a\u0129\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3")
        buf.write("\2\2\2\u012d^\3\2\2\2\u012e\u0136\t\6\2\2\u012f\u0135")
        buf.write("\n\7\2\2\u0130\u0131\7^\2\2\u0131\u0135\t\b\2\2\u0132")
        buf.write("\u0133\7)\2\2\u0133\u0135\7$\2\2\u0134\u012f\3\2\2\2\u0134")
        buf.write("\u0130\3\2\2\2\u0134\u0132\3\2\2\2\u0135\u0138\3\2\2\2")
        buf.write("\u0136\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139\3")
        buf.write("\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a\t\6\2\2\u013a\u013b")
        buf.write("\b\60\2\2\u013b`\3\2\2\2\u013c\u0140\t\t\2\2\u013d\u013e")
        buf.write("\7^\2\2\u013e\u0140\n\b\2\2\u013f\u013c\3\2\2\2\u013f")
        buf.write("\u013d\3\2\2\2\u0140b\3\2\2\2\u0141\u0145\t\n\2\2\u0142")
        buf.write("\u0144\t\13\2\2\u0143\u0142\3\2\2\2\u0144\u0147\3\2\2")
        buf.write("\2\u0145\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146d\3\2")
        buf.write("\2\2\u0147\u0145\3\2\2\2\u0148\u0149\7%\2\2\u0149\u014a")
        buf.write("\7%\2\2\u014a\u014e\3\2\2\2\u014b\u014d\n\f\2\2\u014c")
        buf.write("\u014b\3\2\2\2\u014d\u0150\3\2\2\2\u014e\u014c\3\2\2\2")
        buf.write("\u014e\u014f\3\2\2\2\u014f\u0151\3\2\2\2\u0150\u014e\3")
        buf.write("\2\2\2\u0151\u0152\b\63\3\2\u0152f\3\2\2\2\u0153\u0155")
        buf.write("\t\r\2\2\u0154\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\3\2\2\2")
        buf.write("\u0158\u0159\b\64\3\2\u0159h\3\2\2\2\u015a\u0162\t\6\2")
        buf.write("\2\u015b\u0161\n\7\2\2\u015c\u015d\7^\2\2\u015d\u0161")
        buf.write("\t\b\2\2\u015e\u015f\7)\2\2\u015f\u0161\7$\2\2\u0160\u015b")
        buf.write("\3\2\2\2\u0160\u015c\3\2\2\2\u0160\u015e\3\2\2\2\u0161")
        buf.write("\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162\u0163\3\2\2\2")
        buf.write("\u0163\u0168\3\2\2\2\u0164\u0162\3\2\2\2\u0165\u0166\7")
        buf.write("\17\2\2\u0166\u0169\7\f\2\2\u0167\u0169\t\16\2\2\u0168")
        buf.write("\u0165\3\2\2\2\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2")
        buf.write("\u016a\u016b\b\65\4\2\u016bj\3\2\2\2\u016c\u0174\t\6\2")
        buf.write("\2\u016d\u0173\n\7\2\2\u016e\u016f\7^\2\2\u016f\u0173")
        buf.write("\t\b\2\2\u0170\u0171\7)\2\2\u0171\u0173\7$\2\2\u0172\u016d")
        buf.write("\3\2\2\2\u0172\u016e\3\2\2\2\u0172\u0170\3\2\2\2\u0173")
        buf.write("\u0176\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2")
        buf.write("\u0175\u0177\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\5")
        buf.write("a\61\2\u0178\u0179\b\66\5\2\u0179l\3\2\2\2\u017a\u017b")
        buf.write("\13\2\2\2\u017b\u017c\b\67\6\2\u017cn\3\2\2\2\24\2\u0114")
        buf.write("\u0117\u011c\u0122\u0127\u012c\u0134\u0136\u013f\u0145")
        buf.write("\u014e\u0156\u0160\u0162\u0168\u0172\u0174\7\3\60\2\b")
        buf.write("\2\2\3\65\3\3\66\4\3\67\5")
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
    TRUE = 41
    FALSE = 42
    NUM_LIT = 43
    STR_LIT = 44
    ID = 45
    COMMENT = 46
    WS = 47
    UNCLOSE_STRING = 48
    ILLEGAL_ESCAPE = 49
    ERROR_CHAR = 50

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'number'", "'bool'", "'string'", "'return'", "'var'", "'dynamic'", 
            "'func'", "'for'", "'until'", "'by'", "'break'", "'continue'", 
            "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", "'and'", 
            "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", "')'", 
            "'['", "']'", "','", "'\n'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
            "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", 
            "BEGIN", "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "EQ_STR", "ASSIGN", "DIFFER", "LT", "LE", "GT", 
            "GE", "CONCAT", "EQ_NUM", "LP", "RP", "LS", "RS", "COMMA", "NEWLINE", 
            "TRUE", "FALSE", "NUM_LIT", "STR_LIT", "ID", "COMMENT", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "NUMBER", "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", 
                  "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", 
                  "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "PLUS", 
                  "MINUS", "MUL", "DIV", "MOD", "EQ_STR", "ASSIGN", "DIFFER", 
                  "LT", "LE", "GT", "GE", "CONCAT", "EQ_NUM", "LP", "RP", 
                  "LS", "RS", "COMMA", "NEWLINE", "TRUE", "FALSE", "NUM_LIT", 
                  "INT_PART", "DEC_PART", "EXP_PART", "STR_LIT", "ILL_ESC_CHAR", 
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
            actions[46] = self.STR_LIT_action 
            actions[51] = self.UNCLOSE_STRING_action 
            actions[52] = self.ILLEGAL_ESCAPE_action 
            actions[53] = self.ERROR_CHAR_action 
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
     


