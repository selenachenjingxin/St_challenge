import streamlit as st
# selectbox
st.header('st.selectbox')

option=st.selectbox(
    'What is your favorite color?',
    ('Blue',"Red",'Green'))

st.write("your favorite color is",option)
# multiselect
st.header('st.multiselect')

options=st.multiselect("what are your favorite colors",['Green','Yellow',"Red","Blue"])
st.write("you selected:",options)

#checkbox

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")