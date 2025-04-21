import streamlit as st

st.title('Welcome To Streamlit')
st.subheader('Begining of streamlit')
st.text('----------------------')
st.write('checking functions ')

languages = st.selectbox('Your fav. Language', ['Python', 'Java', 'JavaScript', 'C'])

if languages == 'Python':
    st.write(f'Nice choice for {languages}. Weldone my data scienctist. ')
    st.success('You can try some web dev , Ai, Ml, data science, etc')
if languages == 'Java':
    st.write(f'Nice choice for {languages}. Weldone my my developer. ')
if languages == 'JavaScript':
    st.write(f'Nice choice for {languages}. Weldone my Web dev. ')
if languages == 'C':
    st.write(f'Nice choice for {languages}. Weldone my core player. ')

