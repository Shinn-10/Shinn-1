import streamlit as st
import numpy as np

st.title('Welcome to my Page.')

user_name = st.text_input('Enter your name')

if st.button('Enter'):
    st.write(f" Hello. Nice to see you '{user_name}'.")

st.header('Number Section')

count = st.text_input('Please, enter a number.')

st.write(count)

if st.button('Increase'):
    count = int(count)
    count += 1
    st.write(f'Your number is {count}.')
    
st.header('Your Preference')
    
select = st.selectbox('Select your favourite programming language',('Python','Javascript','Java','PHP','C','C++','Node.js','React'))
                      
if st.button('Submit'):
    st.write(f'"{select}"  is your favourite programming language.')
    
st.write("""
## Comment section ## """)

st.sidebar.title('Options')
input_text = st.sidebar.text_area('Please, say something about my page.')

if st.sidebar.button('Paste'):
    col1,col2 = st.columns(2)
    
    col1_expander = col1.expander('Expand comment')
    with col1_expander:
        col1_expander.write(input_text)
        
st.sidebar.multiselect('Which is your favourite musical instrument?',['Piano','Guitar','Violin','Drum','Organ'])

st.write("""
### ___________________________________ ### """)
         
st.write("""
### Thank you for using my page ### """)

st.slider('Rate me please.And thank you for using my page.',1,100,10)





