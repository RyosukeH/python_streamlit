import streamlit as st
import time

st.title('Stream begin')


st.write('progress bar')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('letter is right')
if button:
    right_column.write('right')

expander = st.beta_expander('FAQ')
expander.write('write down')
