# Generated from d://NLNNLT//Zcode//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,47,288,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,
        1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,
        1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,
        1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,
        1,29,1,29,1,29,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,
        1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,
        1,36,1,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,
        1,40,1,40,1,40,1,41,1,41,5,41,259,8,41,10,41,12,41,262,9,41,1,42,
        4,42,265,8,42,11,42,12,42,266,1,42,1,42,1,43,1,43,1,43,1,43,5,43,
        275,8,43,10,43,12,43,278,9,43,1,43,1,43,1,44,1,44,1,44,1,45,1,45,
        1,46,1,46,1,276,0,47,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
        10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,
        21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,63,
        32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,85,
        43,87,44,89,45,91,46,93,47,1,0,3,3,0,65,90,95,95,97,122,4,0,48,57,
        65,90,95,95,97,122,3,0,8,10,12,13,32,32,290,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,
        0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,
        0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,
        0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,
        0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,
        0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,
        0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,
        0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,
        0,1,95,1,0,0,0,3,97,1,0,0,0,5,99,1,0,0,0,7,101,1,0,0,0,9,103,1,0,
        0,0,11,105,1,0,0,0,13,107,1,0,0,0,15,110,1,0,0,0,17,113,1,0,0,0,
        19,115,1,0,0,0,21,118,1,0,0,0,23,120,1,0,0,0,25,123,1,0,0,0,27,127,
        1,0,0,0,29,130,1,0,0,0,31,132,1,0,0,0,33,134,1,0,0,0,35,136,1,0,
        0,0,37,138,1,0,0,0,39,140,1,0,0,0,41,145,1,0,0,0,43,151,1,0,0,0,
        45,158,1,0,0,0,47,163,1,0,0,0,49,170,1,0,0,0,51,177,1,0,0,0,53,181,
        1,0,0,0,55,189,1,0,0,0,57,194,1,0,0,0,59,198,1,0,0,0,61,204,1,0,
        0,0,63,207,1,0,0,0,65,213,1,0,0,0,67,222,1,0,0,0,69,225,1,0,0,0,
        71,230,1,0,0,0,73,235,1,0,0,0,75,241,1,0,0,0,77,245,1,0,0,0,79,249,
        1,0,0,0,81,253,1,0,0,0,83,256,1,0,0,0,85,264,1,0,0,0,87,270,1,0,
        0,0,89,281,1,0,0,0,91,284,1,0,0,0,93,286,1,0,0,0,95,96,5,43,0,0,
        96,2,1,0,0,0,97,98,5,45,0,0,98,4,1,0,0,0,99,100,5,42,0,0,100,6,1,
        0,0,0,101,102,5,47,0,0,102,8,1,0,0,0,103,104,5,37,0,0,104,10,1,0,
        0,0,105,106,5,61,0,0,106,12,1,0,0,0,107,108,5,60,0,0,108,109,5,45,
        0,0,109,14,1,0,0,0,110,111,5,33,0,0,111,112,5,61,0,0,112,16,1,0,
        0,0,113,114,5,60,0,0,114,18,1,0,0,0,115,116,5,60,0,0,116,117,5,61,
        0,0,117,20,1,0,0,0,118,119,5,62,0,0,119,22,1,0,0,0,120,121,5,62,
        0,0,121,122,5,61,0,0,122,24,1,0,0,0,123,124,5,46,0,0,124,125,5,46,
        0,0,125,126,5,46,0,0,126,26,1,0,0,0,127,128,5,61,0,0,128,129,5,61,
        0,0,129,28,1,0,0,0,130,131,5,40,0,0,131,30,1,0,0,0,132,133,5,41,
        0,0,133,32,1,0,0,0,134,135,5,91,0,0,135,34,1,0,0,0,136,137,5,93,
        0,0,137,36,1,0,0,0,138,139,5,44,0,0,139,38,1,0,0,0,140,141,5,116,
        0,0,141,142,5,114,0,0,142,143,5,117,0,0,143,144,5,101,0,0,144,40,
        1,0,0,0,145,146,5,102,0,0,146,147,5,97,0,0,147,148,5,108,0,0,148,
        149,5,115,0,0,149,150,5,101,0,0,150,42,1,0,0,0,151,152,5,110,0,0,
        152,153,5,117,0,0,153,154,5,109,0,0,154,155,5,98,0,0,155,156,5,101,
        0,0,156,157,5,114,0,0,157,44,1,0,0,0,158,159,5,98,0,0,159,160,5,
        111,0,0,160,161,5,111,0,0,161,162,5,108,0,0,162,46,1,0,0,0,163,164,
        5,115,0,0,164,165,5,116,0,0,165,166,5,114,0,0,166,167,5,105,0,0,
        167,168,5,110,0,0,168,169,5,103,0,0,169,48,1,0,0,0,170,171,5,114,
        0,0,171,172,5,101,0,0,172,173,5,116,0,0,173,174,5,117,0,0,174,175,
        5,114,0,0,175,176,5,110,0,0,176,50,1,0,0,0,177,178,5,118,0,0,178,
        179,5,97,0,0,179,180,5,114,0,0,180,52,1,0,0,0,181,182,5,100,0,0,
        182,183,5,121,0,0,183,184,5,110,0,0,184,185,5,97,0,0,185,186,5,109,
        0,0,186,187,5,105,0,0,187,188,5,99,0,0,188,54,1,0,0,0,189,190,5,
        102,0,0,190,191,5,117,0,0,191,192,5,110,0,0,192,193,5,99,0,0,193,
        56,1,0,0,0,194,195,5,102,0,0,195,196,5,111,0,0,196,197,5,114,0,0,
        197,58,1,0,0,0,198,199,5,117,0,0,199,200,5,110,0,0,200,201,5,116,
        0,0,201,202,5,105,0,0,202,203,5,108,0,0,203,60,1,0,0,0,204,205,5,
        98,0,0,205,206,5,121,0,0,206,62,1,0,0,0,207,208,5,98,0,0,208,209,
        5,114,0,0,209,210,5,101,0,0,210,211,5,97,0,0,211,212,5,107,0,0,212,
        64,1,0,0,0,213,214,5,99,0,0,214,215,5,111,0,0,215,216,5,110,0,0,
        216,217,5,116,0,0,217,218,5,105,0,0,218,219,5,110,0,0,219,220,5,
        117,0,0,220,221,5,101,0,0,221,66,1,0,0,0,222,223,5,105,0,0,223,224,
        5,102,0,0,224,68,1,0,0,0,225,226,5,101,0,0,226,227,5,108,0,0,227,
        228,5,115,0,0,228,229,5,101,0,0,229,70,1,0,0,0,230,231,5,101,0,0,
        231,232,5,108,0,0,232,233,5,105,0,0,233,234,5,102,0,0,234,72,1,0,
        0,0,235,236,5,98,0,0,236,237,5,101,0,0,237,238,5,103,0,0,238,239,
        5,105,0,0,239,240,5,110,0,0,240,74,1,0,0,0,241,242,5,101,0,0,242,
        243,5,110,0,0,243,244,5,100,0,0,244,76,1,0,0,0,245,246,5,110,0,0,
        246,247,5,111,0,0,247,248,5,116,0,0,248,78,1,0,0,0,249,250,5,97,
        0,0,250,251,5,110,0,0,251,252,5,100,0,0,252,80,1,0,0,0,253,254,5,
        111,0,0,254,255,5,114,0,0,255,82,1,0,0,0,256,260,7,0,0,0,257,259,
        7,1,0,0,258,257,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,
        1,0,0,0,261,84,1,0,0,0,262,260,1,0,0,0,263,265,7,2,0,0,264,263,1,
        0,0,0,265,266,1,0,0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,268,1,
        0,0,0,268,269,6,42,0,0,269,86,1,0,0,0,270,271,5,35,0,0,271,272,5,
        35,0,0,272,276,1,0,0,0,273,275,9,0,0,0,274,273,1,0,0,0,275,278,1,
        0,0,0,276,277,1,0,0,0,276,274,1,0,0,0,277,279,1,0,0,0,278,276,1,
        0,0,0,279,280,6,43,0,0,280,88,1,0,0,0,281,282,9,0,0,0,282,283,6,
        44,1,0,283,90,1,0,0,0,284,285,9,0,0,0,285,92,1,0,0,0,286,287,9,0,
        0,0,287,94,1,0,0,0,4,0,260,266,276,2,6,0,0,1,44,0
    ]

class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    MUL = 3
    DIV = 4
    MOD = 5
    ASS = 6
    ARROW = 7
    DIFFER = 8
    LT = 9
    LE = 10
    GT = 11
    GE = 12
    SPREAD = 13
    EQ = 14
    LP = 15
    RP = 16
    LS = 17
    RS = 18
    COMMA = 19
    TRUE = 20
    FALSE = 21
    NUMBER = 22
    BOOL = 23
    STRING = 24
    RETURN = 25
    VAR = 26
    DYNAMIC = 27
    FUNC = 28
    FOR = 29
    UNTIL = 30
    BY = 31
    BREAK = 32
    CONTINUE = 33
    IF = 34
    ELSE = 35
    ELIF = 36
    BEGIN = 37
    END = 38
    NOT = 39
    AND = 40
    OR = 41
    IDENTIFIER = 42
    WS = 43
    COMMENT = 44
    ERROR_CHAR = 45
    UNCLOSE_STRING = 46
    ILLEGAL_ESCAPE = 47

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'='", "'<-'", "'!='", "'<'", 
            "'<='", "'>'", "'>='", "'...'", "'=='", "'('", "')'", "'['", 
            "']'", "','", "'true'", "'false'", "'number'", "'bool'", "'string'", 
            "'return'", "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
            "'by'", "'break'", "'continue'", "'if'", "'else'", "'elif'", 
            "'begin'", "'end'", "'not'", "'and'", "'or'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "MUL", "DIV", "MOD", "ASS", "ARROW", "DIFFER", 
            "LT", "LE", "GT", "GE", "SPREAD", "EQ", "LP", "RP", "LS", "RS", 
            "COMMA", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", "RETURN", 
            "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", 
            "IF", "ELSE", "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "IDENTIFIER", 
            "WS", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "PLUS", "MINUS", "MUL", "DIV", "MOD", "ASS", "ARROW", 
                  "DIFFER", "LT", "LE", "GT", "GE", "SPREAD", "EQ", "LP", 
                  "RP", "LS", "RS", "COMMA", "TRUE", "FALSE", "NUMBER", 
                  "BOOL", "STRING", "RETURN", "VAR", "DYNAMIC", "FUNC", 
                  "FOR", "UNTIL", "BY", "BREAK", "CONTINUE", "IF", "ELSE", 
                  "ELIF", "BEGIN", "END", "NOT", "AND", "OR", "IDENTIFIER", 
                  "WS", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[44] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


