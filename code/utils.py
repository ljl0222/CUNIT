import json
import os

# This class contains many utility functions.
class Utils:
    def __init__(self):
        pass

    def get_correct_answer(self, examples):
        if examples['similarity_query_0'] > examples['similarity_query_1']:
            return f"{examples['candidate_concept_0']} > {examples['candidate_concept_1']}"
        elif examples['similarity_query_0'] < examples['similarity_query_1']:
            return f"{examples['candidate_concept_0']} < {examples['candidate_concept_1']}"
        
    def repeat_three_times(self, input, output, func):
        path_list = output.split('/')
        path_list.pop()
        
        path = ''
        for k in path_list:
            path += k + '/'
            print(path)
            if not os.path.exists(path):
                os.mkdir(path)

        for i in range(3):
            output_i = str(output) + str(f'_try{i}.json')
            func(input, output_i)
    
    def get_json_data(self, path):
        with open(path, 'r', encoding='utf-8') as data:
            ret = json.load(data)
        return ret
    
    def write_data_in_json(self, data, path):
        with open(path, 'w', encoding='utf-8') as storefile:
            json.dump(data, storefile, indent=4, ensure_ascii=False)
            