import streamlit as st
import datetime

st.title('Age Calculator')

dob = st.date_input('Select Your Date', min_value = datetime.date(1900, 1, 1), max_value = datetime.date.today())

if dob:
    current = datetime.datetime.now().year   
    st.success(f'Your age is : {current - dob.year}')