import streamlit as st 
from langchain_community.llms import Ollama 
import pandas as pd
from pandasai import SmartDataframe
from PIL import Image



llm = Ollama(model="llama3")

st.title("Internship Task")

uploader_file = st.file_uploader("Upload a CSV file", type= ["csv"])

if uploader_file is not None:
    data = pd.read_csv(uploader_file)
    st.write(data.head(3))
    df = SmartDataframe(data, config={"llm": llm})
    prompt = st.text_area("Enter your prompt:")
    prompt = prompt + "Result must be in the format of dictionary of type and value"

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                response = df.chat(prompt)
                print(response)
                st.write(response)
                try:
                    image = Image.open(response)
                    st.image(image)
                except:
                    print()
                    
                
        else:
            st.warning("Please enter a prompt!")