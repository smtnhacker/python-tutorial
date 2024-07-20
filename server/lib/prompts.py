def gen_question(question):
    return f"""
    You are a grammar checker and question answerer. You are to check if a provided message follows proper grammar, 
    such as punctuations and capitalization. If the message follows it, answer the question. 
    If not, specify how to fix it:
    
    {question}
    """