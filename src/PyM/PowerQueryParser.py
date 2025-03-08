# Generated from src/PyM/PowerQueryParser.g4 by ANTLR 4.13.2
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
        4,1,75,217,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,4,0,46,8,0,11,0,12,0,47,1,0,1,0,1,1,1,1,3,1,54,
        8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,64,8,3,10,3,12,3,67,9,3,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,83,8,
        5,1,6,1,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,
        3,10,100,8,10,1,10,1,10,1,11,1,11,1,11,3,11,107,8,11,1,12,3,12,110,
        8,12,1,12,1,12,5,12,114,8,12,10,12,12,12,117,9,12,1,13,1,13,1,13,
        3,13,122,8,13,1,13,1,13,1,14,1,14,1,14,5,14,129,8,14,10,14,12,14,
        132,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,3,15,147,8,15,1,15,1,15,3,15,151,8,15,1,15,1,15,1,16,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,164,8,16,1,16,1,16,1,
        17,1,17,1,17,5,17,171,8,17,10,17,12,17,174,9,17,1,18,1,18,1,18,1,
        18,5,18,180,8,18,10,18,12,18,183,9,18,1,18,1,18,1,19,1,19,1,19,1,
        19,5,19,191,8,19,10,19,12,19,194,9,19,3,19,196,8,19,1,19,1,19,1,
        20,1,20,1,20,1,20,5,20,204,8,20,10,20,12,20,207,9,20,3,20,209,8,
        20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,0,0,22,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,1,6,0,34,34,36,36,38,
        38,41,42,45,45,47,47,221,0,45,1,0,0,0,2,53,1,0,0,0,4,55,1,0,0,0,
        6,60,1,0,0,0,8,68,1,0,0,0,10,82,1,0,0,0,12,84,1,0,0,0,14,86,1,0,
        0,0,16,90,1,0,0,0,18,93,1,0,0,0,20,97,1,0,0,0,22,106,1,0,0,0,24,
        109,1,0,0,0,26,118,1,0,0,0,28,125,1,0,0,0,30,133,1,0,0,0,32,154,
        1,0,0,0,34,167,1,0,0,0,36,175,1,0,0,0,38,186,1,0,0,0,40,199,1,0,
        0,0,42,212,1,0,0,0,44,46,3,2,1,0,45,44,1,0,0,0,46,47,1,0,0,0,47,
        45,1,0,0,0,47,48,1,0,0,0,48,49,1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,
        0,51,54,3,4,2,0,52,54,3,10,5,0,53,51,1,0,0,0,53,52,1,0,0,0,54,3,
        1,0,0,0,55,56,5,29,0,0,56,57,3,6,3,0,57,58,5,30,0,0,58,59,3,10,5,
        0,59,5,1,0,0,0,60,65,3,8,4,0,61,62,5,6,0,0,62,64,3,8,4,0,63,61,1,
        0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,7,1,0,0,0,67,
        65,1,0,0,0,68,69,5,72,0,0,69,70,5,5,0,0,70,71,3,10,5,0,71,9,1,0,
        0,0,72,83,3,30,15,0,73,83,3,32,16,0,74,83,3,26,13,0,75,83,3,12,6,
        0,76,83,3,14,7,0,77,83,3,18,9,0,78,83,3,20,10,0,79,83,3,16,8,0,80,
        83,3,38,19,0,81,83,3,40,20,0,82,72,1,0,0,0,82,73,1,0,0,0,82,74,1,
        0,0,0,82,75,1,0,0,0,82,76,1,0,0,0,82,77,1,0,0,0,82,78,1,0,0,0,82,
        79,1,0,0,0,82,80,1,0,0,0,82,81,1,0,0,0,83,11,1,0,0,0,84,85,5,69,
        0,0,85,13,1,0,0,0,86,87,5,11,0,0,87,88,3,10,5,0,88,89,5,12,0,0,89,
        15,1,0,0,0,90,91,5,28,0,0,91,92,3,10,5,0,92,17,1,0,0,0,93,94,3,14,
        7,0,94,95,5,56,0,0,95,96,3,40,20,0,96,19,1,0,0,0,97,99,5,27,0,0,
        98,100,5,16,0,0,99,98,1,0,0,0,99,100,1,0,0,0,100,101,1,0,0,0,101,
        102,3,22,11,0,102,21,1,0,0,0,103,104,5,15,0,0,104,107,3,40,20,0,
        105,107,3,24,12,0,106,103,1,0,0,0,106,105,1,0,0,0,107,23,1,0,0,0,
        108,110,7,0,0,0,109,108,1,0,0,0,109,110,1,0,0,0,110,115,1,0,0,0,
        111,112,5,68,0,0,112,114,5,72,0,0,113,111,1,0,0,0,114,117,1,0,0,
        0,115,113,1,0,0,0,115,116,1,0,0,0,116,25,1,0,0,0,117,115,1,0,0,0,
        118,119,3,34,17,0,119,121,5,11,0,0,120,122,3,28,14,0,121,120,1,0,
        0,0,121,122,1,0,0,0,122,123,1,0,0,0,123,124,5,12,0,0,124,27,1,0,
        0,0,125,130,3,10,5,0,126,127,5,6,0,0,127,129,3,10,5,0,128,126,1,
        0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,29,1,0,
        0,0,132,130,1,0,0,0,133,134,5,66,0,0,134,135,5,11,0,0,135,136,5,
        72,0,0,136,137,5,6,0,0,137,138,3,36,18,0,138,139,5,6,0,0,139,140,
        5,72,0,0,140,141,5,6,0,0,141,142,3,36,18,0,142,143,5,6,0,0,143,146,
        5,69,0,0,144,145,5,6,0,0,145,147,5,72,0,0,146,144,1,0,0,0,146,147,
        1,0,0,0,147,150,1,0,0,0,148,149,5,6,0,0,149,151,5,72,0,0,150,148,
        1,0,0,0,150,151,1,0,0,0,151,152,1,0,0,0,152,153,5,12,0,0,153,31,
        1,0,0,0,154,155,5,67,0,0,155,156,5,11,0,0,156,157,5,72,0,0,157,158,
        5,6,0,0,158,159,5,69,0,0,159,160,5,6,0,0,160,163,3,36,18,0,161,162,
        5,6,0,0,162,164,3,36,18,0,163,161,1,0,0,0,163,164,1,0,0,0,164,165,
        1,0,0,0,165,166,5,12,0,0,166,33,1,0,0,0,167,172,5,72,0,0,168,169,
        5,68,0,0,169,171,5,72,0,0,170,168,1,0,0,0,171,174,1,0,0,0,172,170,
        1,0,0,0,172,173,1,0,0,0,173,35,1,0,0,0,174,172,1,0,0,0,175,176,5,
        9,0,0,176,181,5,69,0,0,177,178,5,6,0,0,178,180,5,69,0,0,179,177,
        1,0,0,0,180,183,1,0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,184,
        1,0,0,0,183,181,1,0,0,0,184,185,5,10,0,0,185,37,1,0,0,0,186,195,
        5,9,0,0,187,192,3,10,5,0,188,189,5,6,0,0,189,191,3,10,5,0,190,188,
        1,0,0,0,191,194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,196,
        1,0,0,0,194,192,1,0,0,0,195,187,1,0,0,0,195,196,1,0,0,0,196,197,
        1,0,0,0,197,198,5,10,0,0,198,39,1,0,0,0,199,208,5,7,0,0,200,205,
        3,42,21,0,201,202,5,6,0,0,202,204,3,42,21,0,203,201,1,0,0,0,204,
        207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,209,1,0,0,0,207,
        205,1,0,0,0,208,200,1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,
        211,5,8,0,0,211,41,1,0,0,0,212,213,3,10,5,0,213,214,5,5,0,0,214,
        215,3,10,5,0,215,43,1,0,0,0,19,47,53,65,82,99,106,109,115,121,130,
        146,150,163,172,181,192,195,205,208
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
                     "'*'", "'&'", "'<='", "'>='", "'Table.NestedJoin'", 
                     "'Table.ExpandTableColumn'", "'.'" ]

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
                      "AMP", "LEQ", "GEQ", "TABLE_NESTED_JOIN", "TABLE_EXPAND_TABLE_COLUMN", 
                      "DOT", "LITERAL", "TEXT_LITERAL", "COLUMN_REFERENCE", 
                      "IDENTIFIER", "REGULAR_IDENTIFIER", "AVAILABLE_IDENTIFIER", 
                      "KEYWORD_OR_IDENTIFIER" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_letExpression = 2
    RULE_assignmentList = 3
    RULE_assignment = 4
    RULE_expression = 5
    RULE_literal_expression = 6
    RULE_parenthesized_expression = 7
    RULE_each_expression = 8
    RULE_meta_expression = 9
    RULE_type_expression = 10
    RULE_type_body = 11
    RULE_dottedTypeName = 12
    RULE_functionCall = 13
    RULE_argumentList = 14
    RULE_tableNestedJoinFunction = 15
    RULE_tableExpandTableColumnFunction = 16
    RULE_dottedIdentifier = 17
    RULE_literalList = 18
    RULE_list_expression = 19
    RULE_record_expression = 20
    RULE_record_field = 21

    ruleNames =  [ "program", "statement", "letExpression", "assignmentList", 
                   "assignment", "expression", "literal_expression", "parenthesized_expression", 
                   "each_expression", "meta_expression", "type_expression", 
                   "type_body", "dottedTypeName", "functionCall", "argumentList", 
                   "tableNestedJoinFunction", "tableExpandTableColumnFunction", 
                   "dottedIdentifier", "literalList", "list_expression", 
                   "record_expression", "record_field" ]

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
    TABLE_EXPAND_TABLE_COLUMN=67
    DOT=68
    LITERAL=69
    TEXT_LITERAL=70
    COLUMN_REFERENCE=71
    IDENTIFIER=72
    REGULAR_IDENTIFIER=73
    AVAILABLE_IDENTIFIER=74
    KEYWORD_OR_IDENTIFIER=75

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
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.statement()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 939526784) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 75) != 0)):
                    break

            self.state = 49
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
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.letExpression()
                pass
            elif token in [7, 9, 11, 27, 28, 66, 67, 69, 72]:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
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
            self.state = 55
            self.match(PowerQueryParser.LET)
            self.state = 56
            self.assignmentList()
            self.state = 57
            self.match(PowerQueryParser.IN)
            self.state = 58
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
            self.state = 60
            self.assignment()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 61
                self.match(PowerQueryParser.COMMA)
                self.state = 62
                self.assignment()
                self.state = 67
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
            self.state = 68
            self.match(PowerQueryParser.IDENTIFIER)
            self.state = 69
            self.match(PowerQueryParser.EQUALS)
            self.state = 70
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


        def tableExpandTableColumnFunction(self):
            return self.getTypedRuleContext(PowerQueryParser.TableExpandTableColumnFunctionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(PowerQueryParser.FunctionCallContext,0)


        def literal_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Literal_expressionContext,0)


        def parenthesized_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Parenthesized_expressionContext,0)


        def meta_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Meta_expressionContext,0)


        def type_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Type_expressionContext,0)


        def each_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Each_expressionContext,0)


        def list_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.List_expressionContext,0)


        def record_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Record_expressionContext,0)


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
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.tableNestedJoinFunction()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.tableExpandTableColumnFunction()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.functionCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.literal_expression()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.parenthesized_expression()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 77
                self.meta_expression()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 78
                self.type_expression()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 79
                self.each_expression()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 80
                self.list_expression()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 81
                self.record_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LITERAL(self):
            return self.getToken(PowerQueryParser.LITERAL, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_literal_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral_expression" ):
                listener.enterLiteral_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral_expression" ):
                listener.exitLiteral_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_expression" ):
                return visitor.visitLiteral_expression(self)
            else:
                return visitor.visitChildren(self)




    def literal_expression(self):

        localctx = PowerQueryParser.Literal_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_literal_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(PowerQueryParser.LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parenthesized_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(PowerQueryParser.OPEN_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(PowerQueryParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_parenthesized_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesized_expression" ):
                listener.enterParenthesized_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesized_expression" ):
                listener.exitParenthesized_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesized_expression" ):
                return visitor.visitParenthesized_expression(self)
            else:
                return visitor.visitChildren(self)




    def parenthesized_expression(self):

        localctx = PowerQueryParser.Parenthesized_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_parenthesized_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 87
            self.expression()
            self.state = 88
            self.match(PowerQueryParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Each_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EACH(self):
            return self.getToken(PowerQueryParser.EACH, 0)

        def expression(self):
            return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_each_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEach_expression" ):
                listener.enterEach_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEach_expression" ):
                listener.exitEach_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEach_expression" ):
                return visitor.visitEach_expression(self)
            else:
                return visitor.visitChildren(self)




    def each_expression(self):

        localctx = PowerQueryParser.Each_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_each_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(PowerQueryParser.EACH)
            self.state = 91
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Meta_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parenthesized_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Parenthesized_expressionContext,0)


        def META(self):
            return self.getToken(PowerQueryParser.META, 0)

        def record_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Record_expressionContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_meta_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMeta_expression" ):
                listener.enterMeta_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMeta_expression" ):
                listener.exitMeta_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMeta_expression" ):
                return visitor.visitMeta_expression(self)
            else:
                return visitor.visitChildren(self)




    def meta_expression(self):

        localctx = PowerQueryParser.Meta_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_meta_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.parenthesized_expression()
            self.state = 94
            self.match(PowerQueryParser.META)
            self.state = 95
            self.record_expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(PowerQueryParser.TYPE, 0)

        def type_body(self):
            return self.getTypedRuleContext(PowerQueryParser.Type_bodyContext,0)


        def NULLABLE(self):
            return self.getToken(PowerQueryParser.NULLABLE, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_type_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_expression" ):
                listener.enterType_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_expression" ):
                listener.exitType_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_expression" ):
                return visitor.visitType_expression(self)
            else:
                return visitor.visitChildren(self)




    def type_expression(self):

        localctx = PowerQueryParser.Type_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(PowerQueryParser.TYPE)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 98
                self.match(PowerQueryParser.NULLABLE)


            self.state = 101
            self.type_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TABLE(self):
            return self.getToken(PowerQueryParser.TABLE, 0)

        def record_expression(self):
            return self.getTypedRuleContext(PowerQueryParser.Record_expressionContext,0)


        def dottedTypeName(self):
            return self.getTypedRuleContext(PowerQueryParser.DottedTypeNameContext,0)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_type_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_body" ):
                listener.enterType_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_body" ):
                listener.exitType_body(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_body" ):
                return visitor.visitType_body(self)
            else:
                return visitor.visitChildren(self)




    def type_body(self):

        localctx = PowerQueryParser.Type_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_body)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.match(PowerQueryParser.TABLE)
                self.state = 104
                self.record_expression()
                pass
            elif token in [-1, 5, 6, 7, 8, 9, 10, 11, 12, 27, 28, 29, 30, 34, 36, 38, 41, 42, 45, 47, 66, 67, 68, 69, 72]:
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.dottedTypeName()
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


    class DottedTypeNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.DOT)
            else:
                return self.getToken(PowerQueryParser.DOT, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.IDENTIFIER)
            else:
                return self.getToken(PowerQueryParser.IDENTIFIER, i)

        def TEXT(self):
            return self.getToken(PowerQueryParser.TEXT, 0)

        def NUMBER(self):
            return self.getToken(PowerQueryParser.NUMBER, 0)

        def DATETIME(self):
            return self.getToken(PowerQueryParser.DATETIME, 0)

        def DATETIMEZONE(self):
            return self.getToken(PowerQueryParser.DATETIMEZONE, 0)

        def LOGICAL(self):
            return self.getToken(PowerQueryParser.LOGICAL, 0)

        def BINARY(self):
            return self.getToken(PowerQueryParser.BINARY, 0)

        def DURATION(self):
            return self.getToken(PowerQueryParser.DURATION, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_dottedTypeName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDottedTypeName" ):
                listener.enterDottedTypeName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDottedTypeName" ):
                listener.exitDottedTypeName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDottedTypeName" ):
                return visitor.visitDottedTypeName(self)
            else:
                return visitor.visitChildren(self)




    def dottedTypeName(self):

        localctx = PowerQueryParser.DottedTypeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dottedTypeName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 182879707463680) != 0):
                self.state = 108
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 182879707463680) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==68:
                self.state = 111
                self.match(PowerQueryParser.DOT)
                self.state = 112
                self.match(PowerQueryParser.IDENTIFIER)
                self.state = 117
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

        def dottedIdentifier(self):
            return self.getTypedRuleContext(PowerQueryParser.DottedIdentifierContext,0)


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
        self.enterRule(localctx, 26, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.dottedIdentifier()
            self.state = 119
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 402655872) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 75) != 0):
                self.state = 120
                self.argumentList()


            self.state = 123
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
        self.enterRule(localctx, 28, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.expression()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 126
                self.match(PowerQueryParser.COMMA)
                self.state = 127
                self.expression()
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 30, self.RULE_tableNestedJoinFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(PowerQueryParser.TABLE_NESTED_JOIN)
            self.state = 134
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 135
            localctx.firstTable = self.match(PowerQueryParser.IDENTIFIER)
            self.state = 136
            self.match(PowerQueryParser.COMMA)
            self.state = 137
            localctx.firstKeyColumns = self.literalList()
            self.state = 138
            self.match(PowerQueryParser.COMMA)
            self.state = 139
            localctx.secondTable = self.match(PowerQueryParser.IDENTIFIER)
            self.state = 140
            self.match(PowerQueryParser.COMMA)
            self.state = 141
            localctx.secondKeyColumns = self.literalList()
            self.state = 142
            self.match(PowerQueryParser.COMMA)
            self.state = 143
            localctx.newColumnName = self.match(PowerQueryParser.LITERAL)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 144
                self.match(PowerQueryParser.COMMA)
                self.state = 145
                localctx.joinKind = self.match(PowerQueryParser.IDENTIFIER)


            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 148
                self.match(PowerQueryParser.COMMA)
                self.state = 149
                localctx.keyEqualityComparer = self.match(PowerQueryParser.IDENTIFIER)


            self.state = 152
            self.match(PowerQueryParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableExpandTableColumnFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.table = None # Token
            self.column = None # Token
            self.columnsList = None # LiteralListContext
            self.NewColumnNamesList = None # LiteralListContext

        def TABLE_EXPAND_TABLE_COLUMN(self):
            return self.getToken(PowerQueryParser.TABLE_EXPAND_TABLE_COLUMN, 0)

        def OPEN_PAREN(self):
            return self.getToken(PowerQueryParser.OPEN_PAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.COMMA)
            else:
                return self.getToken(PowerQueryParser.COMMA, i)

        def CLOSE_PAREN(self):
            return self.getToken(PowerQueryParser.CLOSE_PAREN, 0)

        def IDENTIFIER(self):
            return self.getToken(PowerQueryParser.IDENTIFIER, 0)

        def LITERAL(self):
            return self.getToken(PowerQueryParser.LITERAL, 0)

        def literalList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.LiteralListContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.LiteralListContext,i)


        def getRuleIndex(self):
            return PowerQueryParser.RULE_tableExpandTableColumnFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableExpandTableColumnFunction" ):
                listener.enterTableExpandTableColumnFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableExpandTableColumnFunction" ):
                listener.exitTableExpandTableColumnFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableExpandTableColumnFunction" ):
                return visitor.visitTableExpandTableColumnFunction(self)
            else:
                return visitor.visitChildren(self)




    def tableExpandTableColumnFunction(self):

        localctx = PowerQueryParser.TableExpandTableColumnFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tableExpandTableColumnFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(PowerQueryParser.TABLE_EXPAND_TABLE_COLUMN)
            self.state = 155
            self.match(PowerQueryParser.OPEN_PAREN)
            self.state = 156
            localctx.table = self.match(PowerQueryParser.IDENTIFIER)
            self.state = 157
            self.match(PowerQueryParser.COMMA)
            self.state = 158
            localctx.column = self.match(PowerQueryParser.LITERAL)
            self.state = 159
            self.match(PowerQueryParser.COMMA)
            self.state = 160
            localctx.columnsList = self.literalList()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 161
                self.match(PowerQueryParser.COMMA)
                self.state = 162
                localctx.NewColumnNamesList = self.literalList()


            self.state = 165
            self.match(PowerQueryParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DottedIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.IDENTIFIER)
            else:
                return self.getToken(PowerQueryParser.IDENTIFIER, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.DOT)
            else:
                return self.getToken(PowerQueryParser.DOT, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_dottedIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDottedIdentifier" ):
                listener.enterDottedIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDottedIdentifier" ):
                listener.exitDottedIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDottedIdentifier" ):
                return visitor.visitDottedIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def dottedIdentifier(self):

        localctx = PowerQueryParser.DottedIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_dottedIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(PowerQueryParser.IDENTIFIER)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==68:
                self.state = 168
                self.match(PowerQueryParser.DOT)
                self.state = 169
                self.match(PowerQueryParser.IDENTIFIER)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 36, self.RULE_literalList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(PowerQueryParser.OPEN_BRACE)
            self.state = 176
            self.match(PowerQueryParser.LITERAL)
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 177
                self.match(PowerQueryParser.COMMA)
                self.state = 178
                self.match(PowerQueryParser.LITERAL)
                self.state = 183
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 184
            self.match(PowerQueryParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACE(self):
            return self.getToken(PowerQueryParser.OPEN_BRACE, 0)

        def CLOSE_BRACE(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACE, 0)

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
            return PowerQueryParser.RULE_list_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_expression" ):
                listener.enterList_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_expression" ):
                listener.exitList_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = PowerQueryParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_list_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(PowerQueryParser.OPEN_BRACE)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 402655872) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 75) != 0):
                self.state = 187
                self.expression()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 188
                    self.match(PowerQueryParser.COMMA)
                    self.state = 189
                    self.expression()
                    self.state = 194
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 197
            self.match(PowerQueryParser.CLOSE_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Record_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_BRACKET(self):
            return self.getToken(PowerQueryParser.OPEN_BRACKET, 0)

        def CLOSE_BRACKET(self):
            return self.getToken(PowerQueryParser.CLOSE_BRACKET, 0)

        def record_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.Record_fieldContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.Record_fieldContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PowerQueryParser.COMMA)
            else:
                return self.getToken(PowerQueryParser.COMMA, i)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_record_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord_expression" ):
                listener.enterRecord_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord_expression" ):
                listener.exitRecord_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecord_expression" ):
                return visitor.visitRecord_expression(self)
            else:
                return visitor.visitChildren(self)




    def record_expression(self):

        localctx = PowerQueryParser.Record_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_record_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(PowerQueryParser.OPEN_BRACKET)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 402655872) != 0) or ((((_la - 66)) & ~0x3f) == 0 and ((1 << (_la - 66)) & 75) != 0):
                self.state = 200
                self.record_field()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 201
                    self.match(PowerQueryParser.COMMA)
                    self.state = 202
                    self.record_field()
                    self.state = 207
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 210
            self.match(PowerQueryParser.CLOSE_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Record_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PowerQueryParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(PowerQueryParser.ExpressionContext,i)


        def EQUALS(self):
            return self.getToken(PowerQueryParser.EQUALS, 0)

        def getRuleIndex(self):
            return PowerQueryParser.RULE_record_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecord_field" ):
                listener.enterRecord_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecord_field" ):
                listener.exitRecord_field(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecord_field" ):
                return visitor.visitRecord_field(self)
            else:
                return visitor.visitChildren(self)




    def record_field(self):

        localctx = PowerQueryParser.Record_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_record_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.expression()
            self.state = 213
            self.match(PowerQueryParser.EQUALS)
            self.state = 214
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





