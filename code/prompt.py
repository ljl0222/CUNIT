# Evaluate using different prompts
class Prompt:
    def __init__(self, allDs):
        # Here list some examples.
        self.FoodOneshotDs = allDs[0]
        self.ClothingOneshotDs = allDs[1]
        self.FoodChainOfThoughtDs = allDs[2]
        self.ClothingChainOfThoughtDs = allDs[3]

        self.OneshotDs = allDs[0]
        self.ChainOfThoughtDs = allDs[2]

    # Construct different prompt templates.
    def InputOutputWithFeatures(self, examples):
        question = (
f'''Question: Please sort the following 'Cultural-specific Concepts' in descending order of similarityfeature overlap between 'Cultural-specific Concepts' with '{examples['query_concept']}' in terms of user, occasion and symbolic meaning.
Cultural-specific Concepts: '{examples['candidate_concept_0']}', '{examples['candidate_concept_1']}'
Features of '{examples['query_concept']}': 1. User: {examples['query_user']}; 2. Occasions: {examples['query_occasion']}; 3. Symbolic Meaning: {examples['query_significance']}.
Features of '{examples['candidate_concept_0']}': 1. User: {examples['candidate_user_0']}; 2. Occasions: {examples['candidate_occasion_0']}; 3. Symbolic Meaning: {examples['candidate_significance_0']}.
Features of '{examples['candidate_concept_1']}': 1. User: {examples['candidate_user_1']}; 2. Occasions: {examples['candidate_occasion_1']}; 3. Symbolic Meaning: {examples['candidate_significance_1']}.
Answer Format: If '{examples['query_concept']}' and '{examples['candidate_concept_0']}' are more similar than '{examples['query_concept']}' and '{examples['candidate_concept_1']}' in terms of user, occasion and symbolic meaning, please answer {examples['candidate_concept_0']} > {examples['candidate_concept_1']}, otherwise answer {examples['candidate_concept_0']} < {examples['candidate_concept_1']}.
Answer: ''')
        return question
    
    def InputOutputWithoutFeatures(self, examples):
        question = (
f'''Question: Please sort the following 'Cultural-specific Concepts' in descending order of similarityfeature overlap between 'Cultural-specific Concepts' with '{examples['query_concept']}' in terms of user, occasion and symbolic meaning.
Cultural-specific Concepts: '{examples['candidate_concept_0']}', '{examples['candidate_concept_1']}'
Answer Format: If '{examples['query_concept']}' and '{examples['candidate_concept_0']}' are more similar than '{examples['query_concept']}' and '{examples['candidate_concept_1']}' in terms of user, occasion and symbolic meaning, please answer {examples['candidate_concept_0']} > {examples['candidate_concept_1']}, otherwise answer {examples['candidate_concept_0']} < {examples['candidate_concept_1']}.
Answer: ''')
        return question
    
    def InputOutputWithoutName(self, examples):
        examples['query_concept'] = 'conceptA'
        examples['candidate_concept_0'] = 'conceptB'
        examples['candidate_concept_1'] = 'conceptC'
        question = self.InputOutputWithFeatures(examples)
        return question
    
    def OneshotWithFeatures(self, examples):
        ds = self.OneshotDs
        question = (
f'''{ds}Question: Please sort the following 'Cultural-specific Concepts' in descending order of similarity feature overlap between 'Cultural-specific Concepts' with '{examples['query_concept']}' in terms of user, occasion and symbolic meaning.
Cultural-specific Concepts: '{examples['candidate_concept_0']}', '{examples['candidate_concept_1']}'
Features of '{examples['query_concept']}': 1. User: {examples['query_user']}; 2. Occasions: {examples['query_occasion']}; 3. Symbolic Meaning: {examples['query_significance']}.
Features of '{examples['candidate_concept_0']}': 1. User: {examples['candidate_user_0']}; 2. Occasions: {examples['candidate_occasion_0']}; 3. Symbolic Meaning: {examples['candidate_significance_0']}.
Features of '{examples['candidate_concept_1']}': 1. User: {examples['candidate_user_1']}; 2. Occasions: {examples['candidate_occasion_1']}; 3. Symbolic Meaning: {examples['candidate_significance_1']}.
Answer Format: If '{examples['query_concept']}' and '{examples['candidate_concept_0']}' are more similar than '{examples['query_concept']}' and '{examples['candidate_concept_1']}' in terms of user, occasion and symbolic meaning, please answer {examples['candidate_concept_0']} > {examples['candidate_concept_1']}, otherwise answer {examples['candidate_concept_0']} < {examples['candidate_concept_1']}.
Answer: ''')
        return question
    
    def OneshotWithoutFeatures(self, examples):
        ds = self.OneshotDs
        question = (
f'''{ds}Question: Please sort the following 'Cultural-specific Concepts' in descending order of similarity feature overlap between 'Cultural-specific Concepts' with '{examples['query_concept']}' in terms of user, occasion and symbolic meaning.
Cultural-specific Concepts: '{examples['candidate_concept_0']}', '{examples['candidate_concept_1']}'
Answer Format: If '{examples['query_concept']}' and '{examples['candidate_concept_0']}' are more similar than '{examples['query_concept']}' and '{examples['candidate_concept_1']}' in terms of user, occasion and symbolic meaning, please answer {examples['candidate_concept_0']} > {examples['candidate_concept_1']}, otherwise answer {examples['candidate_concept_0']} < {examples['candidate_concept_1']}.
Answer: ''')
        return question
    
    def OneshotWithoutName(self, examples):
        examples['query_concept'] = 'conceptA'
        examples['candidate_concept_0'] = 'conceptB'
        examples['candidate_concept_1'] = 'conceptC'
        question = self.OneshotWithFeatures(examples)
        return question
    
    def ChainOfThoughtWithFeatures(self, examples):
        ds = self.ChainOfThoughtDs
        question = (
f'''{ds}Question: Please sort the following 'Cultural-specific Concepts' in descending order of similarity feature overlap between 'Cultural-specific Concepts' with '{examples['query_concept']}' in terms of user, occasion and symbolic meaning.
Cultural-specific Concepts: '{examples['candidate_concept_0']}', '{examples['candidate_concept_1']}'
Features of '{examples['query_concept']}': 1. User: {examples['query_user']}; 2. Occasions: {examples['query_occasion']}; 3. Symbolic Meaning: {examples['query_significance']}.
Features of '{examples['candidate_concept_0']}': 1. User: {examples['candidate_user_0']}; 2. Occasions: {examples['candidate_occasion_0']}; 3. Symbolic Meaning: {examples['candidate_significance_0']}.
Features of '{examples['candidate_concept_1']}': 1. User: {examples['candidate_user_1']}; 2. Occasions: {examples['candidate_occasion_1']}; 3. Symbolic Meaning: {examples['candidate_significance_1']}.
Answer Format: If '{examples['query_concept']}' and '{examples['candidate_concept_0']}' are more similar than '{examples['query_concept']}' and '{examples['candidate_concept_1']}' in terms of user, occasion and symbolic meaning, please answer {examples['candidate_concept_0']} > {examples['candidate_concept_1']}, otherwise answer {examples['candidate_concept_0']} < {examples['candidate_concept_1']}.
Answer: ''')
        return question
    
    def ChainOfThoughtWithoutFeatures(self, examples):
        ds = self.ChainOfThoughtDs
        question = (
f'''{ds}Question: Please sort the following 'Cultural-specific Concepts' in descending order of similarity feature overlap between 'Cultural-specific Concepts' with '{examples['query_concept']}' in terms of user, occasion and symbolic meaning.
Cultural-specific Concepts: '{examples['candidate_concept_0']}', '{examples['candidate_concept_1']}'
Answer Format: If '{examples['query_concept']}' and '{examples['candidate_concept_0']}' are more similar than '{examples['query_concept']}' and '{examples['candidate_concept_1']}' in terms of user, occasion and symbolic meaning, please answer {examples['candidate_concept_0']} > {examples['candidate_concept_1']}, otherwise answer {examples['candidate_concept_0']} < {examples['candidate_concept_1']}.
Answer: ''')
        return question
    
    def ChainOfThoughtWithoutName(self, examples):
        examples['query_concept'] = 'conceptA'
        examples['candidate_concept_0'] = 'conceptB'
        examples['candidate_concept_1'] = 'conceptC'
        question = self.ChainOfThoughtWithFeatures(examples)
        return question