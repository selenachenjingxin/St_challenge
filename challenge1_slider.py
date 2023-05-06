import streamlit as st
from datetime import time, datetime

st.header('st.slider')

#样例1
st.subheader('Slider')

age= st.slider("How old are you?",0,130,20)
st.write("I'm",age,'years old')

#样例2
st.subheader('Range slider')

Values=st.slider(
    'select a range of values',
    0.0,100.0,(25.0,80.0))
st.write('Values:',Values)

#样例 3

st.subheader('Range time slider')

appointment=st.slider(

    "schedule your appointment:",
    value= (time(11,30),time(12,45)))

st.write("You're scheduled for:",appointment)

# 样例4
st.subheader('Datetime slider')

start_time=st.slider(
"when do you start?",
value=datetime(2020,1,1),
format="MM/DD/YY-hh:mm")
st.write("start time:",start_time)
