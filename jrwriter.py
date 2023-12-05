import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)

prompt = """Act as a high school student writing a paragraph in English. You will recieve a topic that contains the topic's objective and some background information. Write a paragraph that related to the topic. The paragraph should be at least 50 words. You can write more than one paragraph."""

st.title('Your Junior Writer')
st.markdown('Input the topic. \n\ Do not forget to put an objective and some background information in the topic. :)')

user_input = st.text_area('Enter an objective and some background information')

if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    st.markdown('**AI response:**')
    vocab_dict = response.choices[-1].message.content

    sd = json.loads(vocab_dict)

    print (sd)
    vocab_df = pd.DataFrame.from_dict(sd)
    print(vocab_df)
    st.table(vocab_df)