# Generated from MLTLM.g4 by ANTLR 4.10.1
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
        4,1,24,134,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,3,1,23,8,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,3,2,41,8,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,73,
        8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,
        105,8,3,10,3,12,3,108,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,128,8,4,1,5,1,5,1,5,1,5,1,
        5,0,1,6,6,0,2,4,6,8,10,0,0,146,0,15,1,0,0,0,2,36,1,0,0,0,4,40,1,
        0,0,0,6,72,1,0,0,0,8,127,1,0,0,0,10,129,1,0,0,0,12,14,3,2,1,0,13,
        12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,18,1,0,0,
        0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,0,0,20,21,5,21,0,0,21,23,
        5,1,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,24,25,3,6,3,0,
        25,26,5,2,0,0,26,37,1,0,0,0,27,28,3,4,2,0,28,29,5,2,0,0,29,37,1,
        0,0,0,30,31,3,8,4,0,31,32,5,2,0,0,32,37,1,0,0,0,33,34,3,10,5,0,34,
        35,5,2,0,0,35,37,1,0,0,0,36,22,1,0,0,0,36,27,1,0,0,0,36,30,1,0,0,
        0,36,33,1,0,0,0,37,3,1,0,0,0,38,39,5,21,0,0,39,41,5,1,0,0,40,38,
        1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,3,6,3,0,43,44,5,3,0,0,
        44,45,3,6,3,0,45,5,1,0,0,0,46,47,6,3,-1,0,47,48,5,19,0,0,48,49,5,
        4,0,0,49,50,5,22,0,0,50,51,5,5,0,0,51,52,5,21,0,0,52,53,5,6,0,0,
        53,73,3,6,3,13,54,55,5,19,0,0,55,56,5,4,0,0,56,57,5,22,0,0,57,58,
        5,5,0,0,58,59,5,22,0,0,59,60,5,5,0,0,60,61,5,21,0,0,61,62,5,6,0,
        0,62,73,3,6,3,12,63,64,5,7,0,0,64,73,3,6,3,9,65,66,5,12,0,0,66,67,
        3,6,3,0,67,68,5,13,0,0,68,73,1,0,0,0,69,73,5,21,0,0,70,73,5,14,0,
        0,71,73,5,15,0,0,72,46,1,0,0,0,72,54,1,0,0,0,72,63,1,0,0,0,72,65,
        1,0,0,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,106,1,0,0,0,
        74,75,10,11,0,0,75,76,5,20,0,0,76,77,5,4,0,0,77,78,5,22,0,0,78,79,
        5,5,0,0,79,80,5,21,0,0,80,81,5,6,0,0,81,105,3,6,3,12,82,83,10,10,
        0,0,83,84,5,20,0,0,84,85,5,4,0,0,85,86,5,22,0,0,86,87,5,5,0,0,87,
        88,5,22,0,0,88,89,5,5,0,0,89,90,5,21,0,0,90,91,5,6,0,0,91,105,3,
        6,3,11,92,93,10,8,0,0,93,94,5,8,0,0,94,105,3,6,3,9,95,96,10,7,0,
        0,96,97,5,9,0,0,97,105,3,6,3,8,98,99,10,6,0,0,99,100,5,10,0,0,100,
        105,3,6,3,7,101,102,10,5,0,0,102,103,5,11,0,0,103,105,3,6,3,6,104,
        74,1,0,0,0,104,82,1,0,0,0,104,92,1,0,0,0,104,95,1,0,0,0,104,98,1,
        0,0,0,104,101,1,0,0,0,105,108,1,0,0,0,106,104,1,0,0,0,106,107,1,
        0,0,0,107,7,1,0,0,0,108,106,1,0,0,0,109,110,5,21,0,0,110,111,5,16,
        0,0,111,112,5,17,0,0,112,113,5,12,0,0,113,114,5,21,0,0,114,115,5,
        13,0,0,115,116,5,18,0,0,116,128,5,22,0,0,117,118,5,21,0,0,118,119,
        5,16,0,0,119,120,5,17,0,0,120,121,5,12,0,0,121,122,5,21,0,0,122,
        123,5,5,0,0,123,124,5,22,0,0,124,125,5,13,0,0,125,126,5,18,0,0,126,
        128,5,22,0,0,127,109,1,0,0,0,127,117,1,0,0,0,128,9,1,0,0,0,129,130,
        5,21,0,0,130,131,5,16,0,0,131,132,5,22,0,0,132,11,1,0,0,0,8,15,22,
        36,40,72,104,106,127
    ]

class MLTLMParser ( Parser ):

    grammarFileName = "MLTLM.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "';'", "'=>'", "'['", "','", "']'", 
                     "'!'", "'&'", "'|'", "'<->'", "'->'", "'('", "')'", 
                     "'TRUE'", "'FALSE'", "':='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Filter", "Conditional", "UnaryOperators", 
                      "BinaryOperators", "Identifier", "Number", "Comment", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_contract = 2
    RULE_expr = 3
    RULE_binding = 4
    RULE_mapping = 5

    ruleNames =  [ "program", "statement", "contract", "expr", "binding", 
                   "mapping" ]

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
    T__13=14
    T__14=15
    T__15=16
    Filter=17
    Conditional=18
    UnaryOperators=19
    BinaryOperators=20
    Identifier=21
    Number=22
    Comment=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MLTLMParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLTLMParser.StatementContext)
            else:
                return self.getTypedRuleContext(MLTLMParser.StatementContext,i)


        def getRuleIndex(self):
            return MLTLMParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MLTLMParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MLTLMParser.T__6) | (1 << MLTLMParser.T__11) | (1 << MLTLMParser.T__13) | (1 << MLTLMParser.T__14) | (1 << MLTLMParser.UnaryOperators) | (1 << MLTLMParser.Identifier))) != 0):
                self.state = 12
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(MLTLMParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MLTLMParser.ExprContext,0)


        def Identifier(self):
            return self.getToken(MLTLMParser.Identifier, 0)

        def contract(self):
            return self.getTypedRuleContext(MLTLMParser.ContractContext,0)


        def binding(self):
            return self.getTypedRuleContext(MLTLMParser.BindingContext,0)


        def mapping(self):
            return self.getTypedRuleContext(MLTLMParser.MappingContext,0)


        def getRuleIndex(self):
            return MLTLMParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MLTLMParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 20
                    self.match(MLTLMParser.Identifier)
                    self.state = 21
                    self.match(MLTLMParser.T__0)


                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(MLTLMParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.contract()
                self.state = 28
                self.match(MLTLMParser.T__1)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.binding()
                self.state = 31
                self.match(MLTLMParser.T__1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.mapping()
                self.state = 34
                self.match(MLTLMParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContractContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLTLMParser.ExprContext)
            else:
                return self.getTypedRuleContext(MLTLMParser.ExprContext,i)


        def Identifier(self):
            return self.getToken(MLTLMParser.Identifier, 0)

        def getRuleIndex(self):
            return MLTLMParser.RULE_contract

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContract" ):
                listener.enterContract(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContract" ):
                listener.exitContract(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContract" ):
                return visitor.visitContract(self)
            else:
                return visitor.visitChildren(self)




    def contract(self):

        localctx = MLTLMParser.ContractContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_contract)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 38
                self.match(MLTLMParser.Identifier)
                self.state = 39
                self.match(MLTLMParser.T__0)


            self.state = 42
            self.expr(0)
            self.state = 43
            self.match(MLTLMParser.T__2)
            self.state = 44
            self.expr(0)
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


        def getRuleIndex(self):
            return MLTLMParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Unary_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLTLMParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def UnaryOperators(self):
            return self.getToken(MLTLMParser.UnaryOperators, 0)
        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(MLTLMParser.Number)
            else:
                return self.getToken(MLTLMParser.Number, i)
        def Identifier(self):
            return self.getToken(MLTLMParser.Identifier, 0)
        def expr(self):
            return self.getTypedRuleContext(MLTLMParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary_expr" ):
                listener.enterUnary_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary_expr" ):
                listener.exitUnary_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary_expr" ):
                return visitor.visitUnary_expr(self)
            else:
                return visitor.visitChildren(self)


    class Binary_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLTLMParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLTLMParser.ExprContext)
            else:
                return self.getTypedRuleContext(MLTLMParser.ExprContext,i)

        def BinaryOperators(self):
            return self.getToken(MLTLMParser.BinaryOperators, 0)
        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(MLTLMParser.Number)
            else:
                return self.getToken(MLTLMParser.Number, i)
        def Identifier(self):
            return self.getToken(MLTLMParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinary_expr" ):
                listener.enterBinary_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinary_expr" ):
                listener.exitBinary_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinary_expr" ):
                return visitor.visitBinary_expr(self)
            else:
                return visitor.visitChildren(self)


    class Bool_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLTLMParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_expr" ):
                listener.enterBool_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_expr" ):
                listener.exitBool_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_expr" ):
                return visitor.visitBool_expr(self)
            else:
                return visitor.visitChildren(self)


    class Atom_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLTLMParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Identifier(self):
            return self.getToken(MLTLMParser.Identifier, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom_expr" ):
                listener.enterAtom_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom_expr" ):
                listener.exitAtom_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom_expr" ):
                return visitor.visitAtom_expr(self)
            else:
                return visitor.visitChildren(self)


    class Parens_exprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MLTLMParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(MLTLMParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens_expr" ):
                listener.enterParens_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens_expr" ):
                listener.exitParens_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens_expr" ):
                return visitor.visitParens_expr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MLTLMParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = MLTLMParser.Unary_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 47
                self.match(MLTLMParser.UnaryOperators)
                self.state = 48
                self.match(MLTLMParser.T__3)
                self.state = 49
                self.match(MLTLMParser.Number)
                self.state = 50
                self.match(MLTLMParser.T__4)
                self.state = 51
                self.match(MLTLMParser.Identifier)
                self.state = 52
                self.match(MLTLMParser.T__5)
                self.state = 53
                self.expr(13)
                pass

            elif la_ == 2:
                localctx = MLTLMParser.Unary_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(MLTLMParser.UnaryOperators)
                self.state = 55
                self.match(MLTLMParser.T__3)
                self.state = 56
                self.match(MLTLMParser.Number)
                self.state = 57
                self.match(MLTLMParser.T__4)
                self.state = 58
                self.match(MLTLMParser.Number)
                self.state = 59
                self.match(MLTLMParser.T__4)
                self.state = 60
                self.match(MLTLMParser.Identifier)
                self.state = 61
                self.match(MLTLMParser.T__5)
                self.state = 62
                self.expr(12)
                pass

            elif la_ == 3:
                localctx = MLTLMParser.Unary_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                localctx.op = self.match(MLTLMParser.T__6)
                self.state = 64
                self.expr(9)
                pass

            elif la_ == 4:
                localctx = MLTLMParser.Parens_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                self.match(MLTLMParser.T__11)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(MLTLMParser.T__12)
                pass

            elif la_ == 5:
                localctx = MLTLMParser.Atom_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 69
                self.match(MLTLMParser.Identifier)
                pass

            elif la_ == 6:
                localctx = MLTLMParser.Bool_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.match(MLTLMParser.T__13)
                pass

            elif la_ == 7:
                localctx = MLTLMParser.Bool_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(MLTLMParser.T__14)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 106
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 104
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = MLTLMParser.Binary_exprContext(self, MLTLMParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 75
                        self.match(MLTLMParser.BinaryOperators)
                        self.state = 76
                        self.match(MLTLMParser.T__3)
                        self.state = 77
                        self.match(MLTLMParser.Number)
                        self.state = 78
                        self.match(MLTLMParser.T__4)
                        self.state = 79
                        self.match(MLTLMParser.Identifier)
                        self.state = 80
                        self.match(MLTLMParser.T__5)
                        self.state = 81
                        self.expr(12)
                        pass

                    elif la_ == 2:
                        localctx = MLTLMParser.Binary_exprContext(self, MLTLMParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 82
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 83
                        self.match(MLTLMParser.BinaryOperators)
                        self.state = 84
                        self.match(MLTLMParser.T__3)
                        self.state = 85
                        self.match(MLTLMParser.Number)
                        self.state = 86
                        self.match(MLTLMParser.T__4)
                        self.state = 87
                        self.match(MLTLMParser.Number)
                        self.state = 88
                        self.match(MLTLMParser.T__4)
                        self.state = 89
                        self.match(MLTLMParser.Identifier)
                        self.state = 90
                        self.match(MLTLMParser.T__5)
                        self.state = 91
                        self.expr(11)
                        pass

                    elif la_ == 3:
                        localctx = MLTLMParser.Binary_exprContext(self, MLTLMParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 92
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 93
                        localctx.op = self.match(MLTLMParser.T__7)
                        self.state = 94
                        self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = MLTLMParser.Binary_exprContext(self, MLTLMParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 95
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 96
                        localctx.op = self.match(MLTLMParser.T__8)
                        self.state = 97
                        self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = MLTLMParser.Binary_exprContext(self, MLTLMParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 98
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 99
                        localctx.op = self.match(MLTLMParser.T__9)
                        self.state = 100
                        self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = MLTLMParser.Binary_exprContext(self, MLTLMParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 101
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 102
                        localctx.op = self.match(MLTLMParser.T__10)
                        self.state = 103
                        self.expr(6)
                        pass

             
                self.state = 108
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BindingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self, i:int=None):
            if i is None:
                return self.getTokens(MLTLMParser.Identifier)
            else:
                return self.getToken(MLTLMParser.Identifier, i)

        def Filter(self):
            return self.getToken(MLTLMParser.Filter, 0)

        def Conditional(self):
            return self.getToken(MLTLMParser.Conditional, 0)

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(MLTLMParser.Number)
            else:
                return self.getToken(MLTLMParser.Number, i)

        def getRuleIndex(self):
            return MLTLMParser.RULE_binding

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinding" ):
                listener.enterBinding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinding" ):
                listener.exitBinding(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinding" ):
                return visitor.visitBinding(self)
            else:
                return visitor.visitChildren(self)




    def binding(self):

        localctx = MLTLMParser.BindingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_binding)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(MLTLMParser.Identifier)
                self.state = 110
                self.match(MLTLMParser.T__15)
                self.state = 111
                self.match(MLTLMParser.Filter)
                self.state = 112
                self.match(MLTLMParser.T__11)
                self.state = 113
                self.match(MLTLMParser.Identifier)
                self.state = 114
                self.match(MLTLMParser.T__12)
                self.state = 115
                self.match(MLTLMParser.Conditional)
                self.state = 116
                self.match(MLTLMParser.Number)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 117
                self.match(MLTLMParser.Identifier)
                self.state = 118
                self.match(MLTLMParser.T__15)
                self.state = 119
                self.match(MLTLMParser.Filter)
                self.state = 120
                self.match(MLTLMParser.T__11)
                self.state = 121
                self.match(MLTLMParser.Identifier)
                self.state = 122
                self.match(MLTLMParser.T__4)
                self.state = 123
                self.match(MLTLMParser.Number)
                self.state = 124
                self.match(MLTLMParser.T__12)
                self.state = 125
                self.match(MLTLMParser.Conditional)
                self.state = 126
                self.match(MLTLMParser.Number)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MappingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(MLTLMParser.Identifier, 0)

        def Number(self):
            return self.getToken(MLTLMParser.Number, 0)

        def getRuleIndex(self):
            return MLTLMParser.RULE_mapping

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapping" ):
                listener.enterMapping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapping" ):
                listener.exitMapping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapping" ):
                return visitor.visitMapping(self)
            else:
                return visitor.visitChildren(self)




    def mapping(self):

        localctx = MLTLMParser.MappingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mapping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(MLTLMParser.Identifier)
            self.state = 130
            self.match(MLTLMParser.T__15)
            self.state = 131
            self.match(MLTLMParser.Number)
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
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         




