# The data of CUNIT

This folder contains cultural concepts and triples used by CUNIT. As we stated in the article, we divide the cultural concept triples into three groups according to small, middle and large.

Also, we classify the triplets according to similarity, category, and whether to exchange candidates.

## Instructions

In solution.py and prompt.py in the code, we have defined the method of using cultural concept triples. You can use any feature of cultural concepts by 1. reading JSON files and 2. referencing key-value pairs.



## Key-Value Description

We will use an example to illustrate the Key-Value in the data.

    {
        "query_concept": "Suea pat", # The name of query concept
        "query_country": "Thailand", # The country of query concept
        "query_user": "woman",       # The user features of query concept
        "query_occasion": "wedding", # The occasion features of query concept
        "query_significance": "",    # The significance features of query concept
        
        "candidate_concept_0": "Guan (headwear)", 
        "candidate_country_0": "China",
        "candidate_user_0": "the rulers, ...,
        "candidate_occasion_0": "Guan Li, ...",
        "candidate_significance_0": "social status, ...",

        "candidate_concept_1": "Xiuhefu",
        "candidate_country_1": "China",
        "candidate_user_1": "Han Chinese woman",
        "candidate_occasion_1": "wedding",
        "candidate_significance_1": "love for whole seasons",

        "similarity_query_0": 0.11, # The similarity of query and candidate_0
        "similarity_query_1": 0.8   # The similarity of query and candidate_1
    },