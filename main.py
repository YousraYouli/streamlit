import streamlit as st


st.write ('hello world !')
x = st.text_input ('enter ue favourite movie !')
st.write (f"this is ur movie : {x}")

is_clicked=st.button('click me')
st.write('## this is a h2 title ')
st.write('# this is a h1 title ')
st.write('### this is a h3 title ')