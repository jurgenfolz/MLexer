from antlr4 import *
from src.PyM.MExpression import MExpression
from src.PyM.PowerQueryLexer import PowerQueryLexer
import os

def main():
    file_path = os.path.join('queries', 'table_nested_join.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

    expr = MExpression(query)
    #expr.print_tokens()
    expr.build_dataflow()

    
if __name__ == '__main__':
    main()


