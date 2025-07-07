from src.PyM import MExpression, dataflow_split_queries
import os
import json

def main():
    file_path = os.path.join('queries', 'table_nested_join.txt')
    file_path_nested = os.path.join('queries', 'parameter.txt')
    file_function = os.path.join('queries', 'custom_func.txt')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

    with open(file_path_nested, 'r', encoding='utf-8') as file:
        query_param = file.read()
        
    with open(file_function, 'r', encoding='utf-8') as file:
        query_function = file.read()
    
    
    # dataflow_document = dataflow_json.get("pbi:mashup").get("document")
    # queries_dict = dataflow_split_queries(query)
    # for key, value in queries_dict.items():
    #     print(f"Query Name: {key}")
    #     print(f"Query Text: {value}\n")
   
    #MExpression(dataflow_document).print_tokens()
   
    expr = MExpression(query)
    expr_param = MExpression(query_param)
    expr_function = MExpression(query_function)
    
    print(f"Query: {expr._kind}")
    print(f"Query Parameter: {expr_param._kind}")
    print(f"Query Function: {expr_function._kind}") 
   
    
    
if __name__ == '__main__':
    main()
