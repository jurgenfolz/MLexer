from src.PyM import MExpression, dataflow_split_queries, PowerQueryLexer, PowerQueryParser
import os
import json
import datetime
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorStrategy import BailErrorStrategy, DefaultErrorStrategy
from antlr4.atn.PredictionMode import PredictionMode


def parse_with_fallback(parser: PowerQueryParser, tokens:CommonTokenStream, candidates=("document","expression_document","program","start","file","expression")):
    # Pick the first start rule that exists on this parser
    start = next((name for name in candidates if hasattr(parser, name)), None)
    if not start:
        raise AttributeError(f"No expected start rule found. Available rules: {parser.ruleNames}")

    # Stage 1: FAST SLL + bail
    parser._interp.predictionMode = PredictionMode.SLL
    parser._errHandler = BailErrorStrategy()
    parser.buildParseTrees = True

    try:
        return getattr(parser, start)()
    except Exception:
        # Stage 2: full LL with default error recovery
        tokens.seek(0)
        parser.reset()
        parser._interp.predictionMode = PredictionMode.LL
        parser._errHandler = DefaultErrorStrategy()
        return getattr(parser, start)()


def main():
    start_datetime = datetime.datetime.now()
    file_path = os.path.join('queries', 'dataflow_queries.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
         query = file.read()
    expr = MExpression(query)    


    lexer = PowerQueryLexer(InputStream(query))
    tokens = CommonTokenStream(lexer)
    parser = PowerQueryParser(tokens)

    tree:PowerQueryParser.DocumentContext = parse_with_fallback(parser, tokens)
    print(tree.toStringTree(recog=parser))
    end_datetime = datetime.datetime.now()
    print("Duration:", end_datetime - start_datetime)
    
    
if __name__ == '__main__':
    main()
