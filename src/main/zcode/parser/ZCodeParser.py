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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\7\2\2\3\5\3\3\2\2\2\2")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'='", 
                     "'<-'", "'!='", "'<'", "'<='", "'>'", "'>='", "'...'", 
                     "'=='", "'('", "')'", "'['", "']'", "','", "';'", "'true'", 
                     "'false'", "'number'", "'bool'", "'string'", "'return'", 
                     "'var'", "'dynamic'", "'func'", "'for'", "'until'", 
                     "'by'", "'break'", "'continue'", "'if'", "'else'", 
                     "'elif'", "'begin'", "'end'", "'not'", "'and'", "'or'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "MUL", "DIV", "MOD", 
                      "EQ_STR", "ASSIGN", "DIFFER", "LT", "LE", "GT", "GE", 
                      "CONCAT", "EQ_NUM", "LP", "RP", "LS", "RS", "COMMA", 
                      "SEMI", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "NUM_LIT", "BOO_LIT", "STR_LIT", 
                      "NEWLINE", "ID", "COMMENT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    MUL=3
    DIV=4
    MOD=5
    EQ_STR=6
    ASSIGN=7
    DIFFER=8
    LT=9
    LE=10
    GT=11
    GE=12
    CONCAT=13
    EQ_NUM=14
    LP=15
    RP=16
    LS=17
    RS=18
    COMMA=19
    SEMI=20
    TRUE=21
    FALSE=22
    NUMBER=23
    BOOL=24
    STRING=25
    RETURN=26
    VAR=27
    DYNAMIC=28
    FUNC=29
    FOR=30
    UNTIL=31
    BY=32
    BREAK=33
    CONTINUE=34
    IF=35
    ELSE=36
    ELIF=37
    BEGIN=38
    END=39
    NOT=40
    AND=41
    OR=42
    NUM_LIT=43
    BOO_LIT=44
    STR_LIT=45
    NEWLINE=46
    ID=47
    COMMENT=48
    WS=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51
    ERROR_CHAR=52

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
            self.state = 2
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





