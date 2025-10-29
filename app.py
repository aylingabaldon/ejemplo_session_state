import streamlit as st

st.title("Ejemplo para usar Session State")

if 'count' not in st.session_state:
  st.session_state['count'] = 0
  
# count = 0

# increment = st.button("Increment")
# if increment:
  # count += 1

# st.write("Count =", count)

st.write(st.session_state)
