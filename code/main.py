from chatbot import ChatBot
from utils import Utils
from prompt import Prompt
from solution import Solution
import os

if __name__ == '__main__':
    myChatBot = ChatBot()
    myUtils = Utils()
    allDs = myUtils.get_json_data('prompt.json')
    myPrompt = Prompt(allDs)
    mySolution = Solution(myChatBot, myUtils, myPrompt)

    # example

    input = os.environ.get('MY_INPUT_FILE')
    output = os.environ.get('MY_OUTPUT_FILE')

    mySolution.pipeline(input, output, myPrompt.InputOutputWithFeatures)
    