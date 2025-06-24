from src.PyM.MExpression import MExpression
import os

def main():
    file_path = os.path.join('queries', 'table_nested_join.txt')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

   
    expr = MExpression(query)
    no_comments = expr.remove_comments()
    #print("M Expression without comments:")
    #print(no_comments)
    print(expr.extract_comments())
    
if __name__ == '__main__':
    main()
