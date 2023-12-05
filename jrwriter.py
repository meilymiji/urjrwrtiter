import streamlit as st

prompt = """Act as AI writer in English. You  will recieve a topic that contains the topic's objective and some background information. Write a paragraph that related to the topic. The paragraph should be at least 50 words. You can write more than one paragraph."""

st.title('Your Junior Writer')
st.markdown('Input the topic.\nDo not forget to put an objective and some background information in the topic. :)')

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