import openai
import os
import json
import time

openai.api_key = os.environ.get('MY_API_KEY')
openai.organization = os.environ.get('MY_ORGANIZATION')

# Implement a chatbot that can call different models of GPT through the official API of OpenAI.
class ChatBot:
    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.max_tokens = 1024
        self.temperature = 0
        self.role = "system"
    
    # Try to use the try-catch and get completion.
    def get_completion(self, question):
        while True:
            try:
                completion = openai.ChatCompletion.create(
                    model = self.model,
                    max_tokens = self.max_tokens,
                    temperature = self.temperature,
                    messages = [
                        {
                            "role": self.role,
                            "content": question
                        }
                    ],
                    request_timeout = 20,
                    )
                self.completion = completion
                return completion
            except Exception as e:
                print(f'errors:{e}')
                continue
    
    # Get the text content from the completion.
    def deal_completion(self, completion):
        answer = completion.choices[0].message['content']
        self.answer = answer
        return answer