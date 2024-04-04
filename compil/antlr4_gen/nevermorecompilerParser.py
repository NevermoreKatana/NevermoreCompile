# Generated from nevermorecompiler.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,299,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,3,0,64,8,0,1,0,5,0,67,
        8,0,10,0,12,0,70,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,86,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,5,4,107,8,4,10,4,12,4,110,9,4,
        1,5,5,5,113,8,5,10,5,12,5,116,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,5,9,140,
        8,9,10,9,12,9,143,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,5,12,165,
        8,12,10,12,12,12,168,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,
        177,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,188,8,
        13,10,13,12,13,191,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,
        1,16,1,16,5,16,203,8,16,10,16,12,16,206,9,16,1,16,1,16,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,
        1,20,1,21,1,21,1,22,1,22,1,22,1,22,3,22,232,8,22,1,22,1,22,1,22,
        1,22,3,22,238,8,22,1,22,1,22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,
        1,24,1,24,1,24,1,24,5,24,253,8,24,10,24,12,24,256,9,24,3,24,258,
        8,24,1,25,5,25,261,8,25,10,25,12,25,264,9,25,1,26,1,26,1,27,1,27,
        1,27,1,27,3,27,272,8,27,1,28,1,28,1,28,1,28,3,28,278,8,28,1,29,1,
        29,1,29,5,29,283,8,29,10,29,12,29,286,9,29,3,29,288,8,29,1,30,1,
        30,1,30,3,30,293,8,30,1,30,1,30,3,30,297,8,30,1,30,0,1,26,31,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,0,6,1,0,31,32,1,0,20,21,1,0,18,19,1,0,14,16,1,
        0,25,28,1,0,9,10,307,0,63,1,0,0,0,2,85,1,0,0,0,4,87,1,0,0,0,6,94,
        1,0,0,0,8,108,1,0,0,0,10,114,1,0,0,0,12,117,1,0,0,0,14,129,1,0,0,
        0,16,132,1,0,0,0,18,141,1,0,0,0,20,144,1,0,0,0,22,153,1,0,0,0,24,
        166,1,0,0,0,26,176,1,0,0,0,28,192,1,0,0,0,30,198,1,0,0,0,32,200,
        1,0,0,0,34,209,1,0,0,0,36,213,1,0,0,0,38,217,1,0,0,0,40,219,1,0,
        0,0,42,225,1,0,0,0,44,227,1,0,0,0,46,242,1,0,0,0,48,257,1,0,0,0,
        50,262,1,0,0,0,52,265,1,0,0,0,54,271,1,0,0,0,56,277,1,0,0,0,58,287,
        1,0,0,0,60,289,1,0,0,0,62,64,3,32,16,0,63,62,1,0,0,0,63,64,1,0,0,
        0,64,68,1,0,0,0,65,67,3,44,22,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,
        1,0,0,0,68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,5,0,0,1,
        72,1,1,0,0,0,73,86,3,40,20,0,74,86,3,28,14,0,75,86,3,4,2,0,76,86,
        3,6,3,0,77,86,3,12,6,0,78,86,3,20,10,0,79,86,3,22,11,0,80,86,3,32,
        16,0,81,86,3,44,22,0,82,86,3,60,30,0,83,86,3,46,23,0,84,86,5,36,
        0,0,85,73,1,0,0,0,85,74,1,0,0,0,85,75,1,0,0,0,85,76,1,0,0,0,85,77,
        1,0,0,0,85,78,1,0,0,0,85,79,1,0,0,0,85,80,1,0,0,0,85,81,1,0,0,0,
        85,82,1,0,0,0,85,83,1,0,0,0,85,84,1,0,0,0,86,3,1,0,0,0,87,88,5,1,
        0,0,88,89,3,36,18,0,89,90,5,29,0,0,90,91,3,8,4,0,91,92,5,30,0,0,
        92,93,5,17,0,0,93,5,1,0,0,0,94,95,5,1,0,0,95,96,3,36,18,0,96,97,
        5,29,0,0,97,98,3,8,4,0,98,99,5,30,0,0,99,100,5,2,0,0,100,101,5,29,
        0,0,101,102,3,10,5,0,102,103,5,30,0,0,103,104,5,17,0,0,104,7,1,0,
        0,0,105,107,3,2,1,0,106,105,1,0,0,0,107,110,1,0,0,0,108,106,1,0,
        0,0,108,109,1,0,0,0,109,9,1,0,0,0,110,108,1,0,0,0,111,113,3,2,1,
        0,112,111,1,0,0,0,113,116,1,0,0,0,114,112,1,0,0,0,114,115,1,0,0,
        0,115,11,1,0,0,0,116,114,1,0,0,0,117,118,5,3,0,0,118,119,5,23,0,
        0,119,120,3,16,8,0,120,121,3,36,18,0,121,122,5,17,0,0,122,123,3,
        14,7,0,123,124,5,24,0,0,124,125,5,29,0,0,125,126,3,18,9,0,126,127,
        5,30,0,0,127,128,5,17,0,0,128,13,1,0,0,0,129,130,5,14,0,0,130,131,
        7,0,0,0,131,15,1,0,0,0,132,133,3,42,21,0,133,134,5,14,0,0,134,135,
        5,33,0,0,135,136,3,26,13,0,136,137,5,17,0,0,137,17,1,0,0,0,138,140,
        3,2,1,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,
        1,0,0,0,142,19,1,0,0,0,143,141,1,0,0,0,144,145,5,4,0,0,145,146,5,
        23,0,0,146,147,3,36,18,0,147,148,5,24,0,0,148,149,5,29,0,0,149,150,
        3,24,12,0,150,151,5,30,0,0,151,152,5,17,0,0,152,21,1,0,0,0,153,154,
        5,5,0,0,154,155,5,29,0,0,155,156,3,24,12,0,156,157,5,30,0,0,157,
        158,5,4,0,0,158,159,5,23,0,0,159,160,3,36,18,0,160,161,5,24,0,0,
        161,162,5,17,0,0,162,23,1,0,0,0,163,165,3,2,1,0,164,163,1,0,0,0,
        165,168,1,0,0,0,166,164,1,0,0,0,166,167,1,0,0,0,167,25,1,0,0,0,168,
        166,1,0,0,0,169,170,6,13,-1,0,170,177,5,15,0,0,171,172,5,19,0,0,
        172,177,5,15,0,0,173,177,5,14,0,0,174,177,5,16,0,0,175,177,3,60,
        30,0,176,169,1,0,0,0,176,171,1,0,0,0,176,173,1,0,0,0,176,174,1,0,
        0,0,176,175,1,0,0,0,177,189,1,0,0,0,178,179,10,8,0,0,179,180,5,22,
        0,0,180,188,3,26,13,9,181,182,10,7,0,0,182,183,7,1,0,0,183,188,3,
        26,13,8,184,185,10,6,0,0,185,186,7,2,0,0,186,188,3,26,13,7,187,178,
        1,0,0,0,187,181,1,0,0,0,187,184,1,0,0,0,188,191,1,0,0,0,189,187,
        1,0,0,0,189,190,1,0,0,0,190,27,1,0,0,0,191,189,1,0,0,0,192,193,5,
        6,0,0,193,194,5,23,0,0,194,195,3,30,15,0,195,196,5,24,0,0,196,197,
        5,17,0,0,197,29,1,0,0,0,198,199,7,3,0,0,199,31,1,0,0,0,200,204,5,
        7,0,0,201,203,3,34,17,0,202,201,1,0,0,0,203,206,1,0,0,0,204,202,
        1,0,0,0,204,205,1,0,0,0,205,207,1,0,0,0,206,204,1,0,0,0,207,208,
        5,17,0,0,208,33,1,0,0,0,209,210,3,42,21,0,210,211,5,8,0,0,211,212,
        5,14,0,0,212,35,1,0,0,0,213,214,3,26,13,0,214,215,3,38,19,0,215,
        216,3,26,13,0,216,37,1,0,0,0,217,218,7,4,0,0,218,39,1,0,0,0,219,
        220,3,42,21,0,220,221,5,14,0,0,221,222,5,33,0,0,222,223,3,26,13,
        0,223,224,5,17,0,0,224,41,1,0,0,0,225,226,7,5,0,0,226,43,1,0,0,0,
        227,228,3,54,27,0,228,229,3,52,26,0,229,231,5,23,0,0,230,232,3,48,
        24,0,231,230,1,0,0,0,231,232,1,0,0,0,232,233,1,0,0,0,233,234,5,24,
        0,0,234,235,5,29,0,0,235,237,3,50,25,0,236,238,3,46,23,0,237,236,
        1,0,0,0,237,238,1,0,0,0,238,239,1,0,0,0,239,240,5,30,0,0,240,241,
        5,17,0,0,241,45,1,0,0,0,242,243,5,11,0,0,243,244,3,56,28,0,244,245,
        5,17,0,0,245,47,1,0,0,0,246,247,3,42,21,0,247,254,5,14,0,0,248,249,
        5,12,0,0,249,250,3,42,21,0,250,251,5,14,0,0,251,253,1,0,0,0,252,
        248,1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,
        258,1,0,0,0,256,254,1,0,0,0,257,246,1,0,0,0,257,258,1,0,0,0,258,
        49,1,0,0,0,259,261,3,2,1,0,260,259,1,0,0,0,261,264,1,0,0,0,262,260,
        1,0,0,0,262,263,1,0,0,0,263,51,1,0,0,0,264,262,1,0,0,0,265,266,5,
        14,0,0,266,53,1,0,0,0,267,272,1,0,0,0,268,272,5,13,0,0,269,272,5,
        9,0,0,270,272,5,10,0,0,271,267,1,0,0,0,271,268,1,0,0,0,271,269,1,
        0,0,0,271,270,1,0,0,0,272,55,1,0,0,0,273,278,5,14,0,0,274,278,5,
        15,0,0,275,278,5,16,0,0,276,278,3,60,30,0,277,273,1,0,0,0,277,274,
        1,0,0,0,277,275,1,0,0,0,277,276,1,0,0,0,278,57,1,0,0,0,279,284,3,
        56,28,0,280,281,5,12,0,0,281,283,3,56,28,0,282,280,1,0,0,0,283,286,
        1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,288,1,0,0,0,286,284,
        1,0,0,0,287,279,1,0,0,0,287,288,1,0,0,0,288,59,1,0,0,0,289,290,3,
        52,26,0,290,292,5,23,0,0,291,293,3,58,29,0,292,291,1,0,0,0,292,293,
        1,0,0,0,293,294,1,0,0,0,294,296,5,24,0,0,295,297,5,17,0,0,296,295,
        1,0,0,0,296,297,1,0,0,0,297,61,1,0,0,0,22,63,68,85,108,114,141,166,
        176,187,189,204,231,237,254,257,262,271,277,284,287,292,296
    ]

class nevermorecompilerParser ( Parser ):

    grammarFileName = "nevermorecompiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'while'", 
                     "'do'", "'print'", "'global:'", "':'", "'int'", "'double'", 
                     "'return'", "','", "'void'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "'('", "')'", "'>'", "'<'", "'=='", "'!='", "'{'", 
                     "'}'", "<INVALID>", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "DOUBLE", "END_STATE", 
                      "ADD", "SUB", "MUL", "DIV", "POW", "LPAREN", "RPAREN", 
                      "GT", "LT", "EQ_EQ", "NOT_EQ", "RCORNER", "LCORNER", 
                      "INCREMENT", "DECREMENT", "EQ", "WS", "SINGLE_LINE_COMMENT", 
                      "NEWLINE" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_ifStatement = 2
    RULE_ifElseStatement = 3
    RULE_ifBody = 4
    RULE_elseBody = 5
    RULE_forStatement = 6
    RULE_forModify = 7
    RULE_forInit = 8
    RULE_forBody = 9
    RULE_whileStatement = 10
    RULE_doWhileStatement = 11
    RULE_whileBody = 12
    RULE_expr = 13
    RULE_printState = 14
    RULE_printBody = 15
    RULE_globalStatement = 16
    RULE_globalBody = 17
    RULE_equation = 18
    RULE_relop = 19
    RULE_assignmentStatement = 20
    RULE_type = 21
    RULE_functionStatement = 22
    RULE_ret = 23
    RULE_functionArgs = 24
    RULE_functionBody = 25
    RULE_functionName = 26
    RULE_funcType = 27
    RULE_functionExpr = 28
    RULE_functionParams = 29
    RULE_functionCall = 30

    ruleNames =  [ "prog", "stat", "ifStatement", "ifElseStatement", "ifBody", 
                   "elseBody", "forStatement", "forModify", "forInit", "forBody", 
                   "whileStatement", "doWhileStatement", "whileBody", "expr", 
                   "printState", "printBody", "globalStatement", "globalBody", 
                   "equation", "relop", "assignmentStatement", "type", "functionStatement", 
                   "ret", "functionArgs", "functionBody", "functionName", 
                   "funcType", "functionExpr", "functionParams", "functionCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    ID=14
    INT=15
    DOUBLE=16
    END_STATE=17
    ADD=18
    SUB=19
    MUL=20
    DIV=21
    POW=22
    LPAREN=23
    RPAREN=24
    GT=25
    LT=26
    EQ_EQ=27
    NOT_EQ=28
    RCORNER=29
    LCORNER=30
    INCREMENT=31
    DECREMENT=32
    EQ=33
    WS=34
    SINGLE_LINE_COMMENT=35
    NEWLINE=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(nevermorecompilerParser.EOF, 0)

        def globalStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.GlobalStatementContext,0)


        def functionStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.FunctionStatementContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.FunctionStatementContext,i)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = nevermorecompilerParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 62
                self.globalStatement()


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 26112) != 0):
                self.state = 65
                self.functionStatement()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(nevermorecompilerParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.AssignmentStatementContext,0)


        def printState(self):
            return self.getTypedRuleContext(nevermorecompilerParser.PrintStateContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.IfStatementContext,0)


        def ifElseStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.IfElseStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.ForStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.DoWhileStatementContext,0)


        def globalStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.GlobalStatementContext,0)


        def functionStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionStatementContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionCallContext,0)


        def ret(self):
            return self.getTypedRuleContext(nevermorecompilerParser.RetContext,0)


        def NEWLINE(self):
            return self.getToken(nevermorecompilerParser.NEWLINE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = nevermorecompilerParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.printState()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.ifElseStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.whileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 79
                self.doWhileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 80
                self.globalStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 81
                self.functionStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 82
                self.functionCall()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 83
                self.ret()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 84
                self.match(nevermorecompilerParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equation(self):
            return self.getTypedRuleContext(nevermorecompilerParser.EquationContext,0)


        def RCORNER(self):
            return self.getToken(nevermorecompilerParser.RCORNER, 0)

        def ifBody(self):
            return self.getTypedRuleContext(nevermorecompilerParser.IfBodyContext,0)


        def LCORNER(self):
            return self.getToken(nevermorecompilerParser.LCORNER, 0)

        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = nevermorecompilerParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(nevermorecompilerParser.T__0)
            self.state = 88
            self.equation()
            self.state = 89
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 90
            self.ifBody()
            self.state = 91
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 92
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equation(self):
            return self.getTypedRuleContext(nevermorecompilerParser.EquationContext,0)


        def RCORNER(self, i:int=None):
            if i is None:
                return self.getTokens(nevermorecompilerParser.RCORNER)
            else:
                return self.getToken(nevermorecompilerParser.RCORNER, i)

        def ifBody(self):
            return self.getTypedRuleContext(nevermorecompilerParser.IfBodyContext,0)


        def LCORNER(self, i:int=None):
            if i is None:
                return self.getTokens(nevermorecompilerParser.LCORNER)
            else:
                return self.getToken(nevermorecompilerParser.LCORNER, i)

        def elseBody(self):
            return self.getTypedRuleContext(nevermorecompilerParser.ElseBodyContext,0)


        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_ifElseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElseStatement" ):
                listener.enterIfElseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElseStatement" ):
                listener.exitIfElseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElseStatement" ):
                return visitor.visitIfElseStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifElseStatement(self):

        localctx = nevermorecompilerParser.IfElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ifElseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(nevermorecompilerParser.T__0)
            self.state = 95
            self.equation()
            self.state = 96
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 97
            self.ifBody()
            self.state = 98
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 99
            self.match(nevermorecompilerParser.T__1)
            self.state = 100
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 101
            self.elseBody()
            self.state = 102
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 103
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.StatContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.StatContext,i)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_ifBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBody" ):
                listener.enterIfBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBody" ):
                listener.exitIfBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBody" ):
                return visitor.visitIfBody(self)
            else:
                return visitor.visitChildren(self)




    def ifBody(self):

        localctx = nevermorecompilerParser.IfBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68719505146) != 0):
                self.state = 105
                self.stat()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.StatContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.StatContext,i)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_elseBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBody" ):
                listener.enterElseBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBody" ):
                listener.exitElseBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBody" ):
                return visitor.visitElseBody(self)
            else:
                return visitor.visitChildren(self)




    def elseBody(self):

        localctx = nevermorecompilerParser.ElseBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elseBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68719505146) != 0):
                self.state = 111
                self.stat()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(nevermorecompilerParser.LPAREN, 0)

        def forInit(self):
            return self.getTypedRuleContext(nevermorecompilerParser.ForInitContext,0)


        def equation(self):
            return self.getTypedRuleContext(nevermorecompilerParser.EquationContext,0)


        def END_STATE(self, i:int=None):
            if i is None:
                return self.getTokens(nevermorecompilerParser.END_STATE)
            else:
                return self.getToken(nevermorecompilerParser.END_STATE, i)

        def forModify(self):
            return self.getTypedRuleContext(nevermorecompilerParser.ForModifyContext,0)


        def RPAREN(self):
            return self.getToken(nevermorecompilerParser.RPAREN, 0)

        def RCORNER(self):
            return self.getToken(nevermorecompilerParser.RCORNER, 0)

        def forBody(self):
            return self.getTypedRuleContext(nevermorecompilerParser.ForBodyContext,0)


        def LCORNER(self):
            return self.getToken(nevermorecompilerParser.LCORNER, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = nevermorecompilerParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(nevermorecompilerParser.T__2)
            self.state = 118
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 119
            self.forInit()
            self.state = 120
            self.equation()
            self.state = 121
            self.match(nevermorecompilerParser.END_STATE)
            self.state = 122
            self.forModify()
            self.state = 123
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 124
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 125
            self.forBody()
            self.state = 126
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 127
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForModifyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def INCREMENT(self):
            return self.getToken(nevermorecompilerParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(nevermorecompilerParser.DECREMENT, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_forModify

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForModify" ):
                listener.enterForModify(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForModify" ):
                listener.exitForModify(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForModify" ):
                return visitor.visitForModify(self)
            else:
                return visitor.visitChildren(self)




    def forModify(self):

        localctx = nevermorecompilerParser.ForModifyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forModify)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(nevermorecompilerParser.ID)
            self.state = 130
            _la = self._input.LA(1)
            if not(_la==31 or _la==32):
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


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(nevermorecompilerParser.TypeContext,0)


        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def EQ(self):
            return self.getToken(nevermorecompilerParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(nevermorecompilerParser.ExprContext,0)


        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = nevermorecompilerParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.type_()
            self.state = 133
            self.match(nevermorecompilerParser.ID)
            self.state = 134
            self.match(nevermorecompilerParser.EQ)
            self.state = 135
            self.expr(0)
            self.state = 136
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.StatContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.StatContext,i)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_forBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForBody" ):
                listener.enterForBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForBody" ):
                listener.exitForBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBody" ):
                return visitor.visitForBody(self)
            else:
                return visitor.visitChildren(self)




    def forBody(self):

        localctx = nevermorecompilerParser.ForBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_forBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68719505146) != 0):
                self.state = 138
                self.stat()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(nevermorecompilerParser.LPAREN, 0)

        def equation(self):
            return self.getTypedRuleContext(nevermorecompilerParser.EquationContext,0)


        def RPAREN(self):
            return self.getToken(nevermorecompilerParser.RPAREN, 0)

        def RCORNER(self):
            return self.getToken(nevermorecompilerParser.RCORNER, 0)

        def whileBody(self):
            return self.getTypedRuleContext(nevermorecompilerParser.WhileBodyContext,0)


        def LCORNER(self):
            return self.getToken(nevermorecompilerParser.LCORNER, 0)

        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = nevermorecompilerParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(nevermorecompilerParser.T__3)
            self.state = 145
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 146
            self.equation()
            self.state = 147
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 148
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 149
            self.whileBody()
            self.state = 150
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 151
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RCORNER(self):
            return self.getToken(nevermorecompilerParser.RCORNER, 0)

        def whileBody(self):
            return self.getTypedRuleContext(nevermorecompilerParser.WhileBodyContext,0)


        def LCORNER(self):
            return self.getToken(nevermorecompilerParser.LCORNER, 0)

        def LPAREN(self):
            return self.getToken(nevermorecompilerParser.LPAREN, 0)

        def equation(self):
            return self.getTypedRuleContext(nevermorecompilerParser.EquationContext,0)


        def RPAREN(self):
            return self.getToken(nevermorecompilerParser.RPAREN, 0)

        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhileStatement" ):
                return visitor.visitDoWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def doWhileStatement(self):

        localctx = nevermorecompilerParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(nevermorecompilerParser.T__4)
            self.state = 154
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 155
            self.whileBody()
            self.state = 156
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 157
            self.match(nevermorecompilerParser.T__3)
            self.state = 158
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 159
            self.equation()
            self.state = 160
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 161
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.StatContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.StatContext,i)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_whileBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileBody" ):
                listener.enterWhileBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileBody" ):
                listener.exitWhileBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileBody" ):
                return visitor.visitWhileBody(self)
            else:
                return visitor.visitChildren(self)




    def whileBody(self):

        localctx = nevermorecompilerParser.WhileBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whileBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 68719505146) != 0):
                self.state = 163
                self.stat()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(nevermorecompilerParser.INT, 0)

        def SUB(self):
            return self.getToken(nevermorecompilerParser.SUB, 0)

        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def DOUBLE(self):
            return self.getToken(nevermorecompilerParser.DOUBLE, 0)

        def functionCall(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionCallContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.ExprContext,i)


        def POW(self):
            return self.getToken(nevermorecompilerParser.POW, 0)

        def MUL(self):
            return self.getToken(nevermorecompilerParser.MUL, 0)

        def DIV(self):
            return self.getToken(nevermorecompilerParser.DIV, 0)

        def ADD(self):
            return self.getToken(nevermorecompilerParser.ADD, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = nevermorecompilerParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 170
                self.match(nevermorecompilerParser.INT)
                pass

            elif la_ == 2:
                self.state = 171
                self.match(nevermorecompilerParser.SUB)
                self.state = 172
                self.match(nevermorecompilerParser.INT)
                pass

            elif la_ == 3:
                self.state = 173
                self.match(nevermorecompilerParser.ID)
                pass

            elif la_ == 4:
                self.state = 174
                self.match(nevermorecompilerParser.DOUBLE)
                pass

            elif la_ == 5:
                self.state = 175
                self.functionCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 187
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = nevermorecompilerParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 178
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 179
                        self.match(nevermorecompilerParser.POW)
                        self.state = 180
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = nevermorecompilerParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 181
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 182
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 183
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = nevermorecompilerParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 184
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 185
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 186
                        self.expr(7)
                        pass

             
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrintStateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(nevermorecompilerParser.LPAREN, 0)

        def printBody(self):
            return self.getTypedRuleContext(nevermorecompilerParser.PrintBodyContext,0)


        def RPAREN(self):
            return self.getToken(nevermorecompilerParser.RPAREN, 0)

        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_printState

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintState" ):
                listener.enterPrintState(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintState" ):
                listener.exitPrintState(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintState" ):
                return visitor.visitPrintState(self)
            else:
                return visitor.visitChildren(self)




    def printState(self):

        localctx = nevermorecompilerParser.PrintStateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_printState)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(nevermorecompilerParser.T__5)
            self.state = 193
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 194
            self.printBody()
            self.state = 195
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 196
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def INT(self):
            return self.getToken(nevermorecompilerParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(nevermorecompilerParser.DOUBLE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_printBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintBody" ):
                listener.enterPrintBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintBody" ):
                listener.exitPrintBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintBody" ):
                return visitor.visitPrintBody(self)
            else:
                return visitor.visitChildren(self)




    def printBody(self):

        localctx = nevermorecompilerParser.PrintBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_printBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
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


    class GlobalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def globalBody(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.GlobalBodyContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.GlobalBodyContext,i)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_globalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalStatement" ):
                listener.enterGlobalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalStatement" ):
                listener.exitGlobalStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalStatement" ):
                return visitor.visitGlobalStatement(self)
            else:
                return visitor.visitChildren(self)




    def globalStatement(self):

        localctx = nevermorecompilerParser.GlobalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_globalStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(nevermorecompilerParser.T__6)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 201
                self.globalBody()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 207
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(nevermorecompilerParser.TypeContext,0)


        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_globalBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalBody" ):
                listener.enterGlobalBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalBody" ):
                listener.exitGlobalBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalBody" ):
                return visitor.visitGlobalBody(self)
            else:
                return visitor.visitChildren(self)




    def globalBody(self):

        localctx = nevermorecompilerParser.GlobalBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_globalBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.type_()
            self.state = 210
            self.match(nevermorecompilerParser.T__7)
            self.state = 211
            self.match(nevermorecompilerParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # RelopContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.ExprContext,i)


        def relop(self):
            return self.getTypedRuleContext(nevermorecompilerParser.RelopContext,0)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquation" ):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)




    def equation(self):

        localctx = nevermorecompilerParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.expr(0)
            self.state = 214
            localctx.op = self.relop()
            self.state = 215
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_EQ(self):
            return self.getToken(nevermorecompilerParser.EQ_EQ, 0)

        def GT(self):
            return self.getToken(nevermorecompilerParser.GT, 0)

        def LT(self):
            return self.getToken(nevermorecompilerParser.LT, 0)

        def NOT_EQ(self):
            return self.getToken(nevermorecompilerParser.NOT_EQ, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = nevermorecompilerParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 503316480) != 0)):
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


    class AssignmentStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(nevermorecompilerParser.TypeContext,0)


        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def EQ(self):
            return self.getToken(nevermorecompilerParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(nevermorecompilerParser.ExprContext,0)


        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_assignmentStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentStatement" ):
                listener.enterAssignmentStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentStatement" ):
                listener.exitAssignmentStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentStatement" ):
                return visitor.visitAssignmentStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignmentStatement(self):

        localctx = nevermorecompilerParser.AssignmentStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.type_()
            self.state = 220
            self.match(nevermorecompilerParser.ID)
            self.state = 221
            self.match(nevermorecompilerParser.EQ)
            self.state = 222
            self.expr(0)
            self.state = 223
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = nevermorecompilerParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
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


    class FunctionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcType(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FuncTypeContext,0)


        def functionName(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionNameContext,0)


        def LPAREN(self):
            return self.getToken(nevermorecompilerParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(nevermorecompilerParser.RPAREN, 0)

        def RCORNER(self):
            return self.getToken(nevermorecompilerParser.RCORNER, 0)

        def functionBody(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionBodyContext,0)


        def LCORNER(self):
            return self.getToken(nevermorecompilerParser.LCORNER, 0)

        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def functionArgs(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionArgsContext,0)


        def ret(self):
            return self.getTypedRuleContext(nevermorecompilerParser.RetContext,0)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_functionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionStatement" ):
                listener.enterFunctionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionStatement" ):
                listener.exitFunctionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionStatement" ):
                return visitor.visitFunctionStatement(self)
            else:
                return visitor.visitChildren(self)




    def functionStatement(self):

        localctx = nevermorecompilerParser.FunctionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_functionStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.funcType()
            self.state = 228
            self.functionName()
            self.state = 229
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 230
                self.functionArgs()


            self.state = 233
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 234
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 235
            self.functionBody()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 236
                self.ret()


            self.state = 239
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 240
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionExpr(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionExprContext,0)


        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_ret

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRet" ):
                listener.enterRet(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRet" ):
                listener.exitRet(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRet" ):
                return visitor.visitRet(self)
            else:
                return visitor.visitChildren(self)




    def ret(self):

        localctx = nevermorecompilerParser.RetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ret)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(nevermorecompilerParser.T__10)
            self.state = 243
            self.functionExpr()
            self.state = 244
            self.match(nevermorecompilerParser.END_STATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.TypeContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.TypeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(nevermorecompilerParser.ID)
            else:
                return self.getToken(nevermorecompilerParser.ID, i)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_functionArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArgs" ):
                listener.enterFunctionArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArgs" ):
                listener.exitFunctionArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArgs" ):
                return visitor.visitFunctionArgs(self)
            else:
                return visitor.visitChildren(self)




    def functionArgs(self):

        localctx = nevermorecompilerParser.FunctionArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_functionArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 246
                self.type_()
                self.state = 247
                self.match(nevermorecompilerParser.ID)
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 248
                    self.match(nevermorecompilerParser.T__11)
                    self.state = 249
                    self.type_()
                    self.state = 250
                    self.match(nevermorecompilerParser.ID)
                    self.state = 256
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.StatContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.StatContext,i)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_functionBody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionBody" ):
                listener.enterFunctionBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionBody" ):
                listener.exitFunctionBody(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionBody" ):
                return visitor.visitFunctionBody(self)
            else:
                return visitor.visitChildren(self)




    def functionBody(self):

        localctx = nevermorecompilerParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_functionBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 259
                    self.stat() 
                self.state = 264
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_functionName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionName" ):
                listener.enterFunctionName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionName" ):
                listener.exitFunctionName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionName" ):
                return visitor.visitFunctionName(self)
            else:
                return visitor.visitChildren(self)




    def functionName(self):

        localctx = nevermorecompilerParser.FunctionNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(nevermorecompilerParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_funcType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncType" ):
                listener.enterFuncType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncType" ):
                listener.exitFuncType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncType" ):
                return visitor.visitFuncType(self)
            else:
                return visitor.visitChildren(self)




    def funcType(self):

        localctx = nevermorecompilerParser.FuncTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_funcType)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(nevermorecompilerParser.T__12)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.match(nevermorecompilerParser.T__8)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 270
                self.match(nevermorecompilerParser.T__9)
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


    class FunctionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def INT(self):
            return self.getToken(nevermorecompilerParser.INT, 0)

        def DOUBLE(self):
            return self.getToken(nevermorecompilerParser.DOUBLE, 0)

        def functionCall(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_functionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionExpr" ):
                listener.enterFunctionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionExpr" ):
                listener.exitFunctionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionExpr" ):
                return visitor.visitFunctionExpr(self)
            else:
                return visitor.visitChildren(self)




    def functionExpr(self):

        localctx = nevermorecompilerParser.FunctionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_functionExpr)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(nevermorecompilerParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.match(nevermorecompilerParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.match(nevermorecompilerParser.DOUBLE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 276
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionParamsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.FunctionExprContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.FunctionExprContext,i)


        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_functionParams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionParams" ):
                listener.enterFunctionParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionParams" ):
                listener.exitFunctionParams(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionParams" ):
                return visitor.visitFunctionParams(self)
            else:
                return visitor.visitChildren(self)




    def functionParams(self):

        localctx = nevermorecompilerParser.FunctionParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_functionParams)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                self.state = 279
                self.functionExpr()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 280
                    self.match(nevermorecompilerParser.T__11)
                    self.state = 281
                    self.functionExpr()
                    self.state = 286
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionName(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionNameContext,0)


        def LPAREN(self):
            return self.getToken(nevermorecompilerParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(nevermorecompilerParser.RPAREN, 0)

        def functionParams(self):
            return self.getTypedRuleContext(nevermorecompilerParser.FunctionParamsContext,0)


        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def getRuleIndex(self):
            return nevermorecompilerParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = nevermorecompilerParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.functionName()
            self.state = 290
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 291
                self.functionParams()


            self.state = 294
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 295
                self.match(nevermorecompilerParser.END_STATE)


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
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




