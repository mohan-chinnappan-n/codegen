import streamlit as st

import mymodel as m

st.write("""
# Sales Model
Sales Predictions of the customers
""")

st.write( m.run(window=15))
