# Generated from compil/grammar/nevermorecompiler.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,36,221,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,
        1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,13,1,14,1,14,5,14,147,8,14,10,14,12,14,150,9,14,1,
        15,1,15,1,16,4,16,155,8,16,11,16,12,16,156,1,17,4,17,160,8,17,11,
        17,12,17,161,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,
        22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,
        28,1,28,1,29,1,29,1,29,1,30,1,30,1,31,1,31,1,32,1,32,1,32,1,33,1,
        33,1,33,1,34,1,34,1,35,1,35,1,35,1,35,1,36,1,36,5,36,210,8,36,10,
        36,12,36,213,9,36,1,36,1,36,1,37,3,37,218,8,37,1,37,1,37,0,0,38,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,
        27,14,29,15,31,0,33,0,35,16,37,17,39,18,41,19,43,20,45,21,47,22,
        49,23,51,24,53,25,55,26,57,27,59,28,61,29,63,30,65,31,67,32,69,33,
        71,34,73,35,75,36,1,0,4,1,0,48,57,3,0,65,90,97,122,1040,1103,3,0,
        9,10,13,13,32,32,2,0,10,10,13,13,223,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,
        0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,
        0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,
        0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,
        0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,
        0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,1,77,1,0,0,0,3,80,1,
        0,0,0,5,85,1,0,0,0,7,89,1,0,0,0,9,95,1,0,0,0,11,98,1,0,0,0,13,104,
        1,0,0,0,15,112,1,0,0,0,17,114,1,0,0,0,19,118,1,0,0,0,21,125,1,0,
        0,0,23,132,1,0,0,0,25,134,1,0,0,0,27,139,1,0,0,0,29,144,1,0,0,0,
        31,151,1,0,0,0,33,154,1,0,0,0,35,159,1,0,0,0,37,163,1,0,0,0,39,167,
        1,0,0,0,41,169,1,0,0,0,43,171,1,0,0,0,45,173,1,0,0,0,47,175,1,0,
        0,0,49,177,1,0,0,0,51,179,1,0,0,0,53,181,1,0,0,0,55,183,1,0,0,0,
        57,185,1,0,0,0,59,188,1,0,0,0,61,191,1,0,0,0,63,193,1,0,0,0,65,195,
        1,0,0,0,67,198,1,0,0,0,69,201,1,0,0,0,71,203,1,0,0,0,73,207,1,0,
        0,0,75,217,1,0,0,0,77,78,5,105,0,0,78,79,5,102,0,0,79,2,1,0,0,0,
        80,81,5,101,0,0,81,82,5,108,0,0,82,83,5,115,0,0,83,84,5,101,0,0,
        84,4,1,0,0,0,85,86,5,102,0,0,86,87,5,111,0,0,87,88,5,114,0,0,88,
        6,1,0,0,0,89,90,5,119,0,0,90,91,5,104,0,0,91,92,5,105,0,0,92,93,
        5,108,0,0,93,94,5,101,0,0,94,8,1,0,0,0,95,96,5,100,0,0,96,97,5,111,
        0,0,97,10,1,0,0,0,98,99,5,112,0,0,99,100,5,114,0,0,100,101,5,105,
        0,0,101,102,5,110,0,0,102,103,5,116,0,0,103,12,1,0,0,0,104,105,5,
        103,0,0,105,106,5,108,0,0,106,107,5,111,0,0,107,108,5,98,0,0,108,
        109,5,97,0,0,109,110,5,108,0,0,110,111,5,58,0,0,111,14,1,0,0,0,112,
        113,5,58,0,0,113,16,1,0,0,0,114,115,5,105,0,0,115,116,5,110,0,0,
        116,117,5,116,0,0,117,18,1,0,0,0,118,119,5,100,0,0,119,120,5,111,
        0,0,120,121,5,117,0,0,121,122,5,98,0,0,122,123,5,108,0,0,123,124,
        5,101,0,0,124,20,1,0,0,0,125,126,5,114,0,0,126,127,5,101,0,0,127,
        128,5,116,0,0,128,129,5,117,0,0,129,130,5,114,0,0,130,131,5,110,
        0,0,131,22,1,0,0,0,132,133,5,44,0,0,133,24,1,0,0,0,134,135,5,118,
        0,0,135,136,5,111,0,0,136,137,5,105,0,0,137,138,5,100,0,0,138,26,
        1,0,0,0,139,140,5,99,0,0,140,141,5,97,0,0,141,142,5,108,0,0,142,
        143,5,108,0,0,143,28,1,0,0,0,144,148,3,33,16,0,145,147,3,31,15,0,
        146,145,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,
        149,30,1,0,0,0,150,148,1,0,0,0,151,152,7,0,0,0,152,32,1,0,0,0,153,
        155,7,1,0,0,154,153,1,0,0,0,155,156,1,0,0,0,156,154,1,0,0,0,156,
        157,1,0,0,0,157,34,1,0,0,0,158,160,3,31,15,0,159,158,1,0,0,0,160,
        161,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,36,1,0,0,0,163,164,
        3,35,17,0,164,165,5,46,0,0,165,166,3,35,17,0,166,38,1,0,0,0,167,
        168,5,59,0,0,168,40,1,0,0,0,169,170,5,43,0,0,170,42,1,0,0,0,171,
        172,5,45,0,0,172,44,1,0,0,0,173,174,5,42,0,0,174,46,1,0,0,0,175,
        176,5,47,0,0,176,48,1,0,0,0,177,178,5,40,0,0,178,50,1,0,0,0,179,
        180,5,41,0,0,180,52,1,0,0,0,181,182,5,62,0,0,182,54,1,0,0,0,183,
        184,5,60,0,0,184,56,1,0,0,0,185,186,5,61,0,0,186,187,5,61,0,0,187,
        58,1,0,0,0,188,189,5,33,0,0,189,190,5,61,0,0,190,60,1,0,0,0,191,
        192,5,123,0,0,192,62,1,0,0,0,193,194,5,125,0,0,194,64,1,0,0,0,195,
        196,3,41,20,0,196,197,3,41,20,0,197,66,1,0,0,0,198,199,3,43,21,0,
        199,200,3,43,21,0,200,68,1,0,0,0,201,202,5,61,0,0,202,70,1,0,0,0,
        203,204,7,2,0,0,204,205,1,0,0,0,205,206,6,35,0,0,206,72,1,0,0,0,
        207,211,5,35,0,0,208,210,8,3,0,0,209,208,1,0,0,0,210,213,1,0,0,0,
        211,209,1,0,0,0,211,212,1,0,0,0,212,214,1,0,0,0,213,211,1,0,0,0,
        214,215,6,36,0,0,215,74,1,0,0,0,216,218,5,13,0,0,217,216,1,0,0,0,
        217,218,1,0,0,0,218,219,1,0,0,0,219,220,5,10,0,0,220,76,1,0,0,0,
        6,0,148,156,161,211,217,1,6,0,0
    ]

class nevermorecompilerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    ID = 15
    INT = 16
    DOUBLE = 17
    END_STATE = 18
    ADD = 19
    SUB = 20
    MUL = 21
    DIV = 22
    LPAREN = 23
    RPAREN = 24
    GT = 25
    LT = 26
    EQ_EQ = 27
    NOT_EQ = 28
    RCORNER = 29
    LCORNER = 30
    INCREMENT = 31
    DECREMENT = 32
    EQ = 33
    WS = 34
    SINGLE_LINE_COMMENT = 35
    NEWLINE = 36

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'if'", "'else'", "'for'", "'while'", "'do'", "'print'", "'global:'", 
            "':'", "'int'", "'double'", "'return'", "','", "'void'", "'call'", 
            "';'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'>'", "'<'", 
            "'=='", "'!='", "'{'", "'}'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "DOUBLE", "END_STATE", "ADD", "SUB", "MUL", "DIV", 
            "LPAREN", "RPAREN", "GT", "LT", "EQ_EQ", "NOT_EQ", "RCORNER", 
            "LCORNER", "INCREMENT", "DECREMENT", "EQ", "WS", "SINGLE_LINE_COMMENT", 
            "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "ID", "DIGIT", "LETTER", "INT", "DOUBLE", "END_STATE", 
                  "ADD", "SUB", "MUL", "DIV", "LPAREN", "RPAREN", "GT", 
                  "LT", "EQ_EQ", "NOT_EQ", "RCORNER", "LCORNER", "INCREMENT", 
                  "DECREMENT", "EQ", "WS", "SINGLE_LINE_COMMENT", "NEWLINE" ]

    grammarFileName = "nevermorecompiler.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


