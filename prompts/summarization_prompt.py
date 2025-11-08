from langchain_core.prompts import PromptTemplate

summarization_prompt = '''
You are an expert academic summarizer.

Summarize the following research paper in 4 parts:
1. Objective
2. Methodology
3. Key Findings
4. Limitations

Paper Content:
{context}
'''

summarization_prompt_template = PromptTemplate.from_template(summarization_prompt)

