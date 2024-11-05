from antlr4 import *
from src.PyM.MExpression import MExpression
from src.PyM.visitors.MExpressionVisitors import TableNestedJoinVisitor
from src.PyM.PowerQueryLexer import PowerQueryLexer
from src.PyM.PowerQueryParser import PowerQueryParser
import os

def main():
    file_path = os.path.join('queries', 'table_nested_join.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

    m_expression = MExpression(query)
    m_expression._visit()

    
if __name__ == '__main__':
    main()


