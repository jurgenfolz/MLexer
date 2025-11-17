from src.PyM import MExpression, dataflow_split_queries, PowerQueryLexer, PowerQueryParser, ParserExplorer
import os
import json
import datetime
from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorStrategy import BailErrorStrategy, DefaultErrorStrategy
from antlr4.atn.PredictionMode import PredictionMode


def main():
    
    
    query_file = 'table_nested_join3.txt'
    start_datetime = datetime.datetime.now()
    file_path = os.path.join('queries', query_file)
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()
        
    # expr = MExpression(query)   
    

    explorer = ParserExplorer(query)
    explorer.parse()
    end_datetime = datetime.datetime.now()
    print(f"Parsed query: {query_file}: {end_datetime - start_datetime}")
    #print(explorer.to_string_tree())
    
    print(explorer.collect_summary())
    # save summary to json
    summary = explorer.collect_summary()
    with open('summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
