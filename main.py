from src.PyM import MExpression, dataflow_split_queries
import os
import json

def main():
    file_path = os.path.join('queries', 'imdb_dataflow.txt')
    file_path_nested = os.path.join('queries', 'table_nested_join.txt')
    
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()

    with open(file_path_nested, 'r', encoding='utf-8') as file:
        query_nested = file.read()
    
    #loads a json with queries
    with open(r"C:\Users\KlausFolz\Desktop\Brunner BI Repositories\measurekiller_core\temp\dataflow_api_response.json", 'r', encoding='utf-8') as file:
        dataflow_json = json.load(file)
    
    dataflow_document = dataflow_json.get("pbi:mashup").get("document")
    
    queries_dict = dataflow_split_queries(query)
    
    
    
    for key, value in queries_dict.items():
        print(f"Query Name: {key}")
        print(f"Query Text: {value}\n")
   
    #MExpression(dataflow_document).print_tokens()
   
    #expr = MExpression(query_nested)
    #expr.print_tokens()
    #print(expr.extract_comments())
    
if __name__ == '__main__':
    main()
