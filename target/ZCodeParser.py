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
        buf.write("\u01d2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5")
        buf.write("\3j\n\3\3\4\3\4\3\4\5\4o\n\4\3\5\3\5\3\5\3\5\7\5u\n\5")
        buf.write("\f\5\16\5x\13\5\3\6\3\6\3\6\5\6}\n\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7\u0087\n\7\3\7\3\7\5\7\u008b\n\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u0096\n\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u009e\n\n\3\n\3\n\5\n\u00a2\n\n\3")
        buf.write("\n\3\n\5\n\u00a6\n\n\3\13\3\13\5\13\u00aa\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\5\f\u00b1\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\5\r\u00bb\n\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00c6\n\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u00d9\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\5\23\u00e3\n\23\3\24\3\24\3\24\3\24\5\24\u00e9")
        buf.write("\n\24\3\25\3\25\3\25\5\25\u00ee\n\25\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u00f4\n\25\3\25\3\25\7\25\u00f8\n\25\f\25\16")
        buf.write("\25\u00fb\13\25\3\25\3\25\5\25\u00ff\n\25\3\25\5\25\u0102")
        buf.write("\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u010b\n")
        buf.write("\26\3\26\3\26\3\27\3\27\3\27\5\27\u0112\n\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0121\n\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3")
        buf.write("\33\5\33\u012b\n\33\3\33\3\33\3\34\3\34\3\34\5\34\u0132")
        buf.write("\n\34\3\34\3\34\5\34\u0136\n\34\3\35\3\35\3\35\3\35\3")
        buf.write("\35\5\35\u013d\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u0144")
        buf.write("\n\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u014c\n\37\f")
        buf.write("\37\16\37\u014f\13\37\3 \3 \3 \3 \3 \3 \7 \u0157\n \f")
        buf.write(" \16 \u015a\13 \3!\3!\3!\3!\3!\3!\7!\u0162\n!\f!\16!\u0165")
        buf.write("\13!\3\"\3\"\3\"\5\"\u016a\n\"\3#\3#\3#\5#\u016f\n#\3")
        buf.write("$\3$\3$\3$\3$\3$\3$\3$\7$\u0179\n$\f$\16$\u017c\13$\3")
        buf.write("%\3%\3%\3%\3%\3%\3%\5%\u0185\n%\3&\3&\3&\3&\5&\u018b\n")
        buf.write("&\3\'\3\'\3(\3(\5(\u0191\n(\3(\3(\3)\3)\3)\3)\3)\5)\u019a")
        buf.write("\n)\3*\3*\3*\3*\3*\5*\u01a1\n*\3+\3+\3+\3+\3+\3+\5+\u01a9")
        buf.write("\n+\3,\3,\3,\3,\3-\3-\3-\3-\3-\5-\u01b4\n-\3-\3-\3.\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3/\5/\u01c1\n/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u01ce\n\61\3\61\3")
        buf.write("\61\3\61\2\6<>@F\62\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`\2\7\5\2")
        buf.write("!!#\'))\3\2\32\33\3\2\34\35\3\2\36 \3\2\b\n\2\u01e6\2")
        buf.write("b\3\2\2\2\4i\3\2\2\2\6n\3\2\2\2\bp\3\2\2\2\n|\3\2\2\2")
        buf.write("\f\u0086\3\2\2\2\16\u008c\3\2\2\2\20\u0091\3\2\2\2\22")
        buf.write("\u0097\3\2\2\2\24\u00a9\3\2\2\2\26\u00b0\3\2\2\2\30\u00ba")
        buf.write("\3\2\2\2\32\u00bc\3\2\2\2\34\u00c5\3\2\2\2\36\u00c7\3")
        buf.write("\2\2\2 \u00d8\3\2\2\2\"\u00da\3\2\2\2$\u00e2\3\2\2\2&")
        buf.write("\u00e8\3\2\2\2(\u00ea\3\2\2\2*\u0103\3\2\2\2,\u0111\3")
        buf.write("\2\2\2.\u0120\3\2\2\2\60\u0122\3\2\2\2\62\u0125\3\2\2")
        buf.write("\2\64\u0128\3\2\2\2\66\u0135\3\2\2\28\u013c\3\2\2\2:\u0143")
        buf.write("\3\2\2\2<\u0145\3\2\2\2>\u0150\3\2\2\2@\u015b\3\2\2\2")
        buf.write("B\u0169\3\2\2\2D\u016e\3\2\2\2F\u0170\3\2\2\2H\u0184\3")
        buf.write("\2\2\2J\u018a\3\2\2\2L\u018c\3\2\2\2N\u018e\3\2\2\2P\u0199")
        buf.write("\3\2\2\2R\u01a0\3\2\2\2T\u01a8\3\2\2\2V\u01aa\3\2\2\2")
        buf.write("X\u01ae\3\2\2\2Z\u01b7\3\2\2\2\\\u01bb\3\2\2\2^\u01c4")
        buf.write("\3\2\2\2`\u01c8\3\2\2\2bc\5\4\3\2cd\7\2\2\3d\3\3\2\2\2")
        buf.write("ef\5\6\4\2fg\5\4\3\2gj\3\2\2\2hj\5\6\4\2ie\3\2\2\2ih\3")
        buf.write("\2\2\2j\5\3\2\2\2ko\5\n\6\2lo\5\22\n\2mo\5\b\5\2nk\3\2")
        buf.write("\2\2nl\3\2\2\2nm\3\2\2\2o\7\3\2\2\2pv\7\65\2\2qr\7\66")
        buf.write("\2\2ru\7\65\2\2su\7\65\2\2tq\3\2\2\2ts\3\2\2\2ux\3\2\2")
        buf.write("\2vt\3\2\2\2vw\3\2\2\2w\t\3\2\2\2xv\3\2\2\2y}\5\f\7\2")
        buf.write("z}\5\16\b\2{}\5\20\t\2|y\3\2\2\2|z\3\2\2\2|{\3\2\2\2}")
        buf.write("~\3\2\2\2~\177\5\b\5\2\177\13\3\2\2\2\u0080\u0081\5L\'")
        buf.write("\2\u0081\u0082\7/\2\2\u0082\u0087\3\2\2\2\u0083\u0084")
        buf.write("\5L\'\2\u0084\u0085\5\32\16\2\u0085\u0087\3\2\2\2\u0086")
        buf.write("\u0080\3\2\2\2\u0086\u0083\3\2\2\2\u0087\u008a\3\2\2\2")
        buf.write("\u0088\u0089\7\"\2\2\u0089\u008b\58\35\2\u008a\u0088\3")
        buf.write("\2\2\2\u008a\u008b\3\2\2\2\u008b\r\3\2\2\2\u008c\u008d")
        buf.write("\7\f\2\2\u008d\u008e\7/\2\2\u008e\u008f\7\"\2\2\u008f")
        buf.write("\u0090\58\35\2\u0090\17\3\2\2\2\u0091\u0092\7\r\2\2\u0092")
        buf.write("\u0095\7/\2\2\u0093\u0094\7\"\2\2\u0094\u0096\58\35\2")
        buf.write("\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\21\3\2")
        buf.write("\2\2\u0097\u0098\7\16\2\2\u0098\u0099\7/\2\2\u0099\u009a")
        buf.write("\7*\2\2\u009a\u009b\5\24\13\2\u009b\u00a5\7+\2\2\u009c")
        buf.write("\u009e\5\b\5\2\u009d\u009c\3\2\2\2\u009d\u009e\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\u00a6\5\"\22\2\u00a0\u00a2")
        buf.write("\5\b\5\2\u00a1\u00a0\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00a6\5\64\33\2\u00a4\u00a6\5\b\5")
        buf.write("\2\u00a5\u009d\3\2\2\2\u00a5\u00a1\3\2\2\2\u00a5\u00a4")
        buf.write("\3\2\2\2\u00a6\23\3\2\2\2\u00a7\u00aa\5\26\f\2\u00a8\u00aa")
        buf.write("\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa")
        buf.write("\25\3\2\2\2\u00ab\u00ac\5\30\r\2\u00ac\u00ad\7.\2\2\u00ad")
        buf.write("\u00ae\5\26\f\2\u00ae\u00b1\3\2\2\2\u00af\u00b1\5\30\r")
        buf.write("\2\u00b0\u00ab\3\2\2\2\u00b0\u00af\3\2\2\2\u00b1\27\3")
        buf.write("\2\2\2\u00b2\u00b3\5L\'\2\u00b3\u00b4\7/\2\2\u00b4\u00bb")
        buf.write("\3\2\2\2\u00b5\u00b6\7\r\2\2\u00b6\u00bb\7/\2\2\u00b7")
        buf.write("\u00b8\5L\'\2\u00b8\u00b9\5\32\16\2\u00b9\u00bb\3\2\2")
        buf.write("\2\u00ba\u00b2\3\2\2\2\u00ba\u00b5\3\2\2\2\u00ba\u00b7")
        buf.write("\3\2\2\2\u00bb\31\3\2\2\2\u00bc\u00bd\7/\2\2\u00bd\u00be")
        buf.write("\7,\2\2\u00be\u00bf\5\34\17\2\u00bf\u00c0\7-\2\2\u00c0")
        buf.write("\33\3\2\2\2\u00c1\u00c2\7\63\2\2\u00c2\u00c3\7.\2\2\u00c3")
        buf.write("\u00c6\5\34\17\2\u00c4\u00c6\7\63\2\2\u00c5\u00c1\3\2")
        buf.write("\2\2\u00c5\u00c4\3\2\2\2\u00c6\35\3\2\2\2\u00c7\u00c8")
        buf.write("\7/\2\2\u00c8\u00c9\7,\2\2\u00c9\u00ca\5R*\2\u00ca\u00cb")
        buf.write("\7-\2\2\u00cb\37\3\2\2\2\u00cc\u00d9\5\"\22\2\u00cd\u00d9")
        buf.write("\5(\25\2\u00ce\u00d9\5*\26\2\u00cf\u00d9\5,\27\2\u00d0")
        buf.write("\u00d9\5\60\31\2\u00d1\u00d9\5\62\32\2\u00d2\u00d9\5\64")
        buf.write("\33\2\u00d3\u00d4\5\66\34\2\u00d4\u00d5\5\b\5\2\u00d5")
        buf.write("\u00d9\3\2\2\2\u00d6\u00d9\5\n\6\2\u00d7\u00d9\5\22\n")
        buf.write("\2\u00d8\u00cc\3\2\2\2\u00d8\u00cd\3\2\2\2\u00d8\u00ce")
        buf.write("\3\2\2\2\u00d8\u00cf\3\2\2\2\u00d8\u00d0\3\2\2\2\u00d8")
        buf.write("\u00d1\3\2\2\2\u00d8\u00d2\3\2\2\2\u00d8\u00d3\3\2\2\2")
        buf.write("\u00d8\u00d6\3\2\2\2\u00d8\u00d7\3\2\2\2\u00d9!\3\2\2")
        buf.write("\2\u00da\u00db\7\27\2\2\u00db\u00dc\5\b\5\2\u00dc\u00dd")
        buf.write("\5$\23\2\u00dd\u00de\7\30\2\2\u00de\u00df\5\b\5\2\u00df")
        buf.write("#\3\2\2\2\u00e0\u00e3\5&\24\2\u00e1\u00e3\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e1\3\2\2\2\u00e3%\3\2\2\2\u00e4")
        buf.write("\u00e5\5 \21\2\u00e5\u00e6\5&\24\2\u00e6\u00e9\3\2\2\2")
        buf.write("\u00e7\u00e9\5 \21\2\u00e8\u00e4\3\2\2\2\u00e8\u00e7\3")
        buf.write("\2\2\2\u00e9\'\3\2\2\2\u00ea\u00eb\7\24\2\2\u00eb\u00ed")
        buf.write("\58\35\2\u00ec\u00ee\5\b\5\2\u00ed\u00ec\3\2\2\2\u00ed")
        buf.write("\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f9\5 \21\2")
        buf.write("\u00f0\u00f1\7\26\2\2\u00f1\u00f3\58\35\2\u00f2\u00f4")
        buf.write("\5\b\5\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5\u00f6\5 \21\2\u00f6\u00f8\3\2\2\2")
        buf.write("\u00f7\u00f0\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3")
        buf.write("\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u0101\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fc\u00fe\7\25\2\2\u00fd\u00ff\5\b\5\2\u00fe")
        buf.write("\u00fd\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\3\2\2\2")
        buf.write("\u0100\u0102\5 \21\2\u0101\u00fc\3\2\2\2\u0101\u0102\3")
        buf.write("\2\2\2\u0102)\3\2\2\2\u0103\u0104\7\17\2\2\u0104\u0105")
        buf.write("\7/\2\2\u0105\u0106\7\20\2\2\u0106\u0107\58\35\2\u0107")
        buf.write("\u0108\7\21\2\2\u0108\u010a\58\35\2\u0109\u010b\5\b\5")
        buf.write("\2\u010a\u0109\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c")
        buf.write("\3\2\2\2\u010c\u010d\5 \21\2\u010d+\3\2\2\2\u010e\u0112")
        buf.write("\7/\2\2\u010f\u0110\7/\2\2\u0110\u0112\5.\30\2\u0111\u010e")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113\3\2\2\2\u0113")
        buf.write("\u0114\7\"\2\2\u0114\u0115\58\35\2\u0115\u0116\5\b\5\2")
        buf.write("\u0116-\3\2\2\2\u0117\u0118\7,\2\2\u0118\u0119\58\35\2")
        buf.write("\u0119\u011a\7-\2\2\u011a\u011b\5.\30\2\u011b\u0121\3")
        buf.write("\2\2\2\u011c\u011d\7,\2\2\u011d\u011e\58\35\2\u011e\u011f")
        buf.write("\7-\2\2\u011f\u0121\3\2\2\2\u0120\u0117\3\2\2\2\u0120")
        buf.write("\u011c\3\2\2\2\u0121/\3\2\2\2\u0122\u0123\7\23\2\2\u0123")
        buf.write("\u0124\5\b\5\2\u0124\61\3\2\2\2\u0125\u0126\7\22\2\2\u0126")
        buf.write("\u0127\5\b\5\2\u0127\63\3\2\2\2\u0128\u012a\7\13\2\2\u0129")
        buf.write("\u012b\58\35\2\u012a\u0129\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u012c\3\2\2\2\u012c\u012d\5\b\5\2\u012d\65\3\2")
        buf.write("\2\2\u012e\u012f\7/\2\2\u012f\u0131\7*\2\2\u0130\u0132")
        buf.write("\5R*\2\u0131\u0130\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133\u0136\7+\2\2\u0134\u0136\5T+\2\u0135\u012e")
        buf.write("\3\2\2\2\u0135\u0134\3\2\2\2\u0136\67\3\2\2\2\u0137\u0138")
        buf.write("\5:\36\2\u0138\u0139\7(\2\2\u0139\u013a\5:\36\2\u013a")
        buf.write("\u013d\3\2\2\2\u013b\u013d\5:\36\2\u013c\u0137\3\2\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013d9\3\2\2\2\u013e\u013f\5<\37")
        buf.write("\2\u013f\u0140\t\2\2\2\u0140\u0141\5<\37\2\u0141\u0144")
        buf.write("\3\2\2\2\u0142\u0144\5<\37\2\u0143\u013e\3\2\2\2\u0143")
        buf.write("\u0142\3\2\2\2\u0144;\3\2\2\2\u0145\u0146\b\37\1\2\u0146")
        buf.write("\u0147\5> \2\u0147\u014d\3\2\2\2\u0148\u0149\f\4\2\2\u0149")
        buf.write("\u014a\t\3\2\2\u014a\u014c\5> \2\u014b\u0148\3\2\2\2\u014c")
        buf.write("\u014f\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014e\3\2\2\2")
        buf.write("\u014e=\3\2\2\2\u014f\u014d\3\2\2\2\u0150\u0151\b \1\2")
        buf.write("\u0151\u0152\5@!\2\u0152\u0158\3\2\2\2\u0153\u0154\f\4")
        buf.write("\2\2\u0154\u0155\t\4\2\2\u0155\u0157\5@!\2\u0156\u0153")
        buf.write("\3\2\2\2\u0157\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158")
        buf.write("\u0159\3\2\2\2\u0159?\3\2\2\2\u015a\u0158\3\2\2\2\u015b")
        buf.write("\u015c\b!\1\2\u015c\u015d\5B\"\2\u015d\u0163\3\2\2\2\u015e")
        buf.write("\u015f\f\4\2\2\u015f\u0160\t\5\2\2\u0160\u0162\5B\"\2")
        buf.write("\u0161\u015e\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161\3")
        buf.write("\2\2\2\u0163\u0164\3\2\2\2\u0164A\3\2\2\2\u0165\u0163")
        buf.write("\3\2\2\2\u0166\u0167\7\31\2\2\u0167\u016a\5B\"\2\u0168")
        buf.write("\u016a\5D#\2\u0169\u0166\3\2\2\2\u0169\u0168\3\2\2\2\u016a")
        buf.write("C\3\2\2\2\u016b\u016c\7\35\2\2\u016c\u016f\5D#\2\u016d")
        buf.write("\u016f\5F$\2\u016e\u016b\3\2\2\2\u016e\u016d\3\2\2\2\u016f")
        buf.write("E\3\2\2\2\u0170\u0171\b$\1\2\u0171\u0172\5H%\2\u0172\u017a")
        buf.write("\3\2\2\2\u0173\u0174\f\4\2\2\u0174\u0175\7,\2\2\u0175")
        buf.write("\u0176\5R*\2\u0176\u0177\7-\2\2\u0177\u0179\3\2\2\2\u0178")
        buf.write("\u0173\3\2\2\2\u0179\u017c\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u017b\3\2\2\2\u017bG\3\2\2\2\u017c\u017a\3\2\2")
        buf.write("\2\u017d\u0185\5J&\2\u017e\u017f\7*\2\2\u017f\u0180\5")
        buf.write("8\35\2\u0180\u0181\7+\2\2\u0181\u0185\3\2\2\2\u0182\u0185")
        buf.write("\7/\2\2\u0183\u0185\5\66\34\2\u0184\u017d\3\2\2\2\u0184")
        buf.write("\u017e\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0183\3\2\2\2")
        buf.write("\u0185I\3\2\2\2\u0186\u018b\5N(\2\u0187\u018b\7\63\2\2")
        buf.write("\u0188\u018b\7\60\2\2\u0189\u018b\7\64\2\2\u018a\u0186")
        buf.write("\3\2\2\2\u018a\u0187\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u0189\3\2\2\2\u018bK\3\2\2\2\u018c\u018d\t\6\2\2\u018d")
        buf.write("M\3\2\2\2\u018e\u0190\7,\2\2\u018f\u0191\5P)\2\u0190\u018f")
        buf.write("\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0192\3\2\2\2\u0192")
        buf.write("\u0193\7-\2\2\u0193O\3\2\2\2\u0194\u0195\5J&\2\u0195\u0196")
        buf.write("\7.\2\2\u0196\u0197\5P)\2\u0197\u019a\3\2\2\2\u0198\u019a")
        buf.write("\5J&\2\u0199\u0194\3\2\2\2\u0199\u0198\3\2\2\2\u019aQ")
        buf.write("\3\2\2\2\u019b\u019c\58\35\2\u019c\u019d\7.\2\2\u019d")
        buf.write("\u019e\5R*\2\u019e\u01a1\3\2\2\2\u019f\u01a1\58\35\2\u01a0")
        buf.write("\u019b\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1S\3\2\2\2\u01a2")
        buf.write("\u01a9\5V,\2\u01a3\u01a9\5X-\2\u01a4\u01a9\5Z.\2\u01a5")
        buf.write("\u01a9\5\\/\2\u01a6\u01a9\5^\60\2\u01a7\u01a9\5`\61\2")
        buf.write("\u01a8\u01a2\3\2\2\2\u01a8\u01a3\3\2\2\2\u01a8\u01a4\3")
        buf.write("\2\2\2\u01a8\u01a5\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a9U\3\2\2\2\u01aa\u01ab\7\3\2\2\u01ab\u01ac")
        buf.write("\7*\2\2\u01ac\u01ad\7+\2\2\u01adW\3\2\2\2\u01ae\u01af")
        buf.write("\7\4\2\2\u01af\u01b3\7*\2\2\u01b0\u01b4\7/\2\2\u01b1\u01b4")
        buf.write("\5\36\20\2\u01b2\u01b4\7\63\2\2\u01b3\u01b0\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b6\7+\2\2\u01b6Y\3\2\2\2\u01b7\u01b8\7\5\2\2")
        buf.write("\u01b8\u01b9\7*\2\2\u01b9\u01ba\7+\2\2\u01ba[\3\2\2\2")
        buf.write("\u01bb\u01bc\7\4\2\2\u01bc\u01c0\7*\2\2\u01bd\u01c1\7")
        buf.write("/\2\2\u01be\u01c1\5\36\20\2\u01bf\u01c1\7\60\2\2\u01c0")
        buf.write("\u01bd\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01bf\3\2\2\2")
        buf.write("\u01c1\u01c2\3\2\2\2\u01c2\u01c3\7+\2\2\u01c3]\3\2\2\2")
        buf.write("\u01c4\u01c5\7\6\2\2\u01c5\u01c6\7*\2\2\u01c6\u01c7\7")
        buf.write("+\2\2\u01c7_\3\2\2\2\u01c8\u01c9\7\7\2\2\u01c9\u01cd\7")
        buf.write("*\2\2\u01ca\u01ce\7/\2\2\u01cb\u01ce\5\36\20\2\u01cc\u01ce")
        buf.write("\7\64\2\2\u01cd\u01ca\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d0\7+\2\2")
        buf.write("\u01d0a\3\2\2\2\60intv|\u0086\u008a\u0095\u009d\u00a1")
        buf.write("\u00a5\u00a9\u00b0\u00ba\u00c5\u00d8\u00e2\u00e8\u00ed")
        buf.write("\u00f3\u00f9\u00fe\u0101\u010a\u0111\u0120\u012a\u0131")
        buf.write("\u0135\u013c\u0143\u014d\u0158\u0163\u0169\u016e\u017a")
        buf.write("\u0184\u018a\u0190\u0199\u01a0\u01a8\u01b3\u01c0\u01cd")
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
                     "<INVALID>", "<INVALID>", "'true'", "'false'", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", 
                      "DIV", "MOD", "EQ_STR", "ASSIGN", "DIFFER", "LT", 
                      "LE", "GT", "GE", "CONCAT", "EQ_NUM", "LP", "RP", 
                      "LS", "RS", "COMMA", "ID", "BOO_LIT", "TRUE", "FALSE", 
                      "NUM_LIT", "STR_LIT", "NEWLINE", "COMMENT", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl_list = 1
    RULE_decl = 2
    RULE_ignore = 3
    RULE_vars_decl = 4
    RULE_var_decl = 5
    RULE_imp_var_decl = 6
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
    RULE_value_type = 37
    RULE_array_list = 38
    RULE_list_arr_literal = 39
    RULE_exp_list = 40
    RULE_builtins_call = 41
    RULE_readNumber = 42
    RULE_writeNumber = 43
    RULE_readBool = 44
    RULE_write = 45
    RULE_readString = 46
    RULE_writeString = 47

    ruleNames =  [ "program", "decl_list", "decl", "ignore", "vars_decl", 
                   "var_decl", "imp_var_decl", "dynamic_decl", "funs_decl", 
                   "formal_params", "formal_pms_prm", "formal_pm", "array_type", 
                   "dim_list", "array_ele", "stmt", "block_stmt", "stmtlist", 
                   "stmtprime", "if_stmt", "for_stmt", "assign_stmt", "index_ops", 
                   "continue_stmt", "break_stmt", "return_stmt", "fun_call", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "array_val", "value_type", "array_list", 
                   "list_arr_literal", "exp_list", "builtins_call", "readNumber", 
                   "writeNumber", "readBool", "write", "readString", "writeString" ]

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
    ID=45
    BOO_LIT=46
    TRUE=47
    FALSE=48
    NUM_LIT=49
    STR_LIT=50
    NEWLINE=51
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.decl_list()
            self.state = 97
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
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.decl()
                self.state = 100
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
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


        def ignore(self):
            return self.getTypedRuleContext(ZCodeParser.IgnoreContext,0)


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
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.vars_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.funs_decl()
                pass
            elif token in [ZCodeParser.NEWLINE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 107
                self.ignore()
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

        def COMMENT(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.COMMENT)
            else:
                return self.getToken(ZCodeParser.COMMENT, i)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(ZCodeParser.NEWLINE)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 114
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZCodeParser.COMMENT]:
                        self.state = 111
                        self.match(ZCodeParser.COMMENT)
                        self.state = 112
                        self.match(ZCodeParser.NEWLINE)
                        pass
                    elif token in [ZCodeParser.NEWLINE]:
                        self.state = 113
                        self.match(ZCodeParser.NEWLINE)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 118
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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


        def var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Var_declContext,0)


        def imp_var_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Imp_var_declContext,0)


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
            self.state = 122
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 119
                self.var_decl()
                pass
            elif token in [ZCodeParser.VAR]:
                self.state = 120
                self.imp_var_decl()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 121
                self.dynamic_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 124
            self.ignore()
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

        def value_type(self):
            return self.getTypedRuleContext(ZCodeParser.Value_typeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def array_type(self):
            return self.getTypedRuleContext(ZCodeParser.Array_typeContext,0)


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
        self.enterRule(localctx, 10, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 126
                self.value_type()
                self.state = 127
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 129
                self.value_type()
                self.state = 130
                self.array_type()
                pass


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 134
                self.match(ZCodeParser.ASSIGN)
                self.state = 135
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Imp_var_declContext(ParserRuleContext):
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
            return ZCodeParser.RULE_imp_var_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImp_var_decl" ):
                return visitor.visitImp_var_decl(self)
            else:
                return visitor.visitChildren(self)




    def imp_var_decl(self):

        localctx = ZCodeParser.Imp_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_imp_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(ZCodeParser.VAR)
            self.state = 139
            self.match(ZCodeParser.ID)
            self.state = 140
            self.match(ZCodeParser.ASSIGN)
            self.state = 141
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
            self.state = 143
            self.match(ZCodeParser.DYNAMIC)
            self.state = 144
            self.match(ZCodeParser.ID)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 145
                self.match(ZCodeParser.ASSIGN)
                self.state = 146
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
            self.state = 149
            self.match(ZCodeParser.FUNC)
            self.state = 150
            self.match(ZCodeParser.ID)
            self.state = 151
            self.match(ZCodeParser.LP)
            self.state = 152
            self.formal_params()
            self.state = 153
            self.match(ZCodeParser.RP)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 154
                    self.ignore()


                self.state = 157
                self.block_stmt()
                pass

            elif la_ == 2:
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 158
                    self.ignore()


                self.state = 161
                self.return_stmt()
                pass

            elif la_ == 3:
                self.state = 162
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
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
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
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.formal_pm()
                self.state = 170
                self.match(ZCodeParser.COMMA)
                self.state = 171
                self.formal_pms_prm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
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

        def value_type(self):
            return self.getTypedRuleContext(ZCodeParser.Value_typeContext,0)


        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

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
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.value_type()
                self.state = 177
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(ZCodeParser.DYNAMIC)
                self.state = 180
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 181
                self.value_type()
                self.state = 182
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
            self.state = 186
            self.match(ZCodeParser.ID)
            self.state = 187
            self.match(ZCodeParser.LS)
            self.state = 188
            self.dim_list()
            self.state = 189
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
            self.state = 195
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(ZCodeParser.NUM_LIT)
                self.state = 192
                self.match(ZCodeParser.COMMA)
                self.state = 193
                self.dim_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
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

        def ID(self):
            return self.getToken(ZCodeParser.ID, 0)

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def exp_list(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

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
            self.state = 197
            self.match(ZCodeParser.ID)
            self.state = 198
            self.match(ZCodeParser.LS)
            self.state = 199
            self.exp_list()
            self.state = 200
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


        def funs_decl(self):
            return self.getTypedRuleContext(ZCodeParser.Funs_declContext,0)


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
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 204
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 205
                self.assign_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 206
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 207
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 208
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 209
                self.fun_call()
                self.state = 210
                self.ignore()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 212
                self.vars_decl()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 213
                self.funs_decl()
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
            self.state = 216
            self.match(ZCodeParser.BEGIN)
            self.state = 217
            self.ignore()
            self.state = 218
            self.stmtlist()
            self.state = 219
            self.match(ZCodeParser.END)
            self.state = 220
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
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.T__0, ZCodeParser.T__1, ZCodeParser.T__2, ZCodeParser.T__3, ZCodeParser.T__4, ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FUNC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
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
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.stmt()
                self.state = 227
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
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

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.ExpContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.ExpContext,i)


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
            self.state = 232
            self.match(ZCodeParser.IF)
            self.state = 233
            self.exp()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 234
                self.ignore()


            self.state = 237
            self.stmt()
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 238
                    self.match(ZCodeParser.ELIF)
                    self.state = 239
                    self.exp()
                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZCodeParser.NEWLINE:
                        self.state = 240
                        self.ignore()


                    self.state = 243
                    self.stmt() 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 250
                self.match(ZCodeParser.ELSE)
                self.state = 252
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 251
                    self.ignore()


                self.state = 254
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
            self.state = 257
            self.match(ZCodeParser.FOR)
            self.state = 258
            self.match(ZCodeParser.ID)
            self.state = 259
            self.match(ZCodeParser.UNTIL)
            self.state = 260
            self.exp()
            self.state = 261
            self.match(ZCodeParser.BY)
            self.state = 262
            self.exp()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 263
                self.ignore()


            self.state = 266
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

        def index_ops(self):
            return self.getTypedRuleContext(ZCodeParser.Index_opsContext,0)


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
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 268
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 269
                self.match(ZCodeParser.ID)
                self.state = 270
                self.index_ops()
                pass


            self.state = 273
            self.match(ZCodeParser.ASSIGN)
            self.state = 274
            self.exp()
            self.state = 275
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

        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

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
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(ZCodeParser.LS)
                self.state = 278
                self.exp()
                self.state = 279
                self.match(ZCodeParser.RS)
                self.state = 280
                self.index_ops()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
                self.match(ZCodeParser.LS)
                self.state = 283
                self.exp()
                self.state = 284
                self.match(ZCodeParser.RS)
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

        def exp_list(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_listContext,0)


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
                    self.exp_list()


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
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
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
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
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
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
                self.exp7(0)
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

        def exp8(self):
            return self.getTypedRuleContext(ZCodeParser.Exp8Context,0)


        def exp7(self):
            return self.getTypedRuleContext(ZCodeParser.Exp7Context,0)


        def LS(self):
            return self.getToken(ZCodeParser.LS, 0)

        def exp_list(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_listContext,0)


        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)



    def exp7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Exp7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.exp8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 376
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp7)
                    self.state = 369
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 370
                    self.match(ZCodeParser.LS)
                    self.state = 371
                    self.exp_list()
                    self.state = 372
                    self.match(ZCodeParser.RS) 
                self.state = 378
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 386
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 380
                self.match(ZCodeParser.LP)
                self.state = 381
                self.exp()
                self.state = 382
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 384
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 385
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
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.array_list()
                pass
            elif token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.BOO_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 390
                self.match(ZCodeParser.BOO_LIT)
                pass
            elif token in [ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 391
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


    class Value_typeContext(ParserRuleContext):
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
            return ZCodeParser.RULE_value_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_type" ):
                return visitor.visitValue_type(self)
            else:
                return visitor.visitChildren(self)




    def value_type(self):

        localctx = ZCodeParser.Value_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_value_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
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

        def RS(self):
            return self.getToken(ZCodeParser.RS, 0)

        def list_arr_literal(self):
            return self.getTypedRuleContext(ZCodeParser.List_arr_literalContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(ZCodeParser.LS)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.LS) | (1 << ZCodeParser.BOO_LIT) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                self.state = 397
                self.list_arr_literal()


            self.state = 400
            self.match(ZCodeParser.RS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_arr_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_val(self):
            return self.getTypedRuleContext(ZCodeParser.Array_valContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def list_arr_literal(self):
            return self.getTypedRuleContext(ZCodeParser.List_arr_literalContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_list_arr_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_arr_literal" ):
                return visitor.visitList_arr_literal(self)
            else:
                return visitor.visitChildren(self)




    def list_arr_literal(self):

        localctx = ZCodeParser.List_arr_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_list_arr_literal)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.array_val()
                self.state = 403
                self.match(ZCodeParser.COMMA)
                self.state = 404
                self.list_arr_literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.array_val()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(ZCodeParser.ExpContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def exp_list(self):
            return self.getTypedRuleContext(ZCodeParser.Exp_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = ZCodeParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exp_list)
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.exp()
                self.state = 410
                self.match(ZCodeParser.COMMA)
                self.state = 411
                self.exp_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.exp()
                pass


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


        def write(self):
            return self.getTypedRuleContext(ZCodeParser.WriteContext,0)


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
        self.enterRule(localctx, 82, self.RULE_builtins_call)
        try:
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.readNumber()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.writeNumber()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 418
                self.readBool()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 419
                self.write()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 420
                self.readString()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 421
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
        self.enterRule(localctx, 84, self.RULE_readNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(ZCodeParser.T__0)
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
        self.enterRule(localctx, 86, self.RULE_writeNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(ZCodeParser.T__1)
            self.state = 429
            self.match(ZCodeParser.LP)
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
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
                self.match(ZCodeParser.NUM_LIT)
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
        self.enterRule(localctx, 88, self.RULE_readBool)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(ZCodeParser.T__2)
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


    class WriteContext(ParserRuleContext):
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
            return ZCodeParser.RULE_write

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWrite" ):
                return visitor.visitWrite(self)
            else:
                return visitor.visitChildren(self)




    def write(self):

        localctx = ZCodeParser.WriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_write)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(ZCodeParser.T__1)
            self.state = 442
            self.match(ZCodeParser.LP)
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
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
                self.match(ZCodeParser.BOO_LIT)
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
        self.enterRule(localctx, 92, self.RULE_readString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 450
            self.match(ZCodeParser.T__3)
            self.state = 451
            self.match(ZCodeParser.LP)
            self.state = 452
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
        self.enterRule(localctx, 94, self.RULE_writeString)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.match(ZCodeParser.T__4)
            self.state = 455
            self.match(ZCodeParser.LP)
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 456
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 457
                self.array_ele()
                pass

            elif la_ == 3:
                self.state = 458
                self.match(ZCodeParser.STR_LIT)
                pass


            self.state = 461
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
        self._predicates[34] = self.exp7_sempred
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
         

    def exp7_sempred(self, localctx:Exp7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




