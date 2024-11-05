from antlr4 import *
from src.PyM.PowerQueryLexer import PowerQueryLexer
from src.PyM.PowerQueryParser import PowerQueryParser
from src.PyM.visitors.TableNestedJoin import TableNestedJoinVisitor
import os

def main():

    file_path = os.path.join('queries', 'table_nested_join.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

if __name__ == '__main__':
    main()


