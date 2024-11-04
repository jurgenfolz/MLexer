# Generated from C:/Users/KlausFolz/Desktop/GD/Repositories/MLexer/src/PyM/PowerQueryParser.g4 by ANTLR 4.13.2
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
        4,1,73,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,0,1,0,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,42,
        8,3,10,3,12,3,45,9,3,1,4,1,4,1,4,1,4,1,5,1,5,3,5,53,8,5,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,68,8,6,1,6,1,6,3,
        6,72,8,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,80,8,7,10,7,12,7,83,9,7,1,7,
        1,7,1,8,1,8,1,8,3,8,90,8,8,1,8,1,8,1,9,1,9,1,9,5,9,97,8,9,10,9,12,
        9,100,9,9,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,0,
        101,0,23,1,0,0,0,2,31,1,0,0,0,4,33,1,0,0,0,6,38,1,0,0,0,8,46,1,0,
        0,0,10,52,1,0,0,0,12,54,1,0,0,0,14,75,1,0,0,0,16,86,1,0,0,0,18,93,
        1,0,0,0,20,101,1,0,0,0,22,24,3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,
        25,23,1,0,0,0,25,26,1,0,0,0,26,27,1,0,0,0,27,28,5,0,0,1,28,1,1,0,
        0,0,29,32,3,4,2,0,30,32,3,10,5,0,31,29,1,0,0,0,31,30,1,0,0,0,32,
        3,1,0,0,0,33,34,5,29,0,0,34,35,3,6,3,0,35,36,5,30,0,0,36,37,3,10,
        5,0,37,5,1,0,0,0,38,43,3,8,4,0,39,40,5,6,0,0,40,42,3,8,4,0,41,39,
        1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,7,1,0,0,0,45,
        43,1,0,0,0,46,47,5,70,0,0,47,48,5,5,0,0,48,49,3,10,5,0,49,9,1,0,
        0,0,50,53,3,12,6,0,51,53,3,16,8,0,52,50,1,0,0,0,52,51,1,0,0,0,53,
        11,1,0,0,0,54,55,5,66,0,0,55,56,5,11,0,0,56,57,5,70,0,0,57,58,5,
        6,0,0,58,59,3,14,7,0,59,60,5,6,0,0,60,61,5,70,0,0,61,62,5,6,0,0,
        62,63,3,14,7,0,63,64,5,6,0,0,64,67,5,67,0,0,65,66,5,6,0,0,66,68,
        5,70,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,71,1,0,0,0,69,70,5,6,0,0,
        70,72,5,70,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,73,1,0,0,0,73,74,5,
        12,0,0,74,13,1,0,0,0,75,76,5,9,0,0,76,81,5,67,0,0,77,78,5,6,0,0,
        78,80,5,67,0,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,
        0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,10,0,0,85,15,1,0,0,0,86,
        87,5,70,0,0,87,89,5,11,0,0,88,90,3,18,9,0,89,88,1,0,0,0,89,90,1,
        0,0,0,90,91,1,0,0,0,91,92,5,12,0,0,92,17,1,0,0,0,93,98,3,10,5,0,
        94,95,5,6,0,0,95,97,3,10,5,0,96,94,1,0,0,0,97,100,1,0,0,0,98,96,
        1,0,0,0,98,99,1,0,0,0,99,19,1,0,0,0,100,98,1,0,0,0,101,102,1,0,0,
        0,102,21,1,0,0,0,9,25,31,43,52,67,71,81,89,98
    ]

class PowerQueryParser ( Parser ):

    grammarFileName = "PowerQueryParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "','", "'['", "']'", "'{'", "'}'", 
                     "'('", "')'", "'?'", "'optional'", "'table'", "'nullable'", 
                     "';'", "'section'", "'shared'", "'and'", "'or'", "'otherwise'", 
                     "'try'", "'error'", "'function ('", "'...'", "'type'", 
                     "'each'", "'let'", "'in'", "'if'", "'then'", "'else'", 
                     "'text'", "'record'", "'number'", "'none'", "'logical'", 
                     "'list'", "'fuction'", "'duration'", "'datetimezone'", 
                     "'any'", "'anynonnull'", "'binary'", "'date'", "'datetime'", 
                     "'@'", "'as'", "'=>'", "'..'", "'!'", "'not'", "'+'", 
                     "'-'", "'meta'", "'is'", "'<>'", "'>'", "'<'", "'/'", 
                     "'*'", "'&'", "'<='", "'>='", "'Table.NestedJoin'" ]

    symbolicNames = [ "<INVALID>", "WHITESPACE", "NEW_LINE_CHAR", "COMMENT", 
                      "CHARACHTER_ESCAPE_SEQUENCE", "EQUALS", "COMMA", "OPEN_BRACKET", 
                      "CLOSE_BRACKET", "OPEN_BRACE", "CLOSE_BRACE", "OPEN_PAREN", 
                      "CLOSE_PAREN", "OPTIONAL", "OPTIONAL_TEXT", "TABLE", 
                      "NULLABLE", "SEMICOLON", "SECTION", "SHARED", "AND", 
                      "OR", "OTHERWISE", "TRY", "ERROR", "FUNCTION_START", 
                      "ELLIPSES", "TYPE", "EACH", "LET", "IN", "IF", "THEN", 
                      "ELSE", "TEXT", "RECORD", "NUMBER", "NONE", "LOGICAL", 
                      "LIST", "FUNCTION", "DURATION", "DATETIMEZONE", "ANY", 
                      "ANYNONNULL", "BINARY", "DATE", "DATETIME", "AT", 
                      "AS", "ARROW", "DOTDOT", "BANG", "NOT", "PLUS", "MINUS", 
                      "META", "IS", "NEQ", "GE", "LE", "SLASH", "STAR", 
                      "AMP", "LEQ", "GEQ", "TABLE_NESTED_JOIN", "LITERAL", 
                      "TEXT_LITERAL", "COLUMN_REFERENCE", "IDENTIFIER", 
                      "REGULAR_IDENTIFIER", "AVAILABLE_IDENTIFIER", "KEYWORD_OR_IDENTIFIER" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_letExpression = 2
    RULE_assignmentList = 3
    RULE_assignment = 4
    RULE_expression = 5
    RULE_tableNestedJoinFunction = 6
    RULE_literalList = 7
    RULE_functionCall = 8
    RULE_argumentList = 9
    RULE_otherExpression = 10

    ruleNames =  [ "program", "statement", "letExpression", "assignmentList", 
                   "assignment", "expression", "tableNestedJoinFunction", 
                   "literalList", "functionCall", "argumentList", "otherExpression" ]

    EOF = Token.EOF
    WHITESPACE=1
    NEW_LINE_CHAR=2
    COMMENT=3
    CHARACHTER_ESCAPE_SEQUENCE=4
    EQUALS=5
    COMMA=6
    OPEN_BRACKET=7
    CLOSE_BRACKET=8
    OPEN_BRACE=9
    CLOSE_BRACE=10
    OPEN_PAREN=11
    CLOSE_PAREN=12
    OPTIONAL=13
    OPTIONAL_TEXT=14
    TABLE=15
    NULLABLE=16
    SEMICOLON=17
    SECTION=18
    SHARED=19
    AND=20
    OR=21
    OTHERWISE=22
    TRY=23
    ERROR=24
    FUNCTION_START=25
    ELLIPSES=26
    TYPE=27
    EACH=28
    LET=29
    IN=30
    IF=31
    THEN=32
    ELSE=33
    TEXT=34
    RECORD=35
    NUMBER=36
    NONE=37
    LOGICAL=38
    LIST=39
    FUNCTION=40
    DURATION=41
    DATETIMEZONE=42
    ANY=43
    ANYNONNULL=44
    BINARY=45
    DATE=46
    DATETIME=47
    AT=48
    AS=49
    ARROW=50
    DOTDOT=51
    BANG=52
    NOT=53
    PLUS=54
    MINUS=55
    META=56
    IS=57
    NEQ=58
    GE=59
    LE=60
    SLASH=61
    STAR=62
    AMP=63
    LEQ=64
    GEQ=65
    TABLE_NESTED_JOIN=66
    LITERAL=67
    TEXT_LITERAL=68
    COLUMN_REFERENCE=69
    IDENTIFIER=70
    REGULAR_IDENTIFIER=71
    AVAILABLE_IDENTIFIER=72
    KEYWORD_OR_IDENTIFIER=73

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PowerQueryParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.StatementContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.StatementContext,i)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_program

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

        localctx = PowerQueryParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & 2336462209025) != 0)):
                    break

            self.state = 27
            self.match(PowerQueryParser.EOF)
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

        def letExpression(self):
            return self.getTypedRuleContext(PowerQueryParser.LetExpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_statement

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

        localctx = PowerQueryParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.letExpression()
                pass
            elif token in [66, 70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.expression()
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


    class LetExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(PowerQueryParser.LET, 0)

        def assignmentList(self):
            return self.getTypedRuleContext(PowerQueryParser.AssignmentListContext,0)


        def IN(self):
            return self.getToken(PowerQueryParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_letExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetExpression" ):
                listener.enterLetExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetExpression" ):
                listener.exitLetExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetExpression" ):
                return visitor.visitLetExpression(self)
            else:
                return visitor.visitChildren(self)




    def letExpression(self):

        localctx = PowerQueryParser.LetExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_letExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(PowerQueryParser.LET)
            self.state = 34
            self.assignmentList()
            self.state = 35
            self.match(PowerQueryParser.IN)
            self.state = 36
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.AssignmentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.COMMA)
            else:
                return self.getToken(PowerQueryParser.COMMA, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_assignmentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentList" ):
                listener.enterAssignmentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentList" ):
                listener.exitAssignmentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentList" ):
                return visitor.visitAssignmentList(self)
            else:
                return visitor.visitChildren(self)




    def assignmentList(self):

        localctx = PowerQueryParser.AssignmentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignmentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.assignment()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 39
                self.match(PowerQueryParser.COMMA)
                self.state = 40
                self.assignment()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def EQUALS(self):
            return self.getToken(PowerQueryParser.EQUALS, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = PowerQueryParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(PowerQueryParser.IDENTIFIER)
            self.state = 47
            self.match(PowerQueryParser.EQUALS)
            self.state = 48
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableNestedJoinFunction(self):
            return self.getTypedRuleContext(PowerQueryParser.TableNestedJoinFunctionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(PowerQueryParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PowerQueryParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [66]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.tableNestedJoinFunction()
                pass
            elif token in [70]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.functionCall()
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


    class TableNestedJoinFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.firstTable = None # Token
            self.firstKeyColumns = None # LiteralListContext
            self.secondTable = None # Token
            self.secondKeyColumns = None # LiteralListContext
            self.newColumnName = None # Token
            self.joinKind = None # Token
            self.keyEqualityComparer = None # Token

        def TABLE_NESTED_JOIN(self):
            return self.getToken(PowerQueryParser.TABLE_NESTED_JOIN, 0)

        def OPEN_PAREN(self):
            return self.getToken(PowerQueryParser.OPEN_PAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.COMMA)
            else:
                return self.getToken(PowerQueryParser.COMMA, i)

        def CLOSE_PAREN(self):
            return self.getToken(PowerQueryParser.CLOSE_PAREN, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.IDENTIFIER)
            else:
                return self.getToken(PowerQueryParser.IDENTIFIER, i)

        def literalList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.LiteralListContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.LiteralListContext,i)


        def LITERAL(self):
            return self.getToken(PowerQueryParser.LITERAL, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_tableNestedJoinFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableNestedJoinFunction" ):
                listener.enterTableNestedJoinFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableNestedJoinFunction" ):
                listener.exitTableNestedJoinFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableNestedJoinFunction" ):
                return visitor.visitTableNestedJoinFunction(self)
            else:
                return visitor.visitChildren(self)




    def tableNestedJoinFunction(self):

        localctx = PowerQueryParser.TableNestedJoinFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tableNestedJoinFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(PowerQueryParser.TABLE_NESTED_JOIN)
            self.state = 55
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 56
            localctx.firstTable = self.match(PowerQueryParser.IDENTIFIER)
            self.state = 57
            self.match(PowerQueryParser.COMMA)
            self.state = 58
            localctx.firstKeyColumns = self.literalList()
            self.state = 59
            self.match(PowerQueryParser.COMMA)
            self.state = 60
            localctx.secondTable = self.match(PowerQueryParser.IDENTIFIER)
            self.state = 61
            self.match(PowerQueryParser.COMMA)
            self.state = 62
            localctx.secondKeyColumns = self.literalList()
            self.state = 63
            self.match(PowerQueryParser.COMMA)
            self.state = 64
            localctx.newColumnName = self.match(PowerQueryParser.LITERAL)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 65
                self.match(PowerQueryParser.COMMA)
                self.state = 66
                localctx.joinKind = self.match(PowerQueryParser.IDENTIFIER)


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 69
                self.match(PowerQueryParser.COMMA)
                self.state = 70
                localctx.keyEqualityComparer = self.match(PowerQueryParser.IDENTIFIER)


            self.state = 73
            self.match(PowerQueryParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(PowerQueryParser.OPEN_BRACE, 0)

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.LITERAL)
            else:
                return self.getToken(PowerQueryParser.LITERAL, i)

        def CLOSE_BRACE(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACE, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.COMMA)
            else:
                return self.getToken(PowerQueryParser.COMMA, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_literalList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralList" ):
                listener.enterLiteralList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralList" ):
                listener.exitLiteralList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralList" ):
                return visitor.visitLiteralList(self)
            else:
                return visitor.visitChildren(self)




    def literalList(self):

        localctx = PowerQueryParser.LiteralListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literalList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(PowerQueryParser.OPEN_BRACE)
            self.state = 76
            self.match(PowerQueryParser.LITERAL)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 77
                self.match(PowerQueryParser.COMMA)
                self.state = 78
                self.match(PowerQueryParser.LITERAL)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(PowerQueryParser.CLOSE_BRACE)
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

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def OPEN_PAREN(self):
            return self.getToken(PowerQueryParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(PowerQueryParser.CLOSE_PAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(PowerQueryParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_functionCall

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

        localctx = PowerQueryParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(PowerQueryParser.IDENTIFIER)
            self.state = 87
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==66 or _la==70:
                self.state = 88
                self.argumentList()


            self.state = 91
            self.match(PowerQueryParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.COMMA)
            else:
                return self.getToken(PowerQueryParser.COMMA, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = PowerQueryParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.expression()
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 94
                self.match(PowerQueryParser.COMMA)
                self.state = 95
                self.expression()
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OtherExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PowerQueryParser.RULE_otherExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOtherExpression" ):
                listener.enterOtherExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOtherExpression" ):
                listener.exitOtherExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOtherExpression" ):
                return visitor.visitOtherExpression(self)
            else:
                return visitor.visitChildren(self)




    def otherExpression(self):

        localctx = PowerQueryParser.OtherExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_otherExpression)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





