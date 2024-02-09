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
        4,1,31,163,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,5,0,38,8,0,10,0,12,0,
        41,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,5,4,71,
        8,4,10,4,12,4,74,9,4,1,5,5,5,77,8,5,10,5,12,5,80,9,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,9,5,9,104,8,9,10,9,12,9,107,9,9,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,5,11,119,8,11,10,11,12,11,122,9,11,1,
        12,1,12,1,12,1,12,1,12,3,12,129,8,12,1,12,1,12,1,12,5,12,134,8,12,
        10,12,12,12,137,9,12,1,13,1,13,1,13,1,13,1,13,3,13,144,8,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,0,1,24,18,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,0,3,1,0,15,18,1,0,21,24,1,0,6,9,161,0,39,1,0,0,0,
        2,49,1,0,0,0,4,51,1,0,0,0,6,58,1,0,0,0,8,72,1,0,0,0,10,78,1,0,0,
        0,12,81,1,0,0,0,14,93,1,0,0,0,16,96,1,0,0,0,18,105,1,0,0,0,20,108,
        1,0,0,0,22,120,1,0,0,0,24,128,1,0,0,0,26,138,1,0,0,0,28,148,1,0,
        0,0,30,152,1,0,0,0,32,154,1,0,0,0,34,160,1,0,0,0,36,38,3,2,1,0,37,
        36,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,1,1,0,0,
        0,41,39,1,0,0,0,42,50,3,32,16,0,43,50,3,26,13,0,44,50,3,4,2,0,45,
        50,3,6,3,0,46,50,3,12,6,0,47,50,3,20,10,0,48,50,5,30,0,0,49,42,1,
        0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,1,0,0,0,49,46,1,0,0,0,49,
        47,1,0,0,0,49,48,1,0,0,0,50,3,1,0,0,0,51,52,5,1,0,0,52,53,3,28,14,
        0,53,54,5,25,0,0,54,55,3,8,4,0,55,56,5,26,0,0,56,57,5,14,0,0,57,
        5,1,0,0,0,58,59,5,1,0,0,59,60,3,28,14,0,60,61,5,25,0,0,61,62,3,8,
        4,0,62,63,5,26,0,0,63,64,5,2,0,0,64,65,5,25,0,0,65,66,3,10,5,0,66,
        67,5,26,0,0,67,68,5,14,0,0,68,7,1,0,0,0,69,71,3,2,1,0,70,69,1,0,
        0,0,71,74,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,9,1,0,0,0,74,72,
        1,0,0,0,75,77,3,2,1,0,76,75,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,
        78,79,1,0,0,0,79,11,1,0,0,0,80,78,1,0,0,0,81,82,5,3,0,0,82,83,5,
        19,0,0,83,84,3,16,8,0,84,85,3,28,14,0,85,86,5,14,0,0,86,87,3,14,
        7,0,87,88,5,20,0,0,88,89,5,25,0,0,89,90,3,18,9,0,90,91,5,26,0,0,
        91,92,5,14,0,0,92,13,1,0,0,0,93,94,5,10,0,0,94,95,5,27,0,0,95,15,
        1,0,0,0,96,97,3,34,17,0,97,98,5,10,0,0,98,99,5,28,0,0,99,100,3,24,
        12,0,100,101,5,14,0,0,101,17,1,0,0,0,102,104,3,2,1,0,103,102,1,0,
        0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,19,1,0,0,
        0,107,105,1,0,0,0,108,109,5,4,0,0,109,110,5,19,0,0,110,111,3,28,
        14,0,111,112,5,20,0,0,112,113,5,25,0,0,113,114,3,22,11,0,114,115,
        5,26,0,0,115,116,5,14,0,0,116,21,1,0,0,0,117,119,3,2,1,0,118,117,
        1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,23,1,
        0,0,0,122,120,1,0,0,0,123,124,6,12,-1,0,124,129,5,11,0,0,125,129,
        5,10,0,0,126,129,5,12,0,0,127,129,5,13,0,0,128,123,1,0,0,0,128,125,
        1,0,0,0,128,126,1,0,0,0,128,127,1,0,0,0,129,135,1,0,0,0,130,131,
        10,5,0,0,131,132,7,0,0,0,132,134,3,24,12,6,133,130,1,0,0,0,134,137,
        1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,25,1,0,0,0,137,135,1,
        0,0,0,138,139,5,5,0,0,139,143,5,19,0,0,140,144,3,24,12,0,141,144,
        5,31,0,0,142,144,5,13,0,0,143,140,1,0,0,0,143,141,1,0,0,0,143,142,
        1,0,0,0,144,145,1,0,0,0,145,146,5,20,0,0,146,147,5,14,0,0,147,27,
        1,0,0,0,148,149,3,24,12,0,149,150,3,30,15,0,150,151,3,24,12,0,151,
        29,1,0,0,0,152,153,7,1,0,0,153,31,1,0,0,0,154,155,3,34,17,0,155,
        156,5,10,0,0,156,157,5,28,0,0,157,158,3,24,12,0,158,159,5,14,0,0,
        159,33,1,0,0,0,160,161,7,2,0,0,161,35,1,0,0,0,9,39,49,72,78,105,
        120,128,135,143
    ]

class nevermorecompilerParser ( Parser ):

    grammarFileName = "nevermorecompiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'while'", 
                     "'print'", "'int'", "'double'", "'string'", "'bool'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'>'", 
                     "'<'", "'=='", "'!='", "'{'", "'}'", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "DOUBLE", "STROKE", 
                      "END_STATE", "ADD", "SUB", "MUL", "DIV", "LPAREN", 
                      "RPAREN", "GT", "LT", "EQ_EQ", "NOT_EQ", "RCORNER", 
                      "LCORNER", "INCREMENT", "EQ", "WS", "NEWLINE", "DIGIT" ]

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
    RULE_whileBody = 11
    RULE_expr = 12
    RULE_printState = 13
    RULE_equation = 14
    RULE_relop = 15
    RULE_assignmentStatement = 16
    RULE_type = 17

    ruleNames =  [ "prog", "stat", "ifStatement", "ifElseStatement", "ifBody", 
                   "elseBody", "forStatement", "forModify", "forInit", "forBody", 
                   "whileStatement", "whileBody", "expr", "printState", 
                   "equation", "relop", "assignmentStatement", "type" ]

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
    ID=10
    INT=11
    DOUBLE=12
    STROKE=13
    END_STATE=14
    ADD=15
    SUB=16
    MUL=17
    DIV=18
    LPAREN=19
    RPAREN=20
    GT=21
    LT=22
    EQ_EQ=23
    NOT_EQ=24
    RCORNER=25
    LCORNER=26
    INCREMENT=27
    EQ=28
    WS=29
    NEWLINE=30
    DIGIT=31

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

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.StatContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.StatContext,i)


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
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073742842) != 0):
                self.state = 36
                self.stat()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.printState()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.ifElseStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.whileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 48
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
            self.state = 51
            self.match(nevermorecompilerParser.T__0)
            self.state = 52
            self.equation()
            self.state = 53
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 54
            self.ifBody()
            self.state = 55
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 56
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
            self.state = 58
            self.match(nevermorecompilerParser.T__0)
            self.state = 59
            self.equation()
            self.state = 60
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 61
            self.ifBody()
            self.state = 62
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 63
            self.match(nevermorecompilerParser.T__1)
            self.state = 64
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 65
            self.elseBody()
            self.state = 66
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 67
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
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073742842) != 0):
                self.state = 69
                self.stat()
                self.state = 74
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
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073742842) != 0):
                self.state = 75
                self.stat()
                self.state = 80
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
            self.state = 81
            self.match(nevermorecompilerParser.T__2)
            self.state = 82
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 83
            self.forInit()
            self.state = 84
            self.equation()
            self.state = 85
            self.match(nevermorecompilerParser.END_STATE)
            self.state = 86
            self.forModify()
            self.state = 87
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 88
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 89
            self.forBody()
            self.state = 90
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 91
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
            self.state = 93
            self.match(nevermorecompilerParser.ID)
            self.state = 94
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
            self.state = 96
            self.type_()
            self.state = 97
            self.match(nevermorecompilerParser.ID)
            self.state = 98
            self.match(nevermorecompilerParser.EQ)
            self.state = 99
            self.expr(0)
            self.state = 100
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
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073742842) != 0):
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
            self.state = 108
            self.match(nevermorecompilerParser.T__3)
            self.state = 109
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 110
            self.equation()
            self.state = 111
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 112
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 113
            self.whileBody()
            self.state = 114
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 115
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
        self.enterRule(localctx, 22, self.RULE_whileBody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1073742842) != 0):
                self.state = 117
                self.stat()
                self.state = 122
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
            self.op = None # Token

        def INT(self):
            return self.getToken(nevermorecompilerParser.INT, 0)

        def ID(self):
            return self.getToken(nevermorecompilerParser.ID, 0)

        def DOUBLE(self):
            return self.getToken(nevermorecompilerParser.DOUBLE, 0)

        def STROKE(self):
            return self.getToken(nevermorecompilerParser.STROKE, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(nevermorecompilerParser.ExprContext)
            else:
                return self.getTypedRuleContext(nevermorecompilerParser.ExprContext,i)


        def DIV(self):
            return self.getToken(nevermorecompilerParser.DIV, 0)

        def MUL(self):
            return self.getToken(nevermorecompilerParser.MUL, 0)

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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 124
                self.match(nevermorecompilerParser.INT)
                pass
            elif token in [10]:
                self.state = 125
                self.match(nevermorecompilerParser.ID)
                pass
            elif token in [12]:
                self.state = 126
                self.match(nevermorecompilerParser.DOUBLE)
                pass
            elif token in [13]:
                self.state = 127
                self.match(nevermorecompilerParser.STROKE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 135
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = nevermorecompilerParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 130
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 131
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 132
                    self.expr(6) 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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

        def RPAREN(self):
            return self.getToken(nevermorecompilerParser.RPAREN, 0)

        def END_STATE(self):
            return self.getToken(nevermorecompilerParser.END_STATE, 0)

        def expr(self):
            return self.getTypedRuleContext(nevermorecompilerParser.ExprContext,0)


        def DIGIT(self):
            return self.getToken(nevermorecompilerParser.DIGIT, 0)

        def STROKE(self):
            return self.getToken(nevermorecompilerParser.STROKE, 0)

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
        self.enterRule(localctx, 26, self.RULE_printState)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(nevermorecompilerParser.T__4)
            self.state = 139
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 143
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 140
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 141
                self.match(nevermorecompilerParser.DIGIT)
                pass

            elif la_ == 3:
                self.state = 142
                self.match(nevermorecompilerParser.STROKE)
                pass


            self.state = 145
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 146
            self.match(nevermorecompilerParser.END_STATE)
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
        self.enterRule(localctx, 28, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.expr(0)
            self.state = 149
            localctx.op = self.relop()
            self.state = 150
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
        self.enterRule(localctx, 30, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
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
        self.enterRule(localctx, 32, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.type_()
            self.state = 155
            self.match(nevermorecompilerParser.ID)
            self.state = 156
            self.match(nevermorecompilerParser.EQ)
            self.state = 157
            self.expr(0)
            self.state = 158
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
        self.enterRule(localctx, 34, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 960) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




