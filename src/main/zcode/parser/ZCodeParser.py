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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\u0186\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\7\2R\n\2\f\2\16\2U\13\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3^\n\3\3\4\3\4\5\4b\n\4\3\5\6\5e")
        buf.write("\n\5\r\5\16\5f\3\6\3\6\3\6\5\6l\n\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7v\n\7\3\7\3\7\5\7z\n\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\5\t\u0085\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u008d\n\n\3\n\3\n\5\n\u0091\n\n\3\n\3\n\5\n")
        buf.write("\u0095\n\n\3\13\3\13\5\13\u0099\n\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00a0\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00a8\n\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u00b3")
        buf.write("\n\17\3\20\3\20\5\20\u00b7\n\20\3\20\3\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\5\21\u00c8\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3")
        buf.write("\23\5\23\u00d2\n\23\3\24\3\24\3\24\3\24\5\24\u00d8\n\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\5\25\u00df\n\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\5\25\u00e7\n\25\3\25\3\25\7\25\u00eb")
        buf.write("\n\25\f\25\16\25\u00ee\13\25\3\25\3\25\5\25\u00f2\n\25")
        buf.write("\3\25\5\25\u00f5\n\25\3\26\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u00fe\n\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u0108\n\27\3\27\3\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\5\30\u0113\n\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\5\33\u011d\n\33\3\33\3\33\3\34\3\34\3")
        buf.write("\34\5\34\u0124\n\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\5\35\u012d\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u0134\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u013c\n\37\f\37")
        buf.write("\16\37\u013f\13\37\3 \3 \3 \3 \3 \3 \7 \u0147\n \f \16")
        buf.write(" \u014a\13 \3!\3!\3!\3!\3!\3!\7!\u0152\n!\f!\16!\u0155")
        buf.write("\13!\3\"\3\"\3\"\5\"\u015a\n\"\3#\3#\3#\5#\u015f\n#\3")
        buf.write("$\3$\3$\3$\5$\u0165\n$\3$\5$\u0168\n$\3$\3$\3$\3$\3$\5")
        buf.write("$\u016f\n$\3%\3%\3%\3%\3%\3%\3%\5%\u0178\n%\3&\3&\3&\3")
        buf.write("&\5&\u017e\n&\3\'\3\'\3(\3(\3(\3(\3(\2\5<>@)\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLN\2\7\5\2\34\34\36\"$$\3\2\25\26\3\2\27\30\3\2")
        buf.write("\31\33\3\2\3\5\2\u0194\2S\3\2\2\2\4]\3\2\2\2\6a\3\2\2")
        buf.write("\2\bd\3\2\2\2\nk\3\2\2\2\fu\3\2\2\2\16{\3\2\2\2\20\u0080")
        buf.write("\3\2\2\2\22\u0086\3\2\2\2\24\u0098\3\2\2\2\26\u009f\3")
        buf.write("\2\2\2\30\u00a7\3\2\2\2\32\u00a9\3\2\2\2\34\u00b2\3\2")
        buf.write("\2\2\36\u00b6\3\2\2\2 \u00c7\3\2\2\2\"\u00c9\3\2\2\2$")
        buf.write("\u00d1\3\2\2\2&\u00d7\3\2\2\2(\u00d9\3\2\2\2*\u00f6\3")
        buf.write("\2\2\2,\u0107\3\2\2\2.\u0112\3\2\2\2\60\u0114\3\2\2\2")
        buf.write("\62\u0117\3\2\2\2\64\u011a\3\2\2\2\66\u0120\3\2\2\28\u012c")
        buf.write("\3\2\2\2:\u0133\3\2\2\2<\u0135\3\2\2\2>\u0140\3\2\2\2")
        buf.write("@\u014b\3\2\2\2B\u0159\3\2\2\2D\u015e\3\2\2\2F\u016e\3")
        buf.write("\2\2\2H\u0177\3\2\2\2J\u017d\3\2\2\2L\u017f\3\2\2\2N\u0181")
        buf.write("\3\2\2\2PR\7*\2\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2")
        buf.write("\2\2TV\3\2\2\2US\3\2\2\2VW\5\4\3\2WX\7\2\2\3X\3\3\2\2")
        buf.write("\2YZ\5\6\4\2Z[\5\4\3\2[^\3\2\2\2\\^\5\6\4\2]Y\3\2\2\2")
        buf.write("]\\\3\2\2\2^\5\3\2\2\2_b\5\n\6\2`b\5\22\n\2a_\3\2\2\2")
        buf.write("a`\3\2\2\2b\7\3\2\2\2ce\7*\2\2dc\3\2\2\2ef\3\2\2\2fd\3")
        buf.write("\2\2\2fg\3\2\2\2g\t\3\2\2\2hl\5\f\7\2il\5\16\b\2jl\5\20")
        buf.write("\t\2kh\3\2\2\2ki\3\2\2\2kj\3\2\2\2lm\3\2\2\2mn\5\b\5\2")
        buf.write("n\13\3\2\2\2op\5L\'\2pq\7+\2\2qv\3\2\2\2rs\5L\'\2st\5")
        buf.write("\32\16\2tv\3\2\2\2uo\3\2\2\2ur\3\2\2\2vy\3\2\2\2wx\7\35")
        buf.write("\2\2xz\58\35\2yw\3\2\2\2yz\3\2\2\2z\r\3\2\2\2{|\7\7\2")
        buf.write("\2|}\7+\2\2}~\7\35\2\2~\177\58\35\2\177\17\3\2\2\2\u0080")
        buf.write("\u0081\7\b\2\2\u0081\u0084\7+\2\2\u0082\u0083\7\35\2\2")
        buf.write("\u0083\u0085\58\35\2\u0084\u0082\3\2\2\2\u0084\u0085\3")
        buf.write("\2\2\2\u0085\21\3\2\2\2\u0086\u0087\7\t\2\2\u0087\u0088")
        buf.write("\7+\2\2\u0088\u0089\7%\2\2\u0089\u008a\5\24\13\2\u008a")
        buf.write("\u0094\7&\2\2\u008b\u008d\5\b\5\2\u008c\u008b\3\2\2\2")
        buf.write("\u008c\u008d\3\2\2\2\u008d\u008e\3\2\2\2\u008e\u0095\5")
        buf.write("\"\22\2\u008f\u0091\5\b\5\2\u0090\u008f\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0095\5\64\33")
        buf.write("\2\u0093\u0095\5\b\5\2\u0094\u008c\3\2\2\2\u0094\u0090")
        buf.write("\3\2\2\2\u0094\u0093\3\2\2\2\u0095\23\3\2\2\2\u0096\u0099")
        buf.write("\5\26\f\2\u0097\u0099\3\2\2\2\u0098\u0096\3\2\2\2\u0098")
        buf.write("\u0097\3\2\2\2\u0099\25\3\2\2\2\u009a\u009b\5\30\r\2\u009b")
        buf.write("\u009c\7)\2\2\u009c\u009d\5\26\f\2\u009d\u00a0\3\2\2\2")
        buf.write("\u009e\u00a0\5\30\r\2\u009f\u009a\3\2\2\2\u009f\u009e")
        buf.write("\3\2\2\2\u00a0\27\3\2\2\2\u00a1\u00a2\5L\'\2\u00a2\u00a3")
        buf.write("\7+\2\2\u00a3\u00a8\3\2\2\2\u00a4\u00a5\5L\'\2\u00a5\u00a6")
        buf.write("\5\32\16\2\u00a6\u00a8\3\2\2\2\u00a7\u00a1\3\2\2\2\u00a7")
        buf.write("\u00a4\3\2\2\2\u00a8\31\3\2\2\2\u00a9\u00aa\7+\2\2\u00aa")
        buf.write("\u00ab\7\'\2\2\u00ab\u00ac\5\34\17\2\u00ac\u00ad\7(\2")
        buf.write("\2\u00ad\33\3\2\2\2\u00ae\u00af\7/\2\2\u00af\u00b0\7)")
        buf.write("\2\2\u00b0\u00b3\5\34\17\2\u00b1\u00b3\7/\2\2\u00b2\u00ae")
        buf.write("\3\2\2\2\u00b2\u00b1\3\2\2\2\u00b3\35\3\2\2\2\u00b4\u00b7")
        buf.write("\7+\2\2\u00b5\u00b7\5\66\34\2\u00b6\u00b4\3\2\2\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00b9\7\'\2\2")
        buf.write("\u00b9\u00ba\5.\30\2\u00ba\u00bb\7(\2\2\u00bb\37\3\2\2")
        buf.write("\2\u00bc\u00c8\5\"\22\2\u00bd\u00c8\5(\25\2\u00be\u00c8")
        buf.write("\5*\26\2\u00bf\u00c8\5,\27\2\u00c0\u00c8\5\60\31\2\u00c1")
        buf.write("\u00c8\5\62\32\2\u00c2\u00c8\5\64\33\2\u00c3\u00c4\5\66")
        buf.write("\34\2\u00c4\u00c5\5\b\5\2\u00c5\u00c8\3\2\2\2\u00c6\u00c8")
        buf.write("\5\n\6\2\u00c7\u00bc\3\2\2\2\u00c7\u00bd\3\2\2\2\u00c7")
        buf.write("\u00be\3\2\2\2\u00c7\u00bf\3\2\2\2\u00c7\u00c0\3\2\2\2")
        buf.write("\u00c7\u00c1\3\2\2\2\u00c7\u00c2\3\2\2\2\u00c7\u00c3\3")
        buf.write("\2\2\2\u00c7\u00c6\3\2\2\2\u00c8!\3\2\2\2\u00c9\u00ca")
        buf.write("\7\22\2\2\u00ca\u00cb\5\b\5\2\u00cb\u00cc\5$\23\2\u00cc")
        buf.write("\u00cd\7\23\2\2\u00cd\u00ce\5\b\5\2\u00ce#\3\2\2\2\u00cf")
        buf.write("\u00d2\5&\24\2\u00d0\u00d2\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d0\3\2\2\2\u00d2%\3\2\2\2\u00d3\u00d4\5 \21")
        buf.write("\2\u00d4\u00d5\5&\24\2\u00d5\u00d8\3\2\2\2\u00d6\u00d8")
        buf.write("\5 \21\2\u00d7\u00d3\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("\'\3\2\2\2\u00d9\u00da\7\17\2\2\u00da\u00db\7%\2\2\u00db")
        buf.write("\u00dc\58\35\2\u00dc\u00de\7&\2\2\u00dd\u00df\5\b\5\2")
        buf.write("\u00de\u00dd\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\3")
        buf.write("\2\2\2\u00e0\u00ec\5 \21\2\u00e1\u00e2\7\21\2\2\u00e2")
        buf.write("\u00e3\7%\2\2\u00e3\u00e4\58\35\2\u00e4\u00e6\7&\2\2\u00e5")
        buf.write("\u00e7\5\b\5\2\u00e6\u00e5\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\u00e9\5 \21\2\u00e9\u00eb\3")
        buf.write("\2\2\2\u00ea\u00e1\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00f4\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ef\u00f1\7\20\2\2\u00f0\u00f2\5\b\5")
        buf.write("\2\u00f1\u00f0\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3")
        buf.write("\3\2\2\2\u00f3\u00f5\5 \21\2\u00f4\u00ef\3\2\2\2\u00f4")
        buf.write("\u00f5\3\2\2\2\u00f5)\3\2\2\2\u00f6\u00f7\7\n\2\2\u00f7")
        buf.write("\u00f8\7+\2\2\u00f8\u00f9\7\13\2\2\u00f9\u00fa\58\35\2")
        buf.write("\u00fa\u00fb\7\f\2\2\u00fb\u00fd\58\35\2\u00fc\u00fe\5")
        buf.write("\b\5\2\u00fd\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0100\5 \21\2\u0100+\3\2\2\2\u0101\u0108")
        buf.write("\7+\2\2\u0102\u0103\7+\2\2\u0103\u0104\7\'\2\2\u0104\u0105")
        buf.write("\5.\30\2\u0105\u0106\7(\2\2\u0106\u0108\3\2\2\2\u0107")
        buf.write("\u0101\3\2\2\2\u0107\u0102\3\2\2\2\u0108\u0109\3\2\2\2")
        buf.write("\u0109\u010a\7\35\2\2\u010a\u010b\58\35\2\u010b\u010c")
        buf.write("\5\b\5\2\u010c-\3\2\2\2\u010d\u0113\58\35\2\u010e\u010f")
        buf.write("\58\35\2\u010f\u0110\7)\2\2\u0110\u0111\5.\30\2\u0111")
        buf.write("\u0113\3\2\2\2\u0112\u010d\3\2\2\2\u0112\u010e\3\2\2\2")
        buf.write("\u0113/\3\2\2\2\u0114\u0115\7\16\2\2\u0115\u0116\5\b\5")
        buf.write("\2\u0116\61\3\2\2\2\u0117\u0118\7\r\2\2\u0118\u0119\5")
        buf.write("\b\5\2\u0119\63\3\2\2\2\u011a\u011c\7\6\2\2\u011b\u011d")
        buf.write("\58\35\2\u011c\u011b\3\2\2\2\u011c\u011d\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e\u011f\5\b\5\2\u011f\65\3\2\2\2\u0120")
        buf.write("\u0121\7+\2\2\u0121\u0123\7%\2\2\u0122\u0124\5.\30\2\u0123")
        buf.write("\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0126\7&\2\2\u0126\67\3\2\2\2\u0127\u0128\5:\36")
        buf.write("\2\u0128\u0129\7#\2\2\u0129\u012a\5:\36\2\u012a\u012d")
        buf.write("\3\2\2\2\u012b\u012d\5:\36\2\u012c\u0127\3\2\2\2\u012c")
        buf.write("\u012b\3\2\2\2\u012d9\3\2\2\2\u012e\u012f\5<\37\2\u012f")
        buf.write("\u0130\t\2\2\2\u0130\u0131\5<\37\2\u0131\u0134\3\2\2\2")
        buf.write("\u0132\u0134\5<\37\2\u0133\u012e\3\2\2\2\u0133\u0132\3")
        buf.write("\2\2\2\u0134;\3\2\2\2\u0135\u0136\b\37\1\2\u0136\u0137")
        buf.write("\5> \2\u0137\u013d\3\2\2\2\u0138\u0139\f\4\2\2\u0139\u013a")
        buf.write("\t\3\2\2\u013a\u013c\5> \2\u013b\u0138\3\2\2\2\u013c\u013f")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("=\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0141\b \1\2\u0141")
        buf.write("\u0142\5@!\2\u0142\u0148\3\2\2\2\u0143\u0144\f\4\2\2\u0144")
        buf.write("\u0145\t\4\2\2\u0145\u0147\5@!\2\u0146\u0143\3\2\2\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148\u0149\3\2\2\2")
        buf.write("\u0149?\3\2\2\2\u014a\u0148\3\2\2\2\u014b\u014c\b!\1\2")
        buf.write("\u014c\u014d\5B\"\2\u014d\u0153\3\2\2\2\u014e\u014f\f")
        buf.write("\4\2\2\u014f\u0150\t\5\2\2\u0150\u0152\5B\"\2\u0151\u014e")
        buf.write("\3\2\2\2\u0152\u0155\3\2\2\2\u0153\u0151\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154A\3\2\2\2\u0155\u0153\3\2\2\2\u0156")
        buf.write("\u0157\7\24\2\2\u0157\u015a\5B\"\2\u0158\u015a\5D#\2\u0159")
        buf.write("\u0156\3\2\2\2\u0159\u0158\3\2\2\2\u015aC\3\2\2\2\u015b")
        buf.write("\u015c\7\30\2\2\u015c\u015f\5D#\2\u015d\u015f\5F$\2\u015e")
        buf.write("\u015b\3\2\2\2\u015e\u015d\3\2\2\2\u015fE\3\2\2\2\u0160")
        buf.write("\u0168\7+\2\2\u0161\u0162\7+\2\2\u0162\u0164\7%\2\2\u0163")
        buf.write("\u0165\5.\30\2\u0164\u0163\3\2\2\2\u0164\u0165\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166\u0168\7&\2\2\u0167\u0160\3")
        buf.write("\2\2\2\u0167\u0161\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u016a")
        buf.write("\7\'\2\2\u016a\u016b\5.\30\2\u016b\u016c\7(\2\2\u016c")
        buf.write("\u016f\3\2\2\2\u016d\u016f\5H%\2\u016e\u0167\3\2\2\2\u016e")
        buf.write("\u016d\3\2\2\2\u016fG\3\2\2\2\u0170\u0178\5J&\2\u0171")
        buf.write("\u0172\7%\2\2\u0172\u0173\58\35\2\u0173\u0174\7&\2\2\u0174")
        buf.write("\u0178\3\2\2\2\u0175\u0178\7+\2\2\u0176\u0178\5\66\34")
        buf.write("\2\u0177\u0170\3\2\2\2\u0177\u0171\3\2\2\2\u0177\u0175")
        buf.write("\3\2\2\2\u0177\u0176\3\2\2\2\u0178I\3\2\2\2\u0179\u017e")
        buf.write("\5N(\2\u017a\u017e\7/\2\2\u017b\u017e\7,\2\2\u017c\u017e")
        buf.write("\7\60\2\2\u017d\u0179\3\2\2\2\u017d\u017a\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017c\3\2\2\2\u017eK\3\2\2\2\u017f")
        buf.write("\u0180\t\6\2\2\u0180M\3\2\2\2\u0181\u0182\7\'\2\2\u0182")
        buf.write("\u0183\5.\30\2\u0183\u0184\7(\2\2\u0184O\3\2\2\2+S]af")
        buf.write("kuy\u0084\u008c\u0090\u0094\u0098\u009f\u00a7\u00b2\u00b6")
        buf.write("\u00c7\u00d1\u00d7\u00de\u00e6\u00ec\u00f1\u00f4\u00fd")
        buf.write("\u0107\u0112\u011c\u0123\u012c\u0133\u013d\u0148\u0153")
        buf.write("\u0159\u015e\u0164\u0167\u016e\u0177\u017d")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'number'", "'bool'", "'string'", "'return'", 
                     "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'if'", "'else'", 
                     "'elif'", "'begin'", "'end'", "'not'", "'and'", "'or'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'...'", "'=='", "'('", 
                     "')'", "'['", "']'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "BOOL", "STRING", "RETURN", 
                      "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", 
                      "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", "END", 
                      "NOT", "AND", "OR", "PLUS", "MINUS", "MUL", "DIV", 
                      "MOD", "EQ_STR", "ASSIGN", "DIFFER", "LT", "LE", "GT", 
                      "GE", "CONCAT", "EQ_NUM", "LP", "RP", "LS", "RS", 
                      "COMMA", "NEWLINE", "ID", "BOO_LIT", "TRUE", "FALSE", 
                      "NUM_LIT", "STR_LIT", "COMMENT", "WS", "UNCLOSE_STRING", 
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

    ruleNames =  [ "program", "decl_list", "decl", "ignore", "vars_decl", 
                   "norm_decl", "var_decl", "dynamic_decl", "funs_decl", 
                   "formal_params", "formal_pms_prm", "formal_pm", "array_type", 
                   "dim_list", "array_ele", "stmt", "block_stmt", "stmtlist", 
                   "stmtprime", "if_stmt", "for_stmt", "assign_stmt", "index_ops", 
                   "continue_stmt", "break_stmt", "return_stmt", "fun_call", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "exp7", "exp8", "array_val", "scalar_type", "array_list" ]

    EOF = Token.EOF
    NUMBER=1
    BOOL=2
    STRING=3
    RETURN=4
    VAR=5
    DYNAMIC=6
    FUNC=7
    FOR=8
    UNTIL=9
    BY=10
    BREAK=11
    CONTINUE=12
    IF=13
    ELSE=14
    ELIF=15
    BEGIN=16
    END=17
    NOT=18
    AND=19
    OR=20
    PLUS=21
    MINUS=22
    MUL=23
    DIV=24
    MOD=25
    EQ_STR=26
    ASSIGN=27
    DIFFER=28
    LT=29
    LE=30
    GT=31
    GE=32
    CONCAT=33
    EQ_NUM=34
    LP=35
    RP=36
    LS=37
    RS=38
    COMMA=39
    NEWLINE=40
    ID=41
    BOO_LIT=42
    TRUE=43
    FALSE=44
    NUM_LIT=45
    STR_LIT=46
    COMMENT=47
    WS=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

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
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZCodeParser.NEWLINE:
                self.state = 78
                self.match(ZCodeParser.NEWLINE)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.decl_list()
            self.state = 85
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
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.decl()
                self.state = 88
                self.decl_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
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
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.VAR, ZCodeParser.DYNAMIC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.vars_decl()
                pass
            elif token in [ZCodeParser.FUNC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
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
            self.state = 98 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 97
                self.match(ZCodeParser.NEWLINE)
                self.state = 100 
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
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.state = 102
                self.norm_decl()
                pass
            elif token in [ZCodeParser.VAR]:
                self.state = 103
                self.var_decl()
                pass
            elif token in [ZCodeParser.DYNAMIC]:
                self.state = 104
                self.dynamic_decl()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 107
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
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 109
                self.scalar_type()
                self.state = 110
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 112
                self.scalar_type()
                self.state = 113
                self.array_type()
                pass


            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 117
                self.match(ZCodeParser.ASSIGN)
                self.state = 118
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
            self.state = 121
            self.match(ZCodeParser.VAR)
            self.state = 122
            self.match(ZCodeParser.ID)
            self.state = 123
            self.match(ZCodeParser.ASSIGN)
            self.state = 124
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
            self.state = 126
            self.match(ZCodeParser.DYNAMIC)
            self.state = 127
            self.match(ZCodeParser.ID)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.ASSIGN:
                self.state = 128
                self.match(ZCodeParser.ASSIGN)
                self.state = 129
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
            self.state = 132
            self.match(ZCodeParser.FUNC)
            self.state = 133
            self.match(ZCodeParser.ID)
            self.state = 134
            self.match(ZCodeParser.LP)
            self.state = 135
            self.formal_params()
            self.state = 136
            self.match(ZCodeParser.RP)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 137
                    self.ignore()


                self.state = 140
                self.block_stmt()
                pass

            elif la_ == 2:
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 141
                    self.ignore()


                self.state = 144
                self.return_stmt()
                pass

            elif la_ == 3:
                self.state = 145
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
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 148
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.formal_pm()
                self.state = 153
                self.match(ZCodeParser.COMMA)
                self.state = 154
                self.formal_pms_prm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
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
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.scalar_type()
                self.state = 160
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.scalar_type()
                self.state = 163
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
            self.state = 167
            self.match(ZCodeParser.ID)
            self.state = 168
            self.match(ZCodeParser.LS)
            self.state = 169
            self.dim_list()
            self.state = 170
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
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(ZCodeParser.NUM_LIT)
                self.state = 173
                self.match(ZCodeParser.COMMA)
                self.state = 174
                self.dim_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
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
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 178
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 179
                self.fun_call()
                pass


            self.state = 182
            self.match(ZCodeParser.LS)
            self.state = 183
            self.index_ops()
            self.state = 184
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
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.block_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 188
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 189
                self.assign_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.continue_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 191
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 192
                self.return_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 193
                self.fun_call()
                self.state = 194
                self.ignore()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 196
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
            self.state = 199
            self.match(ZCodeParser.BEGIN)
            self.state = 200
            self.ignore()
            self.state = 201
            self.stmtlist()
            self.state = 202
            self.match(ZCodeParser.END)
            self.state = 203
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
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER, ZCodeParser.BOOL, ZCodeParser.STRING, ZCodeParser.RETURN, ZCodeParser.VAR, ZCodeParser.DYNAMIC, ZCodeParser.FOR, ZCodeParser.BREAK, ZCodeParser.CONTINUE, ZCodeParser.IF, ZCodeParser.BEGIN, ZCodeParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
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
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.stmt()
                self.state = 210
                self.stmtprime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 212
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
            self.state = 215
            self.match(ZCodeParser.IF)
            self.state = 216
            self.match(ZCodeParser.LP)
            self.state = 217
            self.exp()
            self.state = 218
            self.match(ZCodeParser.RP)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 219
                self.ignore()


            self.state = 222
            self.stmt()
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 223
                    self.match(ZCodeParser.ELIF)
                    self.state = 224
                    self.match(ZCodeParser.LP)
                    self.state = 225
                    self.exp()
                    self.state = 226
                    self.match(ZCodeParser.RP)
                    self.state = 228
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZCodeParser.NEWLINE:
                        self.state = 227
                        self.ignore()


                    self.state = 230
                    self.stmt() 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 237
                self.match(ZCodeParser.ELSE)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.NEWLINE:
                    self.state = 238
                    self.ignore()


                self.state = 241
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
            self.state = 244
            self.match(ZCodeParser.FOR)
            self.state = 245
            self.match(ZCodeParser.ID)
            self.state = 246
            self.match(ZCodeParser.UNTIL)
            self.state = 247
            self.exp()
            self.state = 248
            self.match(ZCodeParser.BY)
            self.state = 249
            self.exp()
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.NEWLINE:
                self.state = 250
                self.ignore()


            self.state = 253
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
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 255
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 2:
                self.state = 256
                self.match(ZCodeParser.ID)
                self.state = 257
                self.match(ZCodeParser.LS)
                self.state = 258
                self.index_ops()
                self.state = 259
                self.match(ZCodeParser.RS)
                pass


            self.state = 263
            self.match(ZCodeParser.ASSIGN)
            self.state = 264
            self.exp()
            self.state = 265
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
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.exp()
                self.state = 269
                self.match(ZCodeParser.COMMA)
                self.state = 270
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
            self.state = 274
            self.match(ZCodeParser.CONTINUE)
            self.state = 275
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
            self.state = 277
            self.match(ZCodeParser.BREAK)
            self.state = 278
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
            self.state = 280
            self.match(ZCodeParser.RETURN)
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.BOO_LIT) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                self.state = 281
                self.exp()


            self.state = 284
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
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ZCodeParser.ID)
            self.state = 287
            self.match(ZCodeParser.LP)
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.BOO_LIT) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                self.state = 288
                self.index_ops()


            self.state = 291
            self.match(ZCodeParser.RP)
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
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.exp1()
                self.state = 294
                self.match(ZCodeParser.CONCAT)
                self.state = 295
                self.exp1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
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
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.exp2(0)
                self.state = 301
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.EQ_STR) | (1 << ZCodeParser.DIFFER) | (1 << ZCodeParser.LT) | (1 << ZCodeParser.LE) | (1 << ZCodeParser.GT) | (1 << ZCodeParser.GE) | (1 << ZCodeParser.EQ_NUM))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 302
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
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
            self.state = 308
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 315
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 310
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 311
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.AND or _la==ZCodeParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 312
                    self.exp3(0) 
                self.state = 317
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
            self.state = 319
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 321
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 322
                    _la = self._input.LA(1)
                    if not(_la==ZCodeParser.PLUS or _la==ZCodeParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 323
                    self.exp4(0) 
                self.state = 328
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
            self.state = 330
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 332
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 333
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.MUL) | (1 << ZCodeParser.DIV) | (1 << ZCodeParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 334
                    self.exp5() 
                self.state = 339
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
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(ZCodeParser.NOT)
                self.state = 341
                self.exp5()
                pass
            elif token in [ZCodeParser.MINUS, ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.ID, ZCodeParser.BOO_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
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
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.MINUS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(ZCodeParser.MINUS)
                self.state = 346
                self.exp6()
                pass
            elif token in [ZCodeParser.LP, ZCodeParser.LS, ZCodeParser.ID, ZCodeParser.BOO_LIT, ZCodeParser.NUM_LIT, ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
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
            self.state = 364
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 350
                    self.match(ZCodeParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 351
                    self.match(ZCodeParser.ID)
                    self.state = 352
                    self.match(ZCodeParser.LP)
                    self.state = 354
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.NOT) | (1 << ZCodeParser.MINUS) | (1 << ZCodeParser.LP) | (1 << ZCodeParser.LS) | (1 << ZCodeParser.ID) | (1 << ZCodeParser.BOO_LIT) | (1 << ZCodeParser.NUM_LIT) | (1 << ZCodeParser.STR_LIT))) != 0):
                        self.state = 353
                        self.index_ops()


                    self.state = 356
                    self.match(ZCodeParser.RP)
                    pass


                self.state = 359
                self.match(ZCodeParser.LS)
                self.state = 360
                self.index_ops()
                self.state = 361
                self.match(ZCodeParser.RS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.match(ZCodeParser.LP)
                self.state = 368
                self.exp()
                self.state = 369
                self.match(ZCodeParser.RP)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.match(ZCodeParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
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
            self.state = 379
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.LS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 375
                self.array_list()
                pass
            elif token in [ZCodeParser.NUM_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
                self.match(ZCodeParser.NUM_LIT)
                pass
            elif token in [ZCodeParser.BOO_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 377
                self.match(ZCodeParser.BOO_LIT)
                pass
            elif token in [ZCodeParser.STR_LIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 378
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
            self.state = 381
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
            self.state = 383
            self.match(ZCodeParser.LS)
            self.state = 384
            self.index_ops()
            self.state = 385
            self.match(ZCodeParser.RS)
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
         




