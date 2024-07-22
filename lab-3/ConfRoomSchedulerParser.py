# Generated from /program/ConfRoomScheduler.g4 by ANTLR 4.13.1
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
        4,1,14,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,52,8,4,10,4,12,4,55,9,4,1,5,
        5,5,58,8,5,10,5,12,5,61,9,5,1,5,0,0,6,0,2,4,6,8,10,0,0,61,0,13,1,
        0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,39,1,0,0,0,8,48,1,0,0,0,10,59,
        1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,
        15,16,1,0,0,0,16,1,1,0,0,0,17,18,3,4,2,0,18,19,5,11,0,0,19,25,1,
        0,0,0,20,21,3,6,3,0,21,22,5,11,0,0,22,25,1,0,0,0,23,25,5,11,0,0,
        24,17,1,0,0,0,24,20,1,0,0,0,24,23,1,0,0,0,25,3,1,0,0,0,26,27,5,1,
        0,0,27,28,5,10,0,0,28,29,5,2,0,0,29,30,5,8,0,0,30,31,5,3,0,0,31,
        32,5,9,0,0,32,33,5,4,0,0,33,34,5,9,0,0,34,35,5,5,0,0,35,36,3,8,4,
        0,36,37,5,6,0,0,37,38,3,10,5,0,38,5,1,0,0,0,39,40,5,7,0,0,40,41,
        5,10,0,0,41,42,5,2,0,0,42,43,5,8,0,0,43,44,5,3,0,0,44,45,5,9,0,0,
        45,46,5,4,0,0,46,47,5,9,0,0,47,7,1,0,0,0,48,53,5,13,0,0,49,50,5,
        12,0,0,50,52,5,13,0,0,51,49,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,
        53,54,1,0,0,0,54,9,1,0,0,0,55,53,1,0,0,0,56,58,5,14,0,0,57,56,1,
        0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,11,1,0,0,0,61,
        59,1,0,0,0,4,15,24,53,59
    ]

class ConfRoomSchedulerParser ( Parser ):

    grammarFileName = "ConfRoomScheduler.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'RESERVAR'", "'PARA'", "'DE'", "'A'", 
                     "'CON'", "'DESCR'", "'CANCELAR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "DATE", "TIME", "ID", "NEWLINE", "WS", "WORD", "CHAR" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_reserve = 2
    RULE_cancel = 3
    RULE_name = 4
    RULE_description = 5

    ruleNames =  [ "prog", "stat", "reserve", "cancel", "name", "description" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    DATE=8
    TIME=9
    ID=10
    NEWLINE=11
    WS=12
    WORD=13
    CHAR=14

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
                return self.getTypedRuleContexts(ConfRoomSchedulerParser.StatContext)
            else:
                return self.getTypedRuleContext(ConfRoomSchedulerParser.StatContext,i)


        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ConfRoomSchedulerParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2178) != 0)):
                    break

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


        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class ReserveStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def reserve(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.ReserveContext,0)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserveStat" ):
                listener.enterReserveStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserveStat" ):
                listener.exitReserveStat(self)


    class CancelStatContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ConfRoomSchedulerParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def cancel(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.CancelContext,0)

        def NEWLINE(self):
            return self.getToken(ConfRoomSchedulerParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCancelStat" ):
                listener.enterCancelStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCancelStat" ):
                listener.exitCancelStat(self)



    def stat(self):

        localctx = ConfRoomSchedulerParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ConfRoomSchedulerParser.ReserveStatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.reserve()
                self.state = 18
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [7]:
                localctx = ConfRoomSchedulerParser.CancelStatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.cancel()
                self.state = 21
                self.match(ConfRoomSchedulerParser.NEWLINE)
                pass
            elif token in [11]:
                localctx = ConfRoomSchedulerParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                self.match(ConfRoomSchedulerParser.NEWLINE)
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


    class ReserveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ConfRoomSchedulerParser.ID, 0)

        def DATE(self):
            return self.getToken(ConfRoomSchedulerParser.DATE, 0)

        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)

        def name(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.NameContext,0)


        def description(self):
            return self.getTypedRuleContext(ConfRoomSchedulerParser.DescriptionContext,0)


        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_reserve

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReserve" ):
                listener.enterReserve(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReserve" ):
                listener.exitReserve(self)




    def reserve(self):

        localctx = ConfRoomSchedulerParser.ReserveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_reserve)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(ConfRoomSchedulerParser.T__0)
            self.state = 27
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 28
            self.match(ConfRoomSchedulerParser.T__1)
            self.state = 29
            self.match(ConfRoomSchedulerParser.DATE)
            self.state = 30
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 31
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 32
            self.match(ConfRoomSchedulerParser.T__3)
            self.state = 33
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 34
            self.match(ConfRoomSchedulerParser.T__4)
            self.state = 35
            self.name()
            self.state = 36
            self.match(ConfRoomSchedulerParser.T__5)
            self.state = 37
            self.description()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CancelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ConfRoomSchedulerParser.ID, 0)

        def DATE(self):
            return self.getToken(ConfRoomSchedulerParser.DATE, 0)

        def TIME(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.TIME)
            else:
                return self.getToken(ConfRoomSchedulerParser.TIME, i)

        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_cancel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCancel" ):
                listener.enterCancel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCancel" ):
                listener.exitCancel(self)




    def cancel(self):

        localctx = ConfRoomSchedulerParser.CancelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cancel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ConfRoomSchedulerParser.T__6)
            self.state = 40
            self.match(ConfRoomSchedulerParser.ID)
            self.state = 41
            self.match(ConfRoomSchedulerParser.T__1)
            self.state = 42
            self.match(ConfRoomSchedulerParser.DATE)
            self.state = 43
            self.match(ConfRoomSchedulerParser.T__2)
            self.state = 44
            self.match(ConfRoomSchedulerParser.TIME)
            self.state = 45
            self.match(ConfRoomSchedulerParser.T__3)
            self.state = 46
            self.match(ConfRoomSchedulerParser.TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.WORD)
            else:
                return self.getToken(ConfRoomSchedulerParser.WORD, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.WS)
            else:
                return self.getToken(ConfRoomSchedulerParser.WS, i)

        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = ConfRoomSchedulerParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ConfRoomSchedulerParser.WORD)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 49
                self.match(ConfRoomSchedulerParser.WS)
                self.state = 50
                self.match(ConfRoomSchedulerParser.WORD)
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DescriptionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(ConfRoomSchedulerParser.CHAR)
            else:
                return self.getToken(ConfRoomSchedulerParser.CHAR, i)

        def getRuleIndex(self):
            return ConfRoomSchedulerParser.RULE_description

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDescription" ):
                listener.enterDescription(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDescription" ):
                listener.exitDescription(self)




    def description(self):

        localctx = ConfRoomSchedulerParser.DescriptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_description)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 56
                self.match(ConfRoomSchedulerParser.CHAR)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





