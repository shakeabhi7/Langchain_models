from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

import json
from langchain_core.load import load
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

st.header('Research Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

language_input = st.selectbox( "Select Explanation Length", ["Hindi", "English", "Hinglish","Hindi in English Words"] )

#load prompt template from JSON
with open("template.json","r") as f:
    template = load(json.load(f),
                    allowed_objects=[PromptTemplate]
                    )

if st.button('Summarize'):
    chain = template | llm
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input,
        'language_input':language_input
    })
    st.write(result.content)