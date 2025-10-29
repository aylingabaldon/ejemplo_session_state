import streamlit as st

st.title("Ejemplo para usar Session State")

count = 0

increment = st.button("Incremento")
if increment:
  count += 1

st.write("Count =", count)
