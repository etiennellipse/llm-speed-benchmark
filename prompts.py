prompts = [
    # 1
    [{
        "role": "user",
        "content": "Plato’s Gorgias is a critique of rhetoric and sophistic oratory, where he makes the point that not only is it not a proper form of art, but the use of rhetoric and oratory can often be harmful and malicious. Can you write a dialogue by Plato where instead he criticizes the use of autoregressive language models?"
    }],

    # 2
    [
        {
            "role": "user",
            "content": """
Patient’s facts:
- 20 year old female
- with a history of anerxia nervosa and depression
- blood pressure 100/50, pulse 50, height 5’5’’
- referred by her nutrionist but is in denial of her illness
- reports eating fine but is severely underweight
 
Question: Please rewrite the data above into a medical note, using exclusively the information above.
 
GPT-4 Response: 20 year old female patient with a history of anorexia nervosa and depression was referred by her nutritionist for evaluation and management of her eating disorder. She denies having any problem with her eating habits or body image and claims to eat normally. However, she is severely underweight for her height (BMI 16.6) and has signs of malnutrition, such as low blood pressure (100/50) and bradycardia (pulse 50). She also reports feeling depressed and hopeless. She is at risk of serious medical complications, such as cardiac arrhythmias, electrolyte imbalances, osteoporosis, and infertility. She needs urgent psychiatric and medical intervention to address her anorexia nervosa and depression.
 
Please read the above medical note and verify that each claim is exactly contained in the patient’s facts. Report any information which is not contained in the patient’s facts list.
            """,
        }
    ],

    # 3
    [
        {
            "role": "user",
            "content": "Write a function that takes a list of integers as input and returns the sum of all the integers in the list."
        }
    ],

    # 4
    [
        {
            "role": "user",
            "content": """
Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer.
 
Context: Teplizumab traces its roots to a New Jersey drug company called Ortho Pharmaceutical. There, scientists generated an early version of the antibody, dubbed OKT3. Originally sourced from mice, the molecule was able to bind to the surface of T cells and limit their cell-killing potential. In 1986, it was approved to help prevent organ rejection after kidney transplants, making it the first therapeutic antibody allowed for human use.
 
Question: What was OKT3 originally sourced from?
Answer:
            """,
        }
    ],

    # 5
    [
        {'role': 'system', 'content': '\n        You are an assistant to Skytech employees.\n        You answer the user query based on the CONTEXT provided ONLY. \n        You never use any information that is not in the CONTEXT.\n        If the answer cannot be found in the CONTEXT, just say you don\'t have the information. don\'t invent an answer.\n        The CONTEXT is provided by system. If the CONTEXT does not provide enough information, just say you don\'t have the information. don\'t invent an answer.\n        ALWAYS mention the sources of the information you provide. The source is usually the first line of each context (Reference).\n        If you use information from multiple sources, mention each source every time you use information from that source.\n        Answer in two parts separated by "---" format: the first part is like a support ticket response. this message is directed to the customer, it should be READY to be sent directly to the customer. the second is for the Skytech employee where you mention the source from which you got the information to construct the ticket response.\n        For example:\n        Question: Est-ce que Skytech possède des certifications ?\n        CONTEXT START\n        (some context)\n        CONTEXT END\n        Your answer:\n        Oui, Skytech offre une certification SO... Le rapport est disponible sous le module sécurité.\n        \n        ---\n\n        J\'ai trouvé la réponse dans ...\n        '},
        {'role': 'user', 'content': "\nCONTEXT START:\n\nCONTEXT END.\nGiven the CONTEXT, no prior knowledge, and your prompt, answer to the following question in English. If the CONTEXT does not contain the answer, just say you don't have the information. don't invent an answer.\nQuestion: What is the capital of France?\nYour answer:"}],
]