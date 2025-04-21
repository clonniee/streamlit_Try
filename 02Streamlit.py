import streamlit as st

st.title('Basic App Via StreamLit')

if st.button('Wanna See a Pop-up CLick me'):
    st.write('PoP-up XD')

if st.checkbox('Add Functionality'):
    st.write('More function added')    


hardness = st.slider('Hardness Leavel' , 0, 3, 0) 
# st.write(f'hardness level {hardness}')   

if hardness == 3 :
    st.success('YOu got guts kid')

st.number_input('How much live ?', min_value=0 , max_value=5, step=1) 
st.button('Done Picking Lives ?')   

name = st.text_input('Enter warrior your name')
if name :
    st.write('Welcome to THE WORLD OF RATS')

