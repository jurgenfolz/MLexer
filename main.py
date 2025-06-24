from src.PyM.MExpression import MExpression
import os

def main():
    file_path = os.path.join('queries', 'simple_query.txt')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

    expr = MExpression(query)
    expr.write_tokens_to_txt("tokens.txt")

    
if __name__ == '__main__':
    main()
