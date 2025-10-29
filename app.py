import streamlit as st

st.title("Ejemplo para usar Session State")

if 'count' not in st.session_state:
  st.session_state['count'] = 0

st.write(st.session_state)
# Con el código de arriba se va a agregar el count a la libreria de session state y tendrá el valor indicado

if st.button('Click me'):
  st.session_state['count'] += 1

  
name = st.text_input("Escribe tu nombre")
st.write(name) 
if name not in st.session_state:
  st.session_state['name'] = ' '
# Con este código solo se pone el botón pero no incrementa el número
# count = 0

# increment = st.button("Increment")
# if increment:
  # count += 1

# st.write("Count =", count)


