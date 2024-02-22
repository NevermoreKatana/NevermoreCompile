# Generated from grammar/nevermorecompiler.g4 by ANTLR 4.13.1
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
        4,1,33,240,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,3,0,56,8,0,1,0,5,0,59,8,0,10,0,12,0,62,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,77,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,5,4,98,8,
        4,10,4,12,4,101,9,4,1,5,5,5,104,8,5,10,5,12,5,107,9,5,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,
        8,1,8,1,9,5,9,130,8,9,10,9,12,9,133,9,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,12,5,12,155,8,12,10,12,12,12,158,9,12,1,13,1,13,1,13,1,13,
        3,13,164,8,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,172,8,13,10,13,
        12,13,175,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,
        5,16,187,8,16,10,16,12,16,190,9,16,1,16,1,16,1,17,1,17,1,17,1,17,
        1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,23,5,23,222,
        8,23,10,23,12,23,225,9,23,1,24,1,24,1,25,1,25,3,25,231,8,25,1,26,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,0,1,26,27,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,0,5,1,0,
        19,20,1,0,17,18,1,0,13,15,1,0,23,26,1,0,9,10,235,0,55,1,0,0,0,2,
        76,1,0,0,0,4,78,1,0,0,0,6,85,1,0,0,0,8,99,1,0,0,0,10,105,1,0,0,0,
        12,108,1,0,0,0,14,119,1,0,0,0,16,122,1,0,0,0,18,131,1,0,0,0,20,134,
        1,0,0,0,22,143,1,0,0,0,24,156,1,0,0,0,26,163,1,0,0,0,28,176,1,0,
        0,0,30,182,1,0,0,0,32,184,1,0,0,0,34,193,1,0,0,0,36,197,1,0,0,0,
        38,201,1,0,0,0,40,203,1,0,0,0,42,209,1,0,0,0,44,211,1,0,0,0,46,223,
        1,0,0,0,48,226,1,0,0,0,50,230,1,0,0,0,52,232,1,0,0,0,54,56,3,32,
        16,0,55,54,1,0,0,0,55,56,1,0,0,0,56,60,1,0,0,0,57,59,3,44,22,0,58,
        57,1,0,0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,63,1,0,0,
        0,62,60,1,0,0,0,63,64,5,0,0,1,64,1,1,0,0,0,65,77,3,40,20,0,66,77,
        3,28,14,0,67,77,3,4,2,0,68,77,3,6,3,0,69,77,3,12,6,0,70,77,3,20,
        10,0,71,77,3,22,11,0,72,77,3,32,16,0,73,77,3,44,22,0,74,77,3,52,
        26,0,75,77,5,33,0,0,76,65,1,0,0,0,76,66,1,0,0,0,76,67,1,0,0,0,76,
        68,1,0,0,0,76,69,1,0,0,0,76,70,1,0,0,0,76,71,1,0,0,0,76,72,1,0,0,
        0,76,73,1,0,0,0,76,74,1,0,0,0,76,75,1,0,0,0,77,3,1,0,0,0,78,79,5,
        1,0,0,79,80,3,36,18,0,80,81,5,27,0,0,81,82,3,8,4,0,82,83,5,28,0,
        0,83,84,5,16,0,0,84,5,1,0,0,0,85,86,5,1,0,0,86,87,3,36,18,0,87,88,
        5,27,0,0,88,89,3,8,4,0,89,90,5,28,0,0,90,91,5,2,0,0,91,92,5,27,0,
        0,92,93,3,10,5,0,93,94,5,28,0,0,94,95,5,16,0,0,95,7,1,0,0,0,96,98,
        3,2,1,0,97,96,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,
        0,100,9,1,0,0,0,101,99,1,0,0,0,102,104,3,2,1,0,103,102,1,0,0,0,104,
        107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,11,1,0,0,0,107,105,
        1,0,0,0,108,109,5,3,0,0,109,110,5,21,0,0,110,111,3,16,8,0,111,112,
        3,36,18,0,112,113,5,16,0,0,113,114,3,14,7,0,114,115,5,22,0,0,115,
        116,5,27,0,0,116,117,3,18,9,0,117,118,5,28,0,0,118,13,1,0,0,0,119,
        120,5,13,0,0,120,121,5,29,0,0,121,15,1,0,0,0,122,123,3,42,21,0,123,
        124,5,13,0,0,124,125,5,30,0,0,125,126,3,26,13,0,126,127,5,16,0,0,
        127,17,1,0,0,0,128,130,3,2,1,0,129,128,1,0,0,0,130,133,1,0,0,0,131,
        129,1,0,0,0,131,132,1,0,0,0,132,19,1,0,0,0,133,131,1,0,0,0,134,135,
        5,4,0,0,135,136,5,21,0,0,136,137,3,36,18,0,137,138,5,22,0,0,138,
        139,5,27,0,0,139,140,3,24,12,0,140,141,5,28,0,0,141,142,5,16,0,0,
        142,21,1,0,0,0,143,144,5,5,0,0,144,145,5,27,0,0,145,146,3,24,12,
        0,146,147,5,28,0,0,147,148,5,4,0,0,148,149,5,21,0,0,149,150,3,36,
        18,0,150,151,5,22,0,0,151,152,5,16,0,0,152,23,1,0,0,0,153,155,3,
        2,1,0,154,153,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,1,
        0,0,0,157,25,1,0,0,0,158,156,1,0,0,0,159,160,6,13,-1,0,160,164,5,
        14,0,0,161,164,5,13,0,0,162,164,5,15,0,0,163,159,1,0,0,0,163,161,
        1,0,0,0,163,162,1,0,0,0,164,173,1,0,0,0,165,166,10,5,0,0,166,167,
        7,0,0,0,167,172,3,26,13,6,168,169,10,4,0,0,169,170,7,1,0,0,170,172,
        3,26,13,5,171,165,1,0,0,0,171,168,1,0,0,0,172,175,1,0,0,0,173,171,
        1,0,0,0,173,174,1,0,0,0,174,27,1,0,0,0,175,173,1,0,0,0,176,177,5,
        6,0,0,177,178,5,21,0,0,178,179,3,30,15,0,179,180,5,22,0,0,180,181,
        5,16,0,0,181,29,1,0,0,0,182,183,7,2,0,0,183,31,1,0,0,0,184,188,5,
        7,0,0,185,187,3,34,17,0,186,185,1,0,0,0,187,190,1,0,0,0,188,186,
        1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,188,1,0,0,0,191,192,
        5,16,0,0,192,33,1,0,0,0,193,194,3,42,21,0,194,195,5,8,0,0,195,196,
        5,13,0,0,196,35,1,0,0,0,197,198,3,26,13,0,198,199,3,38,19,0,199,
        200,3,26,13,0,200,37,1,0,0,0,201,202,7,3,0,0,202,39,1,0,0,0,203,
        204,3,42,21,0,204,205,5,13,0,0,205,206,5,30,0,0,206,207,3,26,13,
        0,207,208,5,16,0,0,208,41,1,0,0,0,209,210,7,4,0,0,210,43,1,0,0,0,
        211,212,3,50,25,0,212,213,3,48,24,0,213,214,5,21,0,0,214,215,5,22,
        0,0,215,216,5,27,0,0,216,217,3,46,23,0,217,218,5,28,0,0,218,219,
        5,16,0,0,219,45,1,0,0,0,220,222,3,2,1,0,221,220,1,0,0,0,222,225,
        1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,47,1,0,0,0,225,223,1,
        0,0,0,226,227,5,13,0,0,227,49,1,0,0,0,228,231,3,42,21,0,229,231,
        5,11,0,0,230,228,1,0,0,0,230,229,1,0,0,0,231,51,1,0,0,0,232,233,
        5,12,0,0,233,234,5,11,0,0,234,235,3,48,24,0,235,236,5,21,0,0,236,
        237,5,22,0,0,237,238,5,16,0,0,238,53,1,0,0,0,13,55,60,76,99,105,
        131,156,163,171,173,188,223,230
    ]

class nevermorecompilerParser ( Parser ):

    grammarFileName = "nevermorecompiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'while'", 
                     "'do'", "'print'", "'global:'", "':'", "'int'", "'double'", 
                     "'void'", "'call'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'>'", 
                     "'<'", "'=='", "'!='", "'{'", "'}'", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "DOUBLE", "END_STATE", "ADD", 
                      "SUB", "MUL", "DIV", "LPAREN", "RPAREN", "GT", "LT", 
                      "EQ_EQ", "NOT_EQ", "RCORNER", "LCORNER", "INCREMENT", 
                      "EQ", "WS", "SINGLE_LINE_COMMENT", "NEWLINE" ]

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
    RULE_functionBody = 23
    RULE_functionName = 24
    RULE_funcType = 25
    RULE_functionCall = 26

    ruleNames =  [ "prog", "stat", "ifStatement", "ifElseStatement", "ifBody", 
                   "elseBody", "forStatement", "forModify", "forInit", "forBody", 
                   "whileStatement", "doWhileStatement", "whileBody", "expr", 
                   "printState", "printBody", "globalStatement", "globalBody", 
                   "equation", "relop", "assignmentStatement", "type", "functionStatement", 
                   "functionBody", "functionName", "funcType", "functionCall" ]

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
    ID=13
    INT=14
    DOUBLE=15
    END_STATE=16
    ADD=17
    SUB=18
    MUL=19
    DIV=20
    LPAREN=21
    RPAREN=22
    GT=23
    LT=24
    EQ_EQ=25
    NOT_EQ=26
    RCORNER=27
    LCORNER=28
    INCREMENT=29
    EQ=30
    WS=31
    SINGLE_LINE_COMMENT=32
    NEWLINE=33

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
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 54
                self.globalStatement()


            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0):
                self.state = 57
                self.functionStatement()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
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
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.printState()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 68
                self.ifElseStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 69
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 70
                self.whileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 71
                self.doWhileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 72
                self.globalStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 73
                self.functionStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 74
                self.functionCall()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 75
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
            self.state = 78
            self.match(nevermorecompilerParser.T__0)
            self.state = 79
            self.equation()
            self.state = 80
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 81
            self.ifBody()
            self.state = 82
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 83
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
            self.state = 85
            self.match(nevermorecompilerParser.T__0)
            self.state = 86
            self.equation()
            self.state = 87
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 88
            self.ifBody()
            self.state = 89
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 90
            self.match(nevermorecompilerParser.T__1)
            self.state = 91
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 92
            self.elseBody()
            self.state = 93
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 94
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
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589942522) != 0):
                self.state = 96
                self.stat()
                self.state = 101
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
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589942522) != 0):
                self.state = 102
                self.stat()
                self.state = 107
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


        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

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
            self.state = 108
            self.match(nevermorecompilerParser.T__2)
            self.state = 109
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 110
            self.forInit()
            self.state = 111
            self.equation()
            self.state = 112
            self.match(nevermorecompilerParser.END_STATE)
            self.state = 113
            self.forModify()
            self.state = 114
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 115
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 116
            self.forBody()
            self.state = 117
            self.match(nevermorecompilerParser.LCORNER)
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(nevermorecompilerParser.ID)
            self.state = 120
            self.match(nevermorecompilerParser.INCREMENT)
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
            self.state = 122
            self.type_()
            self.state = 123
            self.match(nevermorecompilerParser.ID)
            self.state = 124
            self.match(nevermorecompilerParser.EQ)
            self.state = 125
            self.expr(0)
            self.state = 126
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
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589942522) != 0):
                self.state = 128
                self.stat()
                self.state = 133
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
            self.state = 134
            self.match(nevermorecompilerParser.T__3)
            self.state = 135
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 136
            self.equation()
            self.state = 137
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 138
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 139
            self.whileBody()
            self.state = 140
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 141
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
            self.state = 143
            self.match(nevermorecompilerParser.T__4)
            self.state = 144
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 145
            self.whileBody()
            self.state = 146
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 147
            self.match(nevermorecompilerParser.T__3)
            self.state = 148
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 149
            self.equation()
            self.state = 150
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 151
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
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589942522) != 0):
                self.state = 153
                self.stat()
                self.state = 158
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

        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def DOUBLE(self):
            return self.getToken(nevermorecompilerParser.DOUBLE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.ExprContext,i)


        def MUL(self):
            return self.getToken(nevermorecompilerParser.MUL, 0)

        def DIV(self):
            return self.getToken(nevermorecompilerParser.DIV, 0)

        def ADD(self):
            return self.getToken(nevermorecompilerParser.ADD, 0)

        def SUB(self):
            return self.getToken(nevermorecompilerParser.SUB, 0)

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
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 160
                self.match(nevermorecompilerParser.INT)
                pass
            elif token in [13]:
                self.state = 161
                self.match(nevermorecompilerParser.ID)
                pass
            elif token in [15]:
                self.state = 162
                self.match(nevermorecompilerParser.DOUBLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 173
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 171
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = nevermorecompilerParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 166
                        _la = self._input.LA(1)
                        if not(_la==19 or _la==20):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 167
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = nevermorecompilerParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 169
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 170
                        self.expr(5)
                        pass

             
                self.state = 175
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
            self.state = 176
            self.match(nevermorecompilerParser.T__5)
            self.state = 177
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 178
            self.printBody()
            self.state = 179
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 180
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
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
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
            self.state = 184
            self.match(nevermorecompilerParser.T__6)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 185
                self.globalBody()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
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
            self.state = 193
            self.type_()
            self.state = 194
            self.match(nevermorecompilerParser.T__7)
            self.state = 195
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
            self.state = 197
            self.expr(0)
            self.state = 198
            localctx.op = self.relop()
            self.state = 199
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
            self.state = 201
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
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
            self.state = 203
            self.type_()
            self.state = 204
            self.match(nevermorecompilerParser.ID)
            self.state = 205
            self.match(nevermorecompilerParser.EQ)
            self.state = 206
            self.expr(0)
            self.state = 207
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
            self.state = 209
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.funcType()
            self.state = 212
            self.functionName()
            self.state = 213
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 214
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 215
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 216
            self.functionBody()
            self.state = 217
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 218
            self.match(nevermorecompilerParser.END_STATE)
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
        self.enterRule(localctx, 46, self.RULE_functionBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8589942522) != 0):
                self.state = 220
                self.stat()
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 48, self.RULE_functionName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
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

        def type_(self):
            return self.getTypedRuleContext(nevermorecompilerParser.TypeContext,0)


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
        self.enterRule(localctx, 50, self.RULE_funcType)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.type_()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.match(nevermorecompilerParser.T__10)
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
        self.enterRule(localctx, 52, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(nevermorecompilerParser.T__11)
            self.state = 233
            self.match(nevermorecompilerParser.T__10)
            self.state = 234
            self.functionName()
            self.state = 235
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 236
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 237
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




