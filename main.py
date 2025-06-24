from src.PyM.MExpression import MExpression
import os

def main():
    file_path = os.path.join('queries', 'complex_query.txt')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

    expr = MExpression(query)
    expr.print_tokens()

    
if __name__ == '__main__':
    main()


