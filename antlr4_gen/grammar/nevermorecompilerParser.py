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
        4,1,29,176,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,5,4,74,8,4,10,4,12,4,77,9,4,1,5,5,5,80,8,5,10,5,12,5,83,
        9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,5,9,106,8,9,10,9,12,9,109,9,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,12,5,12,131,8,12,10,12,12,12,134,9,12,1,13,
        1,13,1,13,1,13,3,13,140,8,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,
        148,8,13,10,13,12,13,151,9,13,1,14,1,14,1,14,1,14,3,14,157,8,14,
        1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,17,1,17,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,0,1,26,19,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,0,4,1,0,15,16,1,0,13,14,1,0,19,22,1,0,7,8,173,
        0,41,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,61,1,0,0,0,8,75,1,0,0,0,
        10,81,1,0,0,0,12,84,1,0,0,0,14,95,1,0,0,0,16,98,1,0,0,0,18,107,1,
        0,0,0,20,110,1,0,0,0,22,119,1,0,0,0,24,132,1,0,0,0,26,139,1,0,0,
        0,28,152,1,0,0,0,30,161,1,0,0,0,32,165,1,0,0,0,34,167,1,0,0,0,36,
        173,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,39,1,0,
        0,0,41,42,1,0,0,0,42,1,1,0,0,0,43,41,1,0,0,0,44,53,3,34,17,0,45,
        53,3,28,14,0,46,53,3,4,2,0,47,53,3,6,3,0,48,53,3,12,6,0,49,53,3,
        20,10,0,50,53,3,22,11,0,51,53,5,28,0,0,52,44,1,0,0,0,52,45,1,0,0,
        0,52,46,1,0,0,0,52,47,1,0,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,
        1,0,0,0,52,51,1,0,0,0,53,3,1,0,0,0,54,55,5,1,0,0,55,56,3,30,15,0,
        56,57,5,23,0,0,57,58,3,8,4,0,58,59,5,24,0,0,59,60,5,12,0,0,60,5,
        1,0,0,0,61,62,5,1,0,0,62,63,3,30,15,0,63,64,5,23,0,0,64,65,3,8,4,
        0,65,66,5,24,0,0,66,67,5,2,0,0,67,68,5,23,0,0,68,69,3,10,5,0,69,
        70,5,24,0,0,70,71,5,12,0,0,71,7,1,0,0,0,72,74,3,2,1,0,73,72,1,0,
        0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,9,1,0,0,0,77,75,
        1,0,0,0,78,80,3,2,1,0,79,78,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,
        81,82,1,0,0,0,82,11,1,0,0,0,83,81,1,0,0,0,84,85,5,3,0,0,85,86,5,
        17,0,0,86,87,3,16,8,0,87,88,3,30,15,0,88,89,5,12,0,0,89,90,3,14,
        7,0,90,91,5,18,0,0,91,92,5,23,0,0,92,93,3,18,9,0,93,94,5,24,0,0,
        94,13,1,0,0,0,95,96,5,9,0,0,96,97,5,25,0,0,97,15,1,0,0,0,98,99,3,
        36,18,0,99,100,5,9,0,0,100,101,5,26,0,0,101,102,3,26,13,0,102,103,
        5,12,0,0,103,17,1,0,0,0,104,106,3,2,1,0,105,104,1,0,0,0,106,109,
        1,0,0,0,107,105,1,0,0,0,107,108,1,0,0,0,108,19,1,0,0,0,109,107,1,
        0,0,0,110,111,5,4,0,0,111,112,5,17,0,0,112,113,3,30,15,0,113,114,
        5,18,0,0,114,115,5,23,0,0,115,116,3,24,12,0,116,117,5,24,0,0,117,
        118,5,12,0,0,118,21,1,0,0,0,119,120,5,5,0,0,120,121,5,23,0,0,121,
        122,3,24,12,0,122,123,5,24,0,0,123,124,5,4,0,0,124,125,5,17,0,0,
        125,126,3,30,15,0,126,127,5,18,0,0,127,128,5,12,0,0,128,23,1,0,0,
        0,129,131,3,2,1,0,130,129,1,0,0,0,131,134,1,0,0,0,132,130,1,0,0,
        0,132,133,1,0,0,0,133,25,1,0,0,0,134,132,1,0,0,0,135,136,6,13,-1,
        0,136,140,5,10,0,0,137,140,5,9,0,0,138,140,5,11,0,0,139,135,1,0,
        0,0,139,137,1,0,0,0,139,138,1,0,0,0,140,149,1,0,0,0,141,142,10,5,
        0,0,142,143,7,0,0,0,143,148,3,26,13,6,144,145,10,4,0,0,145,146,7,
        1,0,0,146,148,3,26,13,5,147,141,1,0,0,0,147,144,1,0,0,0,148,151,
        1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,27,1,0,0,0,151,149,1,
        0,0,0,152,153,5,6,0,0,153,156,5,17,0,0,154,157,3,26,13,0,155,157,
        5,29,0,0,156,154,1,0,0,0,156,155,1,0,0,0,157,158,1,0,0,0,158,159,
        5,18,0,0,159,160,5,12,0,0,160,29,1,0,0,0,161,162,3,26,13,0,162,163,
        3,32,16,0,163,164,3,26,13,0,164,31,1,0,0,0,165,166,7,2,0,0,166,33,
        1,0,0,0,167,168,3,36,18,0,168,169,5,9,0,0,169,170,5,26,0,0,170,171,
        3,26,13,0,171,172,5,12,0,0,172,35,1,0,0,0,173,174,7,3,0,0,174,37,
        1,0,0,0,10,41,52,75,81,107,132,139,147,149,156
    ]

class nevermorecompilerParser ( Parser ):

    grammarFileName = "nevermorecompiler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'while'", 
                     "'do'", "'print'", "'int'", "'double'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'", "'+'", "'-'", "'*'", 
                     "'/'", "'('", "')'", "'>'", "'<'", "'=='", "'!='", 
                     "'{'", "'}'", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "INT", "DOUBLE", "END_STATE", "ADD", 
                      "SUB", "MUL", "DIV", "LPAREN", "RPAREN", "GT", "LT", 
                      "EQ_EQ", "NOT_EQ", "RCORNER", "LCORNER", "INCREMENT", 
                      "EQ", "WS", "NEWLINE", "DIGIT" ]

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
    RULE_equation = 15
    RULE_relop = 16
    RULE_assignmentStatement = 17
    RULE_type = 18

    ruleNames =  [ "prog", "stat", "ifStatement", "ifElseStatement", "ifBody", 
                   "elseBody", "forStatement", "forModify", "forInit", "forBody", 
                   "whileStatement", "doWhileStatement", "whileBody", "expr", 
                   "printState", "equation", "relop", "assignmentStatement", 
                   "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ID=9
    INT=10
    DOUBLE=11
    END_STATE=12
    ADD=13
    SUB=14
    MUL=15
    DIV=16
    LPAREN=17
    RPAREN=18
    GT=19
    LT=20
    EQ_EQ=21
    NOT_EQ=22
    RCORNER=23
    LCORNER=24
    INCREMENT=25
    EQ=26
    WS=27
    NEWLINE=28
    DIGIT=29

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
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435962) != 0):
                self.state = 38
                self.stat()
                self.state = 43
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


        def doWhileStatement(self):
            return self.getTypedRuleContext(nevermorecompilerParser.DoWhileStatementContext,0)


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
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.assignmentStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.printState()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.ifElseStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.forStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 49
                self.whileStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 50
                self.doWhileStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 51
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
            self.state = 54
            self.match(nevermorecompilerParser.T__0)
            self.state = 55
            self.equation()
            self.state = 56
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 57
            self.ifBody()
            self.state = 58
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 59
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
            self.state = 61
            self.match(nevermorecompilerParser.T__0)
            self.state = 62
            self.equation()
            self.state = 63
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 64
            self.ifBody()
            self.state = 65
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 66
            self.match(nevermorecompilerParser.T__1)
            self.state = 67
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 68
            self.elseBody()
            self.state = 69
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 70
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
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435962) != 0):
                self.state = 72
                self.stat()
                self.state = 77
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
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435962) != 0):
                self.state = 78
                self.stat()
                self.state = 83
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
            self.state = 84
            self.match(nevermorecompilerParser.T__2)
            self.state = 85
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 86
            self.forInit()
            self.state = 87
            self.equation()
            self.state = 88
            self.match(nevermorecompilerParser.END_STATE)
            self.state = 89
            self.forModify()
            self.state = 90
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 91
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 92
            self.forBody()
            self.state = 93
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
            self.state = 95
            self.match(nevermorecompilerParser.ID)
            self.state = 96
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
            self.state = 98
            self.type_()
            self.state = 99
            self.match(nevermorecompilerParser.ID)
            self.state = 100
            self.match(nevermorecompilerParser.EQ)
            self.state = 101
            self.expr(0)
            self.state = 102
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
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435962) != 0):
                self.state = 104
                self.stat()
                self.state = 109
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
            self.state = 110
            self.match(nevermorecompilerParser.T__3)
            self.state = 111
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 112
            self.equation()
            self.state = 113
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 114
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 115
            self.whileBody()
            self.state = 116
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 117
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
            self.state = 119
            self.match(nevermorecompilerParser.T__4)
            self.state = 120
            self.match(nevermorecompilerParser.RCORNER)
            self.state = 121
            self.whileBody()
            self.state = 122
            self.match(nevermorecompilerParser.LCORNER)
            self.state = 123
            self.match(nevermorecompilerParser.T__3)
            self.state = 124
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 125
            self.equation()
            self.state = 126
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 127
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
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 268435962) != 0):
                self.state = 129
                self.stat()
                self.state = 134
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
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 136
                self.match(nevermorecompilerParser.INT)
                pass
            elif token in [9]:
                self.state = 137
                self.match(nevermorecompilerParser.ID)
                pass
            elif token in [11]:
                self.state = 138
                self.match(nevermorecompilerParser.DOUBLE)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 147
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = nevermorecompilerParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 142
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 143
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = nevermorecompilerParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 144
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 145
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 146
                        self.expr(5)
                        pass

             
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
            self.state = 152
            self.match(nevermorecompilerParser.T__5)
            self.state = 153
            self.match(nevermorecompilerParser.LPAREN)
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 10, 11]:
                self.state = 154
                self.expr(0)
                pass
            elif token in [29]:
                self.state = 155
                self.match(nevermorecompilerParser.DIGIT)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 158
            self.match(nevermorecompilerParser.RPAREN)
            self.state = 159
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
        self.enterRule(localctx, 30, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.expr(0)
            self.state = 162
            localctx.op = self.relop()
            self.state = 163
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
        self.enterRule(localctx, 32, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
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
        self.enterRule(localctx, 34, self.RULE_assignmentStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.type_()
            self.state = 168
            self.match(nevermorecompilerParser.ID)
            self.state = 169
            self.match(nevermorecompilerParser.EQ)
            self.state = 170
            self.expr(0)
            self.state = 171
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
        self.enterRule(localctx, 36, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            _la = self._input.LA(1)
            if not(_la==7 or _la==8):
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
         




