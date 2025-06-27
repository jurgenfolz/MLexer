from src.PyM import MExpression, dataflow_split_queries
import os

def main():
    file_path = os.path.join('queries', 'dataflow_queries.txt')
    file_path_nested = os.path.join('queries', 'table_nested_join.txt')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

    with open(file_path_nested, 'r', encoding='utf-8') as file:
        query_nested = file.read()
   
    print(dataflow_split_queries(query).get("dCities"))
   
    expr = MExpression(query_nested)
    #expr.print_tokens()
    print(expr.extract_comments())
    
if __name__ == '__main__':
    main()
