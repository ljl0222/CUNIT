import json
import time
from tqdm import tqdm

class Solution:
    def __init__(self, chatbot, utils, prompt):
        self.chatbot = chatbot
        self.utils = utils
        self.prompt = prompt

    def pipeline(self, input, output, template):
        with open(input, 'r', encoding='utf-8') as data:
            test_entities = json.load(data)
        cnt = 1
        ret = []
        # Read data sequentially to evaluate GPT.
        for i in tqdm(range(len(test_entities))):
            examples = test_entities[i]
            question = template(examples)
            correct_answer = self.utils.get_correct_answer(examples)
            completion = self.chatbot.get_completion(question)
            answer = self.chatbot.deal_completion(completion)
            ret.append({
                'index': cnt,
                'time': time.strftime('%Y%m%d-%H:%M:%S', time.localtime()),
                'question': question,
                'entity': examples,
                'answer': answer,
                'correct_answer': correct_answer,
            })
            cnt += 1
        with open(output, 'w', encoding='utf-8') as storefile:
            json.dump(ret, storefile, indent=4, ensure_ascii=False)
