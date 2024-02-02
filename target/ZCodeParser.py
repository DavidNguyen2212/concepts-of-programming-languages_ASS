# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u01c5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3l\n\3\3\4\3\4\5\4p\n\4\3\5\6\5s\n\5\r\5\16\5")
        buf.write("t\3\6\3\6\3\6\5\6z\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\5\7\u0084\n\7\3\7\3\7\5\7\u0088\n\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\t\5\t\u0093\n\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u009b\n\n\3\n\3\n\5\n\u009f\n\n\3\n\3\n\5\n\u00a3")
        buf.write("\n\n\3\13\3\13\5\13\u00a7\n\13\3\f\3\f\3\f\3\f\3\f\5\f")
        buf.write("\u00ae\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b6\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u00c1\n")
        buf.write("\17\3\20\3\20\5\20\u00c5\n\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\5\21")
        buf.write("\u00d6\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\5")
        buf.write("\23\u00e0\n\23\3\24\3\24\3\24\3\24\5\24\u00e6\n\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u00ed\n\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u00f5\n\25\3\25\3\25\7\25\u00f9\n\25")
        buf.write("\f\25\16\25\u00fc\13\25\3\25\3\25\5\25\u0100\n\25\3\25")
        buf.write("\5\25\u0103\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5")
        buf.write("\26\u010c\n\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u0116\n\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u0121\n\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\5\33\u012b\n\33\3\33\3\33\3\34\3\34\3\34\5")
        buf.write("\34\u0132\n\34\3\34\3\34\5\34\u0136\n\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u013d\n\35\3\36\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u0144\n\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u014c")
        buf.write("\n\37\f\37\16\37\u014f\13\37\3 \3 \3 \3 \3 \3 \7 \u0157")
        buf.write("\n \f \16 \u015a\13 \3!\3!\3!\3!\3!\3!\7!\u0162\n!\f!")
        buf.write("\16!\u0165\13!\3\"\3\"\3\"\5\"\u016a\n\"\3#\3#\3#\5#\u016f")
        buf.write("\n#\3$\3$\3$\3$\5$\u0175\n$\3$\5$\u0178\n$\3$\3$\3$\3")
        buf.write("$\3$\5$\u017f\n$\3%\3%\3%\3%\3%\3%\3%\5%\u0188\n%\3&\3")
        buf.write("&\3&\3&\5&\u018e\n&\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\5)\u019c\n)\3*\3*\3*\3*\3+\3+\3+\3+\3+\5+\u01a7\n")
        buf.write("+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\5-\u01b4\n-\3-\3-\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\5/\u01c1\n/\3/\3/\3/\2\5<>@")
        buf.write("\60\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\\2\7\5\2!!#\'))\3\2\32\33")
        buf.write("\3\2\34\35\3\2\36 \3\2\b\n\2\u01d8\2a\3\2\2\2\4k\3\2\2")
        buf.write("\2\6o\3\2\2\2\br\3\2\2\2\ny\3\2\2\2\f\u0083\3\2\2\2\16")
        buf.write("\u0089\3\2\2\2\20\u008e\3\2\2\2\22\u0094\3\2\2\2\24\u00a6")
        buf.write("\3\2\2\2\26\u00ad\3\2\2\2\30\u00b5\3\2\2\2\32\u00b7\3")
        buf.write("\2\2\2\34\u00c0\3\2\2\2\36\u00c4\3\2\2\2 \u00d5\3\2\2")
        buf.write("\2\"\u00d7\3\2\2\2$\u00df\3\2\2\2&\u00e5\3\2\2\2(\u00e7")
        buf.write("\3\2\2\2*\u0104\3\2\2\2,\u0115\3\2\2\2.\u0120\3\2\2\2")
        buf.write("\60\u0122\3\2\2\2\62\u0125\3\2\2\2\64\u0128\3\2\2\2\66")
        buf.write("\u0135\3\2\2\28\u013c\3\2\2\2:\u0143\3\2\2\2<\u0145\3")
        buf.write("\2\2\2>\u0150\3\2\2\2@\u015b\3\2\2\2B\u0169\3\2\2\2D\u016e")
        buf.write("\3\2\2\2F\u017e\3\2\2\2H\u0187\3\2\2\2J\u018d\3\2\2\2")
        buf.write("L\u018f\3\2\2\2N\u0191\3\2\2\2P\u019b\3\2\2\2R\u019d\3")
        buf.write("\2\2\2T\u01a1\3\2\2\2V\u01aa\3\2\2\2X\u01ae\3\2\2\2Z\u01b7")
        buf.write("\3\2\2\2\\\u01bb\3\2\2\2^`\7/\2\2_^\3\2\2\2`c\3\2\2\2")
        buf.write("a_\3\2\2\2ab\3\2\2\2bd\3\2\2\2ca\3\2\2\2de\5\4\3\2ef\7")
        buf.write("\2\2\3f\3\3\2\2\2gh\5\6\4\2hi\5\4\3\2il\3\2\2\2jl\5\6")
        buf.write("\4\2kg\3\2\2\2kj\3\2\2\2l\5\3\2\2\2mp\5\n\6\2np\5\22\n")
        buf.write("\2om\3\2\2\2on\3\2\2\2p\7\3\2\2\2qs\7/\2\2rq\3\2\2\2s")
        buf.write("t\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\t\3\2\2\2vz\5\f\7\2wz\5")
        buf.write("\16\b\2xz\5\20\t\2yv\3\2\2\2yw\3\2\2\2yx\3\2\2\2z{\3\2")
        buf.write("\2\2{|\5\b\5\2|\13\3\2\2\2}~\5L\'\2~\177\7\60\2\2\177")
        buf.write("\u0084\3\2\2\2\u0080\u0081\5L\'\2\u0081\u0082\5\32\16")
        buf.write("\2\u0082\u0084\3\2\2\2\u0083}\3\2\2\2\u0083\u0080\3\2")
        buf.write("\2\2\u0084\u0087\3\2\2\2\u0085\u0086\7\"\2\2\u0086\u0088")
        buf.write("\58\35\2\u0087\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088")
        buf.write("\r\3\2\2\2\u0089\u008a\7\f\2\2\u008a\u008b\7\60\2\2\u008b")
        buf.write("\u008c\7\"\2\2\u008c\u008d\58\35\2\u008d\17\3\2\2\2\u008e")
        buf.write("\u008f\7\r\2\2\u008f\u0092\7\60\2\2\u0090\u0091\7\"\2")
        buf.write("\2\u0091\u0093\58\35\2\u0092\u0090\3\2\2\2\u0092\u0093")
        buf.write("\3\2\2\2\u0093\21\3\2\2\2\u0094\u0095\7\16\2\2\u0095\u0096")
        buf.write("\7\60\2\2\u0096\u0097\7*\2\2\u0097\u0098\5\24\13\2\u0098")
        buf.write("\u00a2\7+\2\2\u0099\u009b\5\b\5\2\u009a\u0099\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u00a3\5")
        buf.write("\"\22\2\u009d\u009f\5\b\5\2\u009e\u009d\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\u00a3\5\64\33")
        buf.write("\2\u00a1\u00a3\5\b\5\2\u00a2\u009a\3\2\2\2\u00a2\u009e")
        buf.write("\3\2\2\2\u00a2\u00a1\3\2\2\2\u00a3\23\3\2\2\2\u00a4\u00a7")
        buf.write("\5\26\f\2\u00a5\u00a7\3\2\2\2\u00a6\u00a4\3\2\2\2\u00a6")
        buf.write("\u00a5\3\2\2\2\u00a7\25\3\2\2\2\u00a8\u00a9\5\30\r\2\u00a9")
        buf.write("\u00aa\7.\2\2\u00aa\u00ab\5\26\f\2\u00ab\u00ae\3\2\2\2")
        buf.write("\u00ac\u00ae\5\30\r\2\u00ad\u00a8\3\2\2\2\u00ad\u00ac")
        buf.write("\3\2\2\2\u00ae\27\3\2\2\2\u00af\u00b0\5L\'\2\u00b0\u00b1")
        buf.write("\7\60\2\2\u00b1\u00b6\3\2\2\2\u00b2\u00b3\5L\'\2\u00b3")
        buf.write("\u00b4\5\32\16\2\u00b4\u00b6\3\2\2\2\u00b5\u00af\3\2\2")
        buf.write("\2\u00b5\u00b2\3\2\2\2\u00b6\31\3\2\2\2\u00b7\u00b8\7")
        buf.write("\60\2\2\u00b8\u00b9\7,\2\2\u00b9\u00ba\5\34\17\2\u00ba")
        buf.write("\u00bb\7-\2\2\u00bb\33\3\2\2\2\u00bc\u00bd\7\64\2\2\u00bd")
        buf.write("\u00be\7.\2\2\u00be\u00c1\5\34\17\2\u00bf\u00c1\7\64\2")
        buf.write("\2\u00c0\u00bc\3\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\35\3")
        buf.write("\2\2\2\u00c2\u00c5\7\60\2\2\u00c3\u00c5\5\66\34\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2")
        buf.write("\u00c6\u00c7\7,\2\2\u00c7\u00c8\5.\30\2\u00c8\u00c9\7")
        buf.write("-\2\2\u00c9\37\3\2\2\2\u00ca\u00d6\5\"\22\2\u00cb\u00d6")
        buf.write("\5(\25\2\u00cc\u00d6\5*\26\2\u00cd\u00d6\5,\27\2\u00ce")
        buf.write("\u00d6\5\60\31\2\u00cf\u00d6\5\62\32\2\u00d0\u00d6\5\64")
        buf.write("\33\2\u00d1\u00d2\5\66\34\2\u00d2\u00d3\5\b\5\2\u00d3")
        buf.write("\u00d6\3\2\2\2\u00d4\u00d6\5\n\6\2\u00d5\u00ca\3\2\2\2")
        buf.write("\u00d5\u00cb\3\2\2\2\u00d5\u00cc\3\2\2\2\u00d5\u00cd\3")
        buf.write("\2\2\2\u00d5\u00ce\3\2\2\2\u00d5\u00cf\3\2\2\2\u00d5\u00d0")
        buf.write("\3\2\2\2\u00d5\u00d1\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6")
        buf.write("!\3\2\2\2\u00d7\u00d8\7\27\2\2\u00d8\u00d9\5\b\5\2\u00d9")
        buf.write("\u00da\5$\23\2\u00da\u00db\7\30\2\2\u00db\u00dc\5\b\5")
        buf.write("\2\u00dc#\3\2\2\2\u00dd\u00e0\5&\24\2\u00de\u00e0\3\2")
        buf.write("\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0%\3")
        buf.write("\2\2\2\u00e1\u00e2\5 \21\2\u00e2\u00e3\5&\24\2\u00e3\u00e6")
        buf.write("\3\2\2\2\u00e4\u00e6\5 \21\2\u00e5\u00e1\3\2\2\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e6\'\3\2\2\2\u00e7\u00e8\7\24\2\2\u00e8")
        buf.write("\u00e9\7*\2\2\u00e9\u00ea\58\35\2\u00ea\u00ec\7+\2\2\u00eb")
        buf.write("\u00ed\5\b\5\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00fa\5 \21\2\u00ef\u00f0\7")
        buf.write("\26\2\2\u00f0\u00f1\7*\2\2\u00f1\u00f2\58\35\2\u00f2\u00f4")
        buf.write("\7+\2\2\u00f3\u00f5\5\b\5\2\u00f4\u00f3\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f7\5 \21\2")
        buf.write("\u00f7\u00f9\3\2\2\2\u00f8\u00ef\3\2\2\2\u00f9\u00fc\3")
        buf.write("\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u0102")
        buf.write("\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fd\u00ff\7\25\2\2\u00fe")
        buf.write("\u0100\5\b\5\2\u00ff\u00fe\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0101\3\2\2\2\u0101\u0103\5 \21\2\u0102\u00fd\3")
        buf.write("\2\2\2\u0102\u0103\3\2\2\2\u0103)\3\2\2\2\u0104\u0105")
        buf.write("\7\17\2\2\u0105\u0106\7\60\2\2\u0106\u0107\7\20\2\2\u0107")
        buf.write("\u0108\58\35\2\u0108\u0109\7\21\2\2\u0109\u010b\58\35")
        buf.write("\2\u010a\u010c\5\b\5\2\u010b\u010a\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010e\5 \21\2\u010e")
        buf.write("+\3\2\2\2\u010f\u0116\7\60\2\2\u0110\u0111\7\60\2\2\u0111")
        buf.write("\u0112\7,\2\2\u0112\u0113\5.\30\2\u0113\u0114\7-\2\2\u0114")
        buf.write("\u0116\3\2\2\2\u0115\u010f\3\2\2\2\u0115\u0110\3\2\2\2")
        buf.write("\u0116\u0117\3\2\2\2\u0117\u0118\7\"\2\2\u0118\u0119\5")
        buf.write("8\35\2\u0119\u011a\5\b\5\2\u011a-\3\2\2\2\u011b\u0121")
        buf.write("\58\35\2\u011c\u011d\58\35\2\u011d\u011e\7.\2\2\u011e")
        buf.write("\u011f\5.\30\2\u011f\u0121\3\2\2\2\u0120\u011b\3\2\2\2")
        buf.write("\u0120\u011c\3\2\2\2\u0121/\3\2\2\2\u0122\u0123\7\23\2")
        buf.write("\2\u0123\u0124\5\b\5\2\u0124\61\3\2\2\2\u0125\u0126\7")
        buf.write("\22\2\2\u0126\u0127\5\b\5\2\u0127\63\3\2\2\2\u0128\u012a")
        buf.write("\7\13\2\2\u0129\u012b\58\35\2\u012a\u0129\3\2\2\2\u012a")
        buf.write("\u012b\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\5\b\5\2")
        buf.write("\u012d\65\3\2\2\2\u012e\u012f\7\60\2\2\u012f\u0131\7*")
        buf.write("\2\2\u0130\u0132\5.\30\2\u0131\u0130\3\2\2\2\u0131\u0132")
        buf.write("\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0136\7+\2\2\u0134")
        buf.write("\u0136\5P)\2\u0135\u012e\3\2\2\2\u0135\u0134\3\2\2\2\u0136")
        buf.write("\67\3\2\2\2\u0137\u0138\5:\36\2\u0138\u0139\7(\2\2\u0139")
        buf.write("\u013a\5:\36\2\u013a\u013d\3\2\2\2\u013b\u013d\5:\36\2")
        buf.write("\u013c\u0137\3\2\2\2\u013c\u013b\3\2\2\2\u013d9\3\2\2")
        buf.write("\2\u013e\u013f\5<\37\2\u013f\u0140\t\2\2\2\u0140\u0141")
        buf.write("\5<\37\2\u0141\u0144\3\2\2\2\u0142\u0144\5<\37\2\u0143")
        buf.write("\u013e\3\2\2\2\u0143\u0142\3\2\2\2\u0144;\3\2\2\2\u0145")
        buf.write("\u0146\b\37\1\2\u0146\u0147\5> \2\u0147\u014d\3\2\2\2")
        buf.write("\u0148\u0149\f\4\2\2\u0149\u014a\t\3\2\2\u014a\u014c\5")
        buf.write("> \2\u014b\u0148\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014e=\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u0150\u0151\b \1\2\u0151\u0152\5@!\2\u0152\u0158")
        buf.write("\3\2\2\2\u0153\u0154\f\4\2\2\u0154\u0155\t\4\2\2\u0155")
        buf.write("\u0157\5@!\2\u0156\u0153\3\2\2\2\u0157\u015a\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159?\3\2\2\2\u015a")
        buf.write("\u0158\3\2\2\2\u015b\u015c\b!\1\2\u015c\u015d\5B\"\2\u015d")
        buf.write("\u0163\3\2\2\2\u015e\u015f\f\4\2\2\u015f\u0160\t\5\2\2")
        buf.write("\u0160\u0162\5B\"\2\u0161\u015e\3\2\2\2\u0162\u0165\3")
        buf.write("\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164A")
        buf.write("\3\2\2\2\u0165\u0163\3\2\2\2\u0166\u0167\7\31\2\2\u0167")
        buf.write("\u016a\5B\"\2\u0168\u016a\5D#\2\u0169\u0166\3\2\2\2\u0169")
        buf.write("\u0168\3\2\2\2\u016aC\3\2\2\2\u016b\u016c\7\35\2\2\u016c")
        buf.write("\u016f\5D#\2\u016d\u016f\5F$\2\u016e\u016b\3\2\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016fE\3\2\2\2\u0170\u0178\7\60\2\2\u0171")
        buf.write("\u0172\7\60\2\2\u0172\u0174\7*\2\2\u0173\u0175\5.\30\2")
        buf.write("\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u0178\7+\2\2\u0177\u0170\3\2\2\2\u0177\u0171")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\7,\2\2\u017a")
        buf.write("\u017b\5.\30\2\u017b\u017c\7-\2\2\u017c\u017f\3\2\2\2")
        buf.write("\u017d\u017f\5H%\2\u017e\u0177\3\2\2\2\u017e\u017d\3\2")
        buf.write("\2\2\u017fG\3\2\2\2\u0180\u0188\5J&\2\u0181\u0182\7*\2")
        buf.write("\2\u0182\u0183\58\35\2\u0183\u0184\7+\2\2\u0184\u0188")
        buf.write("\3\2\2\2\u0185\u0188\7\60\2\2\u0186\u0188\5\66\34\2\u0187")
        buf.write("\u0180\3\2\2\2\u0187\u0181\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0186\3\2\2\2\u0188I\3\2\2\2\u0189\u018e\5N(\2")
        buf.write("\u018a\u018e\7\64\2\2\u018b\u018e\7\61\2\2\u018c\u018e")
        buf.write("\7\65\2\2\u018d\u0189\3\2\2\2\u018d\u018a\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018d\u018c\3\2\2\2\u018eK\3\2\2\2\u018f")
        buf.write("\u0190\t\6\2\2\u0190M\3\2\2\2\u0191\u0192\7,\2\2\u0192")
        buf.write("\u0193\5.\30\2\u0193\u0194\7-\2\2\u0194O\3\2\2\2\u0195")
        buf.write("\u019c\5R*\2\u0196\u019c\5T+\2\u0197\u019c\5V,\2\u0198")
        buf.write("\u019c\5X-\2\u0199\u019c\5Z.\2\u019a\u019c\5\\/\2\u019b")
        buf.write("\u0195\3\2\2\2\u019b\u0196\3\2\2\2\u019b\u0197\3\2\2\2")
        buf.write("\u019b\u0198\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019a\3")
        buf.write("\2\2\2\u019cQ\3\2\2\2\u019d\u019e\7\3\2\2\u019e\u019f")
        buf.write("\7*\2\2\u019f\u01a0\7+\2\2\u01a0S\3\2\2\2\u01a1\u01a2")
        buf.write("\7\4\2\2\u01a2\u01a6\7*\2\2\u01a3\u01a7\7\60\2\2\u01a4")
        buf.write("\u01a7\5\36\20\2\u01a5\u01a7\7\64\2\2\u01a6\u01a3\3\2")
        buf.write("\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8")
        buf.write("\3\2\2\2\u01a8\u01a9\7+\2\2\u01a9U\3\2\2\2\u01aa\u01ab")
        buf.write("\7\5\2\2\u01ab\u01ac\7*\2\2\u01ac\u01ad\7+\2\2\u01adW")
        buf.write("\3\2\2\2\u01ae\u01af\7\4\2\2\u01af\u01b3\7*\2\2\u01b0")
        buf.write("\u01b4\7\60\2\2\u01b1\u01b4\5\36\20\2\u01b2\u01b4\7\61")
        buf.write("\2\2\u01b3\u01b0\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b2")
        buf.write("\3\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\7+\2\2\u01b6")
        buf.write("Y\3\2\2\2\u01b7\u01b8\7\6\2\2\u01b8\u01b9\7*\2\2\u01b9")
        buf.write("\u01ba\7+\2\2\u01ba[\3\2\2\2\u01bb\u01bc\7\7\2\2\u01bc")
        buf.write("\u01c0\7*\2\2\u01bd\u01c1\7\60\2\2\u01be\u01c1\5\36\20")
        buf.write("\2\u01bf\u01c1\7\65\2\2\u01c0\u01bd\3\2\2\2\u01c0\u01be")
        buf.write("\3\2\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2")
        buf.write("\u01c3\7+\2\2\u01c3]\3\2\2\2\60akoty\u0083\u0087\u0092")
        buf.write("\u009a\u009e\u00a2\u00a6\u00ad\u00b5\u00c0\u00c4\u00d5")
        buf.write("\u00df\u00e5\u00ec\u00f4\u00fa\u00ff\u0102\u010b\u0115")
        buf.write("\u0120\u012a\u0131\u0135\u013c\u0143\u014d\u0158\u0163")
        buf.write("\u0169\u016e\u0174\u0177\u017e\u0187\u018d\u019b\u01a6")
        buf.write("\u01b3\u01c0")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'readNumber'", "'writeNumber'", "'readBool'", 
                     "'readString'", "'writeString'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", 
                     "'...'", "'=='", "'('", "')'", "'['", "']'", "','", 
                     "'\n'", "<INVALID>", "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", 
                      "DIV", "MOD", "EQ_STR", "ASSIGN", "DIFFER", "LT", 
                      "LE", "GT", "GE", "CONCAT", "EQ_NUM", "LP", "RP", 
                      "LS", "RS", "COMMA", "NEWLINE", "ID", "BOO_LIT", "TRUE", 
                      "FALSE", "NUM_LIT", "STR_LIT", "COMMENT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_ignore = 3
    RULE_vars_decl = 4
    RULE_norm_decl = 5
    RULE_var_decl = 6
    RULE_dynamic_decl = 7
    RULE_funs_decl = 8
    RULE_formal_params = 9
    RULE_formal_pms_prm = 10
    RULE_formal_pm = 11
    RULE_array_type = 12
    RULE_dim_list = 13
    RULE_array_ele = 14
    RULE_stmt = 15
    RULE_block_stmt = 16
    RULE_stmtlist = 17
    RULE_stmtprime = 18
    RULE_if_stmt = 19
    RULE_for_stmt = 20
    RULE_assign_stmt = 21
    RULE_index_ops = 22
    RULE_continue_stmt = 23
    RULE_break_stmt = 24
    RULE_return_stmt = 25
    RULE_fun_call = 26
    RULE_exp = 27
    RULE_exp1 = 28
    RULE_exp2 = 29
    RULE_exp3 = 30
    RULE_exp4 = 31
    RULE_exp5 = 32
    RULE_exp6 = 33
    RULE_exp7 = 34
    RULE_exp8 = 35
    RULE_array_val = 36
    RULE_scalar_type = 37
    RULE_array_list = 38
    RULE_builtins_call = 39
    RULE_readNumber = 40
    RULE_writeNumber = 41
    RULE_readBool = 42
    RULE_writeBool = 43
    RULE_readString = 44
    RULE_writeString = 45

    ruleNames =  [ "program", "decl_list", "decl", "ignore", "vars_decl", 
                   "norm_decl", "var_decl", "dynamic_decl", "funs_decl", 
                   "formal_params", "formal_pms_prm", "formal_pm", "array_type", 
                   "dim_list", "array_ele", "stmt", "block_stmt", "stmtlist", 
                   "stmtprime", "if_stmt", "for_stmt", "assign_stmt", "index_ops", 
                   "continue_stmt", "break_stmt", "return_stmt", "fun_call", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "array_val", "scalar_type", "array_list", 
                   "builtins_call", "readNumber", "writeNumber", "readBool", 
                   "writeBool", "readString", "writeString" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    BOOL=7
    STRING=8
    RETURN=9
    VAR=10
    DYNAMIC=11
    FUNC=12
    FOR=13
    UNTIL=14
    BY=15
    BREAK=16
    CONTINUE=17
    IF=18
    ELSE=19
    ELIF=20
    BEGIN=21
    END=22
    NOT=23
    AND=24
    OR=25
    PLUS=26
    MINUS=27
    MUL=28
    DIV=29
    MOD=30
    EQ_STR=31
    ASSIGN=32
    DIFFER=33
    LT=34
    LE=35
    GT=36
    GE=37
    CONCAT=38
    EQ_NUM=39
    LP=40
    RP=41
    LS=42
    RS=43
    COMMA=44
    NEWLINE=45
    ID=46
    BOO_LIT=47
    TRUE=48
    FALSE=49
    NUM_LIT=50
    STR_LIT=51
    COMMENT=52
    WS=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55
    ERROR_CHAR=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 92
                self.match(ZCodeParser.NEWLINE)
                self.state = 97
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 98
            self.decl_list()
            self.state = 99
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self):
            return self.getTypedRuleContext(ZCodeParser.DeclContext,0)


        def decl_list(self):
            return self.getTypedRuleContext(ZCodeParser.Decl_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl_list" ):
                return visitor.visitDecl_list(self)
            else:
                return visitor.visitChildren(self)




    def decl_list(self):

        localctx = ZCodeParser.Decl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl_list)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.decl()
                self.state = 102
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vars_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Vars_declContext,0)


        def funs_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Funs_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ZCodeParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.vars_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.funs_decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_ignore

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnore" ):
                return visitor.visitIgnore(self)
            else:
                return visitor.visitChildren(self)




    def ignore(self):

        localctx = ZCodeParser.IgnoreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ignore)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 111
                self.match(ZCodeParser.NEWLINE)
                self.state = 114 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZCodeParser.NEWLINE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vars_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def norm_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Norm_declContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def dynamic_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Dynamic_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_vars_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars_decl" ):
                return visitor.visitVars_decl(self)
            else:
                return visitor.visitChildren(self)




    def vars_decl(self):

        localctx = ZCodeParser.Vars_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vars_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 116
                self.norm_decl()
                pass
            elif token in [ZCodeParser.VAR]:
                self.state = 117
                self.var_decl()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 118
                self.dynamic_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 121
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Norm_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_type(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_typeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Array_typeContext,0)


        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_norm_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNorm_decl" ):
                return visitor.visitNorm_decl(self)
            else:
                return visitor.visitChildren(self)




    def norm_decl(self):

        localctx = ZCodeParser.Norm_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_norm_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 123
                self.scalar_type()
                self.state = 124
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 126
                self.scalar_type()
                self.state = 127
                self.array_type()
                pass


            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 131
                self.match(ZCodeParser.ASSIGN)
                self.state = 132
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = ZCodeParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(ZCodeParser.VAR)
            self.state = 136
            self.match(ZCodeParser.ID)
            self.state = 137
            self.match(ZCodeParser.ASSIGN)
            self.state = 138
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dynamic_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamic_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDynamic_decl" ):
                return visitor.visitDynamic_decl(self)
            else:
                return visitor.visitChildren(self)




    def dynamic_decl(self):

        localctx = ZCodeParser.Dynamic_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dynamic_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ZCodeParser.DYNAMIC)
            self.state = 141
            self.match(ZCodeParser.ID)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 142
                self.match(ZCodeParser.ASSIGN)
                self.state = 143
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Funs_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def formal_params(self):
            return self.getTypedRuleContext(ZCodeParser.Formal_paramsContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_funs_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuns_decl" ):
                return visitor.visitFuns_decl(self)
            else:
                return visitor.visitChildren(self)




    def funs_decl(self):

        localctx = ZCodeParser.Funs_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funs_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(ZCodeParser.FUNC)
            self.state = 147
            self.match(ZCodeParser.ID)
            self.state = 148
            self.match(ZCodeParser.LP)
            self.state = 149
            self.formal_params()
            self.state = 150
            self.match(ZCodeParser.RP)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 151
                    self.ignore()


                self.state = 154
                self.block_stmt()
                pass

            elif la_ == 2:
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 155
                    self.ignore()


                self.state = 158
                self.return_stmt()
                pass

            elif la_ == 3:
                self.state = 159
                self.ignore()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_paramsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formal_pms_prm(self):
            return self.getTypedRuleContext(ZCodeParser.Formal_pms_prmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_formal_params

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal_params" ):
                return visitor.visitFormal_params(self)
            else:
                return visitor.visitChildren(self)




    def formal_params(self):

        localctx = ZCodeParser.Formal_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_formal_params)
        try:
            self.state = 164
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.formal_pms_prm()
                pass
            elif token in [ZCodeParser.RP]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_pms_prmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def formal_pm(self):
            return self.getTypedRuleContext(ZCodeParser.Formal_pmContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def formal_pms_prm(self):
            return self.getTypedRuleContext(ZCodeParser.Formal_pms_prmContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_formal_pms_prm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal_pms_prm" ):
                return visitor.visitFormal_pms_prm(self)
            else:
                return visitor.visitChildren(self)




    def formal_pms_prm(self):

        localctx = ZCodeParser.Formal_pms_prmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_formal_pms_prm)
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.formal_pm()
                self.state = 167
                self.match(ZCodeParser.COMMA)
                self.state = 168
                self.formal_pms_prm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
                self.formal_pm()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Formal_pmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_type(self):
            return self.getTypedRuleContext(ZCodeParser.Scalar_typeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Array_typeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_formal_pm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFormal_pm" ):
                return visitor.visitFormal_pm(self)
            else:
                return visitor.visitChildren(self)




    def formal_pm(self):

        localctx = ZCodeParser.Formal_pmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_formal_pm)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.scalar_type()
                self.state = 174
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.scalar_type()
                self.state = 177
                self.array_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def dim_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dim_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = ZCodeParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ZCodeParser.ID)
            self.state = 182
            self.match(ZCodeParser.LS)
            self.state = 183
            self.dim_list()
            self.state = 184
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dim_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def dim_list(self):
            return self.getTypedRuleContext(ZCodeParser.Dim_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dim_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDim_list" ):
                return visitor.visitDim_list(self)
            else:
                return visitor.visitChildren(self)




    def dim_list(self):

        localctx = ZCodeParser.Dim_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dim_list)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(ZCodeParser.NUM_LIT)
                self.state = 187
                self.match(ZCodeParser.COMMA)
                self.state = 188
                self.dim_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(ZCodeParser.NUM_LIT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def index_ops(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opsContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def fun_call(self):
            return self.getTypedRuleContext(ZCodeParser.Fun_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_ele" ):
                return visitor.visitArray_ele(self)
            else:
                return visitor.visitChildren(self)




    def array_ele(self):

        localctx = ZCodeParser.Array_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 192
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 193
                self.fun_call()
                pass


            self.state = 196
            self.match(ZCodeParser.LS)
            self.state = 197
            self.index_ops()
            self.state = 198
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Block_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.For_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Assign_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Continue_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Break_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(ZCodeParser.Return_stmtContext,0)


        def fun_call(self):
            return self.getTypedRuleContext(ZCodeParser.Fun_callContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def vars_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Vars_declContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = ZCodeParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 202
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 203
                self.assign_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 205
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 206
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 207
                self.fun_call()
                self.state = 208
                self.ignore()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 210
                self.vars_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def stmtlist(self):
            return self.getTypedRuleContext(ZCodeParser.StmtlistContext,0)


        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = ZCodeParser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(ZCodeParser.BEGIN)
            self.state = 214
            self.ignore()
            self.state = 215
            self.stmtlist()
            self.state = 216
            self.match(ZCodeParser.END)
            self.state = 217
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtlist" ):
                return visitor.visitStmtlist(self)
            else:
                return visitor.visitChildren(self)




    def stmtlist(self):

        localctx = ZCodeParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_stmtlist)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.stmtprime()
                pass
            elif token in [ZCodeParser.END]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtprimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def stmtprime(self):
            return self.getTypedRuleContext(ZCodeParser.StmtprimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_stmtprime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtprime" ):
                return visitor.visitStmtprime(self)
            else:
                return visitor.visitChildren(self)




    def stmtprime(self):

        localctx = ZCodeParser.StmtprimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stmtprime)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.stmt()
                self.state = 224
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.LP)
            else:
                return self.getToken(ZCodeParser.LP, i)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.RP)
            else:
                return self.getToken(ZCodeParser.RP, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StmtContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StmtContext,i)


        def ignore(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.IgnoreContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.IgnoreContext,i)


        def ELIF(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.ELIF)
            else:
                return self.getToken(ZCodeParser.ELIF, i)

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = ZCodeParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(ZCodeParser.IF)
            self.state = 230
            self.match(ZCodeParser.LP)
            self.state = 231
            self.exp()
            self.state = 232
            self.match(ZCodeParser.RP)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 233
                self.ignore()


            self.state = 236
            self.stmt()
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 237
                    self.match(ZCodeParser.ELIF)
                    self.state = 238
                    self.match(ZCodeParser.LP)
                    self.state = 239
                    self.exp()
                    self.state = 240
                    self.match(ZCodeParser.RP)
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZCodeParser.NEWLINE:
                        self.state = 241
                        self.ignore()


                    self.state = 244
                    self.stmt() 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 251
                self.match(ZCodeParser.ELSE)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 252
                    self.ignore()


                self.state = 255
                self.stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def stmt(self):
            return self.getTypedRuleContext(ZCodeParser.StmtContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = ZCodeParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(ZCodeParser.FOR)
            self.state = 259
            self.match(ZCodeParser.ID)
            self.state = 260
            self.match(ZCodeParser.UNTIL)
            self.state = 261
            self.exp()
            self.state = 262
            self.match(ZCodeParser.BY)
            self.state = 263
            self.exp()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 264
                self.ignore()


            self.state = 267
            self.stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZCodeParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def index_ops(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opsContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = ZCodeParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 269
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 270
                self.match(ZCodeParser.ID)
                self.state = 271
                self.match(ZCodeParser.LS)
                self.state = 272
                self.index_ops()
                self.state = 273
                self.match(ZCodeParser.RS)
                pass


            self.state = 277
            self.match(ZCodeParser.ASSIGN)
            self.state = 278
            self.exp()
            self.state = 279
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_opsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def index_ops(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_index_ops

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_ops" ):
                return visitor.visitIndex_ops(self)
            else:
                return visitor.visitChildren(self)




    def index_ops(self):

        localctx = ZCodeParser.Index_opsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_index_ops)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.exp()
                self.state = 283
                self.match(ZCodeParser.COMMA)
                self.state = 284
                self.index_ops()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = ZCodeParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(ZCodeParser.CONTINUE)
            self.state = 289
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = ZCodeParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(ZCodeParser.BREAK)
            self.state = 292
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = ZCodeParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(ZCodeParser.RETURN)
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.BOO_LIT) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                self.state = 295
                self.exp()


            self.state = 298
            self.ignore()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fun_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def index_ops(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opsContext,0)


        def builtins_call(self):
            return self.getTypedRuleContext(ZCodeParser.Builtins_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_fun_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFun_call" ):
                return visitor.visitFun_call(self)
            else:
                return visitor.visitChildren(self)




    def fun_call(self):

        localctx = ZCodeParser.Fun_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_fun_call)
        self._la = 0 # Token type
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(ZCodeParser.ID)
                self.state = 301
                self.match(ZCodeParser.LP)
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.BOO_LIT) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                    self.state = 302
                    self.index_ops()


                self.state = 305
                self.match(ZCodeParser.RP)
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.builtins_call()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp1Context,i)


        def CONCAT(self):
            return self.getToken(ZCodeParser.CONCAT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = ZCodeParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.exp1()
                self.state = 310
                self.match(ZCodeParser.CONCAT)
                self.state = 311
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.exp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Exp2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Exp2Context,i)


        def EQ_NUM(self):
            return self.getToken(ZCodeParser.EQ_NUM, 0)

        def EQ_STR(self):
            return self.getToken(ZCodeParser.EQ_STR, 0)

        def DIFFER(self):
            return self.getToken(ZCodeParser.DIFFER, 0)

        def LT(self):
            return self.getToken(ZCodeParser.LT, 0)

        def GT(self):
            return self.getToken(ZCodeParser.GT, 0)

        def LE(self):
            return self.getToken(ZCodeParser.LE, 0)

        def GE(self):
            return self.getToken(ZCodeParser.GE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)




    def exp1(self):

        localctx = ZCodeParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 321
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.exp2(0)
                self.state = 317
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ_STR) | (1 << ZCodeParser.DIFFER) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GE) | (1 << ZCodeParser.EQ_NUM))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 318
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(ZCodeParser.Exp2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 331
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 326
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 327
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 328
                    self.exp3(0) 
                self.state = 333
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(ZCodeParser.Exp3Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 337
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 338
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 339
                    self.exp4(0) 
                self.state = 344
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(ZCodeParser.Exp4Context,0)


        def MUL(self):
            return self.getToken(ZCodeParser.MUL, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 353
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 348
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 349
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 350
                    self.exp5() 
                self.state = 355
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(ZCodeParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = ZCodeParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp5)
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(ZCodeParser.NOT)
                self.state = 357
                self.exp5()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.MINUS, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.ID, ZCodeParser.BOO_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.exp6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def exp6(self):
            return self.getTypedRuleContext(ZCodeParser.Exp6Context,0)


        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)




    def exp6(self):

        localctx = ZCodeParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp6)
        try:
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.match(ZCodeParser.MINUS)
                self.state = 362
                self.exp6()
                pass
            elif token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.ID, ZCodeParser.BOO_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.exp7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def index_ops(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Index_opsContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Index_opsContext,i)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def exp8(self):
            return self.getTypedRuleContext(ZCodeParser.Exp8Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = ZCodeParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp7)
        self._la = 0 # Token type
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 366
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 367
                    self.match(ZCodeParser.ID)
                    self.state = 368
                    self.match(ZCodeParser.LP)
                    self.state = 370
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.T__0) | (1 << ZCodeParser.T__1) | (1 << ZCodeParser.T__2) | (1 << ZCodeParser.T__3) | (1 << ZCodeParser.T__4) | (1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.BOO_LIT) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                        self.state = 369
                        self.index_ops()


                    self.state = 372
                    self.match(ZCodeParser.RP)
                    pass


                self.state = 375
                self.match(ZCodeParser.LS)
                self.state = 376
                self.index_ops()
                self.state = 377
                self.match(ZCodeParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.exp8()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_val(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valContext,0)


        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def fun_call(self):
            return self.getTypedRuleContext(ZCodeParser.Fun_callContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp8" ):
                return visitor.visitExp8(self)
            else:
                return visitor.visitChildren(self)




    def exp8(self):

        localctx = ZCodeParser.Exp8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp8)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
                self.match(ZCodeParser.LP)
                self.state = 384
                self.exp()
                self.state = 385
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 387
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 388
                self.fun_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_listContext,0)


        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def BOO_LIT(self):
            return self.getToken(ZCodeParser.BOO_LIT, 0)

        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_val" ):
                return visitor.visitArray_val(self)
            else:
                return visitor.visitChildren(self)




    def array_val(self):

        localctx = ZCodeParser.Array_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_array_val)
        try:
            self.state = 395
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
                self.array_list()
                pass
            elif token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.BOO_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.match(ZCodeParser.BOO_LIT)
                pass
            elif token in [ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 394
                self.match(ZCodeParser.STR_LIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_scalar_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_type" ):
                return visitor.visitScalar_type(self)
            else:
                return visitor.visitChildren(self)




    def scalar_type(self):

        localctx = ZCodeParser.Scalar_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_scalar_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NUMBER) | (1 << ZCodeParser.BOOL) | (1 << ZCodeParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def index_ops(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opsContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = ZCodeParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_array_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(ZCodeParser.LS)
            self.state = 400
            self.index_ops()
            self.state = 401
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Builtins_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def readNumber(self):
            return self.getTypedRuleContext(ZCodeParser.ReadNumberContext,0)


        def writeNumber(self):
            return self.getTypedRuleContext(ZCodeParser.WriteNumberContext,0)


        def readBool(self):
            return self.getTypedRuleContext(ZCodeParser.ReadBoolContext,0)


        def writeBool(self):
            return self.getTypedRuleContext(ZCodeParser.WriteBoolContext,0)


        def readString(self):
            return self.getTypedRuleContext(ZCodeParser.ReadStringContext,0)


        def writeString(self):
            return self.getTypedRuleContext(ZCodeParser.WriteStringContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_builtins_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuiltins_call" ):
                return visitor.visitBuiltins_call(self)
            else:
                return visitor.visitChildren(self)




    def builtins_call(self):

        localctx = ZCodeParser.Builtins_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_builtins_call)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.readNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.writeNumber()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 405
                self.readBool()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 406
                self.writeBool()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 407
                self.readString()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 408
                self.writeString()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadNumber" ):
                return visitor.visitReadNumber(self)
            else:
                return visitor.visitChildren(self)




    def readNumber(self):

        localctx = ZCodeParser.ReadNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_readNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(ZCodeParser.T__0)
            self.state = 412
            self.match(ZCodeParser.LP)
            self.state = 413
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_ele(self):
            return self.getTypedRuleContext(ZCodeParser.Array_eleContext,0)


        def NUM_LIT(self):
            return self.getToken(ZCodeParser.NUM_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writeNumber

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteNumber" ):
                return visitor.visitWriteNumber(self)
            else:
                return visitor.visitChildren(self)




    def writeNumber(self):

        localctx = ZCodeParser.WriteNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_writeNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(ZCodeParser.T__1)
            self.state = 416
            self.match(ZCodeParser.LP)
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 417
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 418
                self.array_ele()
                pass

            elif la_ == 3:
                self.state = 419
                self.match(ZCodeParser.NUM_LIT)
                pass


            self.state = 422
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadBoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readBool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadBool" ):
                return visitor.visitReadBool(self)
            else:
                return visitor.visitChildren(self)




    def readBool(self):

        localctx = ZCodeParser.ReadBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_readBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(ZCodeParser.T__2)
            self.state = 425
            self.match(ZCodeParser.LP)
            self.state = 426
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteBoolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_ele(self):
            return self.getTypedRuleContext(ZCodeParser.Array_eleContext,0)


        def BOO_LIT(self):
            return self.getToken(ZCodeParser.BOO_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writeBool

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteBool" ):
                return visitor.visitWriteBool(self)
            else:
                return visitor.visitChildren(self)




    def writeBool(self):

        localctx = ZCodeParser.WriteBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_writeBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(ZCodeParser.T__1)
            self.state = 429
            self.match(ZCodeParser.LP)
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.state = 430
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 431
                self.array_ele()
                pass

            elif la_ == 3:
                self.state = 432
                self.match(ZCodeParser.BOO_LIT)
                pass


            self.state = 435
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReadStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_readString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadString" ):
                return visitor.visitReadString(self)
            else:
                return visitor.visitChildren(self)




    def readString(self):

        localctx = ZCodeParser.ReadStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(ZCodeParser.T__3)
            self.state = 438
            self.match(ZCodeParser.LP)
            self.state = 439
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(ZCodeParser.LP, 0)

        def RP(self):
            return self.getToken(ZCodeParser.RP, 0)

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_ele(self):
            return self.getTypedRuleContext(ZCodeParser.Array_eleContext,0)


        def STR_LIT(self):
            return self.getToken(ZCodeParser.STR_LIT, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_writeString

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteString" ):
                return visitor.visitWriteString(self)
            else:
                return visitor.visitChildren(self)




    def writeString(self):

        localctx = ZCodeParser.WriteStringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_writeString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(ZCodeParser.T__4)
            self.state = 442
            self.match(ZCodeParser.LP)
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 443
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 444
                self.array_ele()
                pass

            elif la_ == 3:
                self.state = 445
                self.match(ZCodeParser.STR_LIT)
                pass


            self.state = 448
            self.match(ZCodeParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.exp2_sempred
        self._predicates[30] = self.exp3_sempred
        self._predicates[31] = self.exp4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




